%{
-> acquisition.Session
photostim_datetime: datetime # the time of performing this stimulation with respect to start time of the session, in the scenario of multiple stimulations per session
---
-> stimulation.PhotoStimulationInfo
photostim_timeseries=null: longblob  # (mW)
photostim_start_time=null: float     # (s) first timepoint of photostim recording
photostim_sampling_rate=null: float  # (Hz) sampling rate of photostim recording
%}


classdef PhotoStimulation < dj.Manual
end