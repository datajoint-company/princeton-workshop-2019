%{
-> acquisition.IntracellularAcquisition
---
current_injection: longblob
current_injection_start_time: float     # first timepoint of current injection recording
current_injection_sampling_rate: float  # (Hz) sampling rate of current injection recording
%}


classdef IntracellularAcquisitionCurrentInjection < dj.Imported
end
