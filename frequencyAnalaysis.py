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
ex.placeVoltageClamp(-60, 1e15, -60)
#ex.vClamp.dur1 = 1e15
vclamp = ex.vClamp
#%%
#vclamp =T6.h.SEClamp(T6.inhSyns.seg[0])
#vclamp.dur1 = 1e9
#%%

endTime = 2000
frequency = 4
baseVolts = -38
amplitude = 7

ex.tstop = endTime
t = np.linspace(0,endTime, round(endTime/T6.h.dt))
sin = np.sin(frequency * t * 2* np.pi / 1000) * amplitude + baseVolts
sin = T6.h.Vector(sin)

sin.play(vclamp._ref_amp1, T6.h.dt)       
     

#T6.h.run()
ex.run()

sin.play_remove()
plt.plot(ex.time, ex.rec.ribV[0])

# driving stimulus
#t = T6.h.Vector(np.linspace(0, 2* np.pi, 4000))
#y = T6.h.Vector(np.sin(t))*10000
#t = t*20

#b =  y.play(T6.inhSyns.seg[0]._ref_v, t, True)
#b =  y.play(ex.vClamp._ref_vc, t, True)

#T6.h.finitialize(-60)
#T6.h.continuerun(200)
#plt.plot(ex.rec.ribV[0])
#plt.plot(y/10)
#ex.run()
#ex.makePlot(ex.time, np.array(ex.rec.ribV[0]))



