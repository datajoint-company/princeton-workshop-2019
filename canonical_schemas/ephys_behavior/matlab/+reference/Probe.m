%{
# Description of a particular model of probe.
probe_name: varchar(128)            # String naming probe model
channel_counts: smallint            # number of channels in the probe

%}

classdef Probe < dj.Lookup
end