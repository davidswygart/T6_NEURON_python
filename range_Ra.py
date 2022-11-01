# -*- coding: utf-8 -*-
# Test model over a range of axial resistivity

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
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x0p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% axial resistivity * 0.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 0.5
T6.settings.excSyn['gmax'] = 2340 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 10500  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x0p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% axial resistivity * 0.75 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 0.75
T6.settings.excSyn['gmax'] = 2470 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 9100  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x0p75_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% axial resistivity * 1 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 1
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x1_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% axial resistivity * 1.25 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 1.25
T6.settings.excSyn['gmax'] = 2760 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 7000  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x1p25_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% axial resistivity * 1.5 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 1.5
T6.settings.excSyn['gmax'] = 2940 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 6300  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x1p5_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% axial resistivity * 2 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 2
T6.settings.excSyn['gmax'] = 3340 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 5300  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x2_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);

#%%%%%%%%%%%%%%%%%% axial resistivity * 4 %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.Ra = 132 * 4
T6.settings.excSyn['gmax'] = 6000 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 3100  #conductance at single inhibitory synapse
T6.update()
data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\Ra\\x4_');
#data = ex.LoopThoughInhibitorySynapses(inhInds=[16]);