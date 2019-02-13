%{
probe_source: varchar(64)
-----
number_of_channels: int
%}


classdef ProbeSource < dj.Lookup
   properties
        contents = {
        'Cambridge NeuroTech', 64
        'NeuroNexus', 32
        }
       
   end
end