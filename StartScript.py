import numpy as np
from T6_Sim import Type6_Model
from UtilityFuncs import makePlot
from UtilityFuncs import saveRecordingData
from UtilityFuncs import pullAvg
from UtilityFuncs import rangeCheck


T6 = Type6_Model()
T6.updateAndRun()
#T6.runIV(200) 





#rangeCheck(T6, 4, T6.settings.Ra)









#from hoc2swc import neuron2swc
#neuron2swc("out.swc")

#T6.segment_location[252]    is soma    
#saveRecordingData(T6.segment_recording, 'results/segmentVoltages.txt')

# def multiRun(h, settings, inhSyns, segRec, ribRec):
#     for con in inhSyns.inhNetCon:
#         con.weight[0] = 0
    
#     maxVoltages = np.zeros([len(segRec),len(inhSyns.inhNetCon)])
#     [r, c] = maxVoltages.shape
#     for inhNum in range(c):
#         inhSyns.inhNetCon[inhNum].weight[0] = settings.inhSynWeight
#         h.finitialize(settings.v_init)
#         h.frecord_init()
#         h.continuerun(settings.tstop)
#         makePlot(np.linspace(0, settings.tstop, len(segRec[0])), segRec[0])
#         for recNum in range(r):
#             maxVoltages[recNum,inhNum] = max(segRec[recNum])
            
#         inhSyns.inhNetCon[inhNum].weight[0] = 0
        
#     np.savetxt('results/multiRun.txt', maxVoltages)



#calcDistances(T6.segments.location, T6.segments.location, "results/segDistances.txt")