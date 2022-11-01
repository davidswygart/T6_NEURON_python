# -*- coding: utf-8 -*-
# Test model over a range of K+ conductances

from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()

T6.settings.hcn2_gpeak = .78

T6.settings.Cav_L_gpeak = 1.62

ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% K conductance = normal %%%%%%%%%%%%%%%%%%%%%%%%

T6.settings.Kv1_2_gpeak = 12

# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse

T6.update()

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x1_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);


#%%%%%%%%%%%%%%%%%% K conductance = 0 %%%%%%%%%%%%%%%%%%%%%%%%
# Doesn't work because without any K+ to counteract calcium, there is a runaway depolarization
#%%%%%%%%%%%%%%%%%% K conductance * 0.1 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * .1
T6.settings.excSyn['gmax'] = 65 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 650  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x0p1_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);


#%%%%%%%%%%%%%%%%%% K conductance * 0.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * 0.25
T6.settings.excSyn['gmax'] = 410 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 2550  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x0p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% K conductance * 0.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * 0.5
T6.settings.excSyn['gmax'] = 1050 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 5000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x0p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% K conductance * 0.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * 0.75
T6.settings.excSyn['gmax'] = 1790 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 6700  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x0p75_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% K conductance * 1.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * 1.25
T6.settings.excSyn['gmax'] = 3600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8800  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x1p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% K conductance * 1.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * 1.5
T6.settings.excSyn['gmax'] = 4700 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 9500  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x1p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% K conductance * 1.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * 1.75
T6.settings.excSyn['gmax'] = 6050 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 10200  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x1p75_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% K conductance * 2 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Kv1_2_gpeak = 12 * 2
T6.settings.excSyn['gmax'] = 7500 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 10500  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\K\\x2_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
