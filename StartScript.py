from T6_Sim import Type6_Model

T6 = Type6_Model()
T6.run()

# f.makePlot(np.linspace(0, self.settings.tstop, len(self.segments.recording[0])), self.iRecord)
#                 makePlot(np.linspace(0, settings.tstop, len(segRec[0])), segRec[0])
#     saveSingleRun(ribRec, 'results/singleRun.txt')
        
        
        
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

# def saveSingleRun(ribRec, saveName):
#     data = np.zeros([len(ribRec), len(ribRec[0])])
#     for r_num in range(len(ribRec)):
#         data[r_num,:] = ribRec[r_num]
#     np.savetxt(saveName, data)
#     return 

#calcDistances(T6.segments.location, T6.segments.location, "results/segDistances.txt")