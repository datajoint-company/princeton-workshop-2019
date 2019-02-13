#!/usr/bin/env python3
import os

import sys
from datetime import datetime
from dateutil.tz import tzlocal
import pytz
import re
import numpy as np
import pandas as pd

from pipeline import reference, subject, acquisition, stimulation, analysis, utilities
import pynwb
from pynwb import NWBFile, NWBHDF5IO

# =============================================
# Each NWBFile represent a session, thus for every session in acquisition.Session, we build one NWBFile

for session_key in acquisition.Session.fetch('KEY'):
    this_session = (acquisition.Session & session_key).fetch1()
    # =============== General ====================
    # -- NWB file - a NWB2.0 file for each session
    nwbfile = NWBFile(
        session_description=this_session['session_note'],
        identifier='_'.join([this_session['subject_id'],
                             this_session['session_time'].strftime('%Y-%m-%d_%H-%M-%S')]),
        session_start_time=this_session['session_time'],
        file_create_date=datetime.now(tzlocal()),
        experimenter='; '.join((acquisition.Session.Experimenter & session_key).fetch('experimenter')),
        institution='Janelia Research Campus',  # TODO: not in pipeline
        related_publications='doi:10.1038/nature22324')  # TODO: not in pipeline
    # -- subject
    subj = (subject.Subject & session_key).fetch(as_dict=True)[0]
    nwbfile.subject = pynwb.file.Subject(
        subject_id=this_session['subject_id'],
        description=subj['subject_description'],
        genotype=subj['strain'],
        sex=subj['sex'],
        species=subj['species'])
    # =============== Intracellular ====================
    cell = ((acquisition.Cell & session_key).fetch1()
            if (acquisition.Cell & session_key).fetch().size == 1
            else None)
    if cell:
        # metadata
        whole_cell_device = nwbfile.create_device(name=cell['device_name'])
        ic_electrode = nwbfile.create_ic_electrode(
            name=cell['cell_id'],
            device=whole_cell_device,
            description='N/A',
            filtering='low-pass: 10kHz',  # TODO: not in pipeline
            location='; '.join([f'{k}: {str(v)}'
                                for k, v in (reference.ActionLocation & cell).fetch1().items()]))
        # acquisition - membrane potential
        mp, mp_start_time, mp_fs = (acquisition.IntracellularAcquisition.MembranePotential & cell).fetch1(
            'membrane_potential', 'membrane_potential_start_time', 'membrane_potential_sampling_rate')
        nwbfile.add_acquisition(pynwb.icephys.PatchClampSeries(name='membrane_potential',
                                                               electrode=ic_electrode,
                                                               unit='mV',  # TODO: not in pipeline
                                                               conversion=1e-3,
                                                               gain=1.0,  # TODO: not in pipeline
                                                               data=mp,
                                                               starting_time=mp_start_time,
                                                               rate=mp_fs))
        # acquisition - current injection
        current_injection, ci_start_time, ci_fs = (acquisition.IntracellularAcquisition.CurrentInjection & cell).fetch1(
            'current_injection', 'current_injection_start_time', 'current_injection_sampling_rate')
        nwbfile.add_stimulus(pynwb.icephys.CurrentClampStimulusSeries(name='current_injection',
                                                                      electrode=ic_electrode,
                                                                      unit='nA',
                                                                      conversion=1e-6,
                                                                      gain=1.0,
                                                                      data=current_injection,
                                                                      starting_time=ci_start_time,
                                                                      rate=ci_fs))

        # analysis - membrane potential without spike
        mp_wo_spike, mp_start_time, mp_fs = (acquisition.IntracellularAcquisition.MembranePotential & cell).fetch1(
            'membrane_potential_wo_spike', 'membrane_potential_start_time', 'membrane_potential_sampling_rate')
        mp_rmv_spike = nwbfile.create_processing_module(name='membrane_potential_spike_removal',
                                                        description='Spike removal')
        mp_rmv_spike.add_data_interface(pynwb.icephys.PatchClampSeries(name='membrane_potential_without_spike',
                                                                       electrode=ic_electrode,
                                                                       unit='mV',
                                                                       conversion=1e-3,
                                                                       gain=1.0,
                                                                       data=mp_wo_spike,
                                                                       starting_time=mp_start_time,
                                                                       rate=mp_fs))

    # =============== Extracellular ====================
    probe_insertion = ((acquisition.ProbeInsertion & session_key).fetch1()
                       if (acquisition.ProbeInsertion & session_key).fetch().size == 1
                       else None)
    if probe_insertion:
        probe = nwbfile.create_device(name = probe_insertion['probe_name'])
        electrode_group = nwbfile.create_electrode_group(
            name='; '.join([f'{probe_insertion["probe_name"]}: {str(probe_insertion["channel_counts"])}']),
            description = 'N/A',
            device = probe,
            location = '; '.join([f'{k}: {str(v)}' for k, v in
                                  (reference.ActionLocation & probe_insertion).fetch1().items()]))

        for chn in (reference.Probe.Channel & probe_insertion).fetch(as_dict=True):
            nwbfile.add_electrode(id=chn['channel_id'],
                                  group=electrode_group,
                                  filtering='Bandpass filtered 300-6K Hz',  # TODO: not in pipeline
                                  imp=-1.,  # TODO: not in pipeline
                                  x=chn['channel_x_pos'],
                                  y=chn['channel_y_pos'],
                                  z=chn['channel_z_pos'],
                                  location=electrode_group.location)

        # --- unit spike times ---
        nwbfile.add_unit_column(name='unit_x', description='x-coordinate of this unit')
        nwbfile.add_unit_column(name='unit_y', description='y-coordinate of this unit')
        nwbfile.add_unit_column(name='unit_z', description='z-coordinate of this unit')
        nwbfile.add_unit_column(name='unit_cell_type', description='cell type (e.g. wide width, narrow width spiking)')

        for unit in (acquisition.UnitSpikeTimes & probe_insertion).fetch(as_dict=True):
            # make an electrode table region (which electrode(s) is this unit coming from)
            nwbfile.add_unit(id=unit['unit_id'],
                             electrodes=(unit['channel_id']
                                         if isinstance(unit['channel_id'], np.ndarray) else [unit['channel_id']]),
                             unit_x=unit['unit_x'],
                             unit_y=unit['unit_y'],
                             unit_z=unit['unit_z'],
                             unit_cell_type=unit['unit_cell_type'],
                             spike_times=unit['spike_times'],
                             waveform_mean=np.mean(unit['spike_waveform'], axis=0),
                             waveform_sd=np.std(unit['spike_waveform'], axis=0))

    # =============== Behavior ====================
    behavior = ((acquisition.BehaviorAcquisition & session_key).fetch1()
                       if (acquisition.BehaviorAcquisition & session_key).fetch().size == 1
                       else None)
    if behavior:
        lt_left, lt_right, lt_start_time, lt_fs = (acquisition.BehaviorAcquisition.LickTrace & behavior).fetch1(
            'lick_trace_left', 'lick_trace_right', 'lick_trace_start_time', 'lick_trace_sampling_rate')
        lick_trace = pynwb.behavior.BehavioralTimeSeries(name = 'Lick Trace')
        nwbfile.add_acquisition(lick_trace)
        lick_trace.create_timeseries(name='lick_trace_left',
                                     unit='a.u.',
                                     conversion=1.0,
                                     data=lt_left,
                                     starting_time=lt_start_time,
                                     rate=lt_fs)
        lick_trace.create_timeseries(name='lick_trace_right',
                                     unit='a.u.',
                                     conversion=1.0,
                                     data=lt_right,
                                     starting_time=lt_start_time,
                                     rate=lt_fs)

    # =============== Photostimulation ====================
    photostim = ((acquisition.PhotoStimulation & session_key).fetch1()
                       if (acquisition.PhotoStimulation & session_key).fetch().size == 1
                       else None)
    if photostim:
        photostim_device = (stimulation.PhotoStimDevice & photostim).fetch1()
        stim_device = nwbfile.create_device(name=photostim_device['device_name'])
        stim_site = pynwb.ogen.OptogeneticStimulusSite(
            name='-'.join([photostim['hemisphere'], photostim['brain_region']]),
            device=stim_device,
            excitation_lambda=float(photostim['photo_stim_excitation_lambda']),
            location = '; '.join([f'{k}: {str(v)}' for k, v in
                                  (reference.ActionLocation & photostim).fetch1().items()]),
            description=(stimulation.PhotoStimulationInfo & photostim).fetch1('photo_stim_notes'))
        nwbfile.add_ogen_site(stim_site)

        if photostim['photostim_timeseries'] is not None:
            nwbfile.add_stimulus(pynwb.ogen.OptogeneticSeries(
                name='_'.join(['photostim_on', photostim['photostim_datetime'].strftime('%Y-%m-%d_%H-%M-%S')]),
                site=stim_site,
                unit = 'mW',
                resolution = 0.0,
                conversion = 1e-6,
                data = photostim['photostim_timeseries'],
                starting_time = photostim['photostim_start_time'],
                rate = photostim['photostim_sampling_rate']))

    # =============== TrialSet ====================
    # NWB 'trial' (of type dynamic table) by default comes with three mandatory attributes:
    #                                                                       'id', 'start_time' and 'stop_time'.
    # Other trial-related information needs to be added in to the trial-table as additional columns (with column name
    # and column description)
    if (acquisition.TrialSet & session_key).fetch().size == 1:
        # Get trial descriptors from TrialSet.Trial and TrialStimInfo
        trial_columns = [{'name': tag,
                          'description': re.sub('\s+:|\s+', ' ', re.search(
                              f'(?<={tag})(.*)', str((acquisition.TrialSet.Trial * acquisition.TrialStimInfo).heading)).group())}
                         for tag in (acquisition.TrialSet.Trial * acquisition.TrialStimInfo).fetch(as_dict=True, limit=1)[0].keys()
                         if tag not in (acquisition.TrialSet.Trial & acquisition.TrialStimInfo).primary_key + ['start_time', 'stop_time']]
        # Add new table columns to nwb trial-table
        for c in trial_columns:
            nwbfile.add_trial_column(**c)

        photostim_tag_default = {tag: '' for tag in acquisition.TrialStimInfo.fetch(as_dict=True, limit=1)[0].keys()
                                 if tag not in acquisition.TrialStimInfo.primary_key}
        # Add entry to the trial-table
        for trial in (acquisition.TrialSet.Trial & session_key).fetch(as_dict=True):
            photostim_tag = (acquisition.TrialStimInfo & trial).fetch(as_dict=True)
            trial_tag_value = {**trial, **photostim_tag[0]} if len(photostim_tag) == 1 else {**trial, **photostim_tag_default}
            # rename 'trial_id' to 'id'
            trial_tag_value['id'] = trial_tag_value['trial_id']
            [trial_tag_value.pop(k) for k in acquisition.TrialSet.Trial.primary_key]
            nwbfile.add_trial(**trial_tag_value)

    # =============== Write NWB 2.0 file ===============
    save_path = os.path.join('data', 'NWB 2.0')
    save_file_name = ''.join([nwbfile.identifier, '.nwb'])
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    with NWBHDF5IO(os.path.join(save_path, save_file_name), mode = 'w') as io:
        io.write(nwbfile)
        print(f'Write NWB 2.0 file: {save_file_name}')






