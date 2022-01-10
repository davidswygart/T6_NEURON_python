#cd C:\Users\david\Documents\Code\Github\T6_NEURON_python
from neuron import h
#h.load_file('stdrun.hoc')
#h.load_file('stdrun.hoc')

import numpy as np
from T6_Sim import Type6_Model
from UtilityFuncs import makePlot
from UtilityFuncs import pullAvg
from UtilityFuncs import LoopThoughInhibitorySynapses
from UtilityFuncs import averageRibbonVoltage
from UtilityFuncs import runSingleInh
from UtilityFuncs import pullMin
from UtilityFuncs import pullMax

T6 = Type6_Model()

#%% record distances between recording locations
T6.calcDistances(T6.recordings['inhLocations'],T6.recordings['ribLocations'], 'results\\distances\\inh2ribDist.txt')
T6.calcDistances(T6.recordings['ribLocations'],T6.recordings['ribLocations'], 'results\\distances\\rib2ribDist.txt')
T6.calcDistances(T6.recordings['inhLocations'],T6.recordings['segLocations'], 'results\\distances\\inh2segDist.txt')


#%% Passive model: tstop 200 ms
#set excitation so that average ribbon is -35 mV
T6.updateAndRun()
averageRibbonVoltage(T6) 

#set inhibition so that an individual inhibitory synapse (Vmax) is -50 mV
runSingleInh(T6, T6.inhSyns[0], 1320/1000000)
pullAvg(T6.recordings['time'], T6.recordings['inhV'][0], 150,200)

#Run inhibition for each inh synapse and save data
LoopThoughInhibitorySynapses(T6,'results\\passive\\stim',1320/1000000)
LoopThoughInhibitorySynapses(T6,'results\\passive\\base',0)

#%% active model: change to voltage clamp and lower temp to match isolated cell papers
T6.settings.temp = 22
T6.settings.DoVClamp = 1
T6.settings.ChangeClamp = 200
T6.settings.tstop = 500
T6.settings.excSyn['gmax'] = 0

#%% set HCN current to -0.051 nA when stepping from -70 mV to -135 mV
T6.settings.hcn2_gpeak = 50 / 1000000
T6.updateAndRun()
makePlot(T6.recordings['time'], T6.recordings['iClamp'], title = 'Current Graph', ymin = -.15, xmin = 150)
makePlot(T6.recordings['time'], T6.recordings['iClamp'], title = 'Current Graph', ymin = -.15, xmin = 200, xmax = 210)
hcnCurrent = pullAvg(T6.recordings['time'],T6.recordings['iClamp'],204,205) - pullAvg(T6.recordings['time'],T6.recordings['iClamp'],460,500)
T6.settings.hcn2_gpeak = 0
#%% set Kv current to 1.31 nA when stepping from -60 mV to 30 mV
T6.settings.Hold1 = -60
T6.settings.Hold2 = 30
T6.settings.Kv1_2_gpeak = 550 / 1000000 
T6.settings.Kv1_3_gpeak = 550 / 1000000
T6.updateAndRun()

makePlot(T6.recordings['time'], T6.recordings['vClamp'], title = 'Current Graph', ymax = 1.5, xmin = 180)
KvCurrent = pullAvg(T6.recordings['time'],T6.recordings['vClamp'],240,260)

T6.settings.Kv1_2_gpeak = 0 
T6.settings.Kv1_3_gpeak = 0

#%% set Ca current to 30 pA when stepping from -80 to -35 mV
T6.settings.Hold1 = -80
T6.settings.Hold2 = -35
T6.settings.Cav_L_gpeak = 75000 / 100000
T6.updateAndRun()

makePlot(T6.recordings['time'], T6.recordings['vClamp'], title = 'Current Graph', xmin = 190, ymax = .01)
CaCurrent = pullMin(T6.recordings['time'],T6.recordings['vClamp'],202)
#%% create calcium IV

[Vs, Is] = T6.runIV(minV = -90, maxV = 50, steps = 30) #pulls minimum from anytime after 201 ms
np.savetxt('results\\CaIV\\Voltages.txt', Vs)
np.savetxt('results\\CaIV\\Currents.txt', Is)
#%% Run active model voltage drop
T6 = Type6_Model() #remoake the model in order to remove the voltage clamp
T6.settings.temp = 32
T6.settings.hcn2_gpeak = 50 / 1000000
T6.settings.Kv1_2_gpeak = 550 / 1000000 
T6.settings.Kv1_3_gpeak = 550 / 1000000
T6.settings.Cav_L_gpeak = 75000 / 100000

