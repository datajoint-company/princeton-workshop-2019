import datajoint as dj

schema = dj.schema('workshop_colony_reference')


@schema
class Lab(dj.Lookup):
    definition = """
    lab:                    varchar(63)  # name of lab
    ---
    institution:            varchar(127)
    address:                varchar(127)
    time_zone:              varchar(127)
    """
    contents = [['tanklab', 'Princeton', 'Princeton Neuroscience Institute, Princeton University Princeton, NJ 08544', 'America/New_York']]

@schema
class User(dj.Manual):
    definition = """
    -> Lab
    user:		            varchar(63)	    # username
    ---
    password:		        varchar(63)	    # password
    email=null:		        varchar(63)	    # email address
    first_name=null:        varchar(31)	    # first name
    last_name=null:		    varchar(31)	    # last name
    date_joined=null:	    datetime	    # date joined
    is_active:		        boolean		    # active
    is_staff:		        boolean		    # staff status
    is_superuser:	        boolean		    # superuser status
    is_stock_manager:       boolean         # stock manager status
    """


@schema
class Location(dj.Lookup):
    definition = """
    # The physical location at which an session is performed or appliances are located.
    # This could be a room, a bench, a rig, etc.
    -> Lab
    location:                   varchar(31)    # name of the location
    ---
    location_description='':    varchar(255)
    """
    contents = [
        ['tanklab', 'Benzos2',  ''],
        ['tanklab', 'Benzos3',  ''],
        ['tanklab', 'vivarium', ''],
        ['tanklab', 'pni-171jppw32', ''],
        ['tanklab', 'pni-174cr4jk2', '']
        ]


@schema
class Project(dj.Lookup):
    definition = """
    project:                    varchar(31)
    ---
    project_description=null:   varchar(1023)
    """
    contents = [['mouse behavior', '']]


@schema
class ProjectUser(dj.Manual):
    definition = """
    -> Project
    -> User
    """

