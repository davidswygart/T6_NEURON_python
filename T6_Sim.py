import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from inhSyns import InhSyns
from ribbons import Ribbons
from segments import Segments
from Electrodes import placeCurrentClamp
from Electrodes import placeVoltageClamp


class Model():  
    def __init__(self):
        """Build the model cell."""
        self.settings = Settings(h)                                                       #Load settings (eg. experimental setup, physiology parameters, display settings)    
        self.loadMorphology()                                         #Load axon morphology
        self.ribbons = Ribbons(h, "morphology/RibbonLocations.txt")                #A list of voltage recording vectors at each ribbon
        self.segments = Segments(h)                                                #A list of voltage recording vectors at each segment
        self.inhSyns = InhSyns(h, "morphology/InhSynLocations.txt", self.settings)             #An object containing all inhibitory synapses, their presynaptic stimulation, and their connector
        f.insertActiveChannels(h, self.sections, self.settings)
        self.iClamp_baselineExc = placeCurrentClamp(h, h.dend_0[31], 0, 0, self.settings.tstop, self.settings.BaselineExc) #section, location on the section, delay, duration, amplitude
        self.iClamp_visExc = placeCurrentClamp(h, h.dend_0[31], 0, self.settings.ExcStart, self.settings.ExcEnd - self.settings.ExcStart, self.settings.ExcAmp) #section, location on the section, delay, duration, amplitude
        
        if self.settings.DoVClamp:
            self.settings.v_init = self.settings.Hold1
            self.volClamp = placeVoltageClamp(h, h.dend_0[2], 1, self.settings)
            self.iRecord = h.Vector().record(self.volClamp._ref_i)

    def loadMorphology(self):
        """Load morphology information from pre-created hoc files"""
        h.load_file( "morphology/axonMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.load_file( "morphology/dendriteMorph.hoc") #Load axon morphology (created in Cell Builder)
    
        h.dend_0[0].connect(h.axon[0], 0, 0) #connect the dendrites and the axons together
        self.sections = []
        for sec in h.allsec():
            self.sections.append(sec)
        
    def runSim(self):
        """Run the simulation"""
        if self.settings.DoVClamp:
            f.runSim(h, self.settings, self.inhSyns, self.segments.recording, self.ribbons.recording)
            f.makePlot(np.linspace(0, self.settings.tstop, len(self.segments.recording[0])), self.iRecord)
        else:
            f.runSim(h, self.settings, self.inhSyns, self.segments.recording, self.ribbons.recording)
        
        
        
        
        
        
        
def calcDistances(locations1, locations2, fileName):
    distMatrix = np.zeros([len(locations1), len(locations2)])
    
    for num1, loc1 in enumerate(locations1):
        for num2, loc2 in enumerate(locations2):
            dist = h.distance(loc1[0](loc1[1]), loc2[0](loc2[1]))
            distMatrix[num1, num2] = dist
    
    np.savetxt(fileName, distMatrix)



    