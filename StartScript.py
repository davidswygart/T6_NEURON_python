import os
os.chdir('C:/Users/david/Documents/Code/Github/T6_NEURON_python')

from neuron import h
import numpy as np
from T6_Sim import Type6_Model
from Experiment import Experiment
from UtilityFuncs import makePlot
from UtilityFuncs import pullAvg
from UtilityFuncs import averageRibbonVoltage
from UtilityFuncs import pullMin
from UtilityFuncs import pullMax
from UtilityFuncs import calcDistances
import matplotlib.pyplot as plt

#%% record distances between recording locations
T6 = Type6_Model()
np.savetxt('results\\distances\\inh2ribDist.txt', calcDistances(T6.inhSyns.seg,T6.ribbons.seg))
np.savetxt('results\\distances\\soma2ribDist.txt', calcDistances([T6.soma.seg],T6.ribbons.seg))
np.savetxt('results\\distances\\soma2inhDist.txt', calcDistances([T6.soma.seg],T6.inhSyns.seg))

rib_secNum = np.array(T6.ribbons.secNum)
np.savetxt('results\\distances\\rib_secNum.txt',rib_secNum)
inh_secNum = np.array(T6.inhSyns.secNum)
np.savetxt('results\\distances\\inh_secNum.txt',inh_secNum)
#%% Passive model: tstop 200 ms
T6 = Type6_Model()
ex = Experiment(T6, 300, 32, -35)

#%% set excitation so that average ribbon is -35 mV
T6.settings.excSyn['gmax'] = 4.18e-5
T6.update()
ex.run()
makePlot(ex.time, ex.rec.v[T6.soma.secNum])
ex.avgRibV()

#%% set inhibition so that an individual inhibitory synapse (Vmax) is -45 mV
inhG = 1.5e-3

v_sample = []
for i in range(20): #Check 20 of the 120 inhibitory synapses.  There is some variation, but on average, they should reach ~-45 mV.
    v = ex.runSingleInh(inhG, i*6)
    print('inhV = ', v[-1])
    v_sample.append(v[-1])
    
print('average inhV = ', np.average(v_sample))

#%%
#Run inhibition for each inh synapse and save data
ex.LoopThoughInhibitorySynapses('results\\passive\\', 1.5e-3)




#%% HCN
T6 = Type6_Model()
ex = Experiment(T6, 1000, 22, -70)
ex.placeVoltageClamp(-70, 200, -135)


#%% set HCN current to -0.051 nA when stepping from -70 mV to -120 mV
T6.settings.hcn2_gpeak = 0.0001
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.hcn2_gpeak = 0
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
makePlot(ex.time, dif, title = 'HCN current', xlabel = 'time (ms)', ylabel = 'current (nA)',xmin = 150)

print('HCN current = ', dif[-1])




#%% Kv
T6 = Type6_Model()
ex = Experiment(T6, 2000, 22, -60)
ex.placeVoltageClamp(-60, 200, 30)
#%% Kv
for sec in h.allsec():
    for seg in sec:
        seg.Kv1_2.mTauVHalf = 67.56
        seg.Kv1_2.mTauVWidth = 34.1479
        seg.Kv1_2.mTauBase = 150
        seg.Kv1_2.hTauVHalf = 46.5600
        seg.Kv1_2.hTauVWidth = -44.1479
        seg.Kv1_2.hTauBase = 15000 
        

#%% set Kv current to 1.31 nA when stepping from -60 mV to 30 mV
T6.settings.Kv1_2_gpeak = 11.2#5.6
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.Kv1_2_gpeak = 0 
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
makePlot(ex.time, dif, title = 'Kv current',xlabel = 'time (ms)', ylabel = 'current (nA)', xmin = 150, ymin=-0.1)

print('Kv current = ', np.max(dif))

#%% Ca
T6 = Type6_Model()
ex = Experiment(T6, 700, 22, -80)
ex.placeVoltageClamp(-80, 300, -35)

#%% ca adjust
for sec in h.allsec():
    for seg in sec:
        seg.Ca.mTauMult = 1
        seg.Ca.hTauMult = 1
        seg.Kv1_2.mTauMult = 1
        seg.Kv1_2.hTauMult = 1
 

