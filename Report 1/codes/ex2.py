import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters from the oscilloscope
frequency = 1e9  # 1 GHz
amplitude = 5    # 5V
period = 1e-3    # 1ms
phase_diff = 90  # 90 degrees phase difference

# Create time array
t = np.linspace(0, period, 1000)

# Generate the two sine waves with 90-degree phase difference
wave1 = amplitude * np.sin(2 * np.pi * frequency * t)  # Channel 1
wave2 = amplitude * np.sin(2 * np.pi * frequency * t + np.deg2rad(phase_diff))  # Channel 2

# Create figure with subplots
fig = plt.figure(figsize=(15, 5))

# Plot first sine wave
ax1 = fig.add_subplot(131)
ax1.plot(t, wave1, 'b-', label='Channel 1 (0°)')
ax1.set_title('Sine Wave - Channel 1')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
ax1.grid(True)
ax1.legend()

# Plot second sine wave (90° shifted)
ax2 = fig.add_subplot(132)
ax2.plot(t, wave2, 'g-', label='Channel 2 (90°)')
ax2.set_title('Sine Wave - Channel 2')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Voltage (V)')
ax2.grid(True)
ax2.legend()

# Plot Lissajous figure (X-Y mode)
ax3 = fig.add_subplot(133)
ax3.plot(wave1, wave2, 'r-', label='X-Y Mode')
ax3.set_title('Lissajous Figure (Circle)')
ax3.set_xlabel('Channel 1 (V)')
ax3.set_ylabel('Channel 2 (V)')
ax3.grid(True)
ax3.legend()

# Make the circle look circular by setting equal aspect ratio
ax3.set_aspect('equal')

# Set limits for better visualization
ax3.set_xlim(-amplitude*1.2, amplitude*1.2)
ax3.set_ylim(-amplitude*1.2, amplitude*1.2)

plt.tight_layout()
plt.savefig('../figs/2.jpg')
plt.show()

# Calculate and print key parameters
print(f"Signal Parameters:")
print(f"Frequency: {frequency/1e9:.2f} GHz")
print(f"Period: {period*1e3:.2f} ms")
print(f"Peak-to-peak voltage: {2*amplitude:.2f} V")
print(f"Phase difference: {phase_diff} degrees")


