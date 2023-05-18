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

def runInhSet(n,inhG):
    T6.settings.inhSyn.gMax = inhG
    inds = T6.nNearestInh(n)
    #inhV = ex.loopThroughInhibitorySynapses(inds[[11]]) 
    #inhV = ex.loopThroughInhibitorySynapses(inds[[45]])    
    inhV = ex.loopThroughInhibitorySynapses(inds) 
     
    CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(stimTimeV, preTimeV, inhV)
    print(np.median(Q1Avg))

    ns.append(n)
    CSRs.append(CSR)
    diffs.append(diffQ4toQ1)
    return CSR
    

#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()

##%% set active conductances
T6.settings.Cav_L_gpeak = 0
T6.settings.Kv1_2_gpeak = 0
T6.settings.hcn2_gpeak = 0

ex = Experiment(T6)
ex.tstop = 2500

#%%################ Set Exc ################################## (-45 mV -> -30 mV)
ex.tstop = 2500
T6.settings.inhSyn.gMax = 0
T6.settings.excSyn.gMax = 0.855e-6
T6.settings.excDark.gMax = T6.settings.excSyn.gMax
T6.settings.excDark.frequency = 181
T6.settings.excSyn.frequency = 398
T6.update()
ex.run()

rib1 = 27
rib2 = 83

smallSpotVRib1 = np.array(ex.rec.ribV[rib1])
smallSpotVRib2 = np.array(ex.rec.ribV[rib2])
ex.makePlot(ex.time,smallSpotVRib1)
preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
stimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average

#%% ####### Figure 6b, example traces when activating 2 inh. synapses ######
# large spot (but only 2 inhibitory synapses activated)
ex.tstop = 2500
T6.settings.inhSyn.gMax = 2.22e-6
T6.update()

for con in T6.inhSyns.con: #turn off all inhibitory synapses
    con.weight[0] = 0

inds = [11,12] # example pair of inh synapses
for i in inds: #turn on select ihibitory synapses
    T6.inhSyns.con[i].weight[0] = T6.settings.inhSyn.gMax * 120 / 2 # inhibition normalized by number activated

ex.run()
bigSpotVRib1 = np.array(ex.rec.ribV[rib1])
bigSpotVRib2 = np.array(ex.rec.ribV[rib2])

# plot large and small simultaneously for both examples
f, (ax1, ax2)  = plt.subplots(nrows = 2)

t = ex.time/1000 - 1 #convert to seconds with 0 == stim start
ax1.plot(t, smallSpotVRib1, label='no inh.')
ax1.plot(t, bigSpotVRib1, label='with inh.')
ax2.plot(t, smallSpotVRib2, label='no inh.')
ax2.plot(t, bigSpotVRib2, label='with inh.')
plt.legend()
plt.show()

#%% ########### Figure 1C, turn on each inhbitory synapse individually ############## 
ex.tstop = 2001 # No need to run experiment past stimulus time since I'm not using those datapoints
ns = []
CSRs = []
diffs = []
#%%
CSR = runInhSet(1, 2.22e-6)
#%%
CSR = runInhSet(2, 2.22e-6)
#%%
CSR = runInhSet(15, 2.25e-6)
#%%
CSR = runInhSet(30, 2.25e-6)
#%%
CSR = runInhSet(60, 2.25e-6)
#%%
CSR = runInhSet(90, 2.25e-6)
#%%
CSR = runInhSet(120, 2.22e-6)
#%%
stackedDiffs = np.stack(diffs, axis=1)
med = np.median(stackedDiffs, axis=0)
maxDif = np.max(stackedDiffs, axis=0)
minDif = np.min(stackedDiffs, axis=0)

#%%
exampleInhInd = 0
plt.hist(CSR[exampleInhInd,])
hist, edges = np.histogram(CSR[exampleInhInd,], bins=42, range=(.85, 2.35))