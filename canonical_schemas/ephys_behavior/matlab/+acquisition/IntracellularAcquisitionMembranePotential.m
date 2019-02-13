%{
-> acquisition.IntracellularAcquisition
-----
membrane_potential: longblob            # (mV) membrane potential recording at this cell
membrane_potential_wo_spike: longblob   # (mV) membrane potential without spike data, derived from membrane potential recording    
membrane_potential_start_time: float    # (s) first timepoint of membrane potential recording
membrane_potential_sampling_rate: float # (Hz) sampling rate of membrane potential recording
%}


classdef IntracellularAcquisitionMembranePotential < dj.Imported
end