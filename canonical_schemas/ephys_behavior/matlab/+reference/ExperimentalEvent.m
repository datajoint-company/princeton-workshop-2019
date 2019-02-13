%{
# Experimental paradigm events of this study
event: varchar(32)
-----
description: varchar(256)   
%}

classdef ExperimentalEvent < dj.Lookup
    
    properties
        contents = {
                    'trial_start', 'trial start time'
                    'trial_stop', 'trial end time'
                    'cue_start', 'onset of auditory cue'
                    'cue_end', 'offset of auditory cue'
                    'pole_in', 'onset of pole moving in'
                    'pole_out', 'onset of pole moving out'
                   }
    end
end
