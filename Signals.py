import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)
    return t, waveform

def pulse(t, amp):
    return np.where((t >= -0.5) & (t <= 0.5), amp, 0.0)