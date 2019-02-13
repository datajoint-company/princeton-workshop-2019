%{
# Segmentation of functional movies
-> pni.CorrectedScan
-> pni.SegmentationTask
-----
segmentation_time=CURRENT_TIMESTAMP: timestamp              # automatic
%}

classdef Segmentation < dj.Computed

	methods(Access=protected)

		function makeTuples(self, key)
		%!!! compute missing fields for key here
			 self.insert(key)
		end
	end

end