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
        self.tstop = 500                                          # How long to Run the simulation (ms)
        
        self.temp = 32

        self.DoVClamp = 1                                              # Set to 1 to run in voltage clamp configuration
        self.Hold1 = -70                                               # Initial holding potential (mV)
        self.Hold2 = -135                                               # Step holding potential (mV)
        self.ChangeClamp = 400                                         # What time to change from hold1 to hold2 (ms)

    def passive_properties(self):
        """Initialize settings for passive properties"""
        self.cm = 1.18                                                          # (uF/cm2)
        self.Ra = 132                                                           # Ohm
        self.e_pas = -60                                                        #mV
        self.g_pas =            41.6 / 1000000                                  #(S/cm2) -> (uS/e6) -> 24 kOhm cm2
        self.gapJunction_gmax = 41.6 / 1000000                                  #(S/cm2) -> (uS/e6)                 
        
    def active_conductances(self):
        """Initialize settings for active conductances"""
        self.hcn2_gpeak =     50 / 1000000                                      #(S/cm2) -> (uS/e6)
        self.Kv1_2_gpeak =  5300 / 1000000                                      #(S/cm2) -> (uS/e6)
        self.Kv1_3_gpeak =  5300 / 1000000                                      #(S/cm2) -> (uS/e6)
        self.Cav_L_gpeak = 40000 / 100000                                       #(mS/cm2) -> (uS/e5)
        
    def synaptic_inputs(self):
        """Initialize settings for excitatory and inhibitory inputs"""
        self.v_init = -35
    
        self.darkExc = {
        'start' : 0,
        'stop' : self.tstop + 100,
        'spikeFreq' : 2000,
        'weight' : 30 / 10000000,                                               #uS at start of each spike
        'e' : 10,
        'decayTau' : 40
        }
        
        self.lightExc = {
        'start' : 1500,
        'stop' : 2000,
        'spikeFreq' : 800,
        'weight' : self.darkExc['weight'],
        'e' : self.darkExc['e'],
        'decayTau' : self.darkExc['decayTau']
        }
        
        self.inhSyn = {
        'start' : 0,
        'stop' : 2000,
        'spikeFreq' : 5000,
        'weight' : 0, #3/10000,
        'e' : -60,
        'decayTau' : 19
        }