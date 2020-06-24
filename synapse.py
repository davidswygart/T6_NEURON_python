from UtilityFuncs import readLocation
from UtilityFuncs import findSectionForLocation

class Synapse():
    def __init__(self, h, sec, D, e):
        """Make the Synapse (postsynaptic portion)"""
        self.syn = h.ExpSyn(sec(D))    #Create an inhibitory synapse at the specified section location
        #self.syn.tau = Decay
        self.syn.e = e
        
    def connectStimToSyn(self, h, start, stop, spikeFreq, weight):
        """Make a spike train (virtual presynaptic cell), and connect it to the synapse"""
        stim = h.NetStim()          #Create a netstim
        stim.start = start
        stim.interval = (1 / spikeFreq) * 1000
        duration = stop - start
        stim.number = duration * spikeFreq / 1000
        stim.noise = 1  # 0 deterministic, 1 intervals have negexp distribution.
        self.stim = stim
        
        self.con = h.NetCon(self.stim, self.syn)    #connect the netstim to the inhibitory synapse
        self.con.weight[0] = weight