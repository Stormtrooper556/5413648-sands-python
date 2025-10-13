import numpy as np
import Signals as sn

### Sine signal tests

def test_sinewave():
    t, y = sn.generate_sine_wave(1, 2, 1)
    assert len(t) == 1000

    t, y = sn.generate_sine_wave(1, 2, 1)
    assert y[0] == 0

    t, y = sn.generate_sine_wave(5, 3, 1)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = sn.generate_sine_wave(1, 2, -1)
    assert len(t) == 0 and len(y) == 0

    t, y = sn.generate_sine_wave(5, 0, 1)
    assert np.allclose(y, 0)
    
    print("Hello bastard")
    return

test_sinewave()