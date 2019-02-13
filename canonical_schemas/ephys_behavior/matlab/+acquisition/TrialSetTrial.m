%{
-> acquisition.TrialSet
trial_id: smallint              # id of this trial in this trial set
---
start_time = null: float        # start time of this trial, with respect to starting point of this session
stop_time = null: float         # end time of this trial, with respect to starting point of this session
-> reference.TrialType
-> reference.TrialResponse
trial_stim_present: bool        # is this a stim or no-stim trial
trial_is_good: bool             # is this a good or bad trial
%}


classdef TrialSetTrial < dj.Imported
end