%{
# Motion and raster correction of movies
-> pni.Scan
-----
align_time=CURRENT_TIMESTAMP: timestamp                     # automatic
%}

classdef CorrectedScan < dj.Computed

	methods(Access=protected)

		function makeTuples(self, key)
		%!!! compute missing fields for key here
			 self.insert(key)
		end
	end

end