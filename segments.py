# -*- coding: utf-8 -*-

class Segments():
    """A class for containing all of the segments in the model"""
    
    def __init__(self, h):
        self.recording = []
        self.location = []

        for sec in h.allsec():
            for n in range(sec.nseg):
                D = 1/(2*sec.nseg) + n/sec.nseg
                    
                self.location.append([sec, D])
                self.recording.append(h.Vector().record(sec(D)._ref_v))