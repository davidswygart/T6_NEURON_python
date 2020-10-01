import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from synapse import Synapse
import matplotlib.pyplot as plt


class Type6_Model():  
    def __init__(self):
        """Build the model cell."""
        self.h = h
        self.settings = Settings() 
        self.loadMorphology()
        self.inhSyns = self.addSynapses("morphology/InhSynLocations.txt", self.settings.inhSyn)
        self.excSyns = self.addSynapses("morphology/InputRibbonLocations.txt", self.settings.darkExc)
        for syn in self.excSyns:
            syn.addStim2(self.h, self.settings.lightExc) 
        self.insertChannels()
        self.setRecordingPoints()
        self.channelAdjustment()
        if self.settings.DoVClamp:
            self.placeVoltageClamp(self.h.dend_0[2], .9) #Place voltage clamp at the soma (as defined by widest segment)        
    
    def addSynapses(self, LocationFile, settings):
        """Add synapses to the locations specified in LocationFile"""
        print('....adding synapses: ', LocationFile)
        synapseList = []
        XYZ = f.readLocation(LocationFile)
        for Num in range(len(XYZ)):
            [sec,D] = f.findSectionForLocation(self.h, XYZ[Num,:])
            syn = Synapse(self.h, sec, D, settings)
            synapseList.append(syn)
        return synapseList            
    
    def loadMorphology(self):
        """Load morphology information from pre-created hoc files"""
        print('....loading morphology')
        h.load_file( "morphology/axonMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.load_file( "morphology/dendriteMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.dend_0[0].connect(h.axon[0], 0, 0) #connect the dendrites and the axons together
        
    def insertChannels(self):
        """Insert active channels"""
        print('....inserting channels')
        for sec in self.h.allsec():
            sec.insert('pas')
            sec.insert('hcn2')
            sec.insert('Kv1_2')
            sec.insert('Kv1_3')
            sec.insert('Cav3_1')
            sec.insert('Cav1_4')
            sec.insert('cad')

    
    def channelAdjustment(self):
        """Adjust channels settings"""
        print('....Adjusting biophysics and channels')
        for sec in h.allsec():
            sec.Ra = self.settings.Ra
            for seg in sec:
                seg.cm = self.settings.cm
                
                seg.pas.e = self.settings.e_pas
                seg.pas.g = self.settings.g_pas
                
                seg.hcn2.gpeak = self.settings.hcn2_gpeak
                
                seg.Kv1_2.gKv1_2bar = self.settings.Kv1_2_gpeak
                seg.Kv1_3.gKv1_3bar = self.settings.Kv1_3_gpeak
                
                
                seg.Cav3_1.gCav3_1bar = 0
                seg.Cav1_4.gCabar = 0

        for [sec, d] in self.recordings['ribLocations']:
            if d == 1: d = .99
            if d == 0: d = .01
            sec(d).Cav3_1.gCav3_1bar = self.settings.Cav3_1_gpeak
            #sec(d).Cav3_1.m_vHalf = self.settings.Cav3_1_m_Vhalf
            #sec(d).Cav3_1.h_vHalf = self.settings.Cav3_1_h_Vhalf
            
            sec(d).Cav1_4.gCabar = self.settings.Cav1_4_gpeak
            #sec(d).Cav1_4.VhalfCam =  self.settings.Cav1_4_m_Vhalf

    def setRecordingPoints(self):
        """Set recording points at each ribbon and segment""" 
        print('....setting recording points (voltage and calcium recording points')
        
        self.recordings = {
        'segLocations' : [],
        'segV' : [],
        'segCai' : [],
        'segIca' : [],
        'ribLocations' : [],
        'ribV' : [],
        'ribCai' : [],
        'ribIca' : []
        }
        
        XYZs = f.readLocation("morphology/RibbonLocations.txt")
        for ribNum in range(len(XYZs)):
            [sec,D] = f.findSectionForLocation(h, XYZs[ribNum,:])
            self.recordings['ribLocations'].append([sec,D])
            self.recordings['ribV'].append(h.Vector().record(sec(D)._ref_v ))
            self.recordings['ribCai'].append(h.Vector().record(sec(D)._ref_cai))
            self.recordings['ribIca'].append(h.Vector().record(sec(D)._ref_ica))

        for sec in h.allsec():
            for n in range(sec.nseg):
                D = 1/(2*sec.nseg) + n/sec.nseg
                    
                self.recordings['segLocations'].append([sec, D])
                self.recordings['segV'].append(h.Vector().record(sec(D)._ref_v))
                self.recordings['segCai'].append(h.Vector().record(sec(D)._ref_cai))
                self.recordings['segIca'].append(h.Vector().record(sec(D)._ref_ica))
    
    def placeVoltageClamp(self, sec, D):
        """Put a voltage clamp at a specific location"""
        print('....adding a voltage clamp electrode')
        self.settings.v_init = self.settings.Hold1
        self.vClamp = h.SEClamp(sec(D))
        self.vClamp.dur1  = self.settings.ChangeClamp
        self.vClamp.dur2  = self.settings.tstop - self.settings.ChangeClamp
        self.vClamp.amp1  = self.settings.Hold1
        self.vClamp.amp2  = self.settings.Hold2
        self.recordings['iClamp'] = h.Vector().record(self.vClamp._ref_i)

    def run(self):
        """Run the simulation"""
        print('....running simulation')
        self.h.celsius = self.settings.temp
        self.h.finitialize(self.settings.v_init)
        self.h.frecord_init()
        self.h.continuerun(self.settings.tstop)
        self.recordings['time'] = np.linspace(0, self.settings.tstop, len(self.recordings['segV'][252]))
        #for key in self.recordings.keys():
         #   self.recordings[key] = np.array(self.recordings[key])
        
    def update(self):
        """Update Settings"""
        print('....updating settings')
        self.channelAdjustment()
        
        if self.settings.DoVClamp:
            self.placeVoltageClamp(self.h.dend_0[2], .9) #Place voltage clamp at the soma (as defined by widest segment)
        
        print('....updating synapse values')
        for syn in self.inhSyns:
            syn.updateSettings(syn.stim, syn.con, self.settings.inhSyn)
        for syn in self.excSyns:
            syn.updateSettings(syn.stim, syn.con, self.settings.darkExc)
            syn.updateSettings(syn.stim2, syn.con2, self.settings.lightExc)        
        
    def updateAndRun(self):
        """Update settings and run simulaltion, then plot"""
        self.settings = Settings()
        self.update()
        self.run()
   
        f.makePlot(self.recordings['time'], self.recordings['segV'][252])
        #f.makePlot(self.recordings['time'], self.recordings['ribV'][1], title = 'ribV')
        if self.settings.DoVClamp:
            f.makePlot(self.recordings['time'], self.recordings['iClamp'], title = 'Current Graph')
            
    def runIV(self, startTime, minV = -80, maxV = 40, steps = 12):
        """Run an Current voltage experiment"""
        self.settings = Settings()
        self.settings.DoVClamp = 1
        self.update()
        
        Vs = np.linspace(minV, maxV, steps)
        Is = []
        for [n, v] in enumerate(Vs):
            self.settings.Hold2 = v
            self.update()
            print('Running ', v, 'mV (', n+1, '/', steps, ')')
            self.run()
            
            f.makePlot(self.recordings['time'], self.recordings['iClamp'], ymax = .01, xmin = 390, xmax = 450)
            val = f.pullMax(self.recordings['time'], self.recordings['iClamp'], 405)
            #val = f.pullAvg(self.recordings['time'], self.recordings['iClamp'], startTime, stopTime)
            Is.append(val)
        f.makePlot(Vs, Is, title = 'IV graph')
        return [Vs, Is]
            

    def calcDistances(locations1, locations2, fileName):
        """calculate the path distances between sets of locations"""
        distMatrix = np.zeros([len(locations1), len(locations2)])
        
        for num1, loc1 in enumerate(locations1):
            for num2, loc2 in enumerate(locations2):
                dist = h.distance(loc1[0](loc1[1]), loc2[0](loc2[1]))
                distMatrix[num1, num2] = dist
        
        np.savetxt(fileName, distMatrix)
        
        
        
    def plotSuppression(self, preStart, preEnd, stimStart, stimEnd, plotWhat):
        self.updateAndRun()
        
        supMeans = []
        for rec in self.recordings[plotWhat]:
            preStim = f.pullAvg(self.recordings['time'], rec, preStart, preEnd)
            Stim = f.pullAvg(self.recordings['time'], rec, stimStart, stimEnd)
            supMeans.append(Stim-preStim)
            
        for syn in self.inhSyns:
            syn.con.weight[0] = 0
        self.run()
        f.makePlot(self.recordings['time'], self.recordings['segV'][252])
        
        noSupMeans = []
        for rec in self.recordings[plotWhat]:
            preStim = f.pullAvg(self.recordings['time'], rec, preStart, preEnd)
            Stim = f.pullAvg(self.recordings['time'], rec, stimStart, stimEnd)
            noSupMeans.append(Stim-preStim)
        
        supMeans = np.array(supMeans)
        noSupMeans = np.array(noSupMeans)
        
        sup = 1 - (supMeans/noSupMeans)
        
        plt.hist(sup)
        
        return(sup)
    