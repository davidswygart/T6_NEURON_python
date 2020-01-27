# -*- coding: utf-8 -*- 
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from neuron import h, gui, units
from settings import Settings
from inhSyns import InhSyns


def main():
    #cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python
    settings = Settings() #Load settings (eg. experimental setup, physiology parameters, display settings)    
    axons = loadMorph("T6_V3.hoc") #Load axon morphology
    ribRec = recordRibbons("InputData/RibbonLocations.txt") #A list of voltage recording vectors at each ribbon
    segRec = recordSegments() #A list of voltage recording vectors at each segment
    inhSyns = addInhSyn("InputData/InhSynLocations.txt", settings) #An object containing all inhibitory synapses, their presynaptic stimulation, and their connector
    iClamp_baselineExc = placeCurrentClamp(axons[0], 0, 0, settings.tstop, settings.BaselineExc) #section, location on the section, delay, duration, amplitude
    iClamp_visExc = placeCurrentClamp(axons[0], 0, settings.ExcStart, settings.ExcDur, settings.ExcAmp) #section, location on the section, delay, duration, amplitude

    
    if settings.DoVClamp:
        settings.v_init = settings.Hold1_VolCla
        volClamp = placeVoltageClamp(axons[0], 0, settings.Dur1_VolCla, settings.Dur2_VolCla, settings.Hold1_VolCla, settings.Hold2_VolCla )
    
    runSim(settings, inhSyns)
    
    
    makePlot(np.linspace(0,1,len(segRec[0])), segRec[0])
    saveSingleRun(ribRec, 'singleRun.txt')



def loadMorph(hocFile):
    h.load_file(hocFile) #Load neuron morphology (created in Cell Builder)
    secList = []
    for sec in h.allsec():
        secList.append(sec)
    return secList
        

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
    inhSyns = InhSyns()
    for inhNum in range(len(XYZ)):
        [sec,D] = findSectionForLocation(XYZ[inhNum,:])
        inhSyns.makeInhSyn(sec,D,settings)
    return inhSyns

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

    
def runSim(settings, inhSyns):
    
#    case settings.RunMode
#    
#    1
#    singleRun(settings)
#    
#    2
    for inhSyn in inhSyns.inhSyn:
        inhSyn
        
    

    
def singleRun(settings):
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

def placeCurrentClamp(sec, D, delay, dur, amp):
    iClamp = h.IClamp(sec(D))
    iClamp.delay = delay
    iClamp.dur = dur
    iClamp.amp = amp
    return iClamp

def placeVoltageClamp(sec, D, dur1, dur2, hold1, hold2):
    vClamp = h.SEClamp(sec(D))
    vClamp.dur1  = dur1
    vClamp.dur2  = dur2
    vClamp.amp1  = hold1
    vClamp.amp2  = hold2
    return vClamp
    
main()