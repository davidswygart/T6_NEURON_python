# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:23:13 2020

@author: david
"""
import numpy as np
import math
import matplotlib.pyplot as plt

def findSectionForLocation(h, location):
    for sec in h.allsec():
        for pointNum in range(sec.n3d()):
            dist = math.sqrt( (location[0]-sec.x3d(pointNum))**2  + (location[1]-sec.y3d(pointNum))**2 + (location[2]-sec.z3d(pointNum))**2 )
            if dist < 0.001:
                D = sec.arc3d(pointNum)/sec.L
                return [sec,D]
    raise Exception('Could not find a matching point in the model')
    
    
def readLocation(fileName):
    fileName = 'RibbonLocations.txt'
    with open('InputData/'+fileName) as file_object:
        lines = file_object.readlines()

    XYZ = np.zeros([len(lines), 3])
    
    for lineNum in range(len(lines)):
        XYZ[lineNum,:] = lines[lineNum].split()
        
    return XYZ

def loadMorph(h, hocFile):
    h.load_file(hocFile) #Load neuron morphology (created in Cell Builder)
    secList = []
    for sec in h.allsec():
        secList.append(sec)
    return secList
        

def recordRibbons(h, XYZ_file):
    XYZ = readLocation(XYZ_file)
    ribRec = []
    for ribNum in range(len(XYZ)):
        [sec,D] = findSectionForLocation(h, XYZ[ribNum,:])
        ribRec.append(h.Vector().record(sec(D)._ref_v ))
        
    return ribRec

def recordSegments(h):
    segRec = []
    for sec in h.allsec():
        for n in range(sec.nseg):
            D = 1/(2*sec.nseg) + n/sec.nseg
            segRec.append(h.Vector().record(sec(D)._ref_v))
    return segRec
        
    
def runSim(h, settings, inhSyns):
    
    singleRun(h, settings)
    
    # for inhSyn in inhSyns.inhSyn:
    #     inhSyn
        
    
def singleRun(h, settings):
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