#%% set Ca current to 30 pA when stepping from -80 to -35 mV
T6.settings.Cav_L_gpeak = 2.1
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.Cav_L_gpeak = 0
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
makePlot(ex.time, dif, title = 'Ca current',xlabel = 'time (ms)', ylabel = 'current (nA)', xmin = 150)

print('Ca current = ', np.min(dif))



#%% create calcium IV

voltageRange = np.linspace(-90, 40, 10)
maxCurrent = []
for v2 in voltageRange:
    ex.vClamp.amp2 = v2
    T6.settings.Cav_L_gpeak = 2
    T6.update()
    ex.run()
    current = np.array(ex.vClampRec)

    T6.settings.Cav_L_gpeak = 0
    T6.update()
    ex.run()
    baseline = np.array(ex.vClampRec)

    dif = current - baseline
    makePlot(ex.time, dif, title = 'Ca current ' + str(round(v2)) , xmin = 150)

    indMax = np.argmax(np.abs(dif))
    Imax = dif[indMax]
    print('Ca current = ', Imax)
    maxCurrent.append(Imax)
    
makePlot(voltageRange, maxCurrent)
np.savetxt('results\\CaIV\\Voltages.txt', voltageRange)
np.savetxt('results\\CaIV\\Currents.txt', np.array(maxCurrent))

#%% Run active model voltage drop
T6 = Type6_Model()
ex = Experiment(T6, 750, 32, -35)

#%% set excitation so that average ribbon is -35 mV
T6.settings.hcn2_gpeak = 0.0001
T6.settings.Kv1_2_gpeak = 11.2
T6.settings.Cav_L_gpeak = 2

T6.settings.inhSyn['start'] = 200
T6.settings.inhSyn['gmax'] = 0

T6.settings.excSyn['gmax'] = 2.4e-4

T6.update()
ex.run()
makePlot(ex.time, ex.rec.v[T6.soma.secNum])
ex.avgRibV()


#%% set inhibition so that an individual inhibitory synapse (Vmax) is -45 mV

inhG = 9.4e-3

v_sample = []
for i in range(20): #Check 20 of the 120 inhibitory synapses.  There is some variation, but on average, they should reach ~-45 mV.
    v = ex.runSingleInh(inhG, i*6)
    print('inhV = ', v[-1])
    v_sample.append(v[-1])
    
print('average inhV = ', np.average(v_sample))

#%%
#Run inhibition for each inh synapse and save data
ex.LoopThoughInhibitorySynapses('results\\active\\', 6.2e-3)

#%% get trace for figure
T6 = Type6_Model()
ex = Experiment(T6, 1000, 32, -40)

#%% -43 to -35 to  -45
T6.settings.hcn2_gpeak = 0.0001
T6.settings.Kv1_2_gpeak = 11.2
T6.settings.Cav_L_gpeak = 2

T6.settings.excSyn['gmax'] =  2.4e-4
T6.settings.excSyn['start'] = 500

T6.settings.inhSyn['start'] = 700
inhG = 9.4e-3
T6.update()

#for i in range(2): #turn on a few excitatory synapses to push resting membrane potential to ~-43 mV (dark current)
#    T6.excSyns.syn[i].onset = 0

v = ex.runSingleInh(inhG, 9)

inhTrace = np.array(ex.rec.v[T6.inhSyns.secNum[9]])
excTrace = np.array(ex.rec.v[T6.ribbons.secNum[24]])
time = (ex.time) / 1000
makePlot(time, inhTrace, title = 'example inhibition dV', ylabel = 'mV', xlabel = 'time(s)', ymin = -60, ymax = -25, xmin=.4)# inhibition at axon 67 or 43 (or even 42) --> T6.inhSyns.sec[92]
makePlot(time, excTrace, title = 'example excitatory dV', ylabel = 'mV', xlabel = 'time(s)', ymin = -60, ymax = -25, xmin=.4)# inhibition at axon 67 or 43 (or even 42) --> T6.inhSyns.sec[92]

#inh 17 = axon 98
# ribbon at axon 36 such as --> T6.ribbons.sec[23]
ex.avgRibV()

#%% segment lengths
allL = list()
for sec in h.axon:
    allL.append(sec.L/sec.nseg)
    
print(max(allL))
print(np.average(allL))

