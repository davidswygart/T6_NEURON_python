import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
sys.path.append("/nrn/lib/python")
from neuron import h

import numpy as np
from collections import namedtuple 
from settings import Settings

class Type6_Model():
    def __init__(self):
        """Build the model cell."""
        self.h = h
        self.settings = Settings()
        
        [secList, p3d] = self._loadMorphology()
        self.secList = secList
        self.pnt3D = p3d
        
        self.inhSyns = self._addSynapses("morphology/InhSynLocations.txt", self.settings.inhSyn)
        self.excSyns = self._addSynapses("morphology/InputRibbonLocations.txt", self.settings.excSyn)
        self.ribbons = self._findRibbons("morphology/RibbonLocations.txt")
        self.soma = self._findSoma()
        self._biophys()
        self.update()
        
    def _addSynapses(self, LocationFile, settings):
        """Add synapses to the locations specified in LocationFile"""
        print('....adding synapses: ', LocationFile)
        iList = self.nearestPnt3D(LocationFile)   
        
        Synapse = namedtuple("Synapse", "syn secNum sec secDist seg") #create a datastructure to hold synapse info
        synStruct = Synapse([],[],[],[],[])
        
        for i in iList:
            secNum = self.pnt3D.secNum[i]
            secDist = self.pnt3D.secDist[i]
            
            sec = self.secList[secNum]
            seg = sec(secDist)
            syn = h.biSyn(seg)
            
            synStruct.syn.append(syn)
            synStruct.secNum.append(secNum)
            synStruct.sec.append(sec)
            synStruct.secDist.append(secDist)
            synStruct.seg.append(seg)            
            
        return synStruct

    def _findRibbons(self, LocationFile):
         
        Ribbons = namedtuple("Ribbons", "secNum sec secDist seg") #create a datastructure to hold ribbon data
        ribs = Ribbons([],[],[],[]) #create an instance of this data structure with empty lists
        
        ind3D = self.nearestPnt3D(LocationFile)
        for i in ind3D:
            secNum = self.pnt3D.secNum[i]
            sec = self.secList[secNum]
            secDist = self.pnt3D.secDist[i]
            seg = sec(secDist)
            
            ribs.secNum.append(secNum)
            ribs.sec.append(sec)
            ribs.secDist.append(secDist)
            ribs.seg.append(seg)        
        return ribs
    
    def _findSoma(self):   
        ind3D = np.argmax(self.pnt3D.diam) #find 3d point with maximum diameter
            
        secNum = self.pnt3D.secNum[ind3D]
        secDist = self.pnt3D.secDist[ind3D]
        sec = self.secList[secNum]
        seg = sec(secDist)
        
        
        Soma = namedtuple("Soma", "secNum sec secDist seg") #create a datastructure to hold soma data
        return Soma(secNum,sec,secDist,seg) #create an instance of this data structure with empty lists
      
    def nearestPnt3D(self, LocationFile):
        """A list of the closest xyz index given a list of XYZ points"""
        locList = self.readLocation(LocationFile)
        iList = []
        for Num in range(len(locList)):
            xyz = locList[Num,:]
            dif = np.array(self.pnt3D.XYZ) - np.array(xyz)
            dists = np.sqrt(np.sum(np.square(dif), axis = 1))
            iList.append(np.argmin(dists))
        return iList
            
    def _loadMorphology(self):
        """Load morphology information from pre-created hoc files"""
        print('....loading morphology')
        h.load_file( "morphology/axonMorph.hoc") #Load axon morphology (created in Cell Builder)
        h.load_file( "morphology/dendriteMorph.hoc") #Load dendrite morphology (created in Cell Builder)
        h.dend[0].connect(h.axon[0], 0, 0) #connect the dendrites and the axons together
        
        secList = list(h.allsec())
        
        morphPoints3D = namedtuple("morphPoints3D", "XYZ diam secNum secDist") #create a datastructure to hold xyz data
        p3d = morphPoints3D([], [], [], []) # create an instance of this data structure with empty lists
        
        for [secNum, sec] in enumerate(secList): # loop through every section in the model
            for i in range(int(sec.n3d())):  #loop through every 3D model morphology point for this section (originally specified in swc traces)
                x = sec.x3d(i)
                y = sec.y3d(i)
                z = sec.z3d(i)
                p3d.XYZ.append([x,y,z])
                
                p3d.diam.append(sec.diam3d(i))
                
                p3d.secNum.append(secNum)
                
                dist = sec.arc3d(i) / sec.L
                p3d.secDist.append(dist)
        return [secList, p3d]

    def _biophys(self):
        """Insert active channels and set cell biophysics"""
        print('....inserting channels')
        for sec in h.allsec():
            sec.insert('pas')
            sec.insert('hcn2')
            sec.insert('Kv1_2')
            sec.insert('Ca')
            sec.insert('Cad')

    def update(self):
        """Update all synapses and sections with current model settings"""
        self.updateBiophys()
        self.updateSynapses()

    def updateBiophys(self):
        """Adjust channels settings"""
        print('....Adjusting biophysics and channels')
        for sec in h.allsec():
            sec.Ra = self.settings.Ra
            for seg in sec:
                seg.cm = self.settings.cm

                seg.pas.e = self.settings.e_pas
                seg.pas.g = self.settings.g_pas

                seg.Kv1_2.gMax = self.settings.Kv1_2_gpeak
                
                #Calcium and HC2 channels are only in axons
                seg.Ca.gMax = 0 
                seg.hcn2.gMax = 0
        
        for sec in h.axon:
            for seg in sec:
                seg.Ca.gMax = self.settings.Cav_L_gpeak
                seg.hcn2.gMax = self.settings.hcn2_gpeak


    def updateSynapses(self):
        print('....updating synapse values')
        for syn in self.inhSyns.syn:
            syn.onset = self.settings.inhSyn['start']
            syn.gmax = self.settings.inhSyn['gmax']
            syn.e = self.settings.inhSyn['e']
            
        for syn in self.excSyns.syn:
            syn.onset = self.settings.excSyn['start']
            syn.gmax = self.settings.excSyn['gmax']
            syn.e = self.settings.excSyn['e']
            syn.basePropG = self.settings.excSyn['darkProp']
            
    def readLocation(self, fileName):
        """Read the XYZ locations from a txt file"""
        with open(fileName) as file_object:
            lines = file_object.readlines()
        XYZ = np.zeros([len(lines), 3])
        for lineNum, line in enumerate(lines):
            XYZ[lineNum,:] = line.split()
        return XYZ
    
    def calcDistances(self, segList1, segList2):
        """calculate the path distances between sets of locations"""
        num1 = len(segList1)
        num2 = len(segList2)  
        distMatrix = np.zeros([num1, num2])

        for n1 in range(num1):
            seg1 = segList1[n1]
            for n2 in range(num2):
                seg2 = segList2[n2]

                dist = h.distance(seg1, seg2)
                distMatrix[n1, n2] = dist
        return distMatrix
    
    def nNearestInh(self, n):
        dists = self.calcDistances(self.inhSyns.seg,self.inhSyns.seg)
        nearest = np.argsort(dists, axis = 1)
        inds = nearest[:,0:n]
        return inds.tolist()
        