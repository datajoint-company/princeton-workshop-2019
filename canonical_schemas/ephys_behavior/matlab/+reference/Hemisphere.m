%{
hemisphere: varchar(8)
%}

classdef Hemisphere < dj.Lookup
    
    properties
        contents = {'left'; 'right'};
    end
end