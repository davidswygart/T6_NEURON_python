# -*- coding: utf-8 -*-
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
        stim = h.NetStim()          #Create a netstim
        # stim.interval =
        # stim.number
        # stim.start
        # stim.noise
        self.inhStim.append(stim) 
       
        syn = h.ExpSyn(sec(D))    #Create an inhibitory synapse at the specified section location
        # syn.tau =
        # syn.e =
        # syn.i = 
        self.inhSyn.append(syn)
        
        con = h.NetCon(stim, syn)    #connect the netstim to the inhibitory synapse
        self.inhNetCon.append(con)