%{
# subject.LineAllele
-> subject.Line
-> subject.Allele
%}

classdef LineAllele < dj.Lookup
    properties
        contents = {
            'VGAT-ChR2-EYFP', 'VGAT-ChR2-EYFP'
            'Ai93-Emx1', 'Ai93'
            'Ai93-Emx1', 'Emx1-Cre'
            'Thy1-GP5.3', 'Thy1-GP5.3'
            'Thy1-YFP', 'Thy1-YFP'
            'DAT-IRES-CRE', 'DAT-IRES-Cre'
            'DAT-Ai148', 'DAT-IRES-Cre'
            'DAT-Ai148', 'Ai148'
            'Slc17a7-Ai148', 'Ai148'
            'Slc17a7-Ai148', 'Slc17a7-IRES2-Cre'
            'D1-CRE', 'D1-Cre'
            'D2-CRE', 'D2-Cre'
        }
    end
end