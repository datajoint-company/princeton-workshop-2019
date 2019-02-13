%{
# reference.User
-> reference.Lab
user:                   varchar(63)     # username
----- 
password:		        varchar(63)     # password
email=null:		        varchar(63)     # email address
first_name=null:        varchar(31)     # first name
last_name=null:		    varchar(31)     # last name
date_joined=null:	    datetime	    # date joined
is_active:		        boolean		    # active
is_staff:		        boolean		    # staff status
is_superuser:	        boolean		    # superuser status
is_stock_manager:       boolean         # stock manager status
%}

classdef User < dj.Manual
end