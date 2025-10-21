import numpy as np
import Signals as sn


### Sine signal tests
def test_sinewave():
    
    t, y = sn.generate_sine_wave(1, 2, 1)
    assert len(t) == 1000
    assert y[0] == 0

    t, y = sn.generate_sine_wave(5, 3, 1)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = sn.generate_sine_wave(1, 2, -1)
    assert len(t) == 0 and len(y) == 0

    t, y = sn.generate_sine_wave(5, 0, 1)
    assert np.allclose(y, 0)
    
    print("Hello the sine test worked!")
    return


### Pulse signal tests
def test_pulse():
    
    # Shape & type
    t = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    amp = 3.0
    y = sn.pulse(t, amp)
    assert isinstance(y, np.ndarray)
    assert y.shape == t.shape 

    # Values: inclusive window -0.5 <= t <= 0.5 -> amp, else 0
    expected = np.array([0.0, amp, amp, amp, 0.0])
    assert np.allclose(y, expected, atol=0.0)
    
    print("Hello the pulse test worked!")
    return


### Periodic pulse signal tests
def test_periodic_pulse():
    
    # Shape/type
    t = np.linspace(0.0, 2*np.pi, 1000, endpoint=False)
    y = sn.periodic_pulse(t, 0.3)
    assert isinstance(y, np.ndarray)
    assert y.shape == t.shape

    # Values are only -1 or +1
    assert np.allclose(np.abs(y), 1, atol=1e-6)
    
    # Duty-cycle extremes
    y0 = sn.periodic_pulse(t, 0.0)
    y1 = sn.periodic_pulse(t, 1.0)
    assert np.all(y0 == -1.0)
    assert np.all(y1 ==  1.0)

    # Simple periodicity: f(t) == f(t + 2π)
    t0 = np.array([0.25, 1.0, 2.0])
    assert np.allclose(sn.periodic_pulse(t0, 0.3), sn.periodic_pulse(t0 + 2*np.pi, 0.3))

    print("Hello the periodic pulse test worked!")
    return


### Sawtooth signal tests
def test_sawtooth():

    # Shape/type
    t = np.linspace(0.0, 2*np.pi, 1000, endpoint=False)
    y = sn.sawtooth(t, 0.5)
    assert isinstance(y, np.ndarray)
    assert y.shape == t.shape

    # Range should be within [-1, 1]
    assert y.min() >= -1.000001
    assert y.max() <=  1.000001

    # Simple periodicity: f(t) == f(t + 2π)
    t0 = np.array([0.2, 1.3, 2.1])
    assert np.allclose(sn.sawtooth(t0, 0.5), sn.sawtooth(t0 + 2*np.pi, 0.5))

    print("Hello the sawtooth test worked!")
    return


test_sinewave()
test_pulse()
test_periodic_pulse()
test_sawtooth()