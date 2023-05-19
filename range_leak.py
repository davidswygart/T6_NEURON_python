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

def runNewLeak(leakG = 3.91e-5, inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=[]):
    #Run the model excitation only  (-45 mV -> -30 mV)
    T6.settings.g_pas = leakG
    T6.settings.excDark.frequency = darkFreq
    T6.settings.excSyn.frequency = stimFreq
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
    return diffQ4toQ1
    
#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

# Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop = 2001

#%%
n=60
inds = T6.nNearestInh(n)
#inds = inds[[45]]

diffs60 = [];
#%%
diffs60.append(runNewLeak(leakG = 0, inhG=1.63e-5, stimFreq=440, darkFreq=52.5, inds=inds))
#%%
diffs60.append(runNewLeak(leakG = 3e-5, inhG=1.7e-5, stimFreq=500, darkFreq=65, inds=inds))
#%%
diffs60.append(runNewLeak(leakG = 3.91e-5, inhG=1.73e-5,stimFreq=515, darkFreq=70, inds=inds))
#%%
diffs60.append(runNewLeak(leakG = 6e-5, inhG=1.78e-5, stimFreq=550, darkFreq=80, inds=inds))
#%%
diffs60.append(runNewLeak(leakG = 9e-5, inhG=1.82e-5, stimFreq=620, darkFreq=93, inds=inds))



















