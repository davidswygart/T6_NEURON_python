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
def runNewK(kG = .78 , inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=[]):
    #Run the model excitation only  (-45 mV -> -30 mV)
    T6.settings.Kv1_2_gpeak = kG
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
#%%
diffs120.append(runNewK(kG = 2, inhG=0.33e-5, stimFreq=52, darkFreq=2.9, inds=inds[[0]]))
diffs120.append(runNewK(kG = 4, inhG=0.65e-5, stimFreq=115, darkFreq=17, inds=inds[[0]]))
diffs120.append(runNewK(kG = 8, inhG=1.2e-5, stimFreq=280, darkFreq=44, inds=inds[[0]]))
diffs120.append(runNewK(kG = 12 , inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=inds[[0]]))
diffs120.append(runNewK(kG = 18, inhG=2.1e-5, stimFreq=1000, darkFreq=112, inds=inds[[0]]))
diffs120.append(runNewK(kG = 24, inhG=2.5e-5, stimFreq=1900, darkFreq=160, inds=inds[[0]]))

#%%
n=1
inds = T6.nNearestInh(n)

diffs1 = [];
diffs1.append(runNewK(kG = 2, inhG=0.41e-5, stimFreq=52, darkFreq=2.9, inds=inds))
diffs1.append(runNewK(kG = 4, inhG=0.9e-5, stimFreq=115, darkFreq=17, inds=inds))#perfect
diffs1.append(runNewK(kG = 8, inhG=1.95e-5, stimFreq=280, darkFreq=44, inds=inds))#good
diffs1.append(runNewK(kG = 12 , inhG=2.95e-5, stimFreq=500, darkFreq=70, inds=inds)) #good
diffs1.append(runNewK(kG = 18, inhG=4.5e-5, stimFreq=1000, darkFreq=112, inds=inds))#good
diffs1.append(runNewK(kG = 24, inhG=6e-5, stimFreq=1900, darkFreq=160, inds=inds))#good























