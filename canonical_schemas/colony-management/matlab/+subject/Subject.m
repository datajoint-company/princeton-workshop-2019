%{
# subject.Subject
subject_nickname:		    varchar(63)		# nickname
---
sex:			            enum("M", "F", "U")	# sex
subject_birth_date=null:	date			    # birth date
ear_mark='':			    varchar(7)		# ear mark
-> subject.Line
-> subject.Source
-> reference.User
protocol_number:            int         	# protocol number
subject_description='':     varchar(1023)

%}

classdef Subject < dj.Manual
end