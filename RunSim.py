# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:42:58 2019

@author: david
"""
 cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python

from neuron import h, gui, units
from settings import Settings

settings = Settings() #Load settings (eg. experimental setup, physiology parameters, display settings)
h.load_file("T6_V3.hoc")

ncList = list()

XYZ_rib = ReadLocation("InputData/RibbonLocations.txt")
XYZ_both = ReadLocation("InputData/BothLocations.txt")
XYZ_inh = ReadLocation("InputData/InhSynLocations.txt")

