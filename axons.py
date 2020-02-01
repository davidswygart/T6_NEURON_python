# -*- coding: utf-8 -*-
from neuron import h

class Axons ():
    """A class to for loading the axon morphology created by Cell Builder"""
    
    def __init__(self, hocFile):
        h.load_file(hocFile) #Load neuron morphology (created in Cell Builder)
        self.secs = h.allsec()
        self.changeStuff()
        
    def changeStuff(self):
        for sec in self.secs:
            sec.e_pas = -1000