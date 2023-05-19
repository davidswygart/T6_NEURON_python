def calcCSR(stimTimeV, preTimeV, inhV):
    excDelta = stimTimeV - preTimeV
    inhDelta = stimTimeV - inhV
    CSR = excDelta / inhDelta
    sortedCSR = np.sort(CSR, axis = 1)# sort by low to high suppression
    quartileN = round(len(CSR[0,:])/4)
    Q1Avg = np.mean(sortedCSR[:, 0 : quartileN], axis = 1)
    Q4Avg = np.mean(sortedCSR[:, quartileN*3-1 : ], axis = 1)
    diffQ4toQ1 = Q4Avg-Q1Avg
    return CSR, Q1Avg, Q4Avg, diffQ4toQ1

def runRa(ra = 132, inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=[]):
    #Run the model excitation only  (-45 mV -> -30 mV)
    T6.settings.Ra = ra
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

#%% start with simulating all inhibitory synapses
n=60
inds = T6.nNearestInh(n)
#inds = inds[[45]]

diffs60 = [];
#%%
diffs60.append(runRa(ra = 1, inhG=2.54e-5, stimFreq=330, darkFreq=64.5, inds=inds))
#%%
diffs60.append(runRa(ra = 60, inhG=2.1e-5, stimFreq=404, darkFreq=67, inds=inds))
#%%
diffs60.append(runRa(ra = 132, inhG=1.73e-5,stimFreq=515, darkFreq=70, inds=inds))
#%%
diffs60.append(runRa(ra = 264, inhG=1.3e-5, stimFreq=870, darkFreq=76, inds=inds))
#%%
diffs60.append(runRa(ra = 528, inhG=0.9e-5, stimFreq=5500, darkFreq=87, inds=inds))

    

