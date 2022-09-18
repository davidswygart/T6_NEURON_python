import numpy as np
from T6_Sim import Type6_Model
from Experiment import Experiment

#%% Ca
T6 = Type6_Model()
ex = Experiment(T6)
ex.tstop=700
ex.temp=22
ex.v_init=-70
ex.placeVoltageClamp(-70, 300, -35)

#%% set Ca current to -0.023 nA when stepping from -70 to -35 mV
T6.settings.Cav_L_gpeak = 1.62
T6.update()
ex.run()
current = np.array(ex.vClampRec)

T6.settings.Cav_L_gpeak = 0
T6.update()
ex.run()
baseline = np.array(ex.vClampRec)

dif = current - baseline
ex.makePlot(ex.time, dif, title = 'Ca current',xlabel = 'time (ms)', ylabel = 'current (nA)', xmin = 150)

print('Ca current = ', np.min(dif))


#%% create calcium IV

voltageRange = np.linspace(-90, 40, 10)
maxCurrent = []
for v2 in voltageRange:
    ex.vClamp.amp2 = v2
    T6.settings.Cav_L_gpeak = 2.1
    T6.update()
    ex.run()
    current = np.array(ex.vClampRec)

    T6.settings.Cav_L_gpeak = 0
    T6.update()
    ex.run()
    baseline = np.array(ex.vClampRec)

    dif = current - baseline
    ex.makePlot(ex.time, dif, title = 'Ca current ' + str(round(v2)) , xmin = 150)

    indMax = np.argmax(np.abs(dif))
    Imax = dif[indMax]
    print('Ca current = ', Imax)
    maxCurrent.append(Imax)
    
ex.makePlot(voltageRange, maxCurrent)
