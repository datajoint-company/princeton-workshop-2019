%{
# subject.AlleleSequence
-> subject.Allele
-> subject.Sequence
%}

classdef AlleleSequence < dj.Lookup
    
    properties
        contents = {
                'Thy1-YFP', 'Thy1'
                'Thy1-YFP', 'EYFP'
                'Thy1-GP5.3', 'GCaMP6f'
                'VGAT-ChR2-YFP', 'EYFP'
                'VGAT-ChR2-YFP', 'ChR2'
                'Emx1-Cre', 'Emx1'
                'Emx1-Cre', 'Cre'
                'D1-Cre', 'D1'
                'D1-Cre', 'Cre'
                'D2-Cre', 'D2'
                'D2-Cre', 'Cre'
                'DAT-IRES-Cre', 'Cre'
                'Slc17a7-IRES2-Cre', 'Cre'
        }
    end
end