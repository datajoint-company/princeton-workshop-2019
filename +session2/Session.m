%{
# Experiment session
-> session2.Mouse
session_date               : date                         # date
-----
experiment_setup           : int                          # experiment setup ID
experimenter               : varchar(100)                 # experimenter name
%}

classdef Session < dj.Manual
end