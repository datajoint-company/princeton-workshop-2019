import datajoint as dj
from . import reference, subject

schema = dj.schema('workshop_colony_action')


@schema
class Weighing(dj.Manual):
    # <class 'actions.models.Weighing'>
    definition = """
    -> subject.Subject
    weighing_time:		datetime		# date time
    ---
    weight:			    float			# weight
    -> reference.User
    """