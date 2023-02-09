# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:16:15 2023

@author: dis006
"""

#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()

##%% set active conductances
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12
T6.settings.hcn2_gpeak = .78

T6.settings.excSyn.gMax = 0
T6.settings.inhSyn.gMax = 0


#%% create experiment object
ex = Experiment(T6)
ex.tstop = 500


#%%################ Set Exc ################################## (-45 mV -> -30 mV)
ex.placeVoltageClamp(-38, 1e15, -38)
vclamp = ex.vClamp
#%%
#vclamp =T6.h.SEClamp(T6.inhSyns.seg[0])
#vclamp.dur1 = 1e9
#%%
ex.tstop = 1000
ex.vClampSineWave(frequency=100, baselineV=-38, amplitudeV=7)



