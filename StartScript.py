

#%% record distances between recording locations
T6 = Type6_Model()
np.savetxt('results\\distances\\inh2ribDist.txt', calcDistances(T6.inhSyns.seg,T6.ribbons.seg))
np.savetxt('results\\distances\\soma2ribDist.txt', calcDistances([T6.soma.seg],T6.ribbons.seg))
np.savetxt('results\\distances\\soma2inhDist.txt', calcDistances([T6.soma.seg],T6.inhSyns.seg))

rib_secNum = np.array(T6.ribbons.secNum)
np.savetxt('results\\distances\\rib_secNum.txt',rib_secNum)
inh_secNum = np.array(T6.inhSyns.secNum)
np.savetxt('results\\distances\\inh_secNum.txt',inh_secNum)





#%% segment lengths
allL = list()
for sec in h.axon:
    allL.append(sec.L/sec.nseg)
    
print(max(allL))
print(np.average(allL))

