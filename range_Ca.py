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
def runNewCaG(caG = 1.62, inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=[]):
    #Run the model excitation only  (-45 mV -> -30 mV)
    T6.settings.Cav_L_gpeak = caG 
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
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop = 2001

#%% start with simulating all inhibitory synapses
n=120
inds = T6.nNearestInh(n)

diffs120 = [];
diffs120.append(runNewCaG(caG = 0, inhG=1.8e-5, stimFreq=650, darkFreq=100, inds=inds[[0]]))
diffs120.append(runNewCaG(caG = 0.8, inhG=1.7e-5, stimFreq=575, darkFreq=85, inds=inds[[0]]))
diffs120.append(runNewCaG(caG = 1.62, inhG=1.62e-5, stimFreq=500, darkFreq=70, inds=inds[[0]]))
diffs120.append(runNewCaG(caG = 2.3, inhG=1.52e-5, stimFreq=460, darkFreq=58, inds=inds[[0]]))
diffs120.append(runNewCaG(caG = 3, inhG=1.62e-5, stimFreq=400, darkFreq=46, inds=inds[[0]]))

#%%
n=1
inds = T6.nNearestInh(n)

diffs1 = [];
diffs1.append(runNewCaG(caG = 0, inhG=3.3e-5, stimFreq=650, darkFreq=100, inds=inds))
diffs1.append(runNewCaG(caG = 0.8, inhG=3.12e-5, stimFreq=575, darkFreq=85, inds=inds))
diffs1.append(runNewCaG(caG = 1.62, inhG=2.95e-5, stimFreq=500, darkFreq=70, inds=inds))
diffs1.append(runNewCaG(caG = 2.3, inhG=2.71e-5, stimFreq=460, darkFreq=58, inds=inds))
diffs1.append(runNewCaG(caG = 3, inhG=2.56e-5, stimFreq=400, darkFreq=46, inds=inds))

























