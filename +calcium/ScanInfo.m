%{
# Scanning parameters
-> pni.Scan
-----
nframes                 : int               # frames recorded
px_width                : smallint          # pixels per line
px_height               : smallint          # lines per frame
um_width                : float             # field of view width (microns)
um_height               : float             # field of view height (microns)
bidirectional           : tinyint           # 1=bidirectional scanning
fps                     : float             # frames per second (Hz)
zoom                    : decimal(4,1)      # zoom factor (Scanimage-specific)
nchannels               : tinyint           # number of recorded channels
nslices                 : tinyint           # number of slices
fill_fraction           : float             # raster scan fill fraction (Scanimage-specific)
raster_phase            : float             # shift of odd vs even raster lines

%}

classdef ScanInfo < dj.Manual
end