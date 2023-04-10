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
def runNewInh(inhG=1.62e-5, inds=[]):
    T6.settings.inhSyn.gMax = 0
    T6.update()
    ex.run()
    preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
    excStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
    
    # run with inhibition only
    T6.settings.inhSyn.gMax = inhG
    inhV = ex.loopThroughInhibitorySynapses(inds)   
    CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(excStimTimeV, preTimeV, inhV)
    print('Q1 = ', np.median(Q1Avg))
    return diffQ4toQ1, np.average(inhV)
    
    
#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop = 2001

#%% start with simulating all inhibitory synapses
n=120
inds = T6.nNearestInh(n)

diffs120 = [];
#%%
diffs120.append(runNewInh(inhG=0.29e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=0.38e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=0.52e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=0.68e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=0.91e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=1.22e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=1.62e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=2.43e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=3.65e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=5.47e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=8.2e-5,inds=inds[[0]]))
diffs120.append(runNewInh(inhG=12.3e-5,inds=inds[[0]]))


#%%
n=1
inds = T6.nNearestInh(n)

diffs1 = [];
diffs1.append(runNewInh(inhG=0.52e-5, inds=inds))
diffs1.append(runNewInh(inhG=0.7e-5, inds=inds))
diffs1.append(runNewInh(inhG=0.93e-5, inds=inds))
diffs1.append(runNewInh(inhG=1.24e-5, inds=inds))
diffs1.append(runNewInh(inhG=1.66e-5, inds=inds))
diffs1.append(runNewInh(inhG=2.2e-5, inds=inds))
diffs1.append(runNewInh(inhG=2.95e-5, inds=inds))
diffs1.append(runNewInh(inhG=4.43e-5, inds=inds))
diffs1.append(runNewInh(inhG=6.4e-5, inds=inds))
diffs1.append(runNewInh(inhG=9.6e-5, inds=inds))
diffs1.append(runNewInh(inhG=15e-5, inds=inds))

#%%
med = []
minn = []
maxx = []
hyper = []

for diff, inhV in diffs120:
    med.append(np.median(diff))
    minn.append(np.min(diff))
    maxx.append(np.max(diff))
    hyper.append(inhV)
    
    
hyper = -30 - np.array(hyper)




