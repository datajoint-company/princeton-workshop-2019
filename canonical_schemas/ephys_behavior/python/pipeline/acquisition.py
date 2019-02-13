'''
Schema of aquisition information.
'''
import re
import os
from datetime import datetime

import numpy as np
import scipy.io as sio
import datajoint as dj
import h5py as h5

from . import reference, subject, utilities, stimulation

schema = dj.schema('workshop_gi2017_acquisition')


@schema
class ExperimentType(dj.Lookup):
    definition = """
    experiment_type: varchar(64)
    """
    contents = [['behavior'], ['extracelluar'], ['photostim']]


@schema
class Session(dj.Manual):
    definition = """
    -> subject.Subject
    session_time: datetime    # session time
    ---
    session_directory = "": varchar(256)
    session_note = "" : varchar(256) 
    """

    class Experimenter(dj.Part):
        definition = """
        -> master
        -> reference.Experimenter
        """

    class ExperimentType(dj.Part):
        definition = """
        -> master
        -> ExperimentType
        """


@schema
class BehaviorAcquisition(dj.Imported):
    definition = """
    -> Session
    """    
    
    class LickTrace(dj.Part):
        definition = """
        -> master
        ---
        lick_trace_left: longblob   
        lick_trace_right: longblob
        lick_trace_start_time: float # (s) first timepoint of lick trace recording
        lick_trace_sampling_rate: float # (Hz) sampling rate of lick trace recording
        """       
        
    def make(self, key):
        # ============ Dataset ============
        sess_data_dir = os.path.join('..', 'data', 'whole_cell_nwb2.0')
        # Get the Session definition from the keys of this session
        animal_id = key['subject_id']
        date_of_experiment = key['session_time']
        # Search the files in filenames to find a match for "this" session (based on key)
        sess_data_file = utilities.find_session_matched_nwbfile(sess_data_dir, animal_id, date_of_experiment)
        if sess_data_file is None: 
            print(f'BehaviorAcquisition import failed for: {animal_id} - {date_of_experiment}')
            return
        nwb = h5.File(os.path.join(sess_data_dir, sess_data_file), 'r')
        #  ============= Now read the data and start ingesting =============
        self.insert1(key)
        print('Insert behavioral data for: subject: {0} - date: {1}'.format(key['subject_id'],key['session_time']))
        # -- MembranePotential
        key['lick_trace_left'] = nwb['acquisition']['timeseries']['lick_trace_L']['data'].value
        key['lick_trace_right'] = nwb['acquisition']['timeseries']['lick_trace_R']['data'].value
        lick_trace_time_stamps = nwb['acquisition']['timeseries']['lick_trace_R']['timestamps'].value
        key['lick_trace_start_time'] = lick_trace_time_stamps[0]
        key['lick_trace_sampling_rate'] = 1/np.mean(np.diff(lick_trace_time_stamps))        
        self.LickTrace.insert1(key)


@schema
class PhotoStimulation(dj.Manual):
    definition = """ # Photostimulus profile used for stimulation in this session
    -> Session
    photostim_datetime: datetime # the time of performing this stimulation with respect to start time of the session, in the scenario of multiple stimulations per session
    ---
    -> stimulation.PhotoStimulationInfo
    photostim_timeseries=null: longblob  # (mW)
    photostim_start_time=null: float  # (s) first timepoint of photostim recording
    photostim_sampling_rate=null: float  # (Hz) sampling rate of photostim recording
    """    


@schema
class Cell(dj.Manual):
    definition = """ # A cell undergone intracellular recording in this session
    -> Session
    cell_id: varchar(36) # a string identifying the cell in which this intracellular recording is concerning
    ---
    cell_type: enum('excitatory','inhibitory','N/A')
    -> reference.ActionLocation
    -> reference.WholeCellDevice
    """    
  
    
