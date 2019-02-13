%{
# subject.Source
source:                     varchar(63)     # name of source
-----
source_description='':      varchar(255)	# description
%}

classdef Source < dj.Lookup
    properties
        contents = {
            'Jax Lab', ''
            'Princeton', ''
            'Allen Institute', ''
        }
    end
end