%{
allele_name: varchar(128)
%}

classdef Allele < dj.Lookup
    
    properties
        contents = {'L7-cre', 'rosa26-lsl-ChR2-YFP'}
    end
    
end