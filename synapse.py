from UtilityFuncs import readLocation
from UtilityFuncs import findSectionForLocation

class Synapse():
    def __init__(self, h, sec, D, settings):
        """Make the Synapse (postsynaptic portion), a spike train (virtual presynaptic cell), and connect them together"""
        self.syn = h.ExpSyn(sec(D))    #Create an inhibitory synapse at the specified section location
        self.stim = h.NetStim()          #Create a netstim
        self.con = h.NetCon(self.stim, self.syn)    #connect the netstim to the inhibitory synapse
        self.updateSettings(self.stim, self.con, settings)
 
    def addStim2(self, h, settings):
        """Add a second stimulus train to the synapse"""
        self.stim2 = h.NetStim()          #Create a netstim
        self.con2 = h.NetCon(self.stim2, self.syn)    #connect the netstim to the inhibitory synapse
        self.updateSettings(self.stim2, self.con2, settings)
        
    
    def updateSettings(self, stim, con, settings):
        """Update synapse with our custom settings"""
        start = settings['start']
        stop = settings['stop']
        spikeFreq = settings['spikeFreq']
        weight = settings['weight']
        
        #self.syn.tau = Decay
        self.syn.e = settings['e']
        stim.start = start
        stim.interval = (1 / spikeFreq) * 1000
        duration = stop - start
        stim.number = duration * spikeFreq / 1000
        stim.noise = 1  # 0 deterministic, 1 intervals have negexp distribution.
        con.weight[0] = weight
        

        