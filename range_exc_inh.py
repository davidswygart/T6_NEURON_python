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
    
#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop = 2001


#%%
n=60
inds = T6.nNearestInh(n)
#inds = inds[[45]]

diffs = [];
#%%
diffs.append(runNewExc(inhG=0.359e-5, stimFreq=60, inds=inds))
#%%
diffs.append(runNewExc(inhG=0.66e-5, stimFreq=125, inds=inds))
#%%
diffs.append(runNewExc(inhG=1.1e-5, stimFreq=250, inds=inds))
#%%
diffs.append(runNewExc(inhG=1.73e-5,stimFreq=515, inds=inds))
#%%
diffs.append(runNewExc(inhG=3.05e-5, stimFreq=2000, inds=inds))
#%%
diffs.append(runNewExc(inhG=4.3e-5, stimFreq=10000, inds=inds))
#%%
diffs.append(runNewExc(inhG=4.7e-5, stimFreq=30000, inds=inds))



















