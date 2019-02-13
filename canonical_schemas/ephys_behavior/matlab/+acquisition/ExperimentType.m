%{
experiment_type: varchar(64)
%}


classdef ExperimentType < dj.Lookup
    properties
        contents = {'behavior'; 'extracelluar'; 'photostim'}
    end
end