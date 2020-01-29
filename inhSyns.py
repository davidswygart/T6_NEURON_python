# -*- coding: utf-8 -*-
from neuron import h

class InhSyns():
    def __init__(self):
        self.inhSyn = []
        self.inhNetCon = []
        self.inhStim = []
        
    def makeInhSyn(self,sec,D,settings):
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