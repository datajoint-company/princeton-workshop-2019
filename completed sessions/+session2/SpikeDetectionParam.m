%{
spd_id: int     # unique id for spike detection parameter set.
-----
threshold: float    # thresold for spike detection
%}

classdef SpikeDetectionParam < dj.Lookup
end