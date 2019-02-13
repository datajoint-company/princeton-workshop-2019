%{
# Description of the device used for electrical stimulation
device_name: varchar(32)
-----
device_desc = "": varchar(1024)

%}

classdef WholeCellDevice < dj.Lookup
end    
    

