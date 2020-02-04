# -*- coding: utf-8 -*- 
import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from inhSyns import InhSyns
from ribbons import Ribbons
from Electrodes import placeCurrentClamp
from Electrodes import placeVoltageClamp


class model():  
    def __init__(self):
        #cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python
        self.settings = Settings()                                                       #Load settings (eg. experimental setup, physiology parameters, display settings)    
        self.axons = f.loadMorph(h, "T6_V3.hoc")                                         #Load axon morphology
        self.ribbons = Ribbons(h, "InputData/RibbonLocations.txt")                #A list of voltage recording vectors at each ribbon
        self.segRec = f.recordSegments(h)                                                #A list of voltage recording vectors at each segment
        self.inhSyns = InhSyns(h, "InputData/InhSynLocations.txt", self.settings)             #An object containing all inhibitory synapses, their presynaptic stimulation, and their connector
        self.iClamp_baselineExc = placeCurrentClamp(h, self.axons[0], 0, 0, self.settings.tstop, self.settings.BaselineExc) #section, location on the section, delay, duration, amplitude
        self.iClamp_visExc = placeCurrentClamp(h, self.axons[0], 0, self.settings.ExcStart, self.settings.ExcEnd - self.settings.ExcStart, self.settings.ExcAmp) #section, location on the section, delay, duration, amplitude
        
        if self.settings.DoVClamp:
            self.settings.v_init = self.settings.Hold1
            self.volClamp = placeVoltageClamp(h, self.axons[0], 0, self.settings)
            self.iRecord = h.Vector().record(self.volClamp._ref_i)
            f.runSim(h, self.settings, self.inhSyns, self.segRec, self.ribbons.recording)
            f.makePlot(np.linspace(0, self.settings.tstop, len(self.segRec[0])), self.iRecord)
        else:
            f.runSim(h, self.settings, self.inhSyns, self.segRec, self.ribbons.recording)

T6 = model()



#def calcDistances(secList1,secList2):
    