%{
-> acquisition.TrialSetTrial
-----
photo_stim_type: enum('stimulation','inhibition','N/A')
photo_stim_period: enum('sample','delay','response','N/A')
photo_stim_power: float     # (mW) stimulation power 
photo_loc_galvo_x: float    # (mm) photostim coordinates field 
photo_loc_galvo_y: float    # (mm) photostim coordinates field 
photo_loc_galvo_z: float    # (mm) photostim coordinates field 
%}

classdef TrialStimInfo < dj.Imported
end