#set excitation so that average ribbon is -35 mV
T6.settings.excSyn['gmax'] = 275 / 1000000
T6.updateAndRun()
averageRibbonVoltage(T6) 
#%% set inhibition so that an individual inhibitory synapse (Vmax) is -50 mV
runSingleInh(T6, T6.inhSyns[0], 6000/1000000)
pullAvg(T6.recordings['time'], T6.recordings['inhV'][0], 150,200)


#%% record voltage drop in active model
#Run inhibition for each inh synapse and save data
LoopThoughInhibitorySynapses(T6,'results\\active\\stim',6000/1000000)
LoopThoughInhibitorySynapses(T6,'results\\active\\base',0)

#%% increase internal resistance in at ribbon output locations
#set excitation so that average ribbon is -35 mV
T6.settings.excSyn['gmax'] = 4000 / 1000000    
T6.updateAndRun()

newRa = T6.settings.Ra * 25

for [sec, d] in T6.recordings['ribLocations']:
    sec.Ra = newRa
T6.run()    
makePlot(T6.recordings['time'], T6.recordings['segV'][241])
averageRibbonVoltage(T6)


#%%set inhibition so that an individual inhibitory synapse (Vmax) is -50 mV
runSingleInh(T6, T6.inhSyns[0], 2000/1000000)
pullAvg(T6.recordings['time'], T6.recordings['inhV'][0], 150,200)

#%% record voltage drop in high Ra (active) model
#Run inhibition for each inh synapse and save data
LoopThoughInhibitorySynapses(T6,'results\\highRa\\stim',2000/1000000)
LoopThoughInhibitorySynapses(T6,'results\\highRa\\base',0)

#%% measure membrane area (of axon terminal right now)
np.sum(T6.area()) # 633 um^2


#%% estimate membrane resistance with current pulse
T6.settings.hcn2_gpeak = 50 / 1000000
T6.settings.Kv1_2_gpeak = 550 / 1000000 
T6.settings.Kv1_3_gpeak = 550 / 1000000
T6.settings.Cav_L_gpeak = 75000 / 100000


T6.placeCurrentClamp(T6.h.dend_0[2], .8)
T6.IClamp.amp = 2/1000
T6.IClamp.delay = 200
T6.IClamp.dur = 200
T6.settings.excSyn['gmax'] = 1.2e-4
T6.settings.tstop = 400
T6.settings.v_init = -43
T6.updateAndRun()
preV = pullAvg(T6.recordings['time'], T6.recordings['segV'][241], 190,199)
V = pullMax(T6.recordings['time'], T6.recordings['segV'][241], 201)

R = (preV-V)/T6.IClamp.amp #input resistance in MOhms

makePlot(T6.recordings['time'], T6.recordings['ribIca'][0])




#%% measure distance from soma to ribbons

T6.calcDistances([T6.recordings['segLocations'][241]],T6.recordings['ribLocations'], 'soma2ribDist.txt')[0]

#%% Show excitation and inhibition in same trace
T6.settings.hcn2_gpeak = 50 / 1000000
T6.settings.Kv1_2_gpeak = 550 / 1000000 
T6.settings.Kv1_3_gpeak = 550 / 1000000
T6.settings.Cav_L_gpeak = 75000 / 100000
T6.settings.tstop = 800
T6.settings.v_init = -35
T6.settings.excSyn['start'] = 300
T6.settings.inhSyn['start'] = 500
T6.settings.excSyn['gmax'] = 275 / 1000000
T6.updateAndRun()
i = runSingleInh(T6, T6.inhSyns[40], 3000/1000000)

makePlot(T6.recordings['time'], T6.recordings['inhV'][i], ylabel='mV', xlabel='time (ms)',ymax=0, ymin=-70)
makePlot(T6.recordings['time'], T6.recordings['ribV'][90], ylabel='mV', xlabel='time (ms)',ymax=0, ymin=-70)

#T6.recordings['segLocations'][241]
#[dend_0[2], 0.8333333333333333]
#is soma after updating nseg on 12/15/21


#axon 40(0)
#axon 36(1)