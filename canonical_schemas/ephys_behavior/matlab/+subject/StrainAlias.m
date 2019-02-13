%{
# Other animal strain names that may be used interchangeably in different studies
strain_alias: varchar(24)
-----
-> subject.Strain
%}

classdef StrainAlias < dj.Lookup
    
   properties
    contents = {
            'C57BL6', 'C57BL6'
            'B6', 'C57BL6'
            'C57Bl/6', 'C57BL6'
            'Ai35D', 'Ai35D'
            'PV-IRES-Cre', 'PV-Cre'
            'VGAT-ChR2-EYFP', 'VGAT-ChR2-EYFP'
            'VGAT-ChR2(H134R)-EYFP', 'VGAT-ChR2-EYFP'
            'N/A', 'N/A'
            }
   end
end