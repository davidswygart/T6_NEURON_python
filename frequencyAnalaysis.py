#%% function to analyse response at specific frequency
def rms(data):
    avg = np.mean(data, axis=1, keepdims=1)
    data = data - avg
    squared = (data)**2
    meanSquared = np.mean(squared, axis=1)
    return np.sqrt(meanSquared)

def analyzeFrequency(startTime = 1000):
    startInd = np.argmin(abs(ex.time-startTime))

    iClampV = np.array(ex.iClampRec)
    iClampV = iClampV[startInd:]
    iClampRMS = rms(np.atleast_2d(iClampV)) #need to expand to 2 dimensions for my formula
    
    ribVs = np.array(ex.rec.ribV)
    ribVs = ribVs[:, startInd:]
    ribRMS = rms(ribVs)
    
    ribbonFraction = ribRMS / iClampRMS
    
    print('iClamp mean = ', np.mean(iClampV) )
    print('iClamp RMS = ', iClampRMS)
    print('avg ribbon RMS fraction = ', np.mean(ribbonFraction))
    
    exampleRibV = ribVs[0,:]
    
    plt.plot(ex.time[startInd: ], iClampV, label='Iclamp')
    plt.plot(ex.time[startInd: ], exampleRibV, label='ribbon #0')
    plt.legend()
    plt.xlabel('time (ms)')
    plt.ylabel('mV')
    plt.show()
    return ribbonFraction, ribRMS, iClampRMS

#%%############# Create Model and Experiment #########################
from T6_Sim import Type6_Model
from Experiment import Experiment
import numpy as np
import matplotlib.pyplot as plt

#%% Only make the model once. NEURON can do weird things if you remake it
T6 = Type6_Model()
ex = Experiment(T6)
ex.placeCurrentClamp(T6.soma.seg)
ex.tstop = 6000
T6.settings.excDark.frequency = 70
T6.settings.excSyn.frequency = 515
T6.settings.inhSyn.gMax = 1.64e-5
T6.settings.excSyn.start = 0
T6.settings.excSyn.stop = 1e6
T6.settings.inhSyn.start = 0
T6.settings.inhSyn.stop = 1e6
startTime = 1000
T6.update()

#%%
ribbonRatios = []
frequencies = []

#%% mean == -38 RMS = 5.5
frequency = .25
ex.iClampSineWave(frequency=frequency, amplitudeI=0.15,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = .5
ex.iClampSineWave(frequency=frequency, amplitudeI=0.15,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 1
ex.iClampSineWave(frequency=frequency, amplitudeI=0.143,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 2
ex.iClampSineWave(frequency=frequency, amplitudeI=0.146,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 3
ex.iClampSineWave(frequency=frequency, amplitudeI=0.138,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 5
ex.iClampSineWave(frequency=frequency, amplitudeI=.129,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 10
ex.iClampSineWave(frequency=frequency, amplitudeI=.122,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 20
ex.iClampSineWave(frequency=frequency, amplitudeI=.119,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 35
ex.iClampSineWave(frequency=frequency, amplitudeI=.119,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 50
ex.iClampSineWave(frequency=frequency, amplitudeI=.121,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 65
ex.iClampSineWave(frequency=frequency, amplitudeI=.123,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 80
ex.iClampSineWave(frequency=frequency, amplitudeI=.126,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 100
ex.iClampSineWave(frequency=frequency, amplitudeI=.131,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 250
ex.iClampSineWave(frequency=frequency, amplitudeI=.185,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5
frequency = 500
ex.iClampSineWave(frequency=frequency, amplitudeI=.298,start=startTime)
ribFracs, a,b= analyzeFrequency(startTime = startTime + 1000) # give 1 second of sine wave to adapt
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% Decibels of each ribbon
rat = np.stack(ribbonRatios, axis=1)
decibels = np.log10(rat) * 10
avg_decibels = np.mean(decibels, axis=0)
std_decibels = np.std(decibels, axis=0)

#%% length constant of each ribbon
distances = T6.calcDistances([T6.soma.seg], T6.ribbons.seg)

lengthConstants = -1*distances / np.transpose(np.log(rat))

plt.scatter(distances,ribbonRatios[0])
plt.show()

avgLambda = np.mean(lengthConstants, axis=1)
stdLambda = np.std(lengthConstants, axis=1)

plt.plot(frequencies, avgLambda)
plt.show()


