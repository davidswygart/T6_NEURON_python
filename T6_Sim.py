import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from synapse import Synapse


class Type6_Model():
    def __init__(self):
        """Build the model cell."""
        self.h = h
        self.settings = Settings()
        self.loadMorphology()
        self.inhSyns = self.addSynapses("morphology/InhSynLocations.txt", self.settings.inhSyn)
        self.excSyns = self.addSynapses("morphology/InputRibbonLocations.txt", self.settings.excSyn)
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
            syn = Synapse(self.h, sec, D, settings, Num)
            synapseList.append(syn)
        return synapseList

    def loadMorphology(self):
        """Load morphology information from pre-created hoc files"""
        print('....loading morphology')
        self.h.load_file( "morphology/axonMorph.hoc") #Load axon morphology (created in Cell Builder)
        self.h.load_file( "morphology/dendriteMorph.hoc") #Load axon morphology (created in Cell Builder)
        self.h.dend_0[0].connect(self.h.axon[0], 0, 0) #connect the dendrites and the axons together
    

    def insertChannels(self):
        """Insert active channels"""
        print('....inserting channels')
        for sec in self.h.allsec():
            sec.insert('pas')
            sec.insert('hcn2')
            sec.insert('Kv1_2')
            sec.insert('Kv1_3')
            sec.insert('Ca')
            sec.insert('Cad')
            sec.insert('gapJ')
            # insert gapJunction
            # gmax_gapJunction = 1
            # e_gapJunction = -35


    def channelAdjustment(self):
        """Adjust channels settings"""
        print('....Adjusting biophysics and channels')
        for sec in self.h.allsec():
            sec.Ra = self.settings.Ra
            for seg in sec:
                seg.cm = self.settings.cm

                seg.pas.e = self.settings.e_pas
                seg.pas.g = self.settings.g_pas

                seg.hcn2.gpeak = self.settings.hcn2_gpeak

                seg.Kv1_2.gKv1_2bar = self.settings.Kv1_2_gpeak
                seg.Kv1_3.gKv1_3bar = self.settings.Kv1_3_gpeak

                seg.Ca.gCabar = 0
                seg.gapJ.g = 0

        for [sec, d] in self.recordings['ribLocations']:
            if d == 1: d = .99
            if d == 0: d = .01
            sec(d).Ca.gCabar = self.settings.Cav_L_gpeak
            sec(d).gapJ.g = self.settings.gapJunction_gmax


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
        'ribIca' : [],
        'inhLocations' : [],
        'inhV' : [],
        'inhCai' : [],
        'inhIca' : []
        }

        XYZs = f.readLocation("morphology/RibbonLocations.txt")
        for ribNum in range(len(XYZs)):
            [sec,D] = f.findSectionForLocation(self.h, XYZs[ribNum,:])
            self.recordings['ribLocations'].append([sec,D])
            self.recordings['ribV'].append(self.h.Vector().record(sec(D)._ref_v ))
            self.recordings['ribCai'].append(self.h.Vector().record(sec(D)._ref_Cai))
            self.recordings['ribIca'].append(self.h.Vector().record(sec(D)._ref_iCa))
            
        XYZs = f.readLocation("morphology/InhSynLocations.txt")
        for inhNum in range(len(XYZs)):
            [sec,D] = f.findSectionForLocation(self.h, XYZs[inhNum,:])
            self.recordings['inhLocations'].append([sec,D])
            self.recordings['inhV'].append(self.h.Vector().record(sec(D)._ref_v ))
            self.recordings['inhCai'].append(self.h.Vector().record(sec(D)._ref_Cai))
            self.recordings['inhIca'].append(self.h.Vector().record(sec(D)._ref_iCa))

        for sec in self.h.allsec():
            for n in range(sec.nseg):
                D = 1/(2*sec.nseg) + n/sec.nseg
                self.recordings['segLocations'].append([sec, D])
                self.recordings['segV'].append(self.h.Vector().record(sec(D)._ref_v))
                self.recordings['segCai'].append(self.h.Vector().record(sec(D)._ref_Cai))
                self.recordings['segIca'].append(self.h.Vector().record(sec(D)._ref_iCa))

    def placeVoltageClamp(self, sec, D):
        """Put a voltage clamp at a specific location"""
        print('....adding a voltage clamp electrode')
        self.settings.v_init = self.settings.Hold1
        self.vClamp = self.h.SEClamp(sec(D))
        self.vClamp.dur1  = self.settings.ChangeClamp
        self.vClamp.dur2  = self.settings.tstop - self.settings.ChangeClamp
        self.vClamp.amp1  = self.settings.Hold1
        self.vClamp.amp2  = self.settings.Hold2
        self.recordings['iClamp'] = self.h.Vector().record(self.vClamp._ref_i)
        
    def placeCurrentClamp(self, sec, D, ):
        """Put a current clamp at a specific location"""
        print('....adding a current clamp electrode')
        self.IClamp = self.h.IClamp(sec(D))
        self.IClamp.delay = 100 
        self.IClamp.dur = 100 
        self.IClamp.amp = 100

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
            syn.updateSettings(self.settings.inhSyn)
        for syn in self.excSyns:
            syn.updateSettings(self.settings.excSyn)

    def updateAndRun(self):
        """Update settings and run simulaltion, then plot"""
        #self.settings = Settings()
        self.update()
        self.run()

        f.makePlot(self.recordings['time'], self.recordings['segV'][241])
        #f.makePlot(self.recordings['time'], self.recordings['ribV'][1], title = 'ribV')
        if self.settings.DoVClamp:
            f.makePlot(self.recordings['time'], self.recordings['iClamp'], title = 'Current Graph')

    def runIV(self, sampleTime, minV = -80, maxV = 40, steps = 15):
        """Run an Current voltage experiment"""
        Vs = np.linspace(minV, maxV, steps)
        Is = []
        for [n, v] in enumerate(Vs):
            self.settings.Hold2 = v
            self.update()
            print('Running ', v, 'mV (', n+1, '/', steps, ')')
            self.run()

            f.makePlot(self.recordings['time'], self.recordings['iClamp'], ymax = .05, ymin = -.1, xmin = 190)
            #val = f.pullMax(self.recordings['time'], self.recordings['iClamp'], 405)
            #val = f.pullAvg(self.recordings['time'], self.recordings['iClamp'], sampleTime, sampleTime+1)
            val = f.pullMin(self.recordings['time'],self.recordings['iClamp'],205)
            Is.append(val)
        f.makePlot(Vs, Is, title = 'IV graph')
        return [Vs, Is]


    def calcDistances(self, locations1, locations2, fileName):
        """calculate the path distances between sets of locations"""
        distMatrix = np.zeros([len(locations1), len(locations2)])

        for num1, loc1 in enumerate(locations1):
            for num2, loc2 in enumerate(locations2):
                dist = self.h.distance(loc1[0](loc1[1]), loc2[0](loc2[1]))
                distMatrix[num1, num2] = dist

        np.savetxt(fileName, distMatrix)
        return distMatrix
    def area(self):
        area = []
        for sec in self.h.axon:
            for seg in sec.allseg():
                area.append(seg.area())        
        return area
    
