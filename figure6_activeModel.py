# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:23:09 2023

@author: david
"""

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

#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()

##%% set active conductances
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12
T6.settings.hcn2_gpeak = .78

#%% create experiment object
ex = Experiment(T6)
ex.tstop = 2000

#%%################ Set Exc ################################## (-45 mV -> -30 mV)
T6.settings.excDark.frequency = 70
T6.settings.excSyn.frequency = 500


T6.settings.excSyn.gMax = 1.12e-5
T6.settings.excDark.gMax = T6.settings.excSyn.gMax
T6.settings.inhSyn.gMax = 0
T6.update()
ex.run()

smallSpotVRib1 = np.array(ex.rec.ribV[0])
smallSpotVRib2 = np.array(ex.rec.ribV[24])
ex.makePlot(ex.time,smallSpotVRib1 ,  xmin = 100)
preTimeV = ex.averageRibVoltage(startTimeMs=300, endTimeMs =500) #preTime average
stimTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs=1500) #postTime average
excDelta = stimTimeV - preTimeV

plt.hist(stimTimeV - preTimeV)
plt.title('depolarization')

#%%########### l (all inhibitory activated) (-39.1 mV == CSR 1.1)
T6.settings.inhSyn.frequency = 79

T6.settings.inhSyn.gMax = 1e-5

T6.update()
ex.run()
bigSpotVRib1 = np.array(ex.rec.ribV[0])
bigSpotVRib2 = np.array(ex.rec.ribV[24])

ex.makePlot(ex.time, bigSpotVRib1,  xmin = 100)
ribV = ex.averageRibVoltage(startTimeMs=500, endTimeMs=1500) #postTime average

plt.hist(ribV - stimTimeV)
plt.title('hyperpolarization')
plt.show()

#%% compare depolarization to hyperpolarization
plt.scatter(stimTimeV - preTimeV,ribV - stimTimeV)
plt.xlabel('depolarization')
plt.ylabel('hyperpolarization')
plt.show()
#%% ####### Figure 6b, example traces when activating 2 inh. synapses ######
#%% large spot (but only 2 inhibitory synapses activated)
#(far left example inh = inh #9 & 11 on section axon[83])
T6.settings.inhSyn.frequency = 79

T6.settings.inhSyn.gMax = 2.7e-5
T6.update()

for con in T6.inhSyns.con: #turn off all ihibitory synapses
    con.weight[0] = 0

inds = [9,11] # example pair of inh synapses
for i in inds: #turn on select ihibitory synapses
    T6.inhSyns.con[i].weight[0] = T6.settings.inhSyn.gMax * 120 / 2 # inhibition normalized by number activated

ex.run()
bigSpotVRib1 = np.array(ex.rec.ribV[0])
bigSpotVRib2 = np.array(ex.rec.ribV[24])

#%% plot large and small simultaneously for both examples
f, (ax1, ax2)  = plt.subplots(nrows = 2)

t = ex.time/1000 - .5 #convert to seconds with 0 == stim start
ax1.plot(t, smallSpotVRib1, label='no inh.')
ax1.plot(t, bigSpotVRib1, label='with inh.')
ax1.plot([0,0],[-60,-20])
ax1.plot([1,1],[-60,-20])

ax2.plot(t, smallSpotVRib2, label='no inh.')
ax2.plot(t, bigSpotVRib2, label='with inh.')
ax2.plot([0,0],[-60,-20])
ax2.plot([1,1],[-60,-20])

plt.legend()
plt.show()

#%% ########### Figure 1C, turn on each inhbitory synapse individually ############## 
ex.tstop = 1501 # No need to run experiment past stimulus time since I'm not using those datapoints
ns = []
CSRs = []
diffs = []
#%%
T6.settings.inhSyn.gMax = 2.95e-5

n=1
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])    
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

#ns.append(n)
#CSRs.append(CSR)
#diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 2.7e-5

n=2
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]]) 
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 2.6e-5

n=3
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])   
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 2.5e-5

n=6
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])   
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 1.8e-5

n=15
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])     
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 1.65e-5

n=21
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])    
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 1.62e-5

n=30
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])    
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 1.62e-5

n=60
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])    
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 1.73e-5

n=90
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])     
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)
#%%
T6.settings.inhSyn.gMax = 1.7e-5

n=120
inds = T6.nNearestInh(n)
#inhV = ex.loopThroughInhibitorySynapses(inds[[14,18,56,119]])   
inhV = ex.loopThroughInhibitorySynapses(inds) 
    
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
print(np.median(Q4Avg))

ns.append(n)
CSRs.append(CSR)
diffs.append(diffQ4toQ1)


#np.argmin(abs(Q4Avg-np.median(Q4Avg))) == 86



#%% Figure 6f
stackedDiffs = np.stack(diffs, axis=1)
med = np.median(stackedDiffs, axis=0)
maxDif = np.max(stackedDiffs, axis=0)
minDif = np.min(stackedDiffs, axis=0)



#%% Figure 6c
exampleInhInd = np.argmin(np.mean(abs((stackedDiffs - med)), axis=1)) #use inhibition with values closest to median for example histograms

plt.hist(CSRs[0][exampleInhInd])

plt.hist(CSRs[7][exampleInhInd])
plt.hist(CSRs[9][exampleInhInd])
#%%
hist, edges = np.histogram(CSRs[0][exampleInhInd], bins=26, range=(.9, 2.2))

#%%
hist, edges = np.histogram(CSRs[7][exampleInhInd], bins=26, range=(.9, 2.2))

#%%
hist, edges = np.histogram(CSRs[9][exampleInhInd], bins=26, range=(.9, 2.2))