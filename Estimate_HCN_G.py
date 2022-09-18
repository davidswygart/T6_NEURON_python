import numpy as np
from T6_Sim import Type6_Model
from Experiment import Experiment

#%% Make model and place voltage clamp
T6 = Type6_Model()
ex = Experiment(T6)

ex.tstop=1500
ex.temp=22
ex.v_init=-70

ex.placeVoltageClamp(-70, 100, -135)

#%% set HCN current to -0.051 nA when stepping from -70 mV to -135 mV
T6.settings.hcn2_gpeak = .78
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.hcn2_gpeak = 0
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
ex.makePlot(ex.time, dif, title = 'HCN current', xlabel = 'time (ms)', ylabel = 'current (nA)',xmin = 10)

print('HCN current = ', np.min(dif))
