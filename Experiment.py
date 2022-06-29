# -*- coding: utf-8 -*-
from neuron import h
from collections import namedtuple  
import numpy as np
from T6_Sim import Type6_Model
from UtilityFuncs import makePlot
from UtilityFuncs import calcDistances
import matplotlib.pyplot as plt

class Experiment():
    def __init__(self, model, tstop, temp, v_init):
        self.model = model
        self.rec = self._setRecordingVectors(model.secList)
        self.time = []
        self.tstop = tstop
        self.temp = temp
        self.v_init = v_init
        
             
    def _setRecordingVectors(self, secList):
        """Set recording points at each section"""
        print('....setting recording points')
        
        RecordingStruct = namedtuple("RecordingStruct", "v iCa cai") #create a datastructure to recording vectors
        rec = RecordingStruct([], [], []) # create an instance of this data structure with empty lists

        for sec in secList:
            vVec = h.Vector().record(sec(0.5)._ref_v)
            rec.v.append(vVec)
            
            iCaVec = h.Vector().record(sec(0.5)._ref_Cai)
            rec.iCa.append(iCaVec)
            
            caiVec = h.Vector().record(sec(0.5)._ref_iCa)
            rec.cai.append(caiVec)

        return rec


    def run(self):
        """Run the simulation"""
        print('....running simulation')
        h.load_file('stdrun.hoc')
        h.celsius = self.temp
        h.finitialize(self.v_init)
        h.frecord_init()
        h.continuerun(self.tstop)
        
        recVec = self.rec.v[0] #grab an example recording vector to see how many points it has
        self.time = np.linspace(0,self.tstop, len(recVec))
   

    def runSingleInh(self, newG, i):
        syn = self.model.inhSyns.syn[i]
        
        oldG = syn.gmax
        syn.gmax = newG
        self.run()
        syn.gmax = oldG
        
        
        secNum = self.model.inhSyns.secNum[i]
        v = self.rec.v[secNum]
        makePlot(self.time, v) 
        return v
        
        
    def avgRibV(self):
        volts = np.array(self.rec.v)
        ribVs = volts[self.model.ribbons.secNum, -1]
         
        soma2RibDist = calcDistances([self.model.soma.seg],self.model.ribbons.seg)
        plt.scatter(soma2RibDist, ribVs)
        print('average ribbon voltage = ', np.average(ribVs))
        return ribVs
        
        
    def LoopThoughInhibitorySynapses(self, name, newG):
        """Run function looping though and providing inhibition at each synapse"""        

        self.v_init = -40
        self.run() #run without in inhibition
        volts = np.array(self.rec.v)
        v_baseline = volts[:,-1]
        iCa = np.array(self.rec.iCa)
        iCa_baseline = iCa[:,-1]
        cai = np.array(self.rec.cai)
        cai_baseline = cai[:,-1]
        
        
        
        numRec = len(self.rec.v)
        inhSecNum = self.model.inhSyns.secNum
        numInh = len(inhSecNum)
        
        v_final = np.zeros((numRec, numInh))
        iCa_final = np.zeros((numRec, numInh))
        cai_final = np.zeros((numRec, numInh))
        
        self.v_init = -50
        for i in range(numInh):
            print('running ', i , ' of ', numInh)
            self.runSingleInh(newG, i)
            volts = np.array(self.rec.v)
            
            vDif = volts[:,-1] - v_baseline
            v_final[:, i] = vDif / vDif[inhSecNum[i]]
            plt.hist(v_final[:, i])
            
            iCa = np.array(self.rec.iCa)
            iCaDif = iCa[:,-1] - iCa_baseline
            iCa_final[:, i] = iCaDif / iCaDif[inhSecNum[i]]
            
            cai = np.array(self.rec.cai)
            caiDif = cai[:,-1] - cai_baseline
            cai_final[:, i] = caiDif / caiDif[inhSecNum[i]]
        
        np.savetxt(name + 'v.txt', v_final)
        np.savetxt(name + 'iCa.txt', iCa_final)
        np.savetxt(name + 'cai.txt', cai_final)

    def placeVoltageClamp(self, hold1, duration, hold2):
        """Put a voltage clamp at soma"""
        print('....adding a voltage clamp electrode')
        self.vClamp = h.SEClamp(self.model.soma.seg) 
        self.vClamp.dur1  = duration
        self.vClamp.dur2  = 1e9 #make it super long
        self.vClamp.amp1  = hold1
        self.vClamp.amp2  = hold2
        
        self.v_init = hold1
        self.vClampRec = h.Vector().record(self.vClamp._ref_i)









    # def area(self):
    #     area = []
    #     for sec in h.axon:
    #         for seg in sec.allseg():
    #             area.append(seg.area())        
    #     return area
    
