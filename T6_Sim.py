# -*- coding: utf-8 -*- 
import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from inhSyns import InhSyns
from Electrodes import placeCurrentClamp
from Electrodes import placeVoltageClamp


def main():
    #cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python
    settings = Settings()                                                       #Load settings (eg. experimental setup, physiology parameters, display settings)    
    axons = f.loadMorph(h, "T6_V3.hoc")                                         #Load axon morphology
    ribRec = f.recordRibbons(h, "InputData/RibbonLocations.txt")                #A list of voltage recording vectors at each ribbon
    segRec = f.recordSegments(h)                                                #A list of voltage recording vectors at each segment
    inhSyns = InhSyns(h, "InputData/InhSynLocations.txt", settings)             #An object containing all inhibitory synapses, their presynaptic stimulation, and their connector
    iClamp_baselineExc = placeCurrentClamp(h, axons[0], 0, 0, settings.tstop, settings.BaselineExc) #section, location on the section, delay, duration, amplitude
    iClamp_visExc = placeCurrentClamp(h, axons[0], 0, settings.ExcStart, settings.ExcEnd - settings.ExcStart, settings.ExcAmp) #section, location on the section, delay, duration, amplitude
    
    if settings.DoVClamp:
        settings.v_init = settings.Hold1
        volClamp = placeVoltageClamp(h, axons[0], 0, settings)
        iRecord = h.Vector().record(volClamp._ref_i)
        f.runSim(h, settings, inhSyns, segRec, ribRec)
        f.makePlot(np.linspace(0, settings.tstop, len(segRec[0])), iRecord)
    else:
        f.runSim(h, settings, inhSyns, segRec, ribRec)

main()