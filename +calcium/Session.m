%{
# Experimental Session
-> pni.Mouse
session                     : smallint                      # session number
---
session_date                : date                          # date
person                      : varchar(100)                  # researcher name
scan_path                   : varchar(255)                  # file path for TIFF stacks
%}

classdef Session < dj.Manual
end
