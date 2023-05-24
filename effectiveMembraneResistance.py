#%% For calculating CSR
def calcCSR(stimTimeV, preTimeV, inhV):
    excDelta = stimTimeV - preTimeV
    inhDelta = stimTimeV - inhV
    CSR = excDelta / inhDelta

    # sort CSR and split into quartiles
    sortedCSR = np.sort(CSR, axis = 1)# sort by low to high suppression
    
    quartileN = round(len(CSR[0,:])/4)
    
    Q1Avg = np.mean(sortedCSR[:, 0 : quartileN], axis = 1)
    Q4Avg = np.mean(sortedCSR[:, quartileN*3-1 : ], axis = 1)
    diffQ4toQ1 = Q4Avg-Q1Avg
    
    return CSR, Q1Avg, Q4Avg, diffQ4toQ1

def getCsrRange(inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=[]):
    #Run the model excitation only  (-45 mV -> -30 mV)
    T6.settings.excDark.frequency = darkFreq
    T6.settings.excSyn.frequency = stimFreq
    T6.settings.inhSyn.gMax = 0
    T6.update()
    ex.run()
    preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
    excStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
    
    #run with inhibition only
    T6.settings.inhSyn.gMax = inhG
    inhV = ex.loopThroughInhibitorySynapses(inds)   
    CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(excStimTimeV, preTimeV, inhV)
    print('Q1 = ', np.median(Q1Avg))
    return diffQ4toQ1


def loopAndRecordConductances(inhLists):
    # inhLists is a list of lists of lists inhibitory synapses that should be simultaneously turned on
    numLoops = len(inhLists)
    numInh = len(T6.inhSyns.seg)

    gCa = []
    gKv = []
    gHCN2 = []
    
    for i, loopInhInds in enumerate(inhLists):
        print('running ', i , ' of ', numLoops) #, ', inh Syn #', loopInhInds)
        #turn off all ihibitory synapses
        for con in T6.inhSyns.con:
            con.weight[0] = 0
        #turn on select ihibitory synapses
        for ind in loopInhInds:
            T6.inhSyns.con[ind].weight[0] = T6.settings.inhSyn.gMax * numInh / len(loopInhInds)
        ex.run()
        
        gCa.append(np.array(ex.rec.gCa)[:,0:-1:40])# decimate so I don't run out of memory
        gKv.append(np.array(ex.rec.gKv1_2)[:,0:-1:40])
        gHCN2.append(np.array(ex.rec.gHCN2)[:,0:-1:40])
        
    gCa = np.array(gCa)
    gKv = np.array(gKv)
    gHCN2 = np.array(gHCN2)
    return gCa, gKv, gHCN2

def calcMembraneArea():
    #calculate membrane area for each segment (um2)
    segArea = []
    for sec in T6.h.allsec():
        for seg in sec:
            segArea.append(seg.area())
    segArea = np.expand_dims(np.array(segArea),1)
    plt.hist(segArea)
    return segArea

def calculateTotalConductance(gPerCm):
    Um2Tocm2 = 1e-8  
    segArea = calcMembraneArea()
    gnS = gPerCm * segArea * Um2Tocm2 * 1e9
    gTotal = np.sum(gnS, axis=1)
    gAvg = np.mean(gTotal, axis=0)
    gStd = np.std(gTotal, axis=0)
    return gAvg, gStd

#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop = 2500
#ex.tstop = 2001

#%%
n = 60
inds = T6.nNearestInh(n)
#inds = inds[[45,46]]
gCa, gKv, gHcn2 = loopAndRecordConductances(inds)
gLeak = np.full(np.shape(gCa), T6.settings.g_pas) #just an array with the same value
total = gCa + gKv + gHcn2 + gLeak
#%% plot conductance at soma
i = 131
caAvg = np.mean(gCa[:,i,:]*1e6, axis=0)
caStd = np.std(gCa[:,i,:]*1e6, axis=0)
kvAvg = np.mean(gKv[:,i,:]*1e6, axis=0)
kvStd = np.std(gKv[:,i,:]*1e6, axis=0)
hcn2Avg = np.mean(gHcn2[:,i,:]*1e6, axis=0)
hcn2Std = np.std(gHcn2[:,i,:]*1e6, axis=0)
totalAvg = np.mean(total[:,i,:]*1e6, axis=0)
totalStd = np.std(total[:,i,:]*1e6, axis=0)

