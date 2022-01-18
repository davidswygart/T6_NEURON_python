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

ribs = T6.ribbons.seg
inh = T6.inhSyns.seg
inh2Rib = calcDistances(inh,ribs)
np.savetxt('results\\distances\\inh2ribDist.txt', inh2Rib)

rib_secNum = np.array(T6.ribbons.secNum)
np.savetxt('results\\distances\\rib_secNum.txt',rib_secNum)
inh_secNum = np.array(T6.inhSyns.secNum)
np.savetxt('results\\distances\\inh_secNum.txt',inh_secNum)

#%% Passive model: tstop 200 ms

T6 = Type6_Model()
ex = Experiment(T6, 200, 32, -40)

#%% set excitation so that average ribbon is -40 mV
T6.settings.excSyn['gmax'] = 32 / 1000000
T6.update()
ex.run()
makePlot(ex.time, ex.rec.v[T6.soma.secNum])
ex.avgRibV()

#%% set inhibition so that an individual inhibitory synapse (Vmax) is -45 mV
ex.v_init = -50
ex.tstop = 150
v = ex.runSingleInh(0.787/1000, 0)
print('inhV = ', v)

#%%
#Run inhibition for each inh synapse and save data
ex.LoopThoughInhibitorySynapses('results\\passive\\', 0.787/1000)



#%% HCN
T6 = Type6_Model()
ex = Experiment(T6, 400, 22, -70)
ex.placeVoltageClamp(-70, 200, -135)


#%% set HCN current to -0.051 nA when stepping from -70 mV to -135 mV
T6.settings.hcn2_gpeak = 0.38
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.hcn2_gpeak = 0
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
makePlot(ex.time, dif, title = 'HCN current', xmin = 150)

print('HCN current = ', dif[-1])


#%% Kv
T6 = Type6_Model()
ex = Experiment(T6, 400, 22, -60)
ex.placeVoltageClamp(-60, 200, 30)


#%% set Kv current to 1.31 nA when stepping from -60 mV to 30 mV
T6.settings.Kv1_2_gpeak = 5.6 
T6.settings.Kv1_3_gpeak = 5.6
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.Kv1_2_gpeak = 0 
T6.settings.Kv1_3_gpeak = 0
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
makePlot(ex.time, dif, title = 'HCN current', xmin = 150)

print('Kv current = ', np.max(dif))

#%% Ca
T6 = Type6_Model()
ex = Experiment(T6, 400, 22, -80)
ex.placeVoltageClamp(-80, 200, -35)

#%% set Ca current to 30 pA when stepping from -80 to -35 mV
T6.settings.Cav_L_gpeak = 1.6
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.Cav_L_gpeak = 0
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
makePlot(ex.time, dif, title = 'Ca current', xmin = 150)

print('Ca current = ', np.min(dif))

#%% create calcium IV

voltageRange = np.linspace(-90, 40, 20)
maxCurrent = []
for v2 in voltageRange:
    ex.vClamp.amp2 = v2
    T6.settings.Cav_L_gpeak = 1.6
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
ex = Experiment(T6, 400, 32, -40)

#%%
T6.settings.hcn2_gpeak = 0.38
T6.settings.Kv1_2_gpeak = 5.6 
T6.settings.Kv1_3_gpeak = 5.6
T6.settings.Cav_L_gpeak = 1.6

#set excitation so that average ribbon is -35 mV
T6.settings.excSyn['gmax'] = 130 / 1000000
T6.update()
ex.run()
makePlot(ex.time, ex.rec.v[T6.soma.secNum])
ex.avgRibV()


#%% set inhibition so that an individual inhibitory synapse (Vmax) is -45 mV
ex.v_init = -50
ex.tstop = 300
v = ex.runSingleInh(2.8/1000, 0)
print('inhV = ', v)

#%%
#Run inhibition for each inh synapse and save data
ex.LoopThoughInhibitorySynapses('results\\active\\stim', 2.8/1000)
ex.LoopThoughInhibitorySynapses('results\\active\\base',0)


