#%% For calculating CSR
def calcCSR(stimTimeV, preTimeV, inhV):
    excDelta = stimTimeV - preTimeV
    inhDelta = stimTimeV - inhV
    CSR = excDelta / inhDelta

    # sort CSR and split into quartiles
    CSR = np.expand_dims(CSR, 0)
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
ex = Experiment(T6)
ex.tstop = 2500
#ex.tstop = 2001

#%% Run the normal model with only excitation  (-45 mV -> -30 mV)
T6.settings.inhSyn.gMax = 0
T6.update()
ex.run()

excRib1 = np.array(ex.rec.ribV[0])
excRib2 = np.array(ex.rec.ribV[24])
preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
excStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
plt.plot(ex.time, ex.rec.ribV[0])

#%% Run the normal model with excitation and inhibition
T6.settings.inhSyn.gMax = 1.62e-5
T6.update()
ex.run()

inhRib1 = np.array(ex.rec.ribV[0])
inhRib2 = np.array(ex.rec.ribV[24])
inhStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
plt.plot(ex.time, ex.rec.ribV[0])
plt.show()

CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(excStimTimeV, preTimeV, inhStimTimeV)
print('Q1 = ', Q1Avg)
hist, edges = np.histogram(CSR[0], bins=100, range=(1, 2))
midpoints = edges - (edges[0]-edges[1])/2
midpoints = midpoints[0:-1]
plt.hist(CSR[0])
plt.title("CSR with exc/inh")
plt.show()

#%% calculate membrane area for each segment (um2)
segArea = []
for sec in T6.h.allsec():
    for seg in sec:
        segArea.append(seg.area())
segArea = np.expand_dims(np.array(segArea),1)
plt.hist(segArea)

#%% calculate conductance in each section and cumulative
gCaSiemenPerCm2 = np.array(ex.rec.gCa)
gKvSiemenPerCm2 = np.array(ex.rec.gKv1_2)
gHCN2SiemenPerCm2 = np.array(ex.rec.gHCN2)
gLeakSiemenPerCm2 = np.full(np.shape(gCaSiemenPerCm2), T6.settings.g_pas) 

# convert conductance from S/cm2 to S
Um2Tocm2 = 1e-8
gCaSiemens = gCaSiemenPerCm2 * segArea * Um2Tocm2
gKvSiemens = gKvSiemenPerCm2 * segArea * Um2Tocm2
gHCN2Siemens = gHCN2SiemenPerCm2 * segArea * Um2Tocm2
gLeakSiemen = gLeakSiemenPerCm2 * segArea * Um2Tocm2

# add up synapse conductance
gInh = np.array(ex.rec.gInh) * 1e-6
gExc = np.array(ex.rec.gExc) * 1e-6

# add up cumulative conductance over whole membrane
gCaTotal = np.sum(gCaSiemens, axis=0)
gKvTotal = np.sum(gKvSiemens, axis=0)
gHCN2Total = np.sum(gHCN2Siemens, axis=0)
gLeakTotal = np.sum(gLeakSiemen, axis=0)
gInhTotal = np.sum(gInh, axis=0)
gExcTotal = np.sum(gExc, axis = 0)

# plot all the conductances
plt.plot(ex.time, gCaTotal, label='Ca')
plt.plot(ex.time, gKvTotal, label='Kv')
plt.plot(ex.time, gHCN2Total, label='HCN2')
plt.plot(ex.time, gLeakTotal, label = 'Leak')
#plt.plot(ex.time, gInhTotal, label='Inh.')
#plt.plot(ex.time, gExcTotal, label='Exc.')
plt.title('total conductances')
plt.ylabel("S")
plt.xlabel('ms')
plt.legend()
plt.show()

cellConductance = gCaTotal + gKvTotal + gHCN2Total + gLeakTotal                        

plt.plot(ex.time, 1/cellConductance/1e9, label='active')
plt.plot(ex.time, 1/gLeakTotal/1e9, label='passive')
plt.title('effective membrane resistance')
plt.ylabel("GOhm")
plt.xlabel('ms')
plt.ylim(0,2)
plt.legend()
plt.show()

#%%%%%%%%%%%%%%%%%% increase leak conductance equally accross whole cell in place of active conductances %%%%%%%%%%%%%%%%%%%%%%%%
# no active conductances
T6.settings.hcn2_gpeak = 0
T6.settings.Kv1_2_gpeak = 0
T6.settings.Cav_L_gpeak = 0


