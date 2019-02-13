%{
-> reference.ProbeChannel
channel_id:         smallint     # id of a channel on the probe
---
channel_x_pos:  float   # x position relative to the tip of the probe (um)
channel_y_pos:  float   # y position relative to the tip of the probe (um)
channel_z_pos:  float   # y position relative to the tip of the probe (um)
shank_id: smallint      # the shank id of this probe this channel is located on 

%}


classdef ProbeChannel < dj.Lookup
end