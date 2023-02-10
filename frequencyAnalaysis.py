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
T6.settings.excDark.gMax = 0
T6.settings.inhSyn.gMax = 0
T6.update()


#%% create experiment object
ex = Experiment(T6)
ex.tstop = 500
ex.placeCurrentClamp(T6.soma.seg)



#%% 
ex.tstop = 1000
ex.iClampSineWave(frequency=100, baselineI=.1, amplitudeI=.02)

#%%
startTime = 500
startInd = np.argmin(abs(ex.time-startTime))

data = np.array(ex.iClampRec)
data = data[startInd:]
print(np.sqrt(np.mean((data - np.mean(data))**2)))


data = np.array(ex.rec.ribV[0])
data = data[startInd:]
print(np.sqrt(np.mean((data - np.mean(data))**2)))