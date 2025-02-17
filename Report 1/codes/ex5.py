import numpy as np
import matplotlib.pyplot as plt

# Parameters from the oscilloscope
frequency = 1e9  # 1 GHz
amplitude = 5    # 5V
period = 1e-3    # 1ms
phase_shift = np.pi / 4  # 45 degrees in radians

# Create time array
t = np.linspace(0, period, 1000)

# Generate the sine waves with a phase shift for wave2
wave1 = amplitude * np.sin(2 * np.pi * frequency * t)        # Channel 1
wave2 = amplitude * np.sin(2 * 2 * np.pi * frequency * t + phase_shift)  # Channel 2 with 45 degree phase shift

# Create figure with subplots
plt.style.use('default')
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

# Plot Channel 1
ax1.plot(t, wave1, 'g-', linewidth=1)
ax1.set_title('Channel 1')
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Voltage (V)')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.set_ylim(-6, 6)
ax1.spines['left'].set_color('black')
ax1.spines['bottom'].set_color('black')

# Plot Channel 2
ax2.plot(t, wave2, 'y-', linewidth=1)
ax2.set_title('Channel 2')
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Voltage (V)')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.set_ylim(-6, 6)
ax2.spines['left'].set_color('black')
ax2.spines['bottom'].set_color('black')

# Plot X-Y Mode (Lissajous)
ax3.plot(wave1, wave2, 'r-', linewidth=1)
ax3.set_title('X-Y Mode')
ax3.set_xlabel('Channel 1 (V)')
ax3.set_ylabel('Channel 2 (V)')
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.set_aspect('equal')
ax3.set_xlim(-6, 6)
ax3.set_ylim(-6, 6)
ax3.spines['left'].set_color('black')
ax3.spines['bottom'].set_color('black')

# Adjust layout
plt.tight_layout()

# Set background color for all plots to white
for ax in [ax1, ax2, ax3]:
    ax.set_facecolor('white')  # White background
    ax.grid(True, color='gray', linestyle=':', alpha=0.3)
plt.savefig('../figs/5.jpg')
plt.show()

# Print the parameters
print(f"Channel 1 Frequency: {frequency/1e9:.2f} GHz")
print(f"Channel 2 Frequency: {2*frequency/1e9:.2f} GHz")
print(f"Amplitude: ±{amplitude:.3f} V")
print(f"Period: {period*1000:.3f} ms")

