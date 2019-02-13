%{
-> subject.Subject
-> subject.Allele
-----
zygosity:  enum('Homozygous', 'Heterozygous', 'Negative', 'Unknown')
%}

classdef Zygosity < dj.Manual
end