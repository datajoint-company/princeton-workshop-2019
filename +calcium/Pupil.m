%{
# pupil position and size synced to imaging
-> pni.Scan
-----
pupil_r		: longblob 	# vector of pupil radii synchronized with slice 1 frame times (pixels)
pupil_x		: longblob 	# vector of pupil x positions synchronized with slice 1 frame times (pixels)
pupil_y		: longblob 	# vector of pupil y positions synchronized with slice 1 frame times (pixels)

%}

classdef Pupil < dj.Manual
end