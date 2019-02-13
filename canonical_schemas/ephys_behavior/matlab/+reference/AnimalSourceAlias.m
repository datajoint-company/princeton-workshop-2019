%{
animal_source_alias: varchar(32)      # other names for source of the animal, Jax, Charles River etc.
-----
-> reference.AnimalSource
%}


classdef AnimalSourceAlias < dj.Lookup
    properties
     contents = {
                'Jackson', 'Jackson'
                'Homemade', 'Homemade'
                'Jax', 'Jackson'
                'JAX', 'Jackson'
                'Charles River', 'Charles River'
                'Guoping Feng', 'Guoping Feng'
                }

    end
end