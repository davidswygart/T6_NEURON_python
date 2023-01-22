# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:46:09 2023

@author: david
"""

from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

# Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()

#%% create experiment object
ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%

T6.settings.hcn2_gpeak = .78
T6.settings.Kv1_2_gpeak = 12
T6.settings.Cav_L_gpeak = 1.62


# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse

T6.update()

#data = ex.LoopThoughInhibitorySynapses(folder = 'results\\active\\');
inds = T6.nNearestInh(1)
data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%% calculate membrane area for each segment (um2)

segArea = []

for sec in T6.h.allsec():
    for seg in sec:
        segArea.append(seg.area())
segArea = np.expand_dims(np.array(segArea),1)
        
plt.hist(segArea)

#%% calculate conductance in each section
plt.figure()
t = np.array(ex.time)


# HCN2 and leak conductance are in units of S/cm2
Um2Tocm2 = 1e-8

gCa = np.array(ex.rec.gCa) * segArea * Um2Tocm2
gCaTotal = np.sum(gCa, axis=0)
plt.plot(t,gCaTotal)


gKv = np.array(ex.rec.gKv1_2) * segArea * Um2Tocm2
gKvTotal = np.sum(gKv, axis=0)
plt.plot(t,gKvTotal)


gHCN2 = np.array(ex.rec.gHCN2)  * segArea * Um2Tocm2
gHCN2Total = np.sum(gHCN2, axis=0)
plt.plot(t,gHCN2Total)
        
gLeak = T6.settings.g_pas * segArea * Um2Tocm2
gLeakTotal = np.sum(gLeak)
gLeakTotal = np.repeat(gLeakTotal, len(gHCN2Total), axis=0)
plt.plot(t,gLeakTotal)

plt.title('total conductances')
plt.ylabel("S")
plt.xlabel('ms')
plt.legend(['Ca','Kv', 'Hcn2', 'leak'])

cellConductance = gCaTotal + gKvTotal + gHCN2Total + gLeakTotal

# plot resistance

plt.figure()
plt.plot(t, 1/gLeakTotal / 1e6)

effectiveResistance = 1/cellConductance / 1e6;
plt.plot(t, effectiveResistance)
plt.title('effective membrane resistance')
plt.ylabel("MOhm")
plt.xlabel('ms')
plt.legend(['passive', 'active'])

#%%%%%%%%%%%%%%%%%% increase leak conductance equally accross whole cell in place of active conductances %%%%%%%%%%%%%%%%%%%%%%%%


# no active conductances
T6.settings.hcn2_gpeak = 0
T6.settings.Kv1_2_gpeak = 0
T6.settings.Cav_L_gpeak = 0




# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse

#T6.update()

#data = ex.LoopThoughInhibitorySynapses(folder = 'results\\active\\');
#inds = T6.nNearestInh(1)
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

        