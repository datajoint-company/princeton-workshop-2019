%{
brain_region: varchar(32)
brain_subregion = 'N/A' : varchar(32)
-> reference.CorticalLayer
-> reference.Hemisphere
-----
brain_location_full_name = 'N/A':  varchar(128)
%}


classdef BrainLocation < dj.Manual
end
 