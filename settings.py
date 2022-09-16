class Settings ():
    """A class to store settings and parameters for the simulation"""

    def __init__(self):
        # passive properties
        self.cm = 1.18                                                          # (uF/cm2)
        self.Ra = 132                                                           # Ohm-cm
        self.e_pas = -60                                                        #mV
        self.g_pas =  3.91e-5                                  #(S/cm2) -> (uS/e6) -> 25.6 kOhm cm2               
        
        # active conductances
        self.hcn2_gpeak =   0#  50 / 1000000                                      #(S/cm2) -> (uS/e6)
        self.Kv1_2_gpeak =  0# 550 / 1000000                                      #(S/cm2) -> (uS/e6)
        self.Cav_L_gpeak =  0# 40000 / 100000                                       #(mS/cm2) -> (uS/e5)
        
        # excitatory and inhibitory inputs
        self.excSyn = {
        'start' : 0,
        'gmax' : 0,                                                 #(uS)-> pS/e6 from each synapse (8 synapses total)
        'e' : 10.1,
        }
        
        self.inhSyn = {
        'start' : 0,
        'gmax' : 0,#30 / 10000000,                                              #(uS)-> pS/e6 from each synapse
        'e' : -50.4,
        }