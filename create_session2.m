dj.createSchema()

session2.Mouse
session2.Session

% Insert the following data into the table
    
mouse_data = {
    0 '2018-03-01' 'M'
    1 '2017-11-19' 'M'
    2 '2017-11-20' 'unknown'
    5 '2017-12-25' 'F'
    10 '2018-01-01' 'F'
    11 '2018-01-03' 'F'
    100 '2018-05-12' 'F'
    };


session_data = {
    0 '2018-05-15' 0 'Shan Shen'
    0 '2018-05-19' 0 'Shan Shen'
    5 '2018-01-05' 1 'Dimitri Yatsenko'
    100 '2018-05-25' 100 'Edgar Y. Walker' 
    };

inserti(session2.Mouse, mouse_data)
inserti(session2.Session, session_data)