import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from Signals import sawtooth

t = np.linspace(-10, 10, 10000)

plt.figure(1)
sawtooth1 = sawtooth(t, 1.0)
plt.plot(t, sawtooth1)
plt.title("Sawtooth 1")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(2)
sawtooth2 = sawtooth(t, 0.5)
plt.plot(t, sawtooth2)
plt.title("Sawtooth 2")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(2)
sawtooth3 = sawtooth(t, 0.0)
plt.plot(t, sawtooth3)
plt.title("Sawtooth 3")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()