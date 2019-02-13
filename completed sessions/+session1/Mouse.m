%{
# Experimental mouse
mouse_id:   int   # unique id of a mouse
-----
dob:  date # date of birth
sex:  enum('M', 'F', 'unknown') # sex
%}

classdef Mouse < dj.Manual
end