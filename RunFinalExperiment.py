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
T6.settings.Kv1_2_gpeak = 12
T6.settings.Cav_L_gpeak = 1.62


# set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse

T6.update()

data = ex.LoopThoughInhibitorySynapses(folder = 'results\\active\\');


# %%%%%%%%%%%%%%%%%% create example trace for figure %%%%%%%%%%%%%%%%%%%%%%%%
ex.LoopThoughInhibitorySynapses(inhInds=[9]);

for sec in T6.h.allsec():
    for seg in sec:
        seg.Kv1_2.mVHalf = -9
        seg.Kv1_2.mVWidth = 14
        seg.Kv1_2.mTauMult = .001#1
        
        seg.Kv1_2.hVHalf = 8
        seg.Kv1_2.hVWidth = -9
        seg.Kv1_2.hTauMult = .0001#.1
        
        seg.hcn2.mTauMult = .001
        seg.Ca.mTauMult = .001
        seg.Ca.hTauMult = .001

# %%%%%%%%%%%%%%%%%% create example trace for figure %%%%%%%%%%%%%%%%%%%%%%%%      
for sec in T6.h.allsec():
    for seg in sec:
        seg.Kv1_2.mVHalf = -9
        seg.Kv1_2.mVWidth = 14
        seg.Kv1_2.mTauMult = 1
        
        seg.Kv1_2.hVHalf = 8
        seg.Kv1_2.hVWidth = -9
        seg.Kv1_2.hTauMult = 0.1
        
        seg.hcn2.mTauMult = 1
        seg.Ca.mTauMult = 1
        seg.Ca.hTauMult = 1
        T6.settings.cm = 1.18
        
        #%%%%%%%%%%%%%%%%%% Active Model %%%%%%%%%%%%%%%%%%%%%%%%
        T6.settings.hcn2_gpeak = .78
        T6.settings.Kv1_2_gpeak = 12
        T6.settings.Cav_L_gpeak = 1.62
        
        T6.settings.excSyn['start'] = 300
        T6.settings.inhSyn['start'] = 300
        ex.tstop = 400

        # set excitation so that average ribbon is -35 mV, and inh that drops to -45 mV
        T6.settings.excSyn['gmax'] = 2600 / 8 # conductance at each excitatory input synapse (8 total)
        T6.settings.excSyn['darkProp'] = 0.2 # proportion that is dark current
        T6.settings.inhSyn['gmax'] = 8000  #conductance at single inhibitory synapse

        T6.update()

        data = ex.LoopThoughInhibitorySynapses(inhInds=[9]);


        
