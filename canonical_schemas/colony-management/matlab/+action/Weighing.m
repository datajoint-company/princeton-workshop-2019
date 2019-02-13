%{
# action.Weighing
-> subject.Subject
weighing_time:      datetime
-----
-> reference.User
weight:             float      # in grams
%}

classdef Weighing < dj.Manual
end