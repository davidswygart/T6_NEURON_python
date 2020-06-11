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

def makePlot(x,y):
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()