@schema
class IntracellularAcquisition(dj.Imported):
    definition = """ # Membrane potential recording from a cell, and electrical stimulation profile to this cell
    -> Cell
    """     
    
    class MembranePotential(dj.Part):
        definition = """
        -> master
        ---
        membrane_potential: longblob    # (mV) membrane potential recording at this cell
        membrane_potential_wo_spike: longblob # (mV) membrane potential without spike data, derived from membrane potential recording    
        membrane_potential_start_time: float # (s) first timepoint of membrane potential recording
        membrane_potential_sampling_rate: float # (Hz) sampling rate of membrane potential recording
        """
        
    class CurrentInjection(dj.Part):
        definition = """
        -> master
        ---
        current_injection: longblob
        current_injection_start_time: float  # first timepoint of current injection recording
        current_injection_sampling_rate: float  # (Hz) sampling rate of current injection recording
        """
        
    def make(self, key):
        # ============ Dataset ============
        sess_data_dir = os.path.join('..', 'data', 'whole_cell_nwb2.0')
        # Get the Session definition from the keys of this session
        animal_id = key['subject_id']
        date_of_experiment = key['session_time']
        # Search the files in filenames to find a match for "this" session (based on key)
        sess_data_file = utilities.find_session_matched_nwbfile(sess_data_dir, animal_id, date_of_experiment)
        if sess_data_file is None: 
            print(f'IntracellularAcquisition import failed for: {animal_id} - {date_of_experiment}')
            return
        nwb = h5.File(os.path.join(sess_data_dir, sess_data_file), 'r')
        #  ============= Now read the data and start ingesting =============
        self.insert1(key)
        print('Insert intracellular data for: subject: {0} - date: {1} - cell: {2}'.format(key['subject_id'], key['session_time'], key['cell_id']))
        # -- MembranePotential
        membrane_potential_time_stamps = nwb['acquisition']['timeseries']['membrane_potential']['timestamps'].value
        self.MembranePotential.insert1(dict(key,
            membrane_potential=nwb['acquisition']['timeseries']['membrane_potential']['data'].value,
            membrane_potential_wo_spike=nwb['analysis']['Vm_wo_spikes']['membrane_potential_wo_spike']['data'].value,
            membrane_potential_start_time=membrane_potential_time_stamps[0],
            membrane_potential_sampling_rate=1/np.mean(np.diff(membrane_potential_time_stamps))))
        # -- CurrentInjection
        current_injection_time_stamps = nwb['acquisition']['timeseries']['current_injection']['timestamps'].value
        self.CurrentInjection.insert1(dict(key,
            current_injection=nwb['acquisition']['timeseries']['current_injection']['data'].value,
            current_injection_start_time=current_injection_time_stamps[0],
            current_injection_sampling_rate=1/np.mean(np.diff(current_injection_time_stamps))))
        nwb.close()

    
@schema
class ProbeInsertion(dj.Manual):
    definition = """ # Description of probe insertion details during extracellular recording
    -> Session
    -> reference.Probe
    -> reference.ActionLocation
    """    
    

@schema
class ExtracellularAcquisition(dj.Imported):
    definition = """ # Raw extracellular recording, channel x time (e.g. LFP)
    -> ProbeInsertion
    """    
    
    class Voltage(dj.Part):
        definition = """
        -> master
        ---
        voltage: longblob   # (mV)
        voltage_start_time: float # (second) first timepoint of voltage recording
        voltage_sampling_rate: float # (Hz) sampling rate of voltage recording
        """
        
    def make(self, key):
        # this function implements the ingestion of raw extracellular data into the pipeline
        return None


