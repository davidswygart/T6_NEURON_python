from UtilityFuncs import readLocation
from UtilityFuncs import findSectionForLocation

class Synapse():
    def __init__(self, h, sec, D):
        """Make the Synapse (postsynaptic portion), a spike train (virtual presynaptic cell), and connect them together"""
        self.syn = h.ExpSyn(sec(D))    #Create an inhibitory synapse at the specified section location
        self.stim = h.NetStim()          #Create a netstim
        self.con = h.NetCon(self.stim, self.syn)    #connect the netstim to the inhibitory synapse

        
    def updateSettings(self, settings):
        """Update synapse with our custom settings"""
        #self.syn.tau = Decay
        e = settings['e']
        start = settings['start']
        stop = settings['stop']
        spikeFreq = settings['spikeFreq']
        weight = settings['weight']
        
        self.syn.e = e
        self.stim.start = start
        self.stim.interval = (1 / spikeFreq) * 1000
        duration = stop - start
        self.stim.number = duration * spikeFreq / 1000
        self.stim.noise = 1  # 0 deterministic, 1 intervals have negexp distribution.
        self.con.weight[0] = weight