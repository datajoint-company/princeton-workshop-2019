%{
# subject.Zygosity
-> subject.Subject
-> subject.Allele
-----
zygosity:		    enum("Present", "Absent", "Homozygous", "Heterozygous")  # zygosity
%}

classdef Zygosity < dj.Manual
end