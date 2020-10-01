class Settings ():
    """A class to store settings and parameters for the simulation"""

    def __init__(self):
        """Initialize all settings and parameters for the simulation"""
        self.experimental_parameters()
        self.passive_properties()
        self.active_conductances()
        self.synaptic_inputs()

    def experimental_parameters(self):
        """Initialize settings related to experimental setup"""
        self.tstop = 1000                                            # How long to Run the simulation (ms)
        
        self.temp = 32

        self.DoVClamp = 0                                               # Set to 1 to run in voltage clamp configuration
        self.Hold1 = -70                                               # Initial holding potential (mV)
        self.Hold2 =   -40                                             # Step holding potential (mV)
        self.ChangeClamp = 400                                       # What time to change from hold1 to hold2 (ms)

    def passive_properties(self):
        """Initialize settings for passive properties"""
        self.cm = 1.18
        self.Ra = 132
        self.e_pas = -60
        self.g_pas = 3.91e-5
        
    def active_conductances(self):
        """Initialize settings for active conductances"""
        self.hcn2_gpeak = 0.00004
        self.Kv1_2_gpeak = 0.00056
        self.Kv1_3_gpeak = 0.00056
        self.Cav3_1_gpeak = 0.001
        #self.Cav3_1_m_Vhalf = -55
        #self.Cav3_1_h_Vhalf = -60
        self.Cav1_4_gpeak = 1
        #self.Cav1_4_m_Vhalf = -10
        
    def synaptic_inputs(self):
        """Initialize settings for excitatory and inhibitory inputs"""
        self.v_init = -45
    
        self.darkExc = {
        'start' : 0,
        'stop' : self.tstop + 100,
        'spikeFreq' : 450,
        'weight' : 0.000003,
        'e' : 10,
        'decayTau' : 40
        }
        
        self.lightExc = {
        'start' : 500,
        'stop' : 2000,
        'spikeFreq' : 950,
        'weight' : self.darkExc['weight'],
        'e' : self.darkExc['e'],
        'decayTau' : self.darkExc['decayTau']
        }
        
        self.inhSyn = {
        'start' : 500,
        'stop' : 2000,
        'spikeFreq' : 5,
        'weight' : 0.000,
        'e' : -60,
        'decayTau' : 19
        }