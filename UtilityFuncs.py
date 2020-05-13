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
    with open(fileName) as file_object:
        lines = file_object.readlines()

    XYZ = np.zeros([len(lines), 3])
    
    for lineNum in range(len(lines)):
        XYZ[lineNum,:] = lines[lineNum].split()
        
    return XYZ

def loadMorph(h):
    h.load_file( "morphology/axonMorph.hoc") #Load axon morphology (created in Cell Builder)
    h.load_file( "morphology/dendriteMorph.hoc") #Load axon morphology (created in Cell Builder)
    
    h.dend_0[0].connect(h.axon[0], 0, 0)
    secList = []
    for sec in h.allsec():
        secList.append(sec)
    return secList

        
def runSim(h, settings, inhSyns, segRec, ribRec):
    if settings.RunMode == 2:
        multiRun(h, settings, inhSyns, segRec, ribRec)
    else:
        singleRun(h, settings, segRec, ribRec)
    
def singleRun(h, settings, segRec, ribRec):
    h.finitialize(settings.v_init)
    h.frecord_init()
    h.continuerun(settings.tstop)
    makePlot(np.linspace(0, settings.tstop, len(segRec[0])), segRec[0])
    saveSingleRun(ribRec, 'results/singleRun.txt')
    
def multiRun(h, settings, inhSyns, segRec, ribRec):
    for con in inhSyns.inhNetCon:
        con.weight[0] = 0
    
    maxVoltages = np.zeros([len(segRec),len(inhSyns.inhNetCon)])
    [r, c] = maxVoltages.shape
    for inhNum in range(c):
        inhSyns.inhNetCon[inhNum].weight[0] = settings.inhSynWeight
        h.finitialize(settings.v_init)
        h.frecord_init()
        h.continuerun(settings.tstop)
        makePlot(np.linspace(0, settings.tstop, len(segRec[0])), segRec[0])
        for recNum in range(r):
            maxVoltages[recNum,inhNum] = max(segRec[recNum])
            
        inhSyns.inhNetCon[inhNum].weight[0] = 0
        
    np.savetxt('results/multiRun.txt', maxVoltages)
        
 
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