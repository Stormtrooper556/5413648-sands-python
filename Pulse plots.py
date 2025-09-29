import matplotlib.pyplot as plt
import numpy as np
import scipy as sp #Or just import the signal module from scipy: from scipy import signal. And proceed with signal.square() e.g.
from Signals import pulse

t = np.linspace(-5, 5, 10000)

plt.figure(1)
single_pulse = pulse(t-2, 1.0)
plt.plot(t, single_pulse)
plt.title("Single pulse")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(2)
multi_pulse = pulse(t/4, 2.0) + pulse(t-3, 1.0)
plt.plot(t, multi_pulse)
plt.title("Multi pulse")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


t2 = np.linspace(-10, 10, 10000)

plt.figure(3)
periodic_pulse = sp.signal.square(t2, 0.5) #square(t, duty=0.5). The square wave has a period 2*pi, has value +1 from 0 to 2*pi*duty and -1 from 2*pi*duty to 2*pi. duty must be in the interval [0,1].
plt.plot(t2, periodic_pulse)
plt.title("Periodic pulse")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

