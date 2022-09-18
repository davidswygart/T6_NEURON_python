import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
sys.path.append("/nrn/lib/python")

import numpy as np
from T6_Sim import Type6_Model
from Experiment import Experiment
from UtilityFuncs import makePlot
#%% create model
T6 = Type6_Model()
ex = Experiment(T6, 1000, 32, -40)

#%% set up active conductances, synapse strengths, and experiment timing
T6.settings.hcn2_gpeak = .78
T6.settings.Kv1_2_gpeak = 11
T6.settings.Cav_L_gpeak = 2.1

T6.settings.excSyn['gmax'] = 370
inhG = 9400

T6.settings.excSyn['start'] = 500
T6.settings.inhSyn['start'] = 700

T6.update()

#%% run model and get traces
v = ex.runSingleInh(inhG, 9)

inhTrace = np.array(ex.rec.v[T6.inhSyns.secNum[9]])
excTrace = np.array(ex.rec.v[T6.ribbons.secNum[24]])
time = (ex.time) / 1000
makePlot(time, inhTrace, title = 'example inhibition dV', ylabel = 'mV', xlabel = 'time(s)', ymin = -60, ymax = -25, xmin=.4)# inhibition at axon 67 or 43 (or even 42) --> T6.inhSyns.sec[92]
makePlot(time, excTrace, title = 'example excitatory dV', ylabel = 'mV', xlabel = 'time(s)', ymin = -60, ymax = -25, xmin=.4)# inhibition at axon 67 or 43 (or even 42) --> T6.inhSyns.sec[92]

#inh 17 = axon 98
# ribbon at axon 36 such as --> T6.ribbons.sec[23]
ex.avgRibV()
