%{
virus_source: varchar(64)
%}


classdef VirusSource < dj.Lookup
    properties
        contents = {'UNC'; 'UPenn'; 'MIT'; 'Stanford'; 'Homemade'}
    end
end