totalMembraneAreaUm2 = np.sum(segArea)
newPassiveConductance = cellConductance[int(1500 / T6.h.dt)] / totalMembraneAreaUm2 * 1e8 # chose a timepoint in the middle of the light step, and convert to cm2
T6.settings.g_pas = newPassiveConductance

#%% Run the normal model with only excitation  (-45 mV -> -30 mV)
T6.settings.inhSyn.gMax = 0
T6.settings.excSyn.frequency = 210
T6.settings.excDark.frequency = 93
T6.update()
ex.run()

excRib1 = np.array(ex.rec.ribV[0])
excRib2 = np.array(ex.rec.ribV[24])
preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
excStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
plt.plot(ex.time, ex.rec.ribV[0])

#%% Run the normal model with excitation and inhibition
T6.settings.inhSyn.gMax = 9e-6
T6.update()
ex.run()

inhRib1 = np.array(ex.rec.ribV[0])
inhRib2 = np.array(ex.rec.ribV[24])
inhStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
plt.plot(ex.time, ex.rec.ribV[0])
plt.show()

 
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(excStimTimeV, preTimeV, inhStimTimeV)
print('Q1 = ', Q1Avg)
hist, edges = np.histogram(CSR[0], bins=100, range=(1, 2))
midpoints = edges - (edges[0]-edges[1])/2
midpoints = midpoints[0:-1]
plt.hist(CSR[0])
plt.title("CSR with exc/inh")
plt.show()

#%%%%%%%%%%%%%%%%%% increase leak conductance specific to each segment %%%%%%%%%%%%%%%%%%%%%%%%
# no active conductances
T6.settings.hcn2_gpeak = 0
T6.settings.Kv1_2_gpeak = 0
T6.settings.Cav_L_gpeak = 0

totalMembraneAreaUm2 = np.sum(segArea)
newPassiveConductance = cellConductance[int(1500 / T6.h.dt)] / totalMembraneAreaUm2 * 1e8 # chose a timepoint in the middle of the light step, and convert to cm2
T6.settings.g_pas = newPassiveConductance

totalSegmentConductance = gCaSiemens + gKvSiemens + gHCN2Siemens + gLeakSiemen
totalSegmentConductance = totalSegmentConductance[:, int(1500 / T6.h.dt)] # chose a timepoint in the middle of the light step
totalSegmentConductance = totalSegmentConductance / np.squeeze(segArea) * 1e8 # convert to S/cm2


#%% Run the normal model with only excitation  (-45 mV -> -30 mV)
T6.settings.inhSyn.gMax = 0
T6.settings.excSyn.frequency = 210
T6.settings.excDark.frequency = 93
T6.update()

i=0
for sec in T6.h.allsec():
    for seg in sec:
        seg.pas.g = totalSegmentConductance[i]
        i = i+1

ex.run()

excRib1 = np.array(ex.rec.ribV[0])
excRib2 = np.array(ex.rec.ribV[24])
preTimeV = ex.averageRibVoltage(startTimeMs=500, endTimeMs =999) #preTime average
excStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
plt.plot(ex.time, ex.rec.ribV[0])

#%% Run the normal model with excitation and inhibition
T6.settings.inhSyn.gMax = 9e-6
T6.update()

i=0
for sec in T6.h.allsec():
    for seg in sec:
        seg.pas.g = totalSegmentConductance[i]
        i = i+1

ex.run()

inhRib1 = np.array(ex.rec.ribV[0])
inhRib2 = np.array(ex.rec.ribV[24])
inhStimTimeV = ex.averageRibVoltage(startTimeMs=1000, endTimeMs=2000) #postTime average
plt.plot(ex.time, ex.rec.ribV[0])
plt.show()

 
CSR, Q1Avg, Q4Avg, diffQ4toQ1 = calcCSR(excStimTimeV, preTimeV, inhStimTimeV)
print('Q1 = ', Q1Avg)
hist, edges = np.histogram(CSR[0], bins=100, range=(1, 2))
midpoints = edges - (edges[0]-edges[1])/2
midpoints = midpoints[0:-1]
plt.hist(CSR[0])
plt.title("CSR with exc/inh")
plt.show()
