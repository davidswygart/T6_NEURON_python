import numpy as np
from neuron import h, gui, units
import UtilityFuncs as f
from settings import Settings
from Electrodes import placeVoltageClamp


class Model():  
    def __init__(self):
        #cd C:/Users/david/Box/T6_BP_NEURON_SIM/T6_NEURON_python
        self.settings = Settings(h)                                                       #Load settings (eg. experimental setup, physiology parameters, display settings)    
        sec = h.Section(name = 'sec')                                        #Load axon morphology

        sec.insert('hcn2')
        # for seg in sec:
        #     seg.hcn2.gpeak = settings.hcn2_gpeak
        #     seg.hcn2.a0t = settings.hcn2_tau
        #self.iClamp_baselineExc = placeCurrentClamp(h, h.sec, 0, 0, self.settings.tstop, self.settings.BaselineExc) #section, location on the section, delay, duration, amplitude
        #self.iClamp_visExc = placeCurrentClamp(h, h.sec, 0, self.settings.ExcStart, self.settings.ExcEnd - self.settings.ExcStart, self.settings.ExcAmp) #section, location on the section, delay, duration, amplitude
        
        if self.settings.DoVClamp:
            self.settings.v_init = self.settings.Hold1
            self.volClamp = placeVoltageClamp(h, sec, 1, self.settings)
            self.iRecord = h.Vector().record(self.volClamp._ref_i)
            h.frecord_init()
            h.continuerun(self.settings.tstop)
            f.makePlot(np.linspace(0, self.settings.tstop, len(self.iRecord)), self.iRecord)                


T6 = Model()