#%% plot conducane at axon start
i = 0
caAvg = np.mean(gCa[:,i,:]*1e6, axis=0)
caStd = np.std(gCa[:,i,:]*1e6, axis=0)
kvAvg = np.mean(gKv[:,i,:]*1e6, axis=0)
kvStd = np.std(gKv[:,i,:]*1e6, axis=0)
hcn2Avg = np.mean(gHcn2[:,i,:]*1e6, axis=0)
hcn2Std = np.std(gHcn2[:,i,:]*1e6, axis=0)
totalAvg = np.mean(total[:,i,:]*1e6, axis=0)
totalStd = np.std(total[:,i,:]*1e6, axis=0)
#%% plot conductance at terminal branch (on right)
i = 50
caAvg = np.mean(gCa[:,i,:]*1e6, axis=0)
caStd = np.std(gCa[:,i,:]*1e6, axis=0)
kvAvg = np.mean(gKv[:,i,:]*1e6, axis=0)
kvStd = np.std(gKv[:,i,:]*1e6, axis=0)
hcn2Avg = np.mean(gHcn2[:,i,:]*1e6, axis=0)
hcn2Std = np.std(gHcn2[:,i,:]*1e6, axis=0)
totalAvg = np.mean(total[:,i,:]*1e6, axis=0)
totalStd = np.std(total[:,i,:]*1e6, axis=0)
#%% calculate total conductances across membrane
gCaTotal_avg, gCaTotal_std = calculateTotalConductance(gCa)
gKvTotal_avg ,gKvTotal_std = calculateTotalConductance(gKv)
gHcn2Total_avg, gHcn2Total_std = calculateTotalConductance(gHcn2)
gLeakTotal_avg, gLeakTotal_std = calculateTotalConductance(gLeak)

gTotal_avg, gTotal_std = calculateTotalConductance(gCa+gKv+gHcn2+gLeak)                      

#%%%%%%%%%%%%%%%%%% increase leak conductance equally across whole cell in place of active conductances %%%%%%%%%%%%%%%%%%%%%%%%
# no active conductances
T6.settings.hcn2_gpeak = 0
T6.settings.Kv1_2_gpeak = 0
T6.settings.Cav_L_gpeak = 0

newPassiveConductance = np.mean(gTotal_avg[1000:2000]) / np.sum(calcMembraneArea()) * 1e8 * 1e-9 #average conductance and convert to S/cm2
T6.settings.g_pas = newPassiveConductance

n=60
inds = T6.nNearestInh(n)
#inds = inds[[45]]
diffQ4toQ1_uniformIncrease = getCsrRange(inhG=0.92e-5, stimFreq=212, darkFreq=92, inds=inds)





#%%%%%%%%%%%%%%%%%% increase leak conductance specific to each segment %%%%%%%%%%%%%%%%%%%%%%%%
# no active conductances
T6.settings.hcn2_gpeak = 0
T6.settings.Kv1_2_gpeak = 0
T6.settings.Cav_L_gpeak = 0

def getCsrRangeLocal(inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=[]):
    #Run the model excitation only  (-45 mV -> -30 mV)
    T6.settings.excDark.frequency = darkFreq
    T6.settings.excSyn.frequency = stimFreq
    T6.settings.inhSyn.gMax = 0
    T6.update()
    for i in range(len(T6.segList)):
        T6.segList[i].pas.g = gSegAvg[i]
    
    ex.run()
    preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
    excStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
    
    #run with inhibition only
    T6.settings.inhSyn.gMax = inhG
    inhV = ex.loopThroughInhibitorySynapses(inds)   
    CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(excStimTimeV, preTimeV, inhV)
    print('Q1 = ', np.median(Q1Avg))
    return diffQ4toQ1


gSeg = np.mean(total[:,:,1000:2000], axis=2)
gSegAvg = np.mean(gSeg, axis=0)



n=60
inds = T6.nNearestInh(n)
#inds = inds[[45]]
diffQ4toQ1_localIncrease = getCsrRangeLocal(inhG=0.92e-5, stimFreq=209, darkFreq=91.5, inds=inds)








