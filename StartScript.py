import numpy as np
import pandas as pd
from T6_Sim import Type6_Model
from UtilityFuncs import makePlot
from UtilityFuncs import saveRecordingData
from UtilityFuncs import pullAvg
from UtilityFuncs import rangeCheck
from UtilityFuncs import runBoth
from UtilityFuncs import LoopThoughInhibitorySynapses


T6 = Type6_Model()
T6.updateAndRun()
#T6.runIV(200) 

LoopThoughInhibitorySynapses(T6, 1/100000, 'stim')
LoopThoughInhibitorySynapses(T6, 0, 'base')

#T6.calcDistances(T6.recordings['inhLocations'],T6.recordings['ribLocations'], 'inh2ribDist.txt')
#T6.calcDistances(T6.recordings['ribLocations'],T6.recordings['ribLocations'], 'rib2ribDist.txt')

#rangeCheck(T6, 4, T6.settings.Ra)



        
    



#T6.segment_location[252]    is soma    
