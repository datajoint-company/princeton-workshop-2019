%{
# subject.Sequence
sequence:		            varchar(63)     # informal name
-----
-> subject.SequenceType
base_pairs='':              varchar(1023)	# base pairs
sequence_description='':	varchar(255)	# description
%}

classdef Sequence < dj.Lookup
    properties
        contents = {
                'GCaMP6f', 'calcium sensor', '', ''
                'GCaMP6s', 'calcium sensor', '', ''
                'ChR2', 'optogenetics', '', ''
                'EYFP', 'fluorescent protein', '', ''
                'Thy1', 'promoter', '', ''
                'Emx1', 'promoter', '', ''
                'Cre', 'recombinase', '', ''
                'D1', 'promoter', '', 'dopamine receptor type 1'
                'D2', 'promoter', '', 'dopamine receptor type 2'
                
            }
    end
end