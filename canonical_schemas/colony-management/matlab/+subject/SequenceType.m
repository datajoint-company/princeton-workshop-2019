%{
# reference.SequenceType
sequence_type:              varchar(63)
-----
seq_type_description='':    varchar(255)
%}

classdef SequenceType < dj.Lookup
    properties
        contents = {
            'calcium sensor', '' 
            'optogenetics', ''
            'fluorescent protein', ''
            'promoter', ''
            'recombinase', ''
            'others', ''
        }
    end
end