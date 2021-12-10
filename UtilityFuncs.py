import numpy as np
import math
import matplotlib.pyplot as plt
from settings import Settings
import random

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
    
    x = np.array(x)
    y = np.array(y)
    
    
    
    # if ymin == 'calc': ymin = np.average(y) - 2 * np.std(y)
    # if ymax == 'calc': ymax = np.average(y) + 2 * np.std(y)
    if xmin == 'calc': xmin = min(x)
    if xmax == 'calc': xmax = max(x)
    
   # yStart = np.where(x == xmin)
   # yStop = np.where(x == xmax)
    
    #if ymin == 'calc': ymin = min(y[yStart[0][0]-1:yStop[0][0]+1])
    #if ymax == 'calc': ymax = max(y[yStart[0][0]-1:yStop[0][0]+1])
    
    if ymin == 'calc': ymin = min(y)
    if ymax == 'calc': ymax = max(y)

    
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

def pullMax(x, y, start):
    """Pull the max value after a certain point"""
    y = np.array(y)
    
    diff = abs(start - x)
    startInd = np.where(diff == min(diff))
    
    biggest = np.max(abs(y[startInd[0][0]:-1]))
    bigInd = np.where(biggest == abs(y))
    return y[bigInd]

def compareIVs(Vs, Is_conductance, Is_baseline):
    """Plot the difference between 2 IV curves"""
    Is_baseline = np.array(Is_baseline)
    Is_conductance = np.array(Is_conductance)
    Is = Is_conductance - Is_baseline
    makePlot(Vs, Is, title = 'IV graph: baseline subtracted')
    
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
    
def rangeCheck(model, iterations):
    """Function to check the output of the model over a range of a variable"""
    model.settings = Settings()
    model.update()
    
    baselineC = np.zeros([len(model.recordings['ribCai']), iterations])
    stimC = np.zeros([len(model.recordings['ribCai']), iterations])
    
    baselineV = np.zeros([len(model.recordings['ribCai']), iterations])
    stimV = np.zeros([len(model.recordings['ribCai']), iterations])
    
    
    for i in range(iterations):
        model.settings.Ra = model.settings.Ra * 64
        print(model.settings.Ra)
        for [sec, loc] in model.recordings['ribLocations']:
            sec.Ra = model.settings.Ra

        model.run()
        time = model.recordings['time']
        makePlot(time, model.recordings['ribCai'][0], title='ribCai')
        makePlot(time, model.recordings['ribV'][0], title='ribV')
        makePlot(time, model.recordings['segV'][252], title = 'soma V')
        

        
        
        for [n, ribCai] in enumerate(model.recordings['ribCai']):
            baselineC[n,i] = pullAvg(time, ribCai, 300, 500)
            stimC[n,i] = pullAvg(time, ribCai, 505, 1000)
            
        for [n, ribV] in enumerate(model.recordings['ribV']):
            baselineV[n,i] = pullAvg(time, ribV, 300, 500)
            stimV[n,i] = pullAvg(time, ribV, 505, 1000)
            
            


    
    np.savetxt('baselineC_I.txt', baselineC)
    np.savetxt('stimC_I.txt', stimC)
    np.savetxt('baselineV_I.txt', baselineV)
    np.savetxt('stimV_I.txt', stimV)
    
    model.settings = Settings()
    model.update()
    
def locationInfo(locationList):
    values = np.zeros(len(locationList))
    for [n, location] in enumerate(locationList):
        print(location[0].diam)
        values[n] = location[0].diam
        
    return values



