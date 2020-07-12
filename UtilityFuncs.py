import numpy as np
import math
import matplotlib.pyplot as plt

def findSectionForLocation(h, location):
    """Give a 3D point in space and get the closes model section"""
    dists = []
    for sec in h.allsec():
        for pointNum in range(sec.n3d()):
            dist = math.sqrt( (location[0]-sec.x3d(pointNum))**2  + (location[1]-sec.y3d(pointNum))**2 + (location[2]-sec.z3d(pointNum))**2 )
            if dist < 0.01:
                D = sec.arc3d(pointNum)/sec.L
                return [sec,D]
            dists.append(dist)
    raise Exception('Could not find a matching point in the model for')

def readLocation(fileName):
    """Read the XYZ locations from a txt file"""
    with open(fileName) as file_object:
        lines = file_object.readlines()
    XYZ = np.zeros([len(lines), 3])
    for lineNum, line in enumerate(lines):
        XYZ[lineNum,:] = line.split()
    return XYZ

def makePlot(x, y, title = '', ylabel = '', xlabel = '', ymin = 'calc', ymax = 'calc', xmin = 'calc', xmax = 'calc'):
    """Create a plot X and Y"""
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    # if ymin == 'calc': ymin = np.average(y) - 2 * np.std(y)
    # if ymax == 'calc': ymax = np.average(y) + 2 * np.std(y)
    if ymin == 'calc': ymin = min(y)
    if ymax == 'calc': ymax = max(y)
    if xmin == 'calc': xmin = min(x)
    if xmax == 'calc': xmax = max(x)
    
    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)
    plt.show()
    
def saveRecordingData(dataList, saveName):
    """Save the data in a text document"""
    dataArray = np.zeros([len(dataList), len(dataList[0])])
    for count, Hoc_Vector in enumerate(dataList):
        dataArray[count,:] = Hoc_Vector
    np.savetxt(saveName, dataArray)
    
def pullAvg(x, y, start, stop):
    """Pull the average value from between two timepoints"""
    y = list(y)
    diff = abs(start - x)
    minInd = np.where(diff == min(diff))
    diff = abs(stop - x)
    maxInd = np.where(diff == min(diff))
    
    return np.mean(y[minInd[0][0] : maxInd[0][0]])

def compareIVs(Vs, Is_conductance, Is_baseline):
    """Plot the difference between 2 IV curves"""
    Is_baseline = np.array(Is_baseline)
    Is_conductance = np.array(Is_conductance)
    Is = Is_conductance - Is_baseline
    makePlot(Vs, Is, title = 'IV graph: baseline subtracted')
    
    
    
    
    
    
    
    
    
    
    
    
    
    