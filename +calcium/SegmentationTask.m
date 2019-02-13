%{
# defines the channel and method to use for each slice
-> pni.Scan
slice : tinyint # slice index
channel : tinyint # recording channel
-> pni.SegmentationMethod
-----
%}

classdef SegmentationTask < dj.Manual
end