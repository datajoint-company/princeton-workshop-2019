%{
species: varchar(24)
%}

classdef Species < dj.Lookup
    properties
        contents = {'Mus musculus'}
    end
end