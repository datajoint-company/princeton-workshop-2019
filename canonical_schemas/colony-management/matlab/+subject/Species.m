%{
# subject.Species
binomial:			    varchar(63)	# binomial
-----
species_nickname:		varchar(63)	# nickname
%}

classdef Species < dj.Lookup
    properties
        contents = {'Mus musculus' 'Laboratory mouse'}
    end
end