%{
# The behavioral response of this subject of this trial - correct/incorrect with respect to the trial type
trial_response: varchar(32)
%}


classdef TrialResponse < dj.Lookup
    properties
        contents = {'correct'; 'incorrect'; 'no response'; 'early lick'; 'N/A'}
    end
end