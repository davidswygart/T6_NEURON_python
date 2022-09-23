from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

# Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()

#%% create experiment object
ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% Passive Model %%%%%%%%%%%%%%%%%%%%%%%%
# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 334 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.5 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 1530  #conductance at single inhibitory synapse

T6.update()

#data = ex.LoopThoughInhibitorySynapses(folder ='results\\passive\\');

ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
for sec in T6.h.allsec():
    for seg in sec:
        seg.Kv1_2.mVHalf = -9
        seg.Kv1_2.mVWidth = 14
        seg.Kv1_2.mTauMult = 1
        
        seg.Kv1_2.hVHalf = 8
        seg.Kv1_2.hVWidth = -9
        seg.Kv1_2.hTauMult = 0.1
        
        seg.hcn2.mTauMult = 1
        seg.Ca.mTauMult = 1
        seg.Ca.hTauMult = 1
        T6.settings.cm = 1.18

T6.settings.hcn2_gpeak = .78
T6.settings.Kv1_2_gpeak = 12
T6.settings.Cav_L_gpeak = 1.62


# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse

T6.update()

#data = ex.LoopThoughInhibitorySynapses(folder = 'results\\active\\');
data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
# %%%%%%%%%%%%%%%%%% create example trace for figure %%%%%%%%%%%%%%%%%%%%%%%%
# inh #16 (axon[98](0.551036)) and ribbon #90 (axon[36](0.818943)) are the ones used in the example trace

ex.LoopThoughInhibitorySynapses(inhInds=[16]);
i9_trace = np.array(ex.rec.inhV[16])
r24_trace = np.array(ex.rec.ribV[90])
t = (ex.time-T6.settings.excSyn['start']) / 1000

import os
folder = 'results\\exampleTrace\\'
os.makedirs(folder, exist_ok = True)
np.savetxt(folder+ 'time.csv', t, delimiter=',')
np.savetxt(folder+ 'inhibitory16.csv', i9_trace, delimiter=',')
np.savetxt(folder+ 'ribbon90.csv', r24_trace, delimiter=',')


# %% calculating cumalative currents
excCurrent = 0
for syn in T6.excSyns.syn:
    excCurrent += syn.i
print('excitatory current = ', round(excCurrent*1000), ' (pA)')

inhCurrent = 0
for syn in T6.inhSyns.syn:
    inhCurrent += syn.i
print('inhibitory current = ', round(inhCurrent*1000), ' (pA)')

kCurrent = 0
for sec in T6.h.allsec():
    for seg in sec:
        kCurrent += seg.ik
print('k+ current = ', round(kCurrent*1000), ' (pA)') #471 pA difference between exc and inh
        
    


