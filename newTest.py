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

#%% create experiment object
ex = Experiment(T6)
ex.tstop = 600

#%%
ex.run()
ex.makePlot(ex.time, ex.rec.ribV[0])

#data = ex.LoopThoughInhibitorySynapses(folder = 'results\\active\\');
#inds = T6.nNearestInh(1)
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

