import matplotlib.pyplot as plt
import numpy as np
from Signals import generate_sine_wave

# Parameters
frequency = 5          # Hz
duration = 2           # seconds
sample_rate = 100      # samples per second

# Generate the sine wave
t, waveform = generate_sine_wave(frequency, duration, sample_rate)

# Print the first 10 samples
print(waveform[:10])

# Plot the sine wave
plt.plot(t, waveform)
plt.title("5 Hz Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()