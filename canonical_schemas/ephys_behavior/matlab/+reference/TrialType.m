%{
# The experimental type of this trial; e.g. Lick Left vs Lick Right
trial_type: varchar(32)
%}


classdef TrialType < dj.Lookup
    properties
        contents = {'lick left'; 'lick right'; 'non-performing'; 'N/A'}
    end
end