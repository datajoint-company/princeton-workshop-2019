%{
-> acquisition.Session
cell_id: varchar(36) # a string identifying the cell in which this intracellular recording is concerning
---
cell_type: enum('excitatory','inhibitory','N/A')
-> reference.ActionLocation
-> reference.WholeCellDevice
%}


classdef Cell < dj.Manual
end