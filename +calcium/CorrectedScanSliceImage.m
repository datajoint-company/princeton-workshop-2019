%{
# average image of a slice
-> pni.CorrectedScan
slice : tinyint # slice index
channel : tinyint # recording channel
-----
average_image : longblob # motion-corrected average image
%}

classdef CorrectedScanSliceImage < dj.Part

properties(SetAccess=protected)
		master= pni.CorrectedScan
	end

end