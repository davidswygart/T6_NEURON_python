import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from inhSyns import InhSyns


class Type6_Model():  
    def __init__(self):
        """Initialize the model cell."""
        self.h = h
        self.updateSettings()
        self.buildCell()
        self.addElectrodes()
    
    def updateSettings(self):
        """Load settings from the settings file"""
        self.settings = Settings(h)    
    
    def buildCell(self):
        """Build the model cell""" 
        self.loadMorphology()          
        self.inhSyns = InhSyns(h, "morphology/InhSynLocations.txt", self.settings)             #An object containing all inhibitory synapses, their presynaptic stimulation, and their connector
        self.insertActiveChannels()
        self.setRecordingPoints()
        
    def addElectrodes(self):
        self.iClamp_baselineExc = self.placeCurrentClamp(h.dend_0[31], 0, 0, self.settings.tstop, self.settings.BaselineExc) #section, location on the section, delay, duration, amplitude
        self.iClamp_visExc = self.placeCurrentClamp(h.dend_0[31], 0, self.settings.ExcStart, self.settings.ExcEnd - self.settings.ExcStart, self.settings.ExcAmp) #section, location on the section, delay, duration, amplitude
        if self.settings.DoVClamp:
            self.placeVoltageClamp(self.h.dend_0[2], .9) #Place voltage clamp at the soma (as defined by widest segment)
        
    def loadMorphology(self):
        """Load morphology information from pre-created hoc files"""
        h.load_file( "morphology/axonMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.load_file( "morphology/dendriteMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.dend_0[0].connect(h.axon[0], 0, 0) #connect the dendrites and the axons together
        
    def insertActiveChannels(self):
        for sec in h.allsec():
            sec.insert('hcn2')
            for seg in sec:
                seg.hcn2.gpeak = self.settings.hcn2_gpeak
                seg.hcn2.a0t = self.settings.hcn2_tau

    def setRecordingPoints(self):
        """Set recording points at each ribbon and segment"""        
        XYZs = f.readLocation("morphology/RibbonLocations.txt")
        self.ribbon_recording = []
        self.ribbon_location = []
        for ribNum in range(len(XYZs)):
            [sec,D] = f.findSectionForLocation(h, XYZs[ribNum,:])
            self.ribbon_location.append([sec,D])
            self.ribbon_recording.append(h.Vector().record(sec(D)._ref_v ))

        self.segment_recording = []
        self.segment_location = []

        for sec in h.allsec():
            for n in range(sec.nseg):
                D = 1/(2*sec.nseg) + n/sec.nseg
                    
                self.segment_location.append([sec, D])
                self.segment_recording.append(h.Vector().record(sec(D)._ref_v))

    def placeCurrentClamp(self, sec, D, delay, dur, amp):
        iClamp = h.IClamp(sec(D))
        iClamp.delay = delay
        iClamp.dur = dur
        iClamp.amp = amp
        return iClamp
    
    def placeVoltageClamp(self, sec, D):
        self.settings.v_init = self.settings.Hold1
        self.vClamp = h.SEClamp(sec(D))
        self.vClamp.dur1  = self.settings.ChangeClamp
        self.vClamp.dur2  = self.settings.tstop - self.settings.ChangeClamp
        self.vClamp.amp1  = self.settings.Hold1
        self.vClamp.amp2  = self.settings.Hold2
        self.current_recording = h.Vector().record(self.vClamp._ref_i)

    def run(self):
        """Run the simulation"""
        h.finitialize(self.settings.v_init)
        h.frecord_init()
        h.continuerun(self.settings.tstop)
        self.time = np.linspace(0, self.settings.tstop, len(self.segment_recording[0]))

       
    def calcDistances(locations1, locations2, fileName):
        distMatrix = np.zeros([len(locations1), len(locations2)])
        
        for num1, loc1 in enumerate(locations1):
            for num2, loc2 in enumerate(locations2):
                dist = h.distance(loc1[0](loc1[1]), loc2[0](loc2[1]))
                distMatrix[num1, num2] = dist
        
        np.savetxt(fileName, distMatrix)