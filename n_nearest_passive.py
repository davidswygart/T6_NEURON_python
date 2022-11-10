# -*- coding: utf-8 -*-
# Test model when simultaneously activating n nearest inhibitory synapses
# For passive model

from T6_Sim import Type6_Model
from Experiment import Experiment

#%%%%%%%%%%%%%%%%%% Passive Model %%%%%%%%%%%%%%%%%%%%%%%%
T6 = Type6_Model()
T6.settings.excSyn['gmax'] = 334 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.5 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 1530  #conductance at single inhibitory synapse

ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
ex.tstop = 600

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=1
T6.settings.inhSyn['gmax'] = 1500 / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
#data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=2
T6.settings.inhSyn['gmax'] = 1500  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
#data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=4
T6.settings.inhSyn['gmax'] = 1500  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=8
T6.settings.inhSyn['gmax'] = 1500  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=16
T6.settings.inhSyn['gmax'] = 1500  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=30
T6.settings.inhSyn['gmax'] = 1510  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=45
T6.settings.inhSyn['gmax'] = 1520  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=60
T6.settings.inhSyn['gmax'] = 1520  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=75
T6.settings.inhSyn['gmax'] = 1520 / n   #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=90
T6.settings.inhSyn['gmax'] = 1520  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=105
T6.settings.inhSyn['gmax'] = 1530  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n=120
T6.settings.inhSyn['gmax'] = 1550  / n  #conductance at single inhibitory synapse
T6.update()
inds = T6.nNearestInh(n)
data = ex.LoopThoughInhibitorySynapses(inhLists=inds, folder = 'results\\range\\nNearest_passive\\n' + str(n));
# data = ex.LoopThoughInhibitorySynapses(inhLists= [inds[16]]);

