import numpy as np
import matplotlib.pyplot as plt

# Given values
R = 100  # Resistance in ohms
C = 1e-6  # Capacitance in farads
T = R * C  # Time constant
freq = 1 / T  # Frequency where RC = T
V_in_high = 5  # High voltage of the square wave
V_in_low = 0  # Low voltage of the square wave
time_period = 1 / freq  # Period of the square wave

# Time vector
t = np.linspace(0, 5 * time_period, 1000)  # 5 cycles of the square wave

# Input square wave signal
V_in = V_in_high * (np.mod(t, time_period) < time_period / 2) + \
       V_in_low * (np.mod(t, time_period) >= time_period / 2)

# Initialize the output voltage
V_out = np.zeros_like(t)

# Simulate the capacitor voltage
for i in range(1, len(t)):
    dt = t[i] - t[i - 1]
    dV = (V_in[i - 1] - V_out[i - 1]) / (R * C) * dt
    V_out[i] = V_out[i - 1] + dV

# Plot the input and output voltages
plt.figure(figsize=(10, 6))
plt.plot(t, V_in, label='Input Voltage (V_in)', color='blue')
plt.plot(t, V_out, label='Output Voltage (V_out across capacitor)', color='red')
plt.title('Voltage Across Capacitor in RC Circuit')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.savefig('../figs/1.jpg')
plt.show()


