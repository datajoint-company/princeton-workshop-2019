'''
Schema of stimulation information.
'''
import re
import os
from datetime import datetime

import numpy as np
import scipy.io as sio
import datajoint as dj

from . import reference

schema = dj.schema('workshop_gi2017_stimulation')


@schema
class PhotoStimDevice(dj.Lookup):
    definition = """ # Information about the devices used for photo stimulation
    device_name: varchar(32)
    ---
    device_desc = "": varchar(1024)
    """   
    

@schema
class PhotoStimulationInfo(dj.Manual):
   definition = """
   -> reference.ActionLocation
   -> PhotoStimDevice
   photo_stim_excitation_lambda: decimal(6,2)    # (nm) excitation wavelength
   ---
   photo_stim_method = 'laser' : enum('fiber', 'laser')
   photo_stim_duration = null:                float        # in ms, stimulus duration
   photo_stim_shape = '':                   varchar(24)  # shape of photostim, cosine or pulsive
   photo_stim_freq = null:                    float        # in Hz, frequency of photostimulation
   photo_stim_notes = '':                varchar(128)
   """  

