%{
animal_source: varchar(32)      # source of the animal; Jax; Charles River etc.
%}

classdef AnimalSource < dj.Lookup
    
    properties
        contents = {'Jackson'; 'Charles River'; 'Guoping Feng'; 'Homemade'}
    end
    
end
