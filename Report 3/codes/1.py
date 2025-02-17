import numpy as np
import matplotlib.pyplot as plt

# Sample experimental data (replace these with your actual readings)
frequencies = np.array([100, 500, 1000, 1590, 3000, 5000, 10000])  # Removed last two frequencies
Vin = np.array([2.161] * len(frequencies))  # Input voltage in Volts
Vout = np.array([2.081, 1.921, 1.681, 1.441, 1.041, 0.7, 0.384])  # Removed last two readings

# RC values (replace with your actual R and C values)
R = 10000  # Resistance in Ohms
C = 1e-8  # Capacitance in Farads

# Generate a smooth frequency range for theoretical calculations
frequencies_smooth = np.logspace(2, 5, 1000)  # More points for a sharper curve
omega_smooth = 2 * np.pi * frequencies_smooth
H_theoretical_smooth = 1 / (1 + 1j * omega_smooth * R * C)

# Calculate magnitude for theoretical response
magnitude_theoretical_smooth = 20 * np.log10(np.abs(H_theoretical_smooth))

# Theoretical phase calculation: -tan⁻¹(ωRC)
phase_theoretical_smooth = -np.arctan(omega_smooth * R * C) * (180 / np.pi)

# Experimental magnitude calculation
magnitude_experimental = 20 * np.log10(Vout / Vin)

# Experimental phase correction
delta_t = np.array([-9.8000e-05, -9.4892e-05, -8.7783e-05, -7.6068e-05, -5.5457e-05, -4.1191e-05, -2.4488e-05])
phase_experimental = delta_t * (2 * np.pi * frequencies) * (180 / np.pi)  # Convert to degrees

# Plotting the Bode plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Magnitude plot
ax1.semilogx(frequencies, magnitude_experimental, 'yo-', label='Experimental Magnitude')
ax1.semilogx(frequencies_smooth, magnitude_theoretical_smooth, label='Theoretical Magnitude')  # Scatter plot for sharp points
ax1.set_title('Bode Plot - Magnitude')
ax1.set_ylabel('Magnitude (dB)')
ax1.grid(which='both', axis='both')
ax1.legend()

# Phase plot
ax2.semilogx(frequencies, phase_experimental, 'ro-', label='Experimental Phase')
ax2.semilogx(frequencies_smooth, phase_theoretical_smooth, label='Theoretical Phase')  # Scatter plot for sharp points
ax2.set_title('Bode Plot - Phase')
ax2.set_ylabel('Phase (degrees)')
ax2.set_xlabel('Frequency (Hz)')
ax2.grid(which='both', axis='both')
ax2.legend()

plt.tight_layout()
plt.savefig("../figs/1phase.png")
plt.show()

