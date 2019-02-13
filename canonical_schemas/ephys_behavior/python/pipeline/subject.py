'''
Schema of subject information.
'''
import datajoint as dj
from . import reference

schema = dj.schema('workshop_gi2017_subject')


@schema
class Species(dj.Lookup):
    definition = """
    species: varchar(24)
    """
    contents = zip(['Mus musculus'])


@schema
class Strain(dj.Lookup): 
    definition = """ 
    strain: varchar(24)
    """
    contents = zip(['C57BL6', 'Ai35D', 'VGAT-ChR2-EYFP', 'PV-Cre', 'N/A'])
  
    
@schema
class StrainAlias(dj.Lookup):
    definition = """  # Other animal strain names that may be used interchangeably in different studies
    strain_alias: varchar(24)
    ---
    -> Strain
    """
    contents = [
            ['C57BL6', 'C57BL6'],
            ['B6', 'C57BL6'],
            ['C57Bl/6', 'C57BL6'],
            ['Ai35D', 'Ai35D'],
            ['PV-IRES-Cre', 'PV-Cre'],
            ['VGAT-ChR2-EYFP', 'VGAT-ChR2-EYFP'],
            ['VGAT-ChR2(H134R)-EYFP', 'VGAT-ChR2-EYFP'],
            ['N/A', 'N/A']
            ]


@schema
class Allele(dj.Lookup):
    definition = """
    allele_name: varchar(128)
    """
    contents = zip(
        ['L7-cre', 'rosa26-lsl-ChR2-YFP']
    )


@schema
class Subject(dj.Manual):  # temporarily remove species, strain and animalsource
    definition = """
    subject_id: varchar(64)  # id of the subject (e.g. ANM244028)
    ---
    -> Species
    -> Strain
    -> reference.AnimalSource
    sex = 'U': enum('M', 'F', 'U')
    date_of_birth = NULL: date
    subject_description=null:   varchar(1024) 
    """
    
    
@schema
class Zygosity(dj.Manual):
    definition = """
    -> Subject
    -> Allele
    ---
    zygosity:  enum('Homozygous', 'Heterozygous', 'Negative', 'Unknown')
    """