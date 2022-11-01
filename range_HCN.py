# -*- coding: utf-8 -*-
# Test model over a range of HCN conductances

from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12

ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% HCN conductance = 0 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 0
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x0_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance * 0.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 0.25
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x0p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance * 0.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 0.5
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x0p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance * 0.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 0.75
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x0p75_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance = normal %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x1_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance * 1.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 1.25
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x1p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance * 1.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 1.5
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x1p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance * 1.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 1.75
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x1p75_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% HCN conductance * 2 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78 * 2
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\HCN\\x2_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);