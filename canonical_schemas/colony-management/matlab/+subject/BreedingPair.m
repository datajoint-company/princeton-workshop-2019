%{
# subject.BreedingPair
breeding_pair:			    varchar(63)		    # name
-----
-> subject.Line
(father)  -> subject.Subject                    # father
(mother)  -> subject.Subject                    # mother
bp_description='':      	varchar(2047)		# description
bp_start_date=null:         date		        # start date
bp_end_date=null:           date			    # end date

%}

classdef BreedingPair < dj.Manual
end