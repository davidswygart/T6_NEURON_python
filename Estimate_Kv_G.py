import numpy as np
from T6_Sim import Type6_Model
from Experiment import Experiment

#%% Kv
T6 = Type6_Model()
ex = Experiment(T6)

ex.tstop=2000
ex.temp=22
ex.v_init=-60
ex.placeVoltageClamp(-60, 200, 30)

#%% set Kv current to 1.31 nA when stepping from -60 mV to 30 mV
T6.settings.Kv1_2_gpeak = 11
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.Kv1_2_gpeak = 0 
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
ex.makePlot(ex.time, dif, title = 'Kv current',xlabel = 'time (ms)', ylabel = 'current (nA)', xmin = 150, ymin=-0.1)

print('Kv current = ', np.max(dif))
