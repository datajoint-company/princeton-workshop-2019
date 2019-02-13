%{
allele:                     varchar(63)     # informal name
-----
standard_name='':		    varchar(255)	# standard name
-> subject.Source
original_allele_source:     varchar(255)    # original source of the allele
allele_description='':      varchar(1023)   # description of the allele
%}

classdef Allele < dj.Lookup
    properties
        contents = {
                'Thy1-GP5.3', 'Thy1-GCaMP6f', 'Jax Lab', 'David W. Tank, Princeton University', ''
                'Ai93', '(TITL-GCaMP6f)-D', 'Jax Lab', 'Allen Institute', ''
                'Ai148', '(TIT2L-GC6f-ICL-tTA2)-D', 'Jax Lab', 'Allen Institute', ''
                'Thy1-YFP', '', 'Jax Lab', 'Joshua R Sanes, Harvard University', ''
                'VGAT-ChR2-EYFP', 'Slc32a1-COP4*H134R/EYFP', 'Jax Lab', 'Guoping Feng, Massachusetts Institute of Technology', ''
                'Emx1-Cre', 'Emx-IRES-Cre', 'Jax Lab', 'Kevin R. Jones, University of Colorado- Boulder', ''
                'D1-Cre', 'Drd1-cre', 'Jax Lab', 'Ming Xu, University of Chicago', ''
                'D2-Cre', 'Drd2-cre', 'Jax Lab', 'Unknown', ''
                'DAT-IRES-Cre', 'Slc6a3tm1.1(cre)Bkmn', 'Jax Lab', 'Cristina M Backman, National Institute on Drug Abuse (NIH)', ''
                'Slc17a7-IRES2-Cre', '', 'Jax Lab', 'Allen Institute', ''
            }
    end
end