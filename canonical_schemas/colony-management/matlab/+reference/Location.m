%{
# reference.Location
# The physical location at which an session is performed or appliances are located.
# This could be a room, a bench, a rig, etc.
-> reference.Lab
location:                   varchar(31)
-----
location_description='':    varchar(255)
%}

classdef Location < dj.Lookup
    properties
        contents = {
            'tanklab', 'Benzos2',  ''
            'tanklab', 'Benzos3',  ''
            'tanklab', 'vivarium', ''
            'tanklab', 'pni-171jppw32', ''
            'tanklab', 'pni-174cr4jk2', ''
            }
    end
end