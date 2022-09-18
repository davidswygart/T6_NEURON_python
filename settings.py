class Settings ():
    """A class to store settings and parameters for the simulation"""

    def __init__(self):
        # passive properties
        self.cm = 1.18                                                        
        self.Ra = 132                                                          
        self.e_pas = -60                                                      
        self.g_pas =  3.91e-5                              
        
        # active conductances
        self.hcn2_gpeak =  0
        self.Kv1_2_gpeak = 0
        self.Cav_L_gpeak = 0
        
        # excitatory and inhibitory inputs
        self.excSyn = {
        'start' : 0,
        'gmax' : 0,                 #pS from each synapse (8 synapses total)
        'darkProp' : 0,             #proportion of dark current
        'e' : 10.1,
        }
        
        self.inhSyn = {
        'start' : 0,
        'gmax' : 0,                 #pS from each synapse (8 synapses total)                        
        'e' : -50.4,
        }