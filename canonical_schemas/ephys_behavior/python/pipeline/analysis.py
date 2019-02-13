# -*- coding: utf-8 -*-
'''
Schema of analysis data.
'''
import re
import os
from datetime import datetime

import numpy as np
import scipy.io as sio
import datajoint as dj
import h5py as h5

from . import reference, utilities, acquisition

schema = dj.schema('workshop_gi2017_analysis')


@schema
class TrialSegmentationSetting(dj.Lookup):
    definition = """ 
    trial_seg_setting: smallint
    ---
    -> reference.ExperimentalEvent
    pre_stim_duration: decimal(4,2)  # (s) pre-stimulus duration
    post_stim_duration: decimal(4,2)  # (s) post-stimulus duration
    """
    contents = [[0, 'pole_out', 1.5, 3]]
    
    
@schema
class RealignedEvent(dj.Computed):
    definition = """
    -> TrialSegmentationSetting
    -> acquisition.TrialSet.Trial
    """
    
    class RealignedEventTime(dj.Part):
        definition = """ # experimental paradigm event timing marker(s) for this trial
        -> master
        realigned_trial_event: varchar(36)
        ---
        realigned_event_time = null: float   # (s) event time with respect to the event this trial-segmentation is time-locked to
        """
        
    def make(self, key):
        self.insert1(key)
        # get event, pre/post stim duration
        event_of_interest, pre_stim_dur, post_stim_dur = (TrialSegmentationSetting & key).fetch1(
            'event', 'pre_stim_duration', 'post_stim_duration')
        # get event time
        try: 
            eoi_time_point = get_event_time(event_of_interest, key)
        except EventChoiceError as e:
            print(f'Trial segmentation error - Msg: {str(e)}')
            return
        # get all other events for this trial
        events, event_times = (acquisition.TrialSet.EventTime & key).fetch('trial_event', 'event_time')
        self.RealignedEventTime.insert(dict(key,
                                             realigned_trial_event=eve,
                                             realigned_event_time=event_times[e_idx] - eoi_time_point)
                                        for e_idx, eve in enumerate(events))


@schema
class TrialSegmentedExtracellular(dj.Computed):
    definition = """
    -> acquisition.ExtracellularAcquisition
    -> acquisition.TrialSet.Trial
    -> TrialSegmentationSetting
    """
    
    class Voltage(dj.Part):
        definition = """
        -> master
        ---
        segmented_voltage: longblob   
        """
        
    def make(self, key):
        # make() implementation goes here
        return
    
    
@schema
class TrialSegmentedIntracellular(dj.Computed):
    definition = """
    -> acquisition.IntracellularAcquisition
    -> acquisition.TrialSet.Trial
    -> TrialSegmentationSetting
    """
    
    class MembranePotential(dj.Part):
        definition = """
        -> master
        ---
        segmented_mp: longblob   
        segmented_mp_wo_spike: longblob
        """
    
    class CurrentInjection(dj.Part):
        definition = """
        -> master
        ---
        segmented_current_injection: longblob
        """
    
    def make(self, key):
        self.insert1(key) 
        # get event, pre/post stim duration
        event_name, pre_stim_dur, post_stim_dur = (TrialSegmentationSetting & key).fetch1(
            'event', 'pre_stim_duration', 'post_stim_duration')
        # get raw
        fs, first_time_point, Vm_wo_spike, Vm_w_spike = (acquisition.IntracellularAcquisition.MembranePotential & key).fetch1(
                'membrane_potential_sampling_rate', 'membrane_potential_start_time', 'membrane_potential_wo_spike', 'membrane_potential')
        # segmentation
        segmented_Vm_wo_spike = perform_trial_segmentation(key, event_name, pre_stim_dur, post_stim_dur,
                                                           Vm_wo_spike, fs, first_time_point)
        segmented_Vm_w_spike = perform_trial_segmentation(key, event_name, pre_stim_dur, post_stim_dur,
                                                          Vm_w_spike, fs, first_time_point)

        self.MembranePotential.insert1(dict(key,
                                       segmented_mp=segmented_Vm_w_spike,
                                       segmented_mp_wo_spike=segmented_Vm_wo_spike))
        print(f'Perform trial-segmentation of membrane potential for trial: {key["trial_id"]}')
        
        # -- current injection --
        fs, first_time_point, current_injection = (acquisition.IntracellularAcquisition.CurrentInjection & key).fetch1(
                'current_injection_sampling_rate', 'current_injection_start_time', 'current_injection')
        segmented_current_injection = perform_trial_segmentation(key, event_name, pre_stim_dur, post_stim_dur,
                                                                 current_injection, fs, first_time_point)

        self.CurrentInjection.insert1(dict(key, segmented_current_injection=segmented_current_injection))
        print(f'Perform trial-segmentation of current injection for trial: {key["trial_id"]}')
    
    
