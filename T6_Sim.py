# -*- coding: utf-8 -*- 
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from neuron import h, gui, units
from settings import Settings


def main():
    #cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python
    settings = Settings() #Load settings (eg. experimental setup, physiology parameters, display settings)
    h.load_file("T6_V3.hoc") #Load neuron morphology (created in Cell Builder)
    
    ribRec = recordRibbons("InputData/RibbonLocations.txt")
    segRec = recordSegments()
    [inhSyn, inhNetCon] = addInhSyn("InputData/InhSynLocations.txt", settings)
    runSim(settings)
    
    makePlot(np.linspace(0,1,len(segRec[0])), segRec[0])
    saveSingleRun(ribRec, 'singleRun.txt')



def recordRibbons(XYZ_file):
    XYZ = readLocation(XYZ_file)
    ribRec = []
    for ribNum in range(len(XYZ)):
        [sec,D] = findSectionForLocation(XYZ[ribNum,:])
        ribRec.append(h.Vector().record(sec(D)._ref_v ))
        
    return ribRec

def recordSegments():
    segRec = []
    for sec in h.allsec():
        for n in range(sec.nseg):
            D = 1/(2*sec.nseg) + n/sec.nseg
            segRec.append(h.Vector().record(sec(D)._ref_v))
    return segRec
        

def addInhSyn(XYZ_file, settings):
    XYZ = readLocation(XYZ_file)
    inhSyn = inhNetCon = []
    for inhNum in range(len(XYZ)):
        [sec,D] = findSectionForLocation(XYZ[inhNum,:])
        [inhSyn, inhNetCon] = addPresynapticStim(sec,D,inhSyn,inhNetCon,settings)
    return [inhSyn, inhNetCon]

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
        for pointNum in range(sec.n3d()):
            dist = math.sqrt( (location[0]-sec.x3d(pointNum))**2  + (location[1]-sec.y3d(pointNum))**2 + (location[2]-sec.z3d(pointNum))**2 )
            if dist < 0.001:
                D = sec.arc3d(pointNum)/sec.L
                return [sec,D]
    raise Exception('Could not find a matching point in the model')

def addPresynapticStim(sec,D,inhSyn,inhNetCon,settings):
    
    return [inhSyn, inhNetCon]
    
def runSim(settings):
    h.finitialize(settings.v_init)
    h.frecord_init()
    h.continuerun(settings.tstop)
 
def saveSingleRun(ribRec, saveName):
    data = np.zeros([len(ribRec), len(ribRec[0])])
    for r_num in range(len(ribRec)):
        data[r_num,:] = ribRec[r_num]
    np.savetxt(saveName, data)
    return
    
def makePlot(x,y):
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()


    
main()