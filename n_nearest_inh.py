# -*- coding: utf-8 -*-
# Test model when simultaneously activating n nearest inhibitory synapses

from T6_Sim import Type6_Model
from Experiment import Experiment

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12
T6.settings.hcn2_gpeak = .78

ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% axial resistivity * 0.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 0.25
T6.settings.excSyn['gmax'] = 2230 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 12400  #conductance at single inhibitory synapse
T6.update()
#data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x0p25_');
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\test', inhLists=[[16]]);