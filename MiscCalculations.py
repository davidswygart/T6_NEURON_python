# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:13:13 2022

@author: david
"""

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

# %% calculating cumalative currents
excCurrent = 0
for syn in T6.excSyns.syn:
    excCurrent += syn.i
print('excitatory current = ', round(excCurrent*1000), ' (pA)')

inhCurrent = 0
for syn in T6.inhSyns.syn:
    inhCurrent += syn.i
print('inhibitory current = ', round(inhCurrent*1000), ' (pA)')

kCurrent = 0
for sec in T6.h.allsec():
    for seg in sec:
        kCurrent += seg.ik
print('k+ current = ', round(kCurrent*1000), ' (pA)') #471 pA difference between exc and inh
        
    
b.hcn2.gHCN2
b.Kv1_2.gKv1_2
b.pas.g
b.Ca.gCa

#%% segment lengths
# allL = list()
# for sec in h.axon:
#     allL.append(sec.L/sec.nseg)
    
# print(max(allL))
# print(np.average(allL))

