%{
# Treadmill activity synced to imaging
-> pni.Scan
---
treadmill_vel               : longblob                      # velocity of treadmill (may be positive or negative)
%}

classdef Treadmill < dj.Manual
end
