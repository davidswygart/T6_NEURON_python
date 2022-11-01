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
        
    def LoopThoughInhibitorySynapses(self, folder='no save', inhLists='all'):
        """Run function looping though and providing inhibition at each synapse"""  
        # inhLists is a list of lists of inhibitory synapses that should be simultaneously turned on
        
        for syn in self.model.inhSyns.syn:
            syn.gmax = 0 #double check that all inhibition is turned off for start of experiment
        
        if inhLists=='all':
            inhLists = []
            for i in range(len(self.model.inhSyns.syn)):
                inhLists.append([i])
    
        numLoops = len(inhLists)
        numRibs = len(self.rec.ribV)
        
        inhStart = self.model.settings.inhSyn['start']
        excTime = round((inhStart-1) / self.model.h.dt) #excitation is recorded 1 ms before inhibition onset
        
        excV = np.zeros((numLoops, numRibs+1)) #the first column value is for the inhibitory synapse
        inhV = np.zeros((numLoops, numRibs+1)) #the first column value is for the inhibitory synapse
        
        for i, loopInhInds in enumerate(inhLists):
            print('running ', i , ' of ', numLoops, ', inh Syn #', loopInhInds)
        
            for ind in loopInhInds:
                syn = self.model.inhSyns.syn[ind]
                syn.gmax = self.model.settings.inhSyn['gmax']
            
            self.run()
            
            for ind in loopInhInds:
                syn = self.model.inhSyns.syn[ind]
                syn.gmax = 0
            
            # the first column is data for the activated inh synapse
            avgInhV = np.zeros(len(self.rec.inhV[0]))
            for ind in loopInhInds:
                avgInhV += np.array(self.rec.inhV[ind])
            avgInhV = avgInhV / len(loopInhInds) #average voltage at the activated inhibitory synapses
                
            excV[i,0] = avgInhV[excTime] # voltage at time of excitation
            inhV[i,0] = avgInhV[-1] # voltage at time of inhibition

            # the remaining columns are for the ribbons
            ribV = np.array(self.rec.ribV)

            excV[i,1:] = ribV[:, excTime]
            inhV[i,1:] = ribV[:, -1]
            delta = excV

            
            print('avg. rib mV = ', np.average(excV[i,1:]))
            print('avg inh. Syn mV = ', inhV[i,0],'\n')
            
            self.makePlot(self.time, avgInhV, title='inhibition', xlabel='time (ms)', ylabel='mV')
            self.makePlot(self.time, ribV[90,:], title='ribbon 90',xlabel='time (ms)', ylabel='mV')
        
        delta = excV - inhV
        ratio = delta / delta[:,[0]]
        print('avg. ratio = ', np.average(ratio[:,1:]), ' +- ', np.std(ratio[:,1:]), '\n')

        if folder != 'no save':
            import os
            os.makedirs(folder, exist_ok = True)
            
            file = folder + '\\excV.csv'
            np.savetxt(file, excV, delimiter=',' , header="inh,ribbons")
            
            file = folder + '\\inhV.csv'
            np.savetxt(file, delta, delimiter=',' , header="inh,ribbons")
            
            file = folder + '\\delta.csv'
            np.savetxt(file, delta, delimiter=',' , header="inh,ribbons")
            
            file = folder + '\\ratio.csv'
            np.savetxt(file, ratio, delimiter=',' , header="inh,ribbons")
        return ratio
    
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
