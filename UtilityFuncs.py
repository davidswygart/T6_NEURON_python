import numpy as np
import matplotlib.pyplot as plt
from neuron import h


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
    
    x = np.array(x)
    y = np.array(y)
    
    if xmin == 'calc': xmin = min(x)
    if xmax == 'calc': xmax = max(x)
    
    
    if ymin == 'calc': ymin = np.average(y) - 2*np.std(y)#ymin = min(y)
    if ymax == 'calc': ymax = np.average(y) + 2*np.std(y)#ymax = max(y)

    
    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)
    plt.show()
    
    
def pullAvg(x, y, start, stop):
    """Pull the average value from between two timepoints"""
    y = list(y)
    diff = abs(start - x)
    minInd = np.where(diff == min(diff))
    diff = abs(stop - x)
    maxInd = np.where(diff == min(diff))
    
    return np.mean(y[minInd[0][0] : maxInd[0][0]])

def averageRibbonVoltage(model):
    
    
  
    time = model.recordings['time']
    stopTime = model.settings.tstop
    startTime = stopTime-50
    voltages = []
    
    
    for ribV in model.recordings['ribV']:
        voltages.append(pullAvg(time, ribV, startTime, stopTime))
    
    d = model.calcDistances([model.recordings['segLocations'][241]],model.recordings['ribLocations'], 'soma2ribDist.txt')[0]
    plt.scatter(d,voltages)
    plt.title('range of ribbon voltages')
    plt.ylabel('mV')
    plt.xlabel('distance from soma')
    plt.ylim((np.min(voltages)-2, np.max(voltages)+2))
    
    return np.mean(voltages)
    #return voltages
    

def pullMin(x, y, start):
    """Pull the max value after a certain point"""
    y = np.array(y)
    
    diff = abs(start - x)
    startInd = np.where(diff == min(diff))
    
    small = np.min(y[startInd[0][0]:-1])
    return small


def pullAbs(x, y, start):
    """Pull the max value after a certain point"""
    y = np.array(y)
    x = np.array(x)
    
    diff = abs(start - x)
    startInd = np.where(diff == min(diff))
    
    newY = y[startInd[0][0]:-1]
    absY = np.abs(newY)
    maxAbs = np.max(absY)
    
    ind = np.where(maxAbs == absY)
    
    return newY[ind[0][0]]


def pullMax(x, y, start):
    """Pull the max value after a certain point"""
    y = np.array(y)
    
    diff = abs(start - x)
    startInd = np.where(diff == min(diff))
    
    small = np.max(y[startInd[0][0]:-1])
    smallInd = np.where(small == y)
    return y[smallInd]


    
def interpData(xp, fp, dt):
    """Interpolate data so that it can be saved in smaller files"""
    x = np.arrange(xp[0], xp[-1], dt)
    f = np.interp(x, xp, fp)
    return([x, f])

def hist(vals, title = '', ylabel = '', xlabel = '', xmin = 'calc', xmax = 'calc'):
    fig, ax = plt.subplots()
    ax.hist(vals)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    if xmin == 'calc': xmin = min(vals)
    if xmax == 'calc': xmax = max(vals)

    plt.xlim(xmin, xmax)
    plt.show()
    
def calcDistances(segList1, segList2):
    """calculate the path distances between sets of locations"""
    num1 = len(segList1)
    num2 = len(segList2)  
    distMatrix = np.zeros([num1, num2])

    for n1 in range(num1):
        seg1 = segList1[n1]
        for n2 in range(num2):
            seg2 = segList2[n2]

            dist = h.distance(seg1, seg2)
            distMatrix[n1, n2] = dist
    return distMatrix
    
    
    
    
    
    
    