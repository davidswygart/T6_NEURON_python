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

#%% Only make the model and experiment
T6 = Type6_Model()
ex = Experiment(T6)

#%%################ Exc only ################################## (-45 mV -> -30 mV)
ex.tstop = 2500
T6.settings.inhSyn.gMax = 0
T6.settings.excDark.frequency = 70
T6.settings.excSyn.frequency = 515
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
T6.settings.inhSyn.gMax = 2.38e-5
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
CSR = runInhSet(1, 2.45e-5)
#%%
CSR = runInhSet(2, 2.38e-5)
#%%
CSR = runInhSet(3, 2.2e-5)
#%%
CSR = runInhSet(5, 2.2e-5)
#%%
CSR = runInhSet(10, 2e-5)
#%%
CSR = runInhSet(15, 1.9e-5)
#%%
CSR = runInhSet(18, 1.89e-5)
#%%
CSR = runInhSet(21, 1.8e-5)
#%%
CSR = runInhSet(30,  1.73e-5)
#%%
CSR = runInhSet(40,  1.73e-5)
#%%
CSR = runInhSet(50,  1.73e-5)
#%%
CSR = runInhSet(60,  1.73e-5)
#%%
CSR = runInhSet(70,  1.73e-5)
#%%
CSR = runInhSet(80,  1.78e-5)
#%%
CSR = runInhSet(90, 1.85e-5)
#%%
CSR = runInhSet(100,  1.85e-5)
#%%
CSR = runInhSet(110,  1.72e-5)
#%%
CSR = runInhSet(120,  1.64e-5)


#%% Distance from inhibition
n = 120
inds = T6.nNearestInh(n)
dists = np.zeros(np.shape(CSR))

ribbon2InhDistance = T6.calcDistances(T6.ribbons.seg, T6.inhSyns.seg)
for indInh in range(len(CSR[:,0])):
    for indRib in range(len(CSR[0,:])):
        dists[indInh,indRib] = np.mean(ribbon2InhDistance[indRib, inds[indInh,:]])
        

x = np.reshape(dists, (-1,1))
y = np.reshape(CSR, (-1,1))

plt.scatter(x,y)

#%% Distance from soma
n = 120
inds = T6.nNearestInh(n)
dists = np.zeros(np.shape(CSR))

soma2RibbonDistance = np.repeat(T6.calcDistances(T6.ribbons.seg,[T6.soma.seg]), 120, axis=1)
for indInh in range(len(CSR[:,0])):
    for indRib in range(len(CSR[0,:])):
        dists[indInh,indRib] = np.mean(soma2RibbonDistance[indRib, inds[indInh,:]])
        

x = np.reshape(dists, (-1,1))
y = np.reshape(CSR, (-1,1))

plt.scatter(x,y)
#%%
exampleInhInd = 11
plt.hist(CSR[exampleInhInd,])
hist, edges = np.histogram(CSR[exampleInhInd,], bins=42, range=(.85, 2.35))

