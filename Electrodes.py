# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:27:16 2020

@author: david
"""

def placeCurrentClamp(h, sec, D, delay, dur, amp):
    iClamp = h.IClamp(sec(D))
    iClamp.delay = delay
    iClamp.dur = dur
    iClamp.amp = amp
    return iClamp

def placeVoltageClamp(h ,sec, D, settings):
    vClamp = h.SEClamp(sec(D))
    vClamp.dur1  = settings.ChangeClamp
    vClamp.dur2  = settings.tstop - settings.ChangeClamp
    vClamp.amp1  = settings.Hold1
    vClamp.amp2  = settings.Hold2
    return vClamp