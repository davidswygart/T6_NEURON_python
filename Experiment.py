# -*- coding: utf-8 -*-
from collections import namedtuple  
import numpy as np
import matplotlib.pyplot as plt

class Experiment():
    def __init__(self, model, tstop=2500, temp=32, v_init=-45):
        self.model = model
        self.rec = self._setRecordingVectors(model.secList)
        self.time = []
        self.tstop = tstop
        self.temp = temp
        self.v_init = v_init
        
             
    def _setRecordingVectors(self, secList):
        """Set recording points at inhibitory and ribbon synapses"""
        print('....setting recording points')
        
        RecordingStruct = namedtuple("RecordingStruct", "ribV ribCai inhV inhCai gKv1_2 gHCN2 gCa") #create a datastructure to recording vectors
        rec = RecordingStruct([],[],[],[],[],[],[]) # create an instance of this data structure with empty lists
        
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
            
        for sec in h.allsec():
            for seg in sec:
                rec.gKv1_2.append(h.Vector().record(seg.Kv1_2._ref_gKv1_2))
                rec.gHCN2.append(h.Vector().record(seg.hcn2._ref_gHCN2))
                rec.gCa.append(h.Vector().record(seg.Ca._ref_gCa))
                
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
        
    def loopThroughInhibitorySynapses(self, inhLists):
        # inhLists is a list of lists of lists inhibitory synapses that should be simultaneously turned on
        

    
        numLoops = len(inhLists)
        numRibs = len(self.model.ribbons.sec)
        numInh = len(self.model.inhSyns.seg)
          
        ribbonV = np.zeros((numLoops, numRibs))
        
        for i, loopInhInds in enumerate(inhLists):
            print('running ', i , ' of ', numLoops, ', inh Syn #', loopInhInds)
            
            #turn off all ihibitory synapses
            for con in self.model.inhSyns.con:
                con.weight[0] = 0
                
            #turn on select ihibitory synapses
            for ind in loopInhInds:
                self.model.inhSyns.con[ind].weight[0] = self.model.settings.inhSyn.gMax * numInh / len(loopInhInds)

            
            self.run()
            ribbonV[i,:] = self.averageRibVoltage()
            
            self.makePlot(self.time, self.rec.ribV[90], title='ribbon 90',xlabel='time (ms)', ylabel='mV')

        return ribbonV
    
    def vClampSineWave(self, frequency = 1, baselineV = -38, amplitudeV = 7):

        t = np.linspace(0,self.tstop, round(self.tstop/self.model.h.dt))
        sin = np.sin(frequency * t * 2* np.pi / 1000) * amplitudeV + baselineV
        sin = self.model.h.Vector(sin)

        sin.play(self.vClamp._ref_amp1, self.model.h.dt)       
        
        self.run()

        sin.play_remove()
        plt.plot(self.time, self.rec.ribV[0])
        
        
        
    def LoopThoughInhibitorySynapses2(self, folder='no save', inhLists='all'):
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
            inhSynV = np.array(self.rec.inhV)
            
            inhSynExc = inhSynV[:, excTime]
            inhSynInh = inhSynV[:,-1]
            inhSynDelta = inhSynExc - inhSynInh
            maxDeltaInhSynInd = np.argmax(inhSynDelta)
                
            excV[i,0] = inhSynExc[maxDeltaInhSynInd] # voltage at time of excitation
            inhV[i,0] = inhSynInh[maxDeltaInhSynInd] # voltage at time of inhibition

            # the remaining columns are for the ribbons
            ribV = np.array(self.rec.ribV)

            excV[i,1:] = ribV[:, excTime]
            inhV[i,1:] = ribV[:, -1]

            
            print('avg. rib mV = ', np.average(excV[i,1:]))
            print('inh. Syn mV (max delta) = ', inhV[i,0],'\n')
            
            self.makePlot(self.time, inhSynV[maxDeltaInhSynInd,:], title='inhibition', xlabel='time (ms)', ylabel='mV')
            self.makePlot(self.time, ribV[90,:], title='ribbon 90',xlabel='time (ms)', ylabel='mV')
        
        delta = excV - inhV
        # trace_Rib1 = ribV[np.argmax(delta),:]
        # trace_rib2 = ribV[np.argmin(delta),:]
        
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
    
    def averageRibVoltage(self, startTimeMs = 1000, endTimeMs = 2000):
        """ Average voltage of ribbons between two time points"""
        
        startInd = np.argmin(np.abs(self.time - startTimeMs))
        endInd = np.argmin(np.abs(self.time - endTimeMs))
        
        ribV = np.array(self.rec.ribV)
        ribV = ribV[:,startInd:endInd]
        ribV = np.mean(ribV, axis=1)
        
        print('average ribbon = ', np.round(np.mean(ribV),1), ' V')
        
        return ribV






