%{
# reference.Lab
lab:                    varchar(63)  # name of lab
-----
institution:            varchar(127)
address:                varchar(127)
time_zone:              varchar(127)
%}

classdef Lab < dj.Lookup

    properties
        contents = {'tanklab', 'Princeton', 'Princeton Neuroscience Institute, Princeton University Princeton, NJ 08544', 'America/New_York'}
    end
    
end