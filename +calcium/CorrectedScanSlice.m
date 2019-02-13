%{
# Motion and raster correction of each slice
-> pni.CorrectedScan
slice : tinyint # slice index
-----
template                    : longblob                      # image used as alignment template
y_shifts                    : longblob                      # (pixels) y motion correction shifts
x_shifts                    : longblob                      # (pixels) x motion correction shifts
y_std                       : float                         # (um) standard deviation of y shifts
x_std                       : float                         # (um) standard deviation of x shifts
outlier_frames            : longblob                        # mask with true for frames with high shifts (already corrected)
%}

classdef CorrectedScanSlice < dj.Part

	properties(SetAccess=protected)
		master= pni.CorrectedScan
	end

end