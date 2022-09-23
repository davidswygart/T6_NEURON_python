# -*- coding: utf-8 -*-
from collections import namedtuple  
import numpy as np
import matplotlib.pyplot as plt

class Experiment():
    def __init__(self, model, tstop=1000, temp=32, v_init=-45):
        self.model = model
        self.rec = self._setRecordingVectors(model.secList)
        self.time = []
        self.tstop = tstop
        self.temp = temp
        self.v_init = v_init
        
             
    def _setRecordingVectors(self, secList):
        """Set recording points at inhibitory and ribbon synapses"""
        print('....setting recording points')
        
        RecordingStruct = namedtuple("RecordingStruct", "ribV ribCai inhV inhCai") #create a datastructure to recording vectors
        rec = RecordingStruct([],[],[],[]) # create an instance of this data structure with empty lists
        
        h = self.model.h
        
        for seg in self.model.ribbons.seg:
            vVec = h.Vector().record(seg._ref_v)
            rec.ribV.append(vVec)
            
            caiVec = h.Vector().record(seg._ref_Cai)
            rec.ribCai.append(caiVec)
        
        for seg in self.model.inhSyns.seg:
            vVec = h.Vector().record(seg._ref_v)
            rec.inhV.append(vVec)
            
            caiVec = h.Vector().record(seg._ref_Cai)
            rec.inhCai.append(caiVec)
        
        return rec
  
    def run(self):
        """Run the simulation"""
        print('....running simulation')
        
        h=self.model.h
        h.load_file('stdrun.hoc')
        h.celsius = self.temp
        h.finitialize(self.v_init)
        h.frecord_init()
        h.continuerun(self.tstop)
        
        recVec = self.rec[0][0] #grab an example recording vector to see how many points it has
        self.time = np.linspace(0,self.tstop, len(recVec))
        
    
        
    def LoopThoughInhibitorySynapses(self, folder='no save', inhInds='all'):
        """Run function looping though and providing inhibition at each synapse"""   
        
        if inhInds=='all': inhInds=list(range(len(self.model.inhSyns.syn)))
        
        numInh = len(inhInds)
        numRibs = len(self.rec.ribV)
        
        inhStart = self.model.settings.inhSyn['start']
        excTime = round((inhStart-1) / self.model.h.dt) #excitation is recorded 1 ms before inhibition onset

        dimension2 = ['exc', 'inh', 'delta', 'ratio']
        dimension3 = ['volts','Cai']
        
        dataOut = np.zeros((numInh, numRibs+1, len(dimension2), len(dimension3))) #the first value is for the inhibitory synapse
        
        for inhSyn in self.model.inhSyns.syn:
            inhSyn.gmax = 0 #double check that all inhibtion is turned off
            
        np.seterr(divide='ignore', invalid='ignore')
        
        for i, inhInd in enumerate(inhInds):
            print('running ', i , ' of ', numInh, ', inh Syn #', inhInd)
        
            inhSyn = self.model.inhSyns.syn[inhInd]
            inhSyn.gmax = self.model.settings.inhSyn['gmax']
            
            self.run()
            
            inhSyn.gmax = 0
            
            
            # the first column is data for the activated inh synapse
            volts = np.array(self.rec.inhV[inhInd])
            cai = np.array(self.rec.inhCai[inhInd])
            resp = np.stack((volts, cai), axis=1)
            
            dataOut[i,0,0,:] = resp[excTime, :]
            dataOut[i,0,1,:] = resp[-1, :]
            dataOut[i,0,2,:] = resp[-1, :] - resp[excTime, :]
            dataOut[i,0,3,:] = dataOut[i,0,2,:] / dataOut[i,0,2,:]
            
            
            # the remaining rows are for the ribbons
            volts = np.array(self.rec.ribV)
            cai = np.array(self.rec.ribCai)
            resp = np.stack((volts, cai), axis=2)

            dataOut[i,1:,0,:] = resp[:, excTime, :]
            dataOut[i,1:,1,:] = resp[:, -1, :]
            dataOut[i,1:,2,:] = resp[:, -1, :] - resp[:, excTime, :]
            dataOut[i,1:,3,:] = dataOut[i,1:,2,:] / dataOut[i,0,2,:]
            
            print('avg. rib mV = ', np.average(dataOut[i,1:,0,0]))
            print('inh. Syn mV = ', dataOut[i,0,1,0])
            print('avg. ratio = ', np.average(dataOut[i,1:,3,0]), '\n')
            
            self.makePlot(self.time, np.array(self.rec.inhV[inhInd]), title='inhibition', xlabel='time (ms)', ylabel='mV')
            self.makePlot(self.time, volts[90,:], title='ribbon 90',xlabel='time (ms)', ylabel='mV')

        if folder != 'no save':
            import os
            for r,rType in enumerate(dimension2):
                for u,unit in enumerate(dimension3):
                    fullPath = folder + unit + '\\'
                    os.makedirs(fullPath, exist_ok = True)
                    
                    fullFile = fullPath + rType + '.csv'
                    np.savetxt(fullFile, dataOut[:,:,r,u], delimiter=',' , header="inh,ribbons")
                
        return dataOut
    
    def hist(vals, title = '', ylabel = '', xlabel = '', xmin = 'calc', xmax = 'calc'):
        fig, ax = plt.subplots()
        ax.hist(vals)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        
        if xmin == 'calc': xmin = min(vals)
        if xmax == 'calc': xmax = max(vals)

        plt.xlim(xmin, xmax)
        plt.show()
                
    def placeVoltageClamp(self, hold1, duration, hold2):
        """Put a voltage clamp at soma"""
        print('....adding a voltage clamp electrode')
        h=self.model.h
        self.vClamp = h.SEClamp(self.model.soma.seg) 
        self.vClamp.dur1  = duration
        self.vClamp.dur2  = 1e9 #make it super long
        self.vClamp.amp1  = hold1
        self.vClamp.amp2  = hold2
        
        self.v_init = hold1
        self.vClampRec = h.Vector().record(self.vClamp._ref_i)
        
    def makePlot(self, x, y, title = '', ylabel = '', xlabel = '', ymin = 'calc', ymax = 'calc', xmin = 'calc', xmax = 'calc'):
        """Create a plot X and Y"""
        fig, ax = plt.subplots()
        ax.plot(x,y)
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        
        x = np.array(x)
        y = np.array(y)
        
        if xmin == 'calc': xmin = min(x)
        if xmax == 'calc': xmax = max(x)
        
        
        if ymin == 'calc': ymin = min(y)
        if ymax == 'calc': ymax = max(y)

        
        plt.ylim(ymin, ymax)
        plt.xlim(xmin, xmax)
        plt.show()
