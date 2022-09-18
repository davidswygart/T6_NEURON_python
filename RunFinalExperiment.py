from T6_Sim import Type6_Model
from Experiment import Experiment

# Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()

#%% create experiment object
ex = Experiment(T6)

T6.settings.excSyn['start'] = 200
T6.settings.inhSyn['start'] = 400
ex.tstop = 600

#%%%%%%%%%%%%%%%%%% Passive Model %%%%%%%%%%%%%%%%%%%%%%%%
# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 334 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.5 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 1550  #conductance at single inhibitory synapse

T6.update()

data = ex.LoopThoughInhibitorySynapses(folder ='results\\passive\\');
# inh #9 and ribbon #24 are the ones used in the example trace

#%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
T6.settings.hcn2_gpeak = .78
T6.settings.Kv1_2_gpeak = 11
T6.settings.Cav_L_gpeak = 1.62

# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 4000 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 9600  #conductance at single inhibitory synapse

T6.update()

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\active\\');

# %%%%%%%%%%%%%%%%%% create example trace for figure %%%%%%%%%%%%%%%%%%%%%%%%
ex.LoopThoughInhibitorySynapses(inhInds=[9]);
