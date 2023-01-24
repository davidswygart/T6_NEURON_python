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

#%%
T6.settings.excSyn.start = 500
T6.settings.excSyn.stop = 1000



T6.settings.excSyn.frequency = 2000
T6.settings.excDark.frequency = 600

T6.settings.excSyn.gMax = 5e-6
T6.settings.excDark.gMax = T6.settings.excSyn.gMax

T6.update()
ex.run()
ex.makePlot(ex.time, ex.rec.ribV[0],  xmin = 200)

#data = ex.LoopThoughInhibitorySynapses(folder = 'results\\active\\');
#inds = T6.nNearestInh(1)
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

