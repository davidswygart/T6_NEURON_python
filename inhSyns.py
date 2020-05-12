from UtilityFuncs import readLocation
from UtilityFuncs import findSectionForLocation

class InhSyns():
    def __init__(self, h, XYZ_file, settings):
        XYZ = readLocation(XYZ_file)
        self.inhSyn = []
        self.inhNetCon = []
        self.inhStim = []
        
        for inhNum in range(len(XYZ)):
            [sec,D] = findSectionForLocation(h, XYZ[inhNum,:])
            self.makeInhSyn(h, sec,D,settings)
        
    def makeInhSyn(self, h, sec, D, settings):
        
        #Make the inhibitory spike train (presynaptic amacrine cell)
        stim = h.NetStim()          #Create a netstim
        stim.start = settings.InhStart
        stim.interval = (1 / settings.InhSpikeFreq) * 1000
        inhDur = (settings.InhEnd - settings.InhStart)
        stim.number = inhDur * settings.InhSpikeFreq / 1000
        stim.noise = settings.InhNoise
        self.inhStim.append(stim) 
       
        #Make the inhibitory Synapse (postsynaptic portion)
        syn = h.ExpSyn(sec(D))    #Create an inhibitory synapse at the specified section location
        syn.tau = settings.inhDecay
        syn.e = settings.inhRevPot
        self.inhSyn.append(syn)
        
        #Create the connection between the spike train and the inhibitory synapse
        con = h.NetCon(stim, syn)    #connect the netstim to the inhibitory synapse
        con.weight[0] = settings.inhSynWeight
        self.inhNetCon.append(con)