# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:33:51 2023

@author: dis006
"""


from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

# Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12
T6.settings.hcn2_gpeak = .78

#%% create experiment object
ex = Experiment(T6)
ex.tstop = 1500

#%% small spot
T6.settings.excSyn.frequency = 3000
T6.settings.excDark.frequency = 1000

T6.settings.excSyn.gMax = 4e-6
T6.settings.excDark.gMax = T6.settings.excSyn.gMax

T6.settings.inhSyn.gMax = 0

T6.update()
ex.run()
smallSpotV = np.array(ex.rec.ribV[0])
ex.makePlot(ex.time,smallSpotV ,  xmin = 200)
ribV = ex.averageRibVoltage()

#%% large spot (all inhibitory activated)
T6.settings.inhSyn.frequency = 1000

T6.settings.inhSyn.gMax = 1e-5

T6.update()
ex.run()
bigSpotV = np.array(ex.rec.ribV[0])

ex.makePlot(ex.time, bigSpotV,  xmin = 200)
ribV = ex.averageRibVoltage()

#%%
base = 1e-5
n=1
inds = T6.nNearestInh(n)
T6.settings.inhSyn.gMax = base * 120 / n
T6.update()
inhV = ex.loopThroughInhibitorySynapses(inds)

#%%
inds = T6.nNearestInh(100)

T6.settings.inhSyn.gMax = 0
T6.update()
excV = ex.loopThroughInhibitorySynapses([[0]])

#%%
delta = excV - inhV
delta = np.sort(delta, axis = 1)# sort by low to high hyperpolarization for each trial

nRibbons = len(T6.ribbons.sec)
quartileN = round(nRibbons/4)

quartile1 = np.mean(delta[:, 0 : quartileN], axis = 1)
quartile4 = np.mean(delta[:, quartileN*3-1 : ], axis = 1)

q1Toq4Decay = 1 - quartile1 / quartile4