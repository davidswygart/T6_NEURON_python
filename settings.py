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
        
        
        #### Structure for synapse settings
        from collections import namedtuple

        ############ Excitatory Synapses (on dendrites) ############
        self.excSyn = namedtuple("SynapseSettings", "start stop frequency tauRise tauDecay reversalPotential gMax") #create a datastructure to hold synapse info
        self.excSyn.start = 200
        self.excSyn.stop = 400
        self.excSyn.frequency = 10
        self.excSyn.tauRise = 1
        self.excSyn.tauDecay = 5
        self.excSyn.reversalPotential = 10.1
        self.excSyn.gMax = .001
        
        ############ Inhibitory Synapses (on axonal arbors) ############        
        self.inhSyn= namedtuple("SynapseSettings", "start stop frequency tauRise tauDecay reversalPotential gMax") #create a datastructure to hold synapse info
        self.inhSyn.start = 100
        self.inhSyn.stop = 400
        self.inhSyn.frequency = 20
        self.inhSyn.tauRise = 1
        self.inhSyn.tauDecay = 5
        self.inhSyn.reversalPotential = -150.4
        self.inhSyn.gMax = .00001