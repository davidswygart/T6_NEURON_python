# -*- coding: utf-8 -*-
from UtilityFuncs import readLocation
from UtilityFuncs import findSectionForLocation

class Ribbons():
    """A class for containing all of the ribbon output synapses of the T6 bipolar cell"""
    
    def __init__(self, h, XYZ_file):
        XYZ = readLocation(XYZ_file)
        self.recording = []
        self.location = []
        for ribNum in range(len(XYZ)):
            [sec,D] = findSectionForLocation(h, XYZ[ribNum,:])
            self.location.append([sec,D])
            self.recording.append(h.Vector().record(sec(D)._ref_v ))
        