%{
# experimental paradigm event timing marker(s) for this trial
-> acquisition.TrialSetTrialEventTime
(trial_event) -> reference.ExperimentalEvent.proj('event')
---
event_time = null: float   # (in second) event time with respect to this session's start time
%}


classdef TrialSetTrialEventTime < dj.Imported
end