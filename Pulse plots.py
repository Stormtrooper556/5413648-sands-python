import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from Signals import pulse
from Signals import periodic_pulse

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
periodic_pulse = periodic_pulse(t2, 0.5)
plt.plot(t2, periodic_pulse)
plt.title("Periodic pulse")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

