%{
sdp_id: int         # unique id for spike detection parameter set.
-----
threshold: float    # thresold for spike detection
%}

classdef SpikeDetectionParam < dj.Lookup
    properties
        contents = {
            0, 0.5
            1, 0.9
            2, 2.0
        }
    end
end