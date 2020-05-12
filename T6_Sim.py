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
        #cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python
        self.settings = Settings()                                                       #Load settings (eg. experimental setup, physiology parameters, display settings)    
        self.axons = f.loadMorph(h, "T6_V3.hoc")                                         #Load axon morphology
        self.ribbons = Ribbons(h, "InputData/RibbonLocations.txt")                #A list of voltage recording vectors at each ribbon
        self.segments = Segments(h)                                                #A list of voltage recording vectors at each segment
        self.inhSyns = InhSyns(h, "InputData/InhSynLocations.txt", self.settings)             #An object containing all inhibitory synapses, their presynaptic stimulation, and their connector
        self.iClamp_baselineExc = placeCurrentClamp(h, self.axons[0], 0, 0, self.settings.tstop, self.settings.BaselineExc) #section, location on the section, delay, duration, amplitude
        self.iClamp_visExc = placeCurrentClamp(h, self.axons[0], 0, self.settings.ExcStart, self.settings.ExcEnd - self.settings.ExcStart, self.settings.ExcAmp) #section, location on the section, delay, duration, amplitude
        
        if self.settings.DoVClamp:
            self.settings.v_init = self.settings.Hold1
            self.volClamp = placeVoltageClamp(h, self.axons[0], 0, self.settings)
            self.iRecord = h.Vector().record(self.volClamp._ref_i)
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
                


T6 = Model()
calcDistances(T6.segments.location, T6.segments.location, "segDistances.txt")


    