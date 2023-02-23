# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:16:15 2023

@author: dis006
"""
#%% function to analyse response at specific frequency
def rms(data):
    avg = np.mean(data, axis=1, keepdims=1)
    data = data - avg
    squared = (data)**2
    meanSquared = np.mean(squared, axis=1)
    return np.sqrt(meanSquared)

def analyzeFrequency(startTime = 500):
    startTime = 500
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

##%% set active conductances
T6.settings.Cav_L_gpeak = 1.62
T6.settings.Kv1_2_gpeak = 12
T6.settings.hcn2_gpeak = .78

T6.settings.excSyn.gMax = 0
T6.settings.excDark.gMax = 0
T6.settings.inhSyn.gMax = 0
T6.update()


#%% create experiment object
ex = Experiment(T6)
ex.tstop = 500
ex.placeCurrentClamp(T6.soma.seg)

#%%
ribbonRatios = []
frequencies = []

#%% mean == -38 RMS = 5.5

frequency = .5
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.046)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5

frequency = 1
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.044)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)


#%% mean == -38 RMS = 5.5

frequency = 2
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.04)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5

frequency = 5
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.028)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%% mean == -38 RMS = 5.5

frequency = 10
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.021)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%

frequency = 20
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.025)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%
frequency = 40
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.039)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%
frequency = 50
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.046)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%
frequency = 80
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.07)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%
frequency =160
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.124)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%
frequency =300
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.205)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%
frequency =500
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.3)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)

#%%
frequency =1000
ex.tstop = 5*1000/frequency + 500 ## get 5 cycles after 500 ms adaptation

ex.iClampSineWave(frequency=frequency, baselineI=.075, amplitudeI=.53)
ribFracs, a,b= analyzeFrequency(startTime = 500)
ribbonRatios.append(ribFracs)
frequencies.append(frequency)


#%% Decibels of each ribbon
rat = np.stack(ribbonRatios, axis=1)
decibels = np.log10(rat) * 10
avg_decibels = np.mean(decibels, axis=0)
std_decibels = np.std(decibels, axis=0)

#%% length constant of each ribbon
distances = T6.calcDistances([T6.soma.seg], T6.ribbons.seg)
lengthConstants = -1*distances / np.log(rat)

plt.scatter(distances,ribbonRatios[0])


