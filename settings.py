class Settings ():
    """A class to store settings and parameters for the simulation"""
    #These settings are correct for active model with 120 inhibitory synapses activated

    def __init__(self):
        # passive properties
        self.cm = 1.18              # capacitance (uF/cm2)                                          
        self.Ra = 132               # axial resistivity (Ohm-cm)                                         
        self.e_pas = -60            # leak reversal potential (mV)                                                    
        self.g_pas =  3.91e-5       # passive leak conductance (S/cm2)                         
        
        # active conductances
        self.hcn2_gpeak =  .78        # max channel conductance (restricted to axon arbors) (pS/um2)
        self.Kv1_2_gpeak = 12        # max channel conductance (accross entire cell) (pS/um2)
        self.Cav_L_gpeak = 1.62        # max channel conductance (restricted to axon arbors) (pS/um2)
        
        
        #### Structure for synapse settings
        from collections import namedtuple

        ############ Excitatory Synapses (on dendrites) ############
        self.excSyn = namedtuple("SynapseSettings", "start stop frequency baselineFrequency tauRise tauDecay reversalPotential gMax") #create a datastructure to hold synapse info
        self.excSyn.start = 1000
        self.excSyn.stop = 2000
        self.excSyn.frequency = 500
        self.excSyn.tauRise = 10
        self.excSyn.tauDecay = 100
        self.excSyn.reversalPotential = 10.1
        self.excSyn.gMax = 1e-5
        
        ############ Dark current ############
        self.excDark = namedtuple("SynapseSettings", "start stop frequency baselineFrequency tauRise tauDecay reversalPotential gMax") #create a datastructure to hold synapse info
        self.excDark.start = 0
        self.excDark.stop = 1e9
        self.excDark.frequency = 70
        self.excDark.tauRise = self.excSyn.tauRise
        self.excDark.tauDecay = self.excSyn.tauDecay
        self.excDark.reversalPotential = self.excSyn.reversalPotential
        self.excDark.gMax = self.excSyn.gMax
        
        ############ Inhibitory Synapses (on axonal arbors) ############        
        self.inhSyn= namedtuple("SynapseSettings", "start stop frequency baselineFrequency tauRise tauDecay reversalPotential gMax") #create a datastructure to hold synapse info
        self.inhSyn.start = 1000
        self.inhSyn.stop = 2000
        self.inhSyn.frequency = 79
        self.inhSyn.tauRise = 1.8
        self.inhSyn.tauDecay = 100
        self.inhSyn.reversalPotential = -50.4
        self.inhSyn.gMax = 1.62e-5