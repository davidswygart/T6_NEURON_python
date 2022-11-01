# -*- coding: utf-8 -*-
# Test model when simultaneously activating n nearest inhibitory synapses

from T6_Sim import Type6_Model
from Experiment import Experiment

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12
T6.settings.hcn2_gpeak = .78
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.inhSyn['gmax'] = 8000

ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
ex.tstop = 600

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=1
T6.settings.inhSyn['gmax'] = 8000 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=2
T6.settings.inhSyn['gmax'] = 8000 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=4
T6.settings.inhSyn['gmax'] = 8000 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=6
T6.settings.inhSyn['gmax'] = 8100 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=8
T6.settings.inhSyn['gmax'] = 8200 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=12
T6.settings.inhSyn['gmax'] = 8500 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=16
T6.settings.inhSyn['gmax'] = 8800 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=22
T6.settings.inhSyn['gmax'] = 9000 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=27
T6.settings.inhSyn['gmax'] = 9100 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=32
T6.settings.inhSyn['gmax'] = 9200 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=36
T6.settings.inhSyn['gmax'] = 9250 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=40
T6.settings.inhSyn['gmax'] = 9300 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=45
T6.settings.inhSyn['gmax'] = 9700 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=50
T6.settings.inhSyn['gmax'] = 10000 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=57
T6.settings.inhSyn['gmax'] = 10600 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=64
T6.settings.inhSyn['gmax'] = 11300 /n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\range\\nNearest\\n' + str(n));
#data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);