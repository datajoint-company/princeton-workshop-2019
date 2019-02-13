%{
# reference.Project
project:                    varchar(31)
-----
project_description='':     varchar(1023)
%}

classdef Project < dj.Lookup
    properties
        contents = {'mouse behavior', ''}
    end
end