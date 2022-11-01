class Settings ():
    """A class to store settings and parameters for the simulation"""

    def __init__(self):
        # passive properties
        self.cm = 1.18              # capacitance (uF/cm2)                                          
        self.Ra = 132               # axial resistivity (Ohm-cm)                                         
        self.e_pas = -60            # leak reversal potential (mV)                                                    
        self.g_pas =  3.91e-5       # passive leak conductance (S/cm2)                         
        
        # active conductances
        self.hcn2_gpeak =  0        # max channel conductance (restricted to axon arbors) (pS/um2)
        self.Kv1_2_gpeak = 0        # max channel conductance (accross entire cell) (pS/um2)
        self.Cav_L_gpeak = 0        # max channel conductance (restricted to axon arbors) (pS/um2)
        
        ############ Excitatory Synapses (on dendrites) ############
        # excitatory and inhibitory inputs
        self.excSyn = {
        'start' : 0,                # opening delay from start of experiment (ms)
        'gmax' : 0,                 # pS for each synapse (8 synapses total)
        'darkProp' : 0,             # proportion of gmax that is always active (dark current)
        'e' : 10.1,                 # reversal potential (mV)
        }
        
        ############ Inhibitory Synapses (on axonal arbors) ############
        self.inhSyn = {
        'start' : 0,                # opening delay from start of experiment (ms)
        'gmax' : 0,                 # pS for each synapse (activated 1 at a time for main experiment)                        
        'e' : -50.4,                # reversal potential (mV)
        }
        
        -5
        S -> uS == +6
        cm2 -> m == +4
        m -> um == -12
        == -9