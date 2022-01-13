from neuron import h

class Synapse():
    def __init__(self, seg, settings, pntInd):
        """Make the Synapse (postsynaptic portion), a spike train (virtual presynaptic cell), and connect them together"""
        
        self.syn = h.biSyn(seg)    #Create a synapse at this segment
        self.updateSettings(settings) #Apply the appropriate settings to synapse
        self.pntInd = pntInd
        
    def updateSettings(self, settings):
        """Update synapse with our custom settings"""
        self.syn.onset = settings['start']
        self.syn.gmax = settings['gmax']
        self.syn.e = settings['e']
        
