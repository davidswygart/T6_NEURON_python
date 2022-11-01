# -*- coding: utf-8 -*-
# Test model over a range of calcium conductances

from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()

T6.settings.hcn2_gpeak = .78
T6.settings.Kv1_2_gpeak = 12


ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
ex.tstop = 600


#%%%%%%%%%%%%%%%%%% Ca conductance = 0 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 0
T6.settings.excSyn['gmax'] = 3600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8700  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x0_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance * 0.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 0.25
T6.settings.excSyn['gmax'] = 3300 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8600  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x0p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance * 0.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 0.5
T6.settings.excSyn['gmax'] = 3100 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8500  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x0p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance * 0.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 0.75
T6.settings.excSyn['gmax'] = 2850 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8300  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x0p75_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance = normal %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x1_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance * 1.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 1.25
T6.settings.excSyn['gmax'] = 2400 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7700  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x1p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance * 1.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 1.5
T6.settings.excSyn['gmax'] = 2200 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7450  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x1p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance * 1.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 1.75
T6.settings.excSyn['gmax'] = 2000 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7200  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x1p75_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);
#%%%%%%%%%%%%%%%%%% Ca conductance * 2 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Cav_L_gpeak = 1.62 * 2
T6.settings.excSyn['gmax'] = 1800 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ca\\x2_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);