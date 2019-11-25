# -*- coding: utf-8 -*- 
import numpy as np
import math
from neuron import h, gui, units
from settings import Settings


def runSim():
    #cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python
    settings = Settings() #Load settings (eg. experimental setup, physiology parameters, display settings)
    h.load_file("T6_V3.hoc") #Load neuron morphology (created in Cell Builder)
    
    RibRec = recordRibbons("InputData/RibbonLocations.txt", settings)
    InhSyn = addInhSyn("InputData/InhSynLocations.txt", settings)



def recordRibbons(XYZ_file, settings):
    XYZ = readLocation(XYZ_file)
    for ribNum in range(len(XYZ)):
        sec = findSectionForLocation(XYZ[ribNum,:])
        print(sec)
        

def addInhSyn(XYZ_file, settings):
    XYZ = readLocation(XYZ_file)

def readLocation(fileName):
    fileName = 'RibbonLocations.txt'
    with open('InputData/'+fileName) as file_object:
        lines = file_object.readlines()

    XYZ = np.zeros([len(lines), 3])
    
    for lineNum in range(len(lines)):
        XYZ[lineNum,:] = lines[lineNum].split()
        
    return XYZ

def findSectionForLocation(location):
    for sec in h.allsec():
        print(sec)
        for pointNum in range(sec.n3d()):
            dist = math.sqrt( (location[0]-sec.x3d(pointNum))**2  + (location[1]-sec.y3d(pointNum))**2 + (location[2]-sec.z3d(pointNum))**2 )
            print(dist)
#            if dist < 0.001:
#                print('Found Match')
#                return sec
            
    print("couldn't find a matching section location for this point")
    


    



#def createRibbonSegments(settings, XYZ):
#    RibbonOnly_Bouton = []
#    RibRec_NoInh = []
#    
#    for num in range(len(XYZ[:,1])):
#        RibbonOnly_Bouton.append(h.Section(name = 'RibbonOnly_Bouton'+str(num)))
#        RibbonOnly_Bouton[num].L = 0.1566
#        RibbonOnly_Bouton[num].diam = 1
#        RibbonOnly_Bouton[num].Ra = settings.RA
#        RibbonOnly_Bouton[num].cm = settings.CM
#        RibbonOnly_Bouton[num].insert('pas')
#        RibbonOnly_Bouton[num].g_pas = settings.G_PAS
#        RibbonOnly_Bouton[num].e_pas = settings.EPAS
#        RibbonOnly_Bouton[num].nseg = 1
#        RibRec_NoInh.append(h.Vector().record(RibbonOnly_Bouton[num](1)._ref_v ))
#        
#    return [RibRec_NoInh]
#
#def connectRibbonSegments()
    
runSim()