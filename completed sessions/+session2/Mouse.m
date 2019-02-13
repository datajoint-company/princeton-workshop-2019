%{
# Experimental animals
mouse_id             : int                          # Unique animal ID
-----
dob=null             : date                         # date of birth
sex="unknown"        : enum('M','F','unknown')      # sex

%}

classdef Mouse < dj.Manual
end