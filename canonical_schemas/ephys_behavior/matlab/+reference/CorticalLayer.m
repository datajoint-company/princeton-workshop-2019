%{
cortical_layer : varchar(8) # layer within cortex
%}


classdef CorticalLayer < dj.Lookup
   properties 
    contents = {'N/A'; '1'; '2'; '3'; '4'; '5'; '6'; '2/3'; '3/4'; '4/5'; '5/6'};
   end
end
