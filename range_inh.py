# -*- coding: utf-8 -*-
# Test model over a range of inhibitory steps

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
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)

#%%%%%%%%%%%%%%%%%% inh = -50 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.inhSyn['gmax'] = 150000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\inh\\n50_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% inh = -47.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.inhSyn['gmax'] = 18000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\inh\\n47p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% inh = -45 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\inh\\n45_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% inh = -42.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.inhSyn['gmax'] = 4050  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\inh\\n42p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% inh = -40 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.inhSyn['gmax'] = 2050  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\inh\\n40_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% inh = -37.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.inhSyn['gmax'] = 717  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\inh\\n37p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% inh = -36 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.inhSyn['gmax'] = 135  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\inh\\n36_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
