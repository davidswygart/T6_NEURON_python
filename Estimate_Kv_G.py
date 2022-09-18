import numpy as np
from T6_Sim import Type6_Model
from Experiment import Experiment
import matplotlib.pyplot as plt

#%% Kv
T6 = Type6_Model()
ex = Experiment(T6)

ex.tstop=.4
ex.temp=22
ex.v_init=-60
clampT = 100
ex.placeVoltageClamp(-60, clampT, 30)

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
ex.makePlot(ex.time, dif, title = 'Kv current',xlabel = 'time (ms)', ylabel = 'current (nA)')

print('Kv current = ', np.max(dif))


# kinetics Fig4C (drops to 50% at 2s)
t = (ex.time-clampT)/1000

tau = 1.4
I0 = 0.26
theo = (np.exp(-t/tau) + I0) / (1+I0);
difNorm = dif/np.max(dif) 

plt.plot(t, difNorm , label = "actual")
plt.plot(t,theo, label = "theoretical")
plt.legend()
plt.show()

print('Kv non-inactivatin = ', difNorm[-1])


#%% adjust
for sec in T6.h.allsec():
    for seg in sec:
        seg.Kv1_2.hTauMult = 1#0.15
        seg.Kv1_2.mTauMult = 1
        seg.Kv1_2.hVHalf = 5

#%% IV

# voltageRange = np.linspace(-50, 30, 9)
# maxCurrent = []
# for v2 in voltageRange:
#     ex.vClamp.amp2 = v2
#     T6.settings.Kv1_2_gpeak = 11
#     T6.update()
#     ex.run()
#     current = np.array(ex.vClampRec)

#     T6.settings.Kv1_2_gpeak = 0
#     T6.update()
#     ex.run()
#     baseline = np.array(ex.vClampRec)

#     dif = current - baseline
#     ex.makePlot(ex.time, dif, title = 'Kv current ' + str(round(v2)) , xmin = 150)

#     indMax = np.argmax(np.abs(dif))
#     Imax = dif[indMax]
#     print('Kv current = ', Imax)
#     maxCurrent.append(Imax)
    
# ex.makePlot(voltageRange, maxCurrent)