def LoopThoughInhibitorySynapses(model, weight, name):
    """Run function looping though and providing inhibition at each synapse"""
    ribVs = np.zeros((91,120))
    inhVs = np.zeros((120,120))
    
    for ii, inhSyn in enumerate(model.inhSyns):
        inhSyn.con[0].weight[0] = weight #1 /100000
        model.run()
        time = model.recordings['time']
        makePlot(time, model.recordings['inhV'][ii])
        
        inhSyn.con[0].weight[0] = 0
         
        for [n, v] in enumerate(model.recordings['ribV']):
            ribVs[n,ii] = pullAvg(time,model.recordings['ribV'][n],400,500)
            
        for [n, v] in enumerate(model.recordings['inhV']):
            inhVs[n,ii] = pullAvg(time,model.recordings['inhV'][n],400,500)
            
        print(str(ii) + ' of 120 completed')

    np.savetxt(name + 'ribV.txt', ribVs)
    np.savetxt(name + 'inhV.txt', inhVs)
        
        
        

def runBoth(model):
    """Function to run both with and without inhibition"""
    Ra_factor = 20
    inhRatio = 0.3
    
    model.settings = Settings()
    model.update()
    
    newRa = Ra_factor * model.settings.Ra
    for [sec, loc] in model.recordings['ribLocations']:
        sec.Ra = newRa

    synNums = list(range(len(model.inhSyns)))
    random.shuffle(synNums) 
    NumToChange = round(len(model.inhSyns) * (1-inhRatio))
    print('......zeoring ', NumToChange, ' inhibitory synapses' )
    for n in range(NumToChange):
        model.inhSyns[synNums[n]].con.weight[0] = 0

    
    model.run()
    time = model.recordings['time']
    #makePlot(time, model.recordings['ribCai'][0], title='ribCai with inhibition')
    makePlot(time, model.recordings['ribV'][0], title='ribV  with inhibition')
    #makePlot(time, model.recordings['segV'][252], title = 'somaV  with inhibition')
    
    baselineC = np.zeros(len(model.recordings['ribCai']))
    stimC = np.zeros(len(model.recordings['ribCai']))
    
    baselineV = np.zeros(len(model.recordings['ribCai']))
    stimV = np.zeros(len(model.recordings['ribCai']))
    
    for [n, ribCai] in enumerate(model.recordings['ribCai']):
        baselineC[n] = pullAvg(time, ribCai, 300, 500)
        stimC[n] = pullAvg(time, ribCai, 505, 1000)
        
    for [n, ribV] in enumerate(model.recordings['ribV']):
        baselineV[n] = pullAvg(time, ribV, 300, 500)
        stimV[n] = pullAvg(time, ribV, 505, 1000)   
        
    np.savetxt('baselineC_I.txt', baselineC)
    np.savetxt('stimC_I.txt', stimC)
    np.savetxt('baselineV_I.txt', baselineV)
    np.savetxt('stimV_I.txt', stimV)
        
    
    print('.....turning off inhibition completely')
    model.settings.inhSyn['weight'] = 0
    model.update()
    for [sec, loc] in model.recordings['ribLocations']:
        sec.Ra = newRa
    model.run()
    #makePlot(time, model.recordings['ribCai'][0], title='ribCai: NO inhibition')
    makePlot(time, model.recordings['ribV'][0], title='ribV: NO inhibition')
    #makePlot(time, model.recordings['segV'][252], title = 'somaV: NO inhibition')
    
    baselineC = np.zeros(len(model.recordings['ribCai']))
    stimC = np.zeros(len(model.recordings['ribCai']))
    
    baselineV = np.zeros(len(model.recordings['ribCai']))
    stimV = np.zeros(len(model.recordings['ribCai']))
    
    for [n, ribCai] in enumerate(model.recordings['ribCai']):
        baselineC[n] = pullAvg(time, ribCai, 300, 500)
        stimC[n] = pullAvg(time, ribCai, 505, 1000)
        
    for [n, ribV] in enumerate(model.recordings['ribV']):
        baselineV[n] = pullAvg(time, ribV, 300, 500)
        stimV[n] = pullAvg(time, ribV, 505, 1000)
            
    np.savetxt('baselineC_noI.txt', baselineC)
    np.savetxt('stimC_noI.txt', stimC)
    np.savetxt('baselineV_noI.txt', baselineV)
    np.savetxt('stimV_noI.txt', stimV)
    
    model.settings = Settings()
    model.update()
    
        
        
    
    
    
    
    
    
    
    
    
    
    