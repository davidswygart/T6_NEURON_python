class Settings ():
    """A class to store settings and parameters for the simulation"""
    
    def __init__(self):
        """Initialize all settings and parameters for the simulation"""
        self.initialize_experimental_parameters()
        self.initialize_passive_properties()
        self.initialize_excitation_inhibition()
        self.initialize_active_conductances()
        
    def initialize_experimental_parameters(self):
        """Initialize settings related to experimental setup"""
        #Timing
        self.tstop = 200                                            # How long to Run the simulation (ms)
        self.ExcStart = 10                                           # When to start stimulation of Stem (ms)
        self.ExcEnd = self.tstop                                         # How long to stimulate stem (ms)
        
        
        self.InhStart = 100                                        # When the inhibitory synapses begin to be stimulated (ms)
        self.InhEnd = 	self.tstop                                          # How long to stimulate the inhibitory synapes (ms)
        
        
        #Voltage Clamp Mode (optional)
        self.DoVClamp = 0                                               # Set to 1 to run in voltage clamp configuration
        
        self.Hold1 = 0                                      # Initial holding potential (mV)      
        self.Hold2 = 	self.Hold1                                       # Step holding potential (mV)
        self.ChangeClamp = self.tstop                                       # What time to change from hold1 to hold2 (ms)
        
        
        # Individual Synapse Voltage (optional)
        # self.DoIndSyn = 1                                               # Set to 1 to examine an individual synapse
        # self.SynNum = 0                                                 #Index number of the 
        
        # Set the run mode (single run, multi run, ect.)
        # self.RunMode = 1
        
    def initialize_passive_properties(self):
        """Initialize settings for passive properties"""
        # self.celcius = 32
        self.v_init = -37 #(after excitation)-46.7                    # What voltage to start the cell at (mV)
        # self.CM = 1.18                                                   # Membrance capacitance (uF/Cm2)
        # self.RA = 132                                                    # Axial resistance (Ohm cm2)
        # self.EPAS = -60                                                  # Equilibrium potential of passive conductances (mV)
        # self.G_PAS = 0.00003906                                          # Passive membrane conductance (mho cm2)
        self.BaselineExc = 4  / 1000                                         # How much current to inject (pA), push to restin membrane potential of -46.7 mV (3.5 &)
        
    def initialize_excitation_inhibition(self):
        """Initialize settings for excitation and inhibition"""
        #Excitatory input
        self.ExcAmp = 3 / 1000                                                # How much current to inject (pA)
        
        self.inhDecay = 2 #19.2                                           # decays time on inhibitory synapse (ms)
        self.InhSpikeFreq = 100                                              # Frequency of inhibitory spiking (hZ)
        self.InhNoise = 0                                               # 0 deterministic, 1 intervals have negexp distribution.
        self.inhSynWeight = 0.0001                                  # Initial weight set for each inhibitory synapse
        # self.SynWeight_MultiRun = 0.0001                                   # Weight each synapse is changed to 1 by 1 (Only applicable for LoopedRun)
        self.inhRevPot = -60                                                # Reversal Potential of each inhibitory synapse (mV)
        
        
    def initialize_active_conductances(self):
        """Initialize settings for active conductances"""
        #L-type voltage gated calcium channels
        # self.GCAL = 0#0.0025 #Gives 30 pA calcium current when stepped from -70 to -35
        # self.KI = .001 #
        # self.ET = 113                                                    #cv inactivation?
        # self.CT = 1 				#dc calcium concentration?
        # self.MT = 1 				#c activation?
        # self.VHFA = -36 		# Activation half-max?
        # self.SLPA = 5#8   		# slope activation (mv)?
        # self.VHFI = -31		# inactivation half-max?
        # self.SLPI = 13 		# slope inactivation (mv)?