%{
subject_id: varchar(64)  # id of the subject (e.g. ANM244028)
-----
-> subject.Species
-> subject.Strain
-> reference.AnimalSource
sex = 'U': enum('M', 'F', 'U')
date_of_birth = null: date
subject_description = '':   varchar(1024)
%}

classdef Subject < dj.Manual
end