%{
# individual fluorescence trace from one mask
-> pni.Fluorescence
-> pni.SegmentationMask
-----
trace : longblob # fluorescence trace
%}

classdef FluorescenceTrace < dj.Part

	properties(SetAccess=protected)
		master= pni.Fluorescence
	end

end