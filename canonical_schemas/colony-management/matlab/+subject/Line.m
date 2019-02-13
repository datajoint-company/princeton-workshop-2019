%{
# subject.Line
line:                   varchar(128)	# name
---
-> subject.Species
-> subject.Strain
line_description='':	varchar(2048)	# description
target_phenotype='':	varchar(255)	# target phenotype
is_active:				boolean		    # is active
%}

classdef Line < dj.Lookup
    properties
        contents = {
            'C57BL6/J', 'Mus musculus', 'C57BL6/J', 'wild-type mice', '', 1
            'VGAT-ChR2-EYFP', 'Mus musculus', 'C57BL6/J', '', '', 1
            'Ai93-Emx1', 'Mus musculus', 'C57BL6/J', '', '', 1
            'Thy1-GP5.3', 'Mus musculus', 'C57BL6/J', '', '', 1
            'Thy1-YFP', 'Mus musculus', 'C57BL6/J', '', '', 1
            'DAT-IRES-CRE', 'Mus musculus', 'C57BL6/J', '', '', 1
            'DAT-Ai148', 'Mus musculus', 'C57BL6/J', '', '', 1
            'Slc17a7-Ai148', 'Mus musculus', 'C57BL6/J', '', '', 1
            'D1-CRE', 'Mus musculus', 'C57BL6/J', '', '', 1
            'D2-CRE', 'Mus musculus', 'C57BL6/J', '', '', 1
        }
    end
end