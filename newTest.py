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
ex.makePlot(ex.time, ex.rec.ribV[0],  xmin = 200)
ribV = ex.averageRibVoltage()

#%% large spot (all inhibitory activated)
T6.settings.inhSyn.frequency = 1000

T6.settings.inhSyn.gMax = 1e-5

T6.update()
ex.run()
ex.makePlot(ex.time, ex.rec.ribV[0],  xmin = 200)
ribV = ex.averageRibVoltage()

#%%

ex.loopThroughInhibitorySynapses([[*range(0,119)]])
