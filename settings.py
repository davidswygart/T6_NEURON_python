class Settings ():
    """A class to store settings and parameters for the simulation"""
    
    def __init__(self):
        """Initialize all settings and parameters for the simulation"""
        self.initialize_experimental_parameters
        self.initialize_passive_properties
        self.initialize_excitation_inhibition
        self.initialize_active_conductances
        
    def initialize_experimental_parameters(self):
        """Initialize settings related to experimental setup"""
        #Timing
        self.ExcStart = 0                                           # When to start stimulation of Stem (ms)
        self.ExcDur = 100                                         # How long to stimulate stem (ms)
        self.SpikeStart = 25                                        # When the inhibitory synapses begin to be stimulated (ms)
        self.SpikeDur = 	75                                          # How long to stimulate the inhibitory synapes (ms)
        self.SpikeStart_Dyad = self.SpikeStart                               # When the inhibitory synapses begin to be stimulated (ms)
        self.SpikeDur_Dyad = self.SpikeDur                                   # How long to stimulate the inhibitory synapes (ms)
        self.tstop = 100                                            # How long to Run the simulation (ms)
        
        #Voltage Clamp Mode (optional)
        self.DoVClamp = 0                                               # Set to 1 to run in voltage clamp configuration
        
        self.Hold1_VolCla = 0                                      # Initial holding potential (mV)
        self.Dur1_VolCla = 100                                       # Duration to hold at this potential (ms)
        
        self.Hold2_VolCla = 	0                                       # Step holding potential (mV)
        self.Dur2_VolCla = 	0                                       # Duration to hold at second potential
        
        #Graphs
        self.Vmin = -70                                             # Minimum voltage shown on graph (mV)
        self.Vmax = 20                                               # Maximum voltage shown on graph (mV)
        
        self.Imin = 	5                                                  # Minimum current shown on graph (pA) # Only aplicable if in voltage clamp mode
        self.Imax = 	25                                                 # Maximum current shown on graph (pA) # Only aplicable if in voltage clamp mode
        
        # Individual Synapse Voltage (optional)
        self.DoIndSyn = 1                                               # Set to 1 to examine an individual synapse
        self.SynNum = 0                                                 #Index number of the 
        
    def initialize_passive_properties(self):
        """Initialize settings for passive properties"""
        self.celcius = 32
        self.v_init = -37 #(after excitation)-46.7                    # What voltage to start the cell at (mV)
        self.CM = 1.18                                                   # Membrance capacitance (uF/Cm2)
        self.RA = 132                                                    # Axial resistance (Ohm cm2)
        self.EPAS = -60                                                  # Equilibrium potential of passive conductances (mV)
        self.G_PAS = 0.00003906                                          # Passive membrane conductance (mho cm2)
        self.BaselineExc = 3.5                                           # How much current to inject (pA), push to restin membrane potential of -46.7 mV (3.5 &)
        
    def initialize_excitation_inhibition(self):
        """Initialize settings for excitation and inhibition"""
        #Excitatory input
        self.ExcAmp = 2.5                                                # How much current to inject (pA)
        
        # Inhibition to non-dyad sites
        self.inhDecay = 2 #19.2                                           # decays time on inhibitory synapse (ms)
        self.SpikeFreq = 10                                              # Frequency of inhibitory spiking (hZ)
        self.StimNoise = 0                                               # 0 deterministic, 1 intervals have negexp distribution.
        self.SynWeight_Initial = 0.0001                                  # Initial weight set for each inhibitory synapse
        self.SynWeight_Change = 0.0001                                   # Weight each synapse is changed to 1 by 1 (Only applicable for LoopedRun)
        self.RevPot = -60                                                # Reversal Potential of each inhibitory synapse (mV)
        
        
        # Inhibition directly onto dyads (can just be the same as above)
        self.SpikeFreq_Dyad = self.SpikeFreq
        self.SynWeight_Initial_Dyad = self.SynWeight_Initial                  # Initial weight set for each inhibitory synapse (.00001 give 30 pA inhibition at 0mV)(Erika Eggars 2007)
        self.SynWeight_Change_Dyad = self.SynWeight_Change                    # Weight each synapse is changed to 1 by 1 (Only applicable for LoopedRun)
        self.RevPot_Dyad = self.RevPot                                        # Reversal Potential of each inhibitory synapse (mV)
        
    def initialize_active_conductances(self):
        """Initialize settings for active conductances"""
        #L-type voltage gated calcium channels
        self.GCAL = 0#0.0025 #Gives 30 pA calcium current when stepped from -70 to -35
        self.KI = .001 #
        self.ET = 113                                                    #cv inactivation?
        self.CT = 1 				#dc calcium concentration?
        self.MT = 1 				#c activation?
        self.VHFA = -36 		# Activation half-max?
        self.SLPA = 5#8   		# slope activation (mv)?
        self.VHFI = -31		# inactivation half-max?
        self.SLPI = 13 		# slope inactivation (mv)?