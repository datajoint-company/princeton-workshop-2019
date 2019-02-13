import datajoint as dj
from . import reference

schema = dj.schema('workshop_colony_subject')

@schema
class Species(dj.Lookup):
    definition = """
    binomial:			    varchar(63)	# binomial
    ---
    species_nickname:		varchar(63)	# nick name
    """


@schema
class Source(dj.Lookup):
    definition = """
    source:				        varchar(63)	# name of source
    ---
    source_description='':	    varchar(255)	# description
    """


@schema
class Strain(dj.Lookup):
    definition = """
    strain:		                varchar(63)	    # strain name
    ---
    strain_description='':      varchar(255)	# description
    """


@schema
class SequenceType(dj.Lookup):
    definition = """
    sequence_type:              varchar(63)
    ---
    seq_type_description='':    varchar(255)
    """

@schema
class Sequence(dj.Lookup):
    definition = """
    sequence:		            varchar(63)	# informal name
    ---
    -> SequenceType            
    base_pairs='':	            varchar(1023)	# base pairs
    sequence_description='':	varchar(255)	# description
    """


@schema
class Allele(dj.Lookup):
    definition = """
    allele:			            varchar(63)    # informal name
    ---
    standard_name='':		    varchar(255)	# standard name
    -> Source
    original_allele_source='':  varchar(255)    # source of the allele
    allele_description='':      varchar(1023)   # description of the allele
    """


@schema
class AlleleSequence(dj.Lookup):
    definition = """
    -> Allele
    -> Sequence
    """


@schema
class Line(dj.Lookup):
    definition = """
    line:				    varchar(63)	    # name
    ---
    -> Species
    -> Strain
    line_description='':	varchar(2047)	# description
    target_phenotype='':	varchar(255)	# target phenotype
    is_active:				boolean		    # is active
    """


@schema
class LineAllele(dj.Lookup):
    definition = """
    -> Line
    -> Allele
    """


@schema
class Subject(dj.Manual):
    definition = """
    -> reference.Lab
    subject:		            varchar(63)		# nickname
    ---
    sex:			            enum("M", "F", "U")	# sex
    subject_birth_date=null:	date			    # birth date
    ear_mark='':			    varchar(7)		# ear mark
    -> Line
    -> Source
    -> reference.User
    protocol_number:            tinyint         	# protocol number
    subject_description='':     varchar(1023)
    """


@schema
class BreedingPair(dj.Manual):
    definition = """
    breeding_pair:			varchar(63)		        # name
    ---
    -> Line
    bp_description='':	    varchar(2047)		    # description
    bp_start_date='':	    date		            # start date
    bp_end_date='':		    date			        # end date
    -> Subject.proj(father='subject_nickname')      # father
    -> Subject.proj(mother='subject_nickname')      # mother
    """


@schema
class Litter(dj.Manual):
    definition = """
    litter:                         varchar(63)
    ---
    -> BreedingPair
    -> Line
    litter_descriptive_name='':	    varchar(255)	# descriptive name
    litter_description='':	        varchar(255)	# description
    litter_birth_date=null:			date		    # birth date
    """


@schema
class LitterSubject(dj.Manual):
    definition = """
    -> Subject
    ---
    -> Litter
    """


@schema
class SubjectProject(dj.Manual):
    definition = """
    -> Subject
    -> reference.Project
    """


@schema
class Weaning(dj.Manual):
    definition = """
    -> Subject
    ---
    wean_date:			date			# wean date
    """


@schema
class GenotypeTest(dj.Manual):
    definition = """
    -> Subject
    -> Sequence
    genotype_test_id:           varchar(63)
    ---
    test_result:		        enum("Present", "Absent")		# test result
    """


@schema
class Zygosity(dj.Manual):
    definition = """
    -> Subject
    -> Allele
    ---
    zygosity:		    enum("Present", "Absent", "Homozygous", "Heterozygous")  # zygosity
    """


@schema
class Death(dj.Manual):
    definition = """
    -> Subject
    ---
    death_date:                 date                    # death date
    """
