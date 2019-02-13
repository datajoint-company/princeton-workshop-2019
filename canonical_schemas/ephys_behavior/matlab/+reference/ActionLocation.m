%{
# Location of any experimental task (e.g. recording (extra/intra cellular), stimulation (photo or current) )
-> reference.BrainLocation
-> reference.CoordinateReference
coordinate_ap: decimal(4,2)    # in mm, anterior positive, posterior negative 
coordinate_ml: decimal(4,2)    # in mm, always postive, number larger when more lateral
coordinate_dv: decimal(4,2)    # in mm, always postive, number larger when more ventral (deeper)
%}


classdef ActionLocation < dj.Manual
end
    