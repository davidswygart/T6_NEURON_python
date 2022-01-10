from neuron import h

class Synapse():
    def __init__(self, sec, D, settings, index):
        """Make the Synapse (postsynaptic portion), a spike train (virtual presynaptic cell), and connect them together"""
        
        self.syn = h.biSyn(sec(D))    #Create a synapse at the specified section location.
        self.updateSettings(settings) #Apply the appropriate settings to synapse
        self.index = index
        
    def updateSettings(self, settings):
        """Update synapse with our custom settings"""
        self.syn.onset = settings['start']
        self.syn.gmax = settings['gmax']
        self.syn.e = settings['e']
        
