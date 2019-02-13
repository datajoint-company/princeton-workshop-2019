%{
# Experimental session
-> session1.Mouse
session_date:   date   # date of the session
-----
experiment_setup: int  # setup number
experimenter:   varchar(100)  # name of the experimenter
%}

classdef Session < dj.Manual
end