@schema     
class TrialSegmentedBehavior(dj.Computed):   
    definition = """
    -> acquisition.BehaviorAcquisition
    -> acquisition.TrialSet.Trial
    -> TrialSegmentationSetting
    """
    
    class LickTrace(dj.Part):
        definition = """
        -> master
        ---
        segmented_lt_left: longblob   
        segmented_lt_right: longblob
        """   
        
    def make(self, key):
        self.insert1(key) 
        # get event, pre/post stim duration
        event_name, pre_stim_dur, post_stim_dur = (TrialSegmentationSetting & key).fetch1(
            'event', 'pre_stim_duration', 'post_stim_duration')
        # get raw
        fs, first_time_point, lt_left, lt_right = (acquisition.BehaviorAcquisition.LickTrace & key).fetch1(
                'lick_trace_sampling_rate', 'lick_trace_start_time', 'lick_trace_left', 'lick_trace_right')
        # segmentation
        key['segmented_lt_left'] = perform_trial_segmentation(key, event_name, pre_stim_dur, post_stim_dur,
                                                              lt_left, fs, first_time_point)
        key['segmented_lt_right'] = perform_trial_segmentation(key, event_name, pre_stim_dur, post_stim_dur,
                                                               lt_right, fs, first_time_point)
        self.LickTrace.insert1(key) 
        print(f'Perform trial-segmentation of lick traces for trial: {key["trial_id"]}')
    
    
@schema
class TrialSegmentedPhotoStimulus(dj.Computed):
    definition = """
    -> acquisition.PhotoStimulation
    -> acquisition.TrialSet.Trial
    -> TrialSegmentationSetting
    ---
    segmented_photostim: longblob
    """
    
    # custom key_source where acquisition.PhotoStimulation.photostim_timeseries exist
    key_source = acquisition.TrialSet.Trial * TrialSegmentationSetting * (acquisition.PhotoStimulation - 'photostim_timeseries is NULL')
    
    def make(self, key):
        # get event, pre/post stim duration
        event_name, pre_stim_dur, post_stim_dur = (TrialSegmentationSetting & key).fetch1(
            'event', 'pre_stim_duration', 'post_stim_duration')
        # get raw
        fs, first_time_point, photostim_timeseries = (acquisition.PhotoStimulation & key).fetch1(
                'photostim_sampling_rate', 'photostim_start_time', 'photostim_timeseries')
        # segmentation
        try: 
            key['segmented_photostim'] = perform_trial_segmentation(key, event_name, pre_stim_dur, post_stim_dur,
                                                                    photostim_timeseries, fs, first_time_point)
        except EventChoiceError as e:
            print(f'Trial segmentation error - Msg: {str(e)}')
            return

        self.insert1(key) 
        print(f'Perform trial-segmentation of photostim for trial: {key["trial_id"]}')
    
    
