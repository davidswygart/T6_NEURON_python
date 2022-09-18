import numpy as np
from T6_Sim import Type6_Model
import os

#%% record distances between recording locations
folder = 'results\\distances\\'
os.makedirs(folder, exist_ok = True)


T6 = Type6_Model()
np.savetxt(folder+ 'inh2ribDist.txt', T6.calcDistances(T6.inhSyns.seg,T6.ribbons.seg))
np.savetxt(folder+ 'soma2ribDist.txt', T6.calcDistances([T6.soma.seg],T6.ribbons.seg))
np.savetxt(folder+ 'soma2inhDist.txt', T6.calcDistances([T6.soma.seg],T6.inhSyns.seg))

rib_secNum = np.array(T6.ribbons.secNum)
np.savetxt(folder+ 'rib_secNum.txt',rib_secNum)
inh_secNum = np.array(T6.inhSyns.secNum)
np.savetxt(folder+ 'inh_secNum.txt',inh_secNum)





#%% segment lengths
# allL = list()
# for sec in h.axon:
#     allL.append(sec.L/sec.nseg)
    
# print(max(allL))
# print(np.average(allL))

