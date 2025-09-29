import numpy as np
import scipy as sp #Or just import the signal module from scipy: from scipy import signal. And proceed with signal.square() e.g.

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)
    return t, waveform

def pulse(t, amp):
    return np.where((t >= -0.5) & (t <= 0.5), amp, 0.0)

def periodic_pulse(t, duty_cycle):
    return sp.signal.square(t, duty_cycle)

def sawtooth(t, width):
    return sp.signal.sawtooth(t, width)