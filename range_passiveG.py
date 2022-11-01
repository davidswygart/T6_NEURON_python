# -*- coding: utf-8 -*-
# Test model over a range of passive conductances

from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12
T6.settings.hcn2_gpeak = .78 * 0

ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% passive leak conductance * 0 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 0
T6.settings.excSyn['gmax'] = 2150 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7500  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\zero_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 0.1 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 0.1
T6.settings.excSyn['gmax'] = 2200 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7600  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x0p1');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 0.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 0.25
T6.settings.excSyn['gmax'] = 2270 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7700  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x0p25');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 0.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 0.5
T6.settings.excSyn['gmax'] = 2390 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7800  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x0p5');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 0.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 0.75
T6.settings.excSyn['gmax'] = 2510 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7900  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x0p75');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance normal %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 10

T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x1');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 1.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 1.25
T6.settings.excSyn['gmax'] = 2760 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8100  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x1p25');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 1.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 1.5
T6.settings.excSyn['gmax'] = 2890 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8180  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x1p5');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 1.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 1.75
T6.settings.excSyn['gmax'] = 3010 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8260  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x1p75');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% passive leak conductance * 2 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.g_pas =  3.91e-5 * 2
T6.settings.excSyn['gmax'] = 3140 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8320  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\leak\\x2');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);






















