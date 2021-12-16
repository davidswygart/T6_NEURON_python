import numpy as np
import pandas as pd
from T6_Sim import Type6_Model
from UtilityFuncs import makePlot
from UtilityFuncs import saveRecordingData
from UtilityFuncs import pullAvg
from UtilityFuncs import rangeCheck
from UtilityFuncs import runBoth
from UtilityFuncs import LoopThoughInhibitorySynapses
from UtilityFuncs import averageRibbonVoltage
import matplotlib.pyplot as plt


T6 = Type6_Model()
T6.updateAndRun()



# LoopThoughInhibitorySynapses(T6, 5/100000, 'stim')
# LoopThoughInhibitorySynapses(T6, 0, 'base')

# T6.calcDistances(T6.recordings['inhLocations'],T6.recordings['ribLocations'], 'results//distances//inh2ribDist.txt')
# T6.calcDistances(T6.recordings['ribLocations'],T6.recordings['ribLocations'], 'results//distances//rib2ribDist.txt')
# T6.calcDistances(T6.recordings['inhLocations'],T6.recordings['segLocations'], 'results//distances//inh2segDist.txt')

#pullAvg(T6.recordings['time'],T6.recordings['segV'][241],400,500)
#running for -35 to -50 recorded at rib1




#T6.recordings['segLocations'][241]
#[dend_0[2], 0.8333333333333333]
#is soma after updating nseg on 12/15/21

#a =T6.calcDistances([T6.recordings['segLocations'][241]],T6.recordings['ribLocations'], 'soma2ribDist.txt')[0]