class Settings ():
    """A class to store settings and parameters for the simulation"""

    def __init__(self):
        """Initialize all settings and parameters for the simulation"""
        self.experimental_parameters()
        self.passive_properties()
        self.synaptic_inputs()
        self.active_conductances()

    def experimental_parameters(self):
        """Initialize settings related to experimental setup"""
        self.tstop = 300                                            # How long to Run the simulation (ms)
        
        self.temp = 32

        self.DoVClamp = 1                                               # Set to 1 to run in voltage clamp configuration
        self.Hold1 = -80                                                # Initial holding potential (mV)
        self.Hold2 = 	-20                                               # Step holding potential (mV)
        self.ChangeClamp = 100                                       # What time to change from hold1 to hold2 (ms)

    def synaptic_inputs(self):
        """Initialize settings for excitatory and inhibitory inputs"""
        self.inhSyn = {
        'start' : 400,
        'stop' : self.tstop,
        'spikeFreq' : 100,
        'weight' : 0,#.2,
        'e' : -60
        }
        
        self.darkExc = {
        'start' : 0,
        'stop' : self.tstop,
        'spikeFreq' : 1000,
        'weight' : 0,#.001,
        'e' : 10
        }
        
        self.lightExc = {
        'start' : 200,
        'stop' : self.tstop,
        'spikeFreq' : 1000,
        'weight' : 0,#.01,
        'e' : self.darkExc['e']
        }
        
    def passive_properties(self):
        """Initialize settings for passive properties"""
        self.v_init = -37 #(after excitation)-46.7                    # What voltage to start the cell at (mV)
        self.cm = 1.1                                                  # Membrance capacitance (uF/Cm2)
        self.Ra = 130                                                    # Axial resistance (Ohm cm2)
        self.e_pas = -60                                                  # Equilibrium potential of passive conductances (mV)
        self.g_pas = 4.17e-005                                         # Passive membrane conductance (mho cm2)

    def active_conductances(self):
        """Initialize settings for active conductances"""
        self.hcn2_gpeak = 0.00005
        self.Kv1_2_gpeak = 0.0005
        self.Kv1_3_gpeak = 0.0005
        self.Cav3_1_gpeak = 0.00005
        self.Cav1_4_gpeak = 0.13
