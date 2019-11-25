# -*- coding: utf-8 -*-
from neuron import h, gui, units

h.load_file("T6_V3.hoc") #Load neuron morphology (created in Cell Builder)

for sec in h.allsec():
    print(sec)
    
    for pointNum in range(sec.n3d()):
        print(sec.x3d(pointNum), sec.y3d(pointNum), sec.z3d(pointNum))