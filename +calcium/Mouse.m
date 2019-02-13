%{
# Experimental animals
mouse_id                    : int                           # Unique animal ID
---
dob=null                    : date                          # date of birth
sex="unknown"               : enum('M','F','unknown')       # sex
mouse_notes=''              : varchar(4096)                 # other comments and distinguishing features
%}

classdef Mouse < dj.Manual
end
