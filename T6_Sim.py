import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from synapse import Synapse


class Type6_Model():  
    def __init__(self):
        """Initialize the model cell."""
        self.h = h
        self.settings = Settings() 
        self.buildCell()
        self.addElectrodes()
    
    def buildCell(self):
        """Build the model cell""" 
        self.loadMorphology()
        self.inhSyns = self.addSynapses("morphology/InhSynLocations.txt", self.settings.inhSyn)
        self.excSyns = self.addSynapses("morphology/InputRibbonLocations.txt", self.settings.darkExc)
        for syn in self.excSyns:
            syn.addStim2(self.h, self.settings.lightExc)
        self.insertChannels()
        self.setRecordingPoints()
        
    def addElectrodes(self):
        if self.settings.DoVClamp:
            self.placeVoltageClamp(self.h.dend_0[2], .9) #Place voltage clamp at the soma (as defined by widest segment)
    
    def addSynapses(self, LocationFile, settings):
        synapseList = []
        XYZ = f.readLocation(LocationFile)
        for Num in range(len(XYZ)):
            [sec,D] = f.findSectionForLocation(self.h, XYZ[Num,:])
            syn = Synapse(self.h, sec, D, settings)
            synapseList.append(syn)
        return synapseList            
    
    def loadMorphology(self):
        """Load morphology information from pre-created hoc files"""
        h.load_file( "morphology/axonMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.load_file( "morphology/dendriteMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.dend_0[0].connect(h.axon[0], 0, 0) #connect the dendrites and the axons together
        
    def insertChannels(self):
        for sec in h.allsec():
            sec.Ra = self.settings.Ra
            sec.insert('pas')
            sec.insert('hcn2')
            sec.insert('Kv1_2')
            sec.insert('Kv1_3')
            #sec.insert('CaL')
            for seg in sec:
                seg.cm = self.settings.cm
                
                seg.pas.e = self.settings.e_pas
                seg.pas.g = self.settings.g_pas
                
                seg.hcn2.gpeak = self.settings.hcn2_gpeak
                seg.hcn2.a0t = self.settings.hcn2_tau
                
                seg.Kv1_2.gKv1_2bar = self.settings.Kv1_2_gpeak
                seg.Kv1_3.gKv1_3bar = self.settings.Kv1_3_gpeak

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
        self.h.celsius = self.settings.temp
        self.h.finitialize(self.settings.v_init)
        self.h.frecord_init()
        self.h.continuerun(self.settings.tstop)
        self.time = np.linspace(0, self.settings.tstop, len(self.segment_recording[0]))
        
        
    def updateAndRun(self):
        self.settings = Settings()
        self.insertChannels()
        self.addElectrodes()
        
        for syn in self.inhSyns:
            syn.updateSettings(syn.stim, syn.con, self.settings.inhSyn)
        for syn in self.excSyns:
            syn.updateSettings(syn.stim, syn.con, self.settings.darkExc)
            syn.updateSettings(syn.stim2, syn.con2, self.settings.lightExc)        
        self.run()
        

            
        f.makePlot(self.time, self.segment_recording[0])
        if self.settings.DoVClamp:
            f.makePlot(self.time, self.current_recording, title = 'Current Graph', ymax = 2)

       
    def calcDistances(locations1, locations2, fileName):
        distMatrix = np.zeros([len(locations1), len(locations2)])
        
        for num1, loc1 in enumerate(locations1):
            for num2, loc2 in enumerate(locations2):
                dist = h.distance(loc1[0](loc1[1]), loc2[0](loc2[1]))
                distMatrix[num1, num2] = dist
        
        np.savetxt(fileName, distMatrix)