@schema
class UnitSpikeTimes(dj.Imported):
    definition = """ 
    -> ProbeInsertion
    unit_id : smallint
    ---
    -> reference.Probe.Channel
    spike_times: longblob  # (s) time of each spike, with respect to the start of session 
    unit_cell_type: varchar(32)  # e.g. cell-type of this unit (e.g. wide width, narrow width spiking)
    unit_x: float  # (mm)
    unit_y: float  # (mm)
    unit_z: float  # (mm)
    spike_waveform: longblob  # waveform(s) of each spike at each spike time (spike_time x waveform_timestamps)
    """
        
    def make(self, key):
        # ================ Dataset ================
        sess_data_dir = os.path.join('..', 'data', 'extracellular', 'datafiles')
        # Get the Session definition from the keys of this session
        animal_id = key['subject_id']
        date_of_experiment = key['session_time']
        # Search the files in filenames to find a match for "this" session (based on key)
        sess_data_file = utilities.find_session_matched_nwbfile(sess_data_dir, animal_id, date_of_experiment)
        if sess_data_file is None: 
            print(f'UnitSpikeTimes import failed for: {animal_id} - {date_of_experiment}')
            return
        nwb = h5.File(os.path.join(sess_data_dir,sess_data_file), 'r')
        # ------ Spike ------
        ec_event_waveform = nwb['processing']['extracellular_units']['EventWaveform']
        ec_unit_times = nwb['processing']['extracellular_units']['UnitTimes']
        # - unit cell type
        cell_type = {}
        for tmp_str in ec_unit_times.get('cell_types').value:
            tmp_str = tmp_str.decode('UTF-8')
            split_str = re.split(' - ', tmp_str)
            cell_type[split_str[0]] = split_str[1]
        # - unit info
        print('Inserting spike unit: ', end="")
        for unit_str in ec_event_waveform.keys():
            unit_id = int(re.search('\d+', unit_str).group())
            unit_depth = ec_unit_times.get(unit_str).get('depth').value
            key['unit_id'] = unit_id
            key['channel_id'] = ec_event_waveform.get(unit_str).get('electrode_idx').value.item(0) - 1  # TODO: check if electrode_idx has MATLAB 1-based indexing (starts at 1)
            key['spike_times'] = ec_unit_times.get(unit_str).get('times').value
            key['unit_cell_type'] = cell_type[unit_str]
            key.update(zip(('unit_x', 'unit_y', 'unit_z'), unit_depth))
            key['spike_waveform'] = ec_event_waveform.get(unit_str).get('data').value
            self.insert1(key)
            print(f'{unit_id} ', end="")
        print('')
        nwb.close()
    

@schema
class TrialSet(dj.Imported):
    definition = """
    -> Session
    ---
    trial_counts: int # total number of trials
    """
    
    class Trial(dj.Part):
        definition = """
        -> master
        trial_id: smallint           # id of this trial in this trial set
        ---
        start_time = null: float               # start time of this trial, with respect to starting point of this session
        stop_time = null: float                # end time of this trial, with respect to starting point of this session
        -> reference.TrialType
        -> reference.TrialResponse
        trial_stim_present: bool  # is this a stim or no-stim trial
        trial_is_good: bool  # is this a good or bad trial
        """
        
    class EventTime(dj.Part):
        definition = """ # experimental paradigm event timing marker(s) for this trial
        -> master.Trial
        -> reference.ExperimentalEvent.proj(trial_event="event")
        ---
        event_time = null: float   # (in second) event time with respect to this session's start time
        """

    def make(self, key):
        # this function implements the ingestion of Trial data into the pipeline
        return None
    
    
@schema
class TrialStimInfo(dj.Imported):
    definition = """ # information related to the stimulation settings for this trial
    -> TrialSet.Trial
    ---
    photo_stim_type: enum('stimulation','inhibition','N/A')
    photo_stim_period: enum('sample','delay','response','N/A')
    photo_stim_power: float  # (mW) stimulation power 
    photo_loc_galvo_x: float  # (mm) photostim coordinates field 
    photo_loc_galvo_y: float  # (mm) photostim coordinates field 
    photo_loc_galvo_z: float  # (mm) photostim coordinates field 
    """    
    
    def make(self, key):
        # this function implements the ingestion of Trial stim info into the pipeline
        return None
    
    