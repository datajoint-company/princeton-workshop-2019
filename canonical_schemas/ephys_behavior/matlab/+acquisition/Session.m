%{
-> subject.Subject
session_time: datetime    # session time
---
session_directory = "": varchar(256)
session_note = "" : varchar(256) 
%}


classdef Session < dj.Manual
end
   