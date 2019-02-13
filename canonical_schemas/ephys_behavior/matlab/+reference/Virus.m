%{
virus: varchar(64) # name of the virus
---
-> reference.VirusSource
virus_lot_number="":  varchar(128)  # lot numnber of the virus
virus_titer=null:       float       # x10^12GC/mL
%}


classdef Virus < dj.Lookup
end
   