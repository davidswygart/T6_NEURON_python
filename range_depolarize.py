# -*- coding: utf-8 -*-
# Test model over a range of depolarization steps

from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
T6.settings.Cav_L_gpeak = 1.62
T6.settings.hcn2_gpeak = .78
T6.settings.Kv1_2_gpeak = 12

ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% depol = -43 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.excSyn['gmax'] = 922 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 1100  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\depol\\n43_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% depol = -40 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.excSyn['gmax'] = 1350 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 3100  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\depol\\n40_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% depol = -35 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\depol\\n35_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% depol = -30 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.excSyn['gmax'] = 5300 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 14000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\depol\\n30_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% depol = -25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.excSyn['gmax'] = 11600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 22000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\depol\\n25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% depol = -20 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.excSyn['gmax'] = 30000 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 30000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\depol\\n20_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% depol = -15 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.excSyn['gmax'] = 150000 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 38000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\depol\\n15_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);