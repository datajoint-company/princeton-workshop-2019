%{
strain: varchar(24)
%}

classdef Strain < dj.Lookup
    properties
        contents = {'C57BL6'; 'Ai35D'; 'VGAT-ChR2-EYFP'; 'PV-Cre'; 'N/A'}
    end
end