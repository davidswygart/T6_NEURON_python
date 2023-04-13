def calcCSR(stimTimeV, preTimeV, inhV):
    excDelta = stimTimeV - preTimeV
    inhDelta = stimTimeV - inhV
    CSR = excDelta / inhDelta
    csrInds = np.argsort(CSR, axis = 1)# sort by low to high suppression
    quartileN = round(len(CSR[0,:])/4)
    q1Inds = csrInds[:, 0 : quartileN]
    q4Inds = csrInds[:, quartileN*3-1 : ]
    return q1Inds, q4Inds

def run(inhG=1.62e-5, inds=[]):

    T6.settings.inhSyn.gMax = 0
    T6.update()
    ex.run()
    preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
    excStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
    
    # run with inhibition only
    T6.settings.inhSyn.gMax = inhG
    inhV = ex.loopThroughInhibitorySynapses(inds)   
    q1Inds, q4Inds = calcCSR(excStimTimeV, preTimeV, inhV)

    return q1Inds, q4Inds

def getDistances(q1Inds,q4Inds):
    
    d = []
    for inhNum in range(np.shape(q1Inds)[0]):
        q1 = q1Inds[inhNum,:]
        q4 = q4Inds[inhNum,:]
        for r1 in q1:
            for r4 in q4:
                d.append(ribbonDistanceMatrix[r1,r4])
    return d

    
#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np

# Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop = 2001

#%%
ribbonDistanceMatrix = T6.calcDistances(T6.ribbons.seg, T6.ribbons.seg) #acessed as global
allRibDistances = np.empty(0)
for i in range(len(ribbonDistanceMatrix)):
    allRibDistances = np.concatenate((allRibDistances, ribbonDistanceMatrix[i,i+1:]), axis=0)


#%%
inds = T6.nNearestInh(1)
q1Inds, q4Inds = run(inhG=2.95e-5, inds=inds)
n1Distances = getDistances(q1Inds,q4Inds)
#%%
inds = T6.nNearestInh(60)
q1Inds, q4Inds = run(inhG=1.62e-5, inds=inds)
n60Distances = getDistances(q1Inds,q4Inds)

#%%
inds = T6.nNearestInh(120)
q1Inds, q4Inds = run(inhG=1.62e-5, inds=inds[[0]])
n120Distances = getDistances(q1Inds,q4Inds)


        



