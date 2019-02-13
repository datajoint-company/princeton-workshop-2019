%{
# List of segmentation methods
segmentation_method : tinyint # index of segmentation method
-----
name : varchar(32) # name of segmentation method
details : varchar(500) # description of segmentation method
language : enum('matlab','python') # language used to populate segmentation method
%}

classdef SegmentationMethod < dj.Lookup
end