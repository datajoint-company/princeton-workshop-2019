%{
# The stimulation type of this trial; e.g. 'no stim'; 'photo stimulation'; 'photo inhibition'
trial_stim_type: varchar(32)
%}


classdef TrialStimType < dj.Lookup
    properties
        contents = {'no stim'; 'photo stimulation'; 'photo inhibition'; 'N/A'}
    end
end
    