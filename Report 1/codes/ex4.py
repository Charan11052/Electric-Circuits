import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters from the oscilloscope
frequency = 1e6    # 1 MHz
amplitude = 5      # 5V
period = 1.0      # 1ms
phase1 = 0        # 0 degrees for channel 1
phase2 = 45       # 45 degrees for channel 2
phase2_rad = np.deg2rad(phase2)  # Convert to radians

# Create time array
t = np.linspace(0, period, 1000)

# Generate the two sine waves
wave1 = amplitude * np.sin(2 * np.pi * frequency * t + phase1)
wave2 = amplitude * np.sin(2 * np.pi * frequency * t + phase2_rad)

# Create figure with subplots
fig = plt.figure(figsize=(15, 5))

# Plot first sine wave
ax1 = fig.add_subplot(131)
ax1.plot(t, wave1, 'b-', label='Channel 1')
ax1.set_title('Sine Wave - Channel 1 (0°)')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
ax1.grid(True)
ax1.legend()

# Plot second sine wave
ax2 = fig.add_subplot(132)
ax2.plot(t, wave2, 'g-', label='Channel 2')
ax2.set_title('Sine Wave - Channel 2 (45°)')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Voltage (V)')
ax2.grid(True)
ax2.legend()

# Plot Lissajous figure (X-Y mode)
ax3 = fig.add_subplot(133)
ax3.plot(wave1, wave2, 'r-', label='X-Y Mode')
ax3.set_title('Lissajous Figure (45° Phase Shift)')
ax3.set_xlabel('Channel 1 (V)')
ax3.set_ylabel('Channel 2 (V)')
ax3.grid(True)
ax3.legend()
ax3.set_xlim(-amplitude-1, amplitude+1)
ax3.set_ylim(-amplitude-1, amplitude+1)

plt.tight_layout()
plt.savefig('../figs/4.jpg')
plt.show()

# Calculate and print key parameters
print(f"Signal Parameters:")
print(f"Frequency: {frequency/1e3:.3f} kHz")
print(f"Period: {period*1e3:.2f} ms")
print(f"Peak-to-peak voltage: {2*amplitude:.2f} V")
print(f"Channel 1 phase: {phase1} degrees")
print(f"Channel 2 phase: {phase2} degrees")
print(f"Phase difference: {phase2-phase1} degrees")
print(f"Load: 50 ohm")
