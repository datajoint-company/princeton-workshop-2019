%{
# subject.Litter
litter:                         varchar(63)
---
-> subject.BreedingPair
-> subject.Line
litter_descriptive_name='':     varchar(255)	# descriptive name
litter_description='':          varchar(255)	# description
litter_birth_date=null:			date		    # birth date
%}

classdef Litter < dj.Manual
end