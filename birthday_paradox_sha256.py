import numpy as np
import matplotlib.pyplot as plt

N = 2**256
k = np.logspace(0, 40, 500, base=2)

# Collision probability
approx_collision_prob = 1 - np.exp(-(k**2) / (2 * N))

# Harmonic bounce (visual only)
diminishing_harmonic = np.abs(np.sin(k / 5)) / np.sqrt(k)
diminishing_harmonic = np.clip(diminishing_harmonic, 0, 1)

# Theoretical threshold for 50% collision
threshold_k = np.sqrt(2 * N * np.log(2))
threshold_value = 0.5

# Plot
plt.figure(figsize=(12, 6))
plt.plot(k, approx_collision_prob, label='Approx. Collision Probability', color='green')
plt.plot(k, diminishing_harmonic, label='Diminishing Harmonic Bounce', color='purple', linestyle='--')
plt.axhline(0.5, color='gray', linestyle=':', label='50% Threshold')
plt.axvline(threshold_k, color='gray', linestyle=':', label=f'k ≈ 2^128')

# Annotate
plt.scatter(threshold_k, threshold_value, color='red')
plt.annotate(f'~50% at k ≈ 2^128',
             xy=(threshold_k, threshold_value),
             xytext=(threshold_k * 10, threshold_value - 0.1),
             arrowprops=dict(arrowstyle='->', color='red'),
             color='red',
             fontsize=10)

plt.xscale('log')
plt.title('SHA-256: Birthday Collision Probability with Harmonic Bounce')
plt.xlabel('Number of Hashes (k, log scale)')
plt.ylabel('Probability / Amplitude')
plt.grid(True, which="both", ls='--')
plt.legend()
plt.ylim(0, 1.1)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

N = 2**256
k = np.logspace(0, 130, 500, base=2)  # extend k to cover 2^128

# Collision probability
approx_collision_prob = 1 - np.exp(-(k**2) / (2 * N))

# Harmonic bounce (visual only)
diminishing_harmonic = np.abs(np.sin(k / 5)) / np.sqrt(k)
diminishing_harmonic = np.clip(diminishing_harmonic, 0, 1)

# Theoretical threshold for 50% collision
threshold_k = np.sqrt(2 * N * np.log(2))
threshold_value = 0.5

# Plot
plt.figure(figsize=(12, 6))
plt.plot(k, approx_collision_prob, label='Approx. Collision Probability', color='green')
plt.plot(k, diminishing_harmonic, label='Diminishing Harmonic Bounce', color='purple', linestyle='--')
plt.axhline(threshold_value, color='gray', linestyle=':', label='50% Threshold')
plt.axvline(threshold_k, color='gray', linestyle=':', label=f'k ≈ 2^128')

# Annotate
plt.scatter(threshold_k, threshold_value, color='red')
plt.annotate(f'~50% at k ≈ 2^128',
             xy=(threshold_k, threshold_value),
             xytext=(threshold_k * 1.2, threshold_value - 0.1),
             arrowprops=dict(arrowstyle='->', color='red'),
             color='red',
             fontsize=10)

plt.xscale('log')
plt.title('SHA-256: Birthday Collision Probability with Harmonic Bounce')
plt.xlabel('Number of Hashes (k, log scale)')
plt.ylabel('Probability / Amplitude')
plt.grid(True, which="both", ls='--')
plt.legend()
plt.ylim(0, 0.6)  # limit y-axis to just above 50%

# Use float limit safely for xlim
plt.xlim(1, float(2**130))  # explicitly cast to float

plt.show()

