import numpy as np
import scipy as sp #Or just import the signal module from scipy: from scipy import signal. And proceed with signal.square() e.g.

def generate_sine_wave(frequency, amplitude, duration, sample_rate=1000):
    """
    Create a sinusoidal signal.

    Parameters
    ----------
    frequency : float
        Frequency of the sine wave (Hz).
    amplitude : float
        Amplitude of the sine wave.
    duration : float
        Duration of the sine wave (seconds).
    sample_rate : int, optional
        Sampling rate in samples per second (default is 1000).
    
    Returns
    -------
    t : np.ndarray
        Time array corresponding to the waveform.
    waveform : np.ndarray
        Generated sine wave samples.
    """
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, waveform

def pulse(t, amp):
    """
    Generate a single rectangular pulse.

    The pulse has amplitude 'amp' between -0.5 <= t <= 0.5 and is zero elsewhere.
    The input array 't' defines the time values.

    Parameters
    ----------
    t : np.ndarray
        Time array (independent variable).
    amp : float
        Amplitude of the pulse.

    Returns
    -------
    np.ndarray
        Array representing the pulse waveform.
    """
    return np.where((t >= -0.5) & (t <= 0.5), amp, 0.0)

def periodic_pulse(t, duty_cycle):
    """
    Generate a periodic square-wave signal.

    The waveform has a period of 2π, taking values +1 from 0 to 2π*duty_cycle
    and -1 from 2π*duty_cycle to 2π. The duty cycle must be in the interval [0, 1].
    The input array 't' defines the time values.

    Parameters
    ----------
    t : np.ndarray
        Time array (independent variable).
    duty_cycle : float
        Fraction of one period during which the signal is high (in [0, 1]).

    Returns
    -------
    np.ndarray
        Array representing the periodic square-wave waveform.
    """
    return sp.signal.square(t, duty_cycle)

def sawtooth(t, width):
    """
    Generate a periodic sawtooth or triangular waveform.

    The waveform has a period of 2π. It rises linearly from -1 to 1 over the interval
    0 to width*2π, then drops from 1 to -1 over width*2π to 2π. The width parameter
    must be in the interval [0, 1]. The input array 't' defines the time values.

    Parameters
    ----------
    t : np.ndarray
        Time array (independent variable).
    width : float
        Fraction of the period where the signal rises (in [0, 1]).

    Returns
    -------
    np.ndarray
        Array representing the sawtooth waveform.
    """
    return sp.signal.sawtooth(t, width)