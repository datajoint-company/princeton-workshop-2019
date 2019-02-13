%{
# subject.Strain
strain_name:		      varchar(63)	# strain name
---
strain_description='':    varchar(255)	# description
%}

classdef Strain < dj.Lookup
    properties
        contents = {
            'C57BL6/J', ''
        }
    end
end