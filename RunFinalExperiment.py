import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
sys.path.append("/nrn/lib/python")


from neuron import h
import numpy as np
from T6_Sim import Type6_Model
from Experiment import Experiment
from UtilityFuncs import makePlot
from UtilityFuncs import calcDistances

#%%%%%%%%%%%%%%%%%% Passive Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
ex = Experiment(T6, 100, 32, -40)

# all active conductances = 0
T6.settings.hcn2_gpeak = 0
T6.settings.Kv1_2_gpeak = 0
T6.settings.Cav_L_gpeak = 0

# set exc and inh conductances for passive model determined in Estimate_Exc_and_Inh.py
T6.settings.excSyn['gmax'] = 370
T6.settings.inhSyn['gmax'] = 0 # turn off all inhibitory synapses. We will turn them on one-by-one below.

#Run inhibition for each inh synapse and save data
T6.update()
ex.LoopThoughInhibitorySynapses('results\\passive\\', 1.5e-3)


#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
ex = Experiment(T6, 750, 32, -35)

#%% set up active conductances, synapse strengths, and experiment timing
T6.settings.hcn2_gpeak = .78
T6.settings.Kv1_2_gpeak = 11
T6.settings.Cav_L_gpeak = 2.1

T6.settings.excSyn['gmax'] = 370
inhG = 9400

T6.settings.excSyn['start'] = 500
T6.settings.inhSyn['start'] = 700

T6.update()

#%% increas all taus
for sec in h.allsec():
    for seg in sec:
        seg.Ca.mTauMult = 1
        seg.Ca.hTauMult = 1
        seg.Kv1_2.mTauMult = 1
        seg.Kv1_2.hTauMult = 1
        
        


#%%
#Run inhibition for each inh synapse and save data
ex.LoopThoughInhibitorySynapses('results\\active\\', 6.2e-3)
