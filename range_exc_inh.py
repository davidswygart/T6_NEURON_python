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

#%%
def runNewExc(inhG=1.62e-5, stimFreq=500, inds=[]):
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
    return diffQ4toQ1, np.mean(excStimTimeV)
    #return excStimTimeV
    
    
#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop = 2001

#%% start with simulating all inhibitory synapses
n=120
inds = T6.nNearestInh(n)

diffs120 = [];

diffs120.append(runNewExc(inhG=0.352e-5, stimFreq=60, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=0.64e-5, stimFreq=125, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=1.06e-5, stimFreq=250, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=1.62e-5, stimFreq=500, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=2.24e-5, stimFreq=1000, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=2.88e-5, stimFreq=2000, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=3.42e-5, stimFreq=4000, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=4e-5, stimFreq=10000, inds=inds[[0]]))
diffs120.append(runNewExc(inhG=4.4e-5, stimFreq=30000, inds=inds[[0]]))

#%%
n=1
inds = T6.nNearestInh(n)

diffs1 = [];
#%%
diffs1.append(runNewExc(inhG=0.425e-5, stimFreq=60, inds=inds))
diffs1.append(runNewExc(inhG=0.84e-5, stimFreq=125, inds=inds))
diffs1.append(runNewExc(inhG=1.6e-5, stimFreq=250, inds=inds))
diffs1.append(runNewExc(inhG=2.95e-5, stimFreq=500, inds=inds))#1.087
diffs1.append(runNewExc(inhG=8.64e-5, stimFreq=2000, inds=inds))
diffs1.append(runNewExc(inhG=22e-5, stimFreq=10000, inds=inds))
diffs1.append(runNewExc(inhG=32e-5, stimFreq=30000, inds=inds))

#%%
difMax = []
difMed = []
difMin = []
exc = []
for diff, excV in diffs1:
    exc.append(excV+45)
    difMax.append(np.max(diff))
    difMed.append(np.median(diff))
    difMin.append(np.min(diff))
    



















