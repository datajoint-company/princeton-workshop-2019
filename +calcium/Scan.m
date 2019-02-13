%{
# Two-photon functional scans
-> pni.Session
scan_idx        : smallint 		# scan ID
-----
depth           : int           # Scan depth from the surface (microns)
laser_power 	: int           # Laser power (mW)
wavelength      : int           # Laser wavelength (nm)
filename 		: varchar(255) 	# Scan base filename
%}

classdef Scan < dj.Manual
end