%{
coordinate_ref: varchar(32)
%}

classdef CoordinateReference < dj.Lookup
    properties
        contents = {'lambda'; 'bregma'};
    end
end