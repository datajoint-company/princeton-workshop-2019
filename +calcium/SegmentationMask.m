%{
# neuron pixel masks
-> pni.Segmentation
mask_id : int # unique mask id for this segmentation
-----
pixels : blob # pixel indexes of mask
weights : blob # weights of each pixel in mask
%}

classdef SegmentationMask < dj.Part

	properties(SetAccess=protected)
		master= pni.Segmentation
	end

end