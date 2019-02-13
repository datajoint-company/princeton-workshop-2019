%{
# Visual stimulus synced to imaging
-> pni.Scan
---
movie                       : longblob                      # stimulus images synchronized with slice 1 frame times (HxWxtimes matrix 90x160x27300)
conditions                  : longblob                      # vector indicating direction of moving noise, or NaN for stationary synchronized with slice 1 frame times (degrees)
%}

classdef Stimulus < dj.Manual
end
