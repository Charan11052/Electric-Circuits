import numpy as np
import matplotlib.pyplot as plt

# Sample experimental data (replace these with your actual readings)
frequencies = np.array([100, 500, 1000, 1590, 3000, 5000, 10000])  # Frequencies in Hz
Vin = np.array([2.161] * len(frequencies))  # Input voltage in Volts
Vout = np.array([2.052, 1.498, 1.041, 0.687, 0.362, 0.184, 0.071])  # Output voltage in Volts

# RC values (replace with your actual R and C values)
R = 10000  # Resistance in Ohms
C = 1e-8  # Capacitance in Farads

# Calculate the theoretical transfer function
omega = 2 * np.pi * frequencies
H_theoretical = (1 / (1 + (1j * omega * R * C)**2 + 3 * 1j * omega * R * C))

# Calculate theoretical phase using the new formula
theoretical_phase = -np.arctan(3 * omega * R * C / (1 - (omega * R * C)**2)) * (180 / np.pi)

# Calculate magnitude and phase for theoretical response
magnitude_theoretical = 20 * np.log10(np.abs(H_theoretical))

# Calculate experimental magnitude and phase
magnitude_experimental = 20 * np.log10(Vout / Vin)
delta_t = np.array([-3.0324e-4, -2.6241e-4, -2.0392e-4, -1.6217e-4, 6.2952e-5, 2.6612e-5, 7.8945e-6])
experimental_phase =delta_t * (2 * np.pi * frequencies) * (180 / np.pi) 

# Generate a smooth curve for theoretical phase
frequencies_smooth = np.logspace(2, 5, 100)  # Smooth frequency range from 100 Hz to 100000 Hz
omega_smooth = 2 * np.pi * frequencies_smooth
H_theoretical_smooth = (1 / (1 + (1j * omega_smooth * R * C)**2 + 3 * 1j * omega_smooth * R * C))
theoretical_phase_smooth = -np.arctan(3 * omega_smooth * R * C / (1 - (omega_smooth * R * C)**2)) * (180 / np.pi)
magnitude_theoretical_smooth = 20 * np.log10(np.abs(H_theoretical_smooth))

# Plotting the Bode plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Magnitude plot
ax1.semilogx(frequencies, magnitude_experimental, 'yo-', label='Experimental Magnitude')
ax1.semilogx(frequencies_smooth, magnitude_theoretical_smooth, label='Theoretical Magnitude')
ax1.set_title('Bode Plot - Magnitude')
ax1.set_ylabel('Magnitude (dB)')
ax1.grid(which='both', axis='both')
ax1.legend()

# Phase plot
ax2.semilogx(frequencies, experimental_phase, 'ro', label='Experimental Phase')
ax2.semilogx(frequencies_smooth, theoretical_phase_smooth, label='Theoretical Phase')
ax2.set_title('Bode Plot - Phase')
ax2.set_ylabel('Phase (degrees)')
ax2.set_xlabel('Frequency (Hz)')
ax2.grid(which='both', axis='both')
ax2.legend()

plt.tight_layout()
plt.savefig("../figs/2phase.png")
plt.show()
