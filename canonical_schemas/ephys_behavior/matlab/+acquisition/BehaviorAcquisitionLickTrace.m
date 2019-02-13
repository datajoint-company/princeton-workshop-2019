%{
-> acquisition.BehaviorAcquisition
-----
lick_trace_left: longblob   
lick_trace_right: longblob
lick_trace_start_time: float    # (s) first timepoint of lick trace recording
lick_trace_sampling_rate: float # (Hz) sampling rate of lick trace recording
%}


classdef BehaviorAcquisitionLickTrace < dj.Imported
end