import numpy as np
import matplotlib.pyplot as plt

# Given values
R = 100  # Resistance in ohms
C = 1e-6  # Capacitance in farads
T_square = 1e-3  # Period of the square wave (1 ms)
V_in_high = 5  # High voltage of the square wave
V_in_low = 0  # Low voltage of the square wave

# RC time constant
tau = R * C  # RC = 100 us, much smaller than T = 1 ms

# Time vector for simulation
t = np.linspace(0, 5 * T_square, 1000)  # Simulate for 5 periods of the square wave

# Input square wave signal
V_in = V_in_high * (np.mod(t, T_square) < T_square / 2) + \
       V_in_low * (np.mod(t, T_square) >= T_square / 2)

# Initialize the output voltage
V_out = np.zeros_like(t)

# Simulate the capacitor voltage
for i in range(1, len(t)):
    dt = t[i] - t[i - 1]
    dV = (V_in[i - 1] - V_out[i - 1]) / tau * dt
    V_out[i] = V_out[i - 1] + dV

# Plot the input and output voltages
plt.figure(figsize=(10, 6))
plt.plot(t * 1e3, V_in, label='Input Voltage (V_in)', color='blue')
plt.plot(t * 1e3, V_out, label='Output Voltage (V_out across capacitor)', color='red')
plt.title('Voltage Across Capacitor in RC Circuit (RC << T)')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.savefig('../figs/2.jpg')
plt.show()