@schema
class TrialSegmentedUnitSpikeTimes(dj.Computed):
    definition = """
    -> acquisition.UnitSpikeTimes
    -> acquisition.TrialSet.Trial
    -> TrialSegmentationSetting
    ---
    segmented_spike_times: longblob
    """

    def make(self, key):
        # get event, pre/post stim duration
        event_name, pre_stim_dur, post_stim_dur = (TrialSegmentationSetting & key).fetch1(
            'event', 'pre_stim_duration', 'post_stim_duration')
        # get event time
        try: 
            event_time_point = get_event_time(event_name, key)
        except EventChoiceError as e:
            print(f'Trial segmentation error - Msg: {str(e)}')
            return
            
        pre_stim_dur = float(pre_stim_dur)
        post_stim_dur = float(post_stim_dur)
        # check if pre/post stim dur is within start/stop time
        trial_start, trial_stop = (acquisition.TrialSet.Trial & key).fetch1('start_time', 'stop_time')
        if event_time_point - pre_stim_dur < trial_start:
            print('Warning: Out of bound prestimulus duration, set to 0')
            pre_stim_dur = 0
        if event_time_point + post_stim_dur > trial_stop:
            print('Warning: Out of bound poststimulus duration, set to trial end time')
            post_stim_dur = trial_stop - event_time_point
            
        # get raw & segment
        spike_times = (acquisition.UnitSpikeTimes & key).fetch1('spike_times')
        key['segmented_spike_times'] = spike_times[np.logical_and(
            (spike_times >= (event_time_point - pre_stim_dur)),
            (spike_times <= (event_time_point + post_stim_dur)))] - event_time_point

        self.insert1(key)
        print(f'Perform trial-segmentation of spike times for unit: {key["unit_id"]} and trial: {key["trial_id"]}')


def perform_trial_segmentation(trial_key, event_name, pre_stim_dur, post_stim_dur, data, fs, first_time_point):
        # get event time
        try: 
            event_time_point = get_event_time(event_name, trial_key)
        except EventChoiceError as e:
            raise e
        #
        pre_stim_dur = float(pre_stim_dur)
        post_stim_dur = float(post_stim_dur)
        # check if pre/post stim dur is within start/stop time, if not, pad with NaNs
        trial_start, trial_stop = (acquisition.TrialSet.Trial & trial_key).fetch1('start_time', 'stop_time')

        pre_stim_nan_count = 0
        post_stim_nan_count = 0
        if event_time_point - pre_stim_dur < trial_start:
            pre_stim_nan_count = (trial_start - (event_time_point - pre_stim_dur)) * fs
            pre_stim_dur = 0
            print(f'Warning: Out of bound prestimulus duration, pad {pre_stim_nan_count} NaNs')
        if event_time_point + post_stim_dur > trial_stop:
            post_stim_nan_count = (event_time_point + post_stim_dur - trial_stop) * fs
            post_stim_dur = trial_stop - event_time_point
            print(f'Warning: Out of bound poststimulus duration, pad {post_stim_nan_count} NaNs')

        event_sample_point = (event_time_point - first_time_point) * fs
        
        sample_points_to_extract = range((event_sample_point - pre_stim_dur * fs).astype(int),
                                             (event_sample_point + post_stim_dur * fs + 1).astype(int))
        segmented_data = data[sample_points_to_extract]    
        # pad with NaNs
        segmented_data = np.hstack((np.full(pre_stim_nan_count, np.nan), segmented_data,
                                    np.full(post_stim_nan_count, np.nan)))
        
        return segmented_data
       

def get_event_time(event_name, key):
    # get event time
    try:
        t = (acquisition.TrialSet.EventTime & key & {'trial_event': event_name}).fetch1('event_time')
    except:
        raise EventChoiceError(event_name, f'{event_name}: event not found')  
    if np.isnan(t):
        raise EventChoiceError(event_name, msg=f'{event_name}: event_time is nan')
    else:
        return t
    
    
class EventChoiceError(Exception):
    '''Raise when "event" does not exist or "event_type" is invalid (e.g. nan)'''
    def __init__(self, event_name, msg=None):
        if msg is None:
            msg = f'Invalid event type or time for: {event_name}'
        super().__init__(msg)
        self.event_name = event_name
    pass
    
    