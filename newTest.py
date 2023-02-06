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

#%% small spot (-45 mV -> -30 mV)
T6.settings.excDark.frequency = 70
T6.settings.excSyn.frequency = 500


T6.settings.excSyn.gMax = 1.12e-5
T6.settings.excDark.gMax = T6.settings.excSyn.gMax

T6.settings.inhSyn.gMax = 0

T6.update()
ex.run()
smallSpotVRib1 = np.array(ex.rec.ribV[0])
smallSpotVRib2 = np.array(ex.rec.ribV[24])
ex.makePlot(ex.time,smallSpotVRib1 ,  xmin = 100)
ex.averageRibVoltage(startTimeMs=300, endTimeMs =500) #preTime average
a=ex.averageRibVoltage(startTimeMs=500, endTimeMs=1000) #postTime average

#%% large spot (all inhibitory activated) (-39.1 mV == CSR 1.1)
T6.settings.inhSyn.frequency = 79

T6.settings.inhSyn.gMax = 1e-5

T6.update()
ex.run()
bigSpotVRib1 = np.array(ex.rec.ribV[0])
bigSpotVRib2 = np.array(ex.rec.ribV[24])

ex.makePlot(ex.time, bigSpotVRib1,  xmin = 100)
ribV = ex.averageRibVoltage(startTimeMs=500, endTimeMs=1000) #postTime average




#%% large spot (but only 2 inhibitory synapses activated) (far left example inh = inh #9 & 11 on section axon[83])
T6.settings.inhSyn.frequency = 79

T6.settings.inhSyn.gMax = 1e-5
T6.update()

for con in T6.inhSyns.con: #turn off all ihibitory synapses
    con.weight[0] = 0

inds = [9,11] # example pair of inh synapses
for i in inds: #turn on select ihibitory synapses
    T6.inhSyns.con[i].weight[0] = T6.settings.inhSyn.gMax * 120 / 2 # inhibition normalized by number activated

ex.run()
bigSpotVRib1 = np.array(ex.rec.ribV[0])
bigSpotVRib2 = np.array(ex.rec.ribV[24])

#%% plot large and small simultaneously for both examples

f, (ax1, ax2)  = plt.subplots(nrows = 2)

ax1.plot(ex.time, smallSpotVRib1, label='no inh.')
ax1.plot(ex.time, bigSpotVRib1, label='with inh.')
ax1.plot([500,500],[-60,-20])
ax1.plot([1000,1000],[-60,-20])

ax2.plot(ex.time, smallSpotVRib2, label='no inh.')
ax2.plot(ex.time, bigSpotVRib2, label='with inh.')
ax2.plot([500,500],[-60,-20])
ax2.plot([1000,1000],[-60,-20])

plt.legend()

plt.plot([500,500],[-60,-20])
plt.plot([1000,1000],[-60,-20])
plt.show()



# #%%
# base = 1e-5
# n=1
# inds = T6.nNearestInh(n)
# T6.settings.inhSyn.gMax = base * 120 / n
# T6.update()
# inhV = ex.loopThroughInhibitorySynapses(inds)

# #%%
# inds = T6.nNearestInh(100)

# T6.settings.inhSyn.gMax = 0
# T6.update()
# excV = ex.loopThroughInhibitorySynapses([[0]])

# #%%
# delta = excV - inhV
# delta = np.sort(delta, axis = 1)# sort by low to high hyperpolarization for each trial

# nRibbons = len(T6.ribbons.sec)
# quartileN = round(nRibbons/4)

# quartile1 = np.mean(delta[:, 0 : quartileN], axis = 1)
# quartile4 = np.mean(delta[:, quartileN*3-1 : ], axis = 1)

# q1Toq4Decay = 1 - quartile1 / quartile4