%{
whisker_config: varchar(32)
%}


classdef WhiskerConfig < dj.Lookup
    properties
        contents = {'full'; 'C2'}
    end
end
       