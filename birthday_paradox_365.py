import matplotlib.pyplot as plt

# Parameters
N = 365  # Number of unique values (e.g., days in a year)
k = np.arange(1, 101)  # Sample size (number of people/hashes)

# Approximate collision probability using Taylor approximation
approx_collision_prob = 1 - np.exp(-(k * (k - 1)) / (2 * N))

# Diminishing harmonic bounce (illustrative only)
diminishing_harmonic = np.abs(np.sin(k / 5)) * (1 / k**0.5)


# Find the index where the collision probability exceeds 50%
threshold_index = np.argmax(approx_collision_prob >= 0.5)
threshold_k = k[threshold_index]
threshold_value = approx_collision_prob[threshold_index]


plt.figure(figsize=(12, 6))
plt.plot(k, approx_collision_prob, label='Approx. Collision Probability', color='green')
plt.plot(k, diminishing_harmonic, label='Diminishing Harmonic Bounce', color='purple', linestyle='--')
plt.axhline(0.5, color='gray', linestyle=':', label='50% Threshold')
plt.axvline(threshold_k, color='gray', linestyle=':', label=f'k ≈ {threshold_k}')

# Annotate the 50% crossing point
plt.scatter(threshold_k, threshold_value, color='red')
plt.annotate(f'~50% at k={threshold_k}',
             xy=(threshold_k, threshold_value),
             xytext=(threshold_k + 5, threshold_value - 0.1),
             arrowprops=dict(arrowstyle='->', color='red'),
             color='red',
             fontsize=10)

plt.title('Birthday Paradox: Collision Probability with Harmonic Bounce')
plt.xlabel('Number of People / Hashes (k)')
plt.ylabel('Probability / Amplitude')
plt.grid(True)
plt.legend()
plt.ylim(0, 1.1)
plt.show()

