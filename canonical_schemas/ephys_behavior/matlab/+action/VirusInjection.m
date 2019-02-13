%{
-> subject.Subject
-> reference.Virus
-> reference.BrainLocation
-> reference.Hemisphere
injection_date: date   
---
injection_volume: float          # in nL
injection_coordinate_ap: float   # in mm, negative if posterior, positive if anterior
injection_coordinate_ml: float   # in mm, always positive, larger number if more lateral
injection_coordinate_dv: float   # in mm, always positive, larger number if more ventral (deeper)
(injection_coordinate_ref) -> reference.CoordinateReference.proj('coordinate_ref')
%}


classdef VirusInjection < dj.Manual
end