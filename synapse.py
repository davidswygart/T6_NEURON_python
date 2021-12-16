class Synapse():
    def __init__(self, h, sec, D, settings):
        """Make the Synapse (postsynaptic portion), a spike train (virtual presynaptic cell), and connect them together"""
        self.syn = h.ExpSyn(sec(D))    #Create a synapse at the specified section location.
        self.stim = [] #Create an empty list for your stimuli
        self.con = [] #Create an empty list for your connections
        self.addStim(h, settings) #Add the first stimuli and connection


    def addStim(self, h, settings):
        """Add a stimulus train to the synapse"""
        stim = h.NetStim()          #Create a netstim
        con = h.NetCon(stim, self.syn)    #connect the netstim to the synapse
        self.updateSettings(stim, con, settings) #Apply the appropriate settings to synapse
        self.stim.append(stim)  #Add the stimulus to the list for easy access
        self.con.append(con) #Add the connection to the list for easy access


    def updateSettings(self, stim, con, settings):
        """Update synapse with our custom settings"""
        start = settings['start']
        stop = settings['stop']
        spikeFreq = settings['spikeFreq']
        weight = settings['weight']

        self.syn.tau =  settings['decayTau']
        self.syn.e = settings['e']
        stim.start = start
        stim.interval = (1 / spikeFreq) * 1000
        duration = stop - start
        stim.number = duration * spikeFreq / 1000
        stim.noise = 0  # 0 deterministic, 1 intervals have negexp distribution.
        con.weight[0] = weight
