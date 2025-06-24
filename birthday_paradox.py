import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Function to calculate exact collision probability
def collision_probability_exact(k, N):
    """Exact formula: 1 - exp(-k(k-1)/(2N))"""
    return 1 - np.exp(-(k * (k - 1)) / (2 * N))

# Taylor series approximation functions
def taylor_series_exp(x, terms=10):
    """Taylor series for e^x around x=0"""
    result = 0
    for n in range(terms):
        result += (x**n) / factorial(n)
    return result

def collision_probability_taylor(k, N, terms=10):
    """Taylor series approximation of collision probability"""
    x = -(k * (k - 1)) / (2 * N)
    exp_approx = taylor_series_exp(x, terms)
    return 1 - exp_approx

def collision_probability_first_order(k, N):
    """First-order Taylor approximation: P ≈ k(k-1)/(2N)"""
    return (k * (k - 1)) / (2 * N)

def collision_probability_second_order(k, N):
    """Second-order Taylor approximation"""
    x = (k * (k - 1)) / (2 * N)
    return x - (x**2) / 2

# Settings
k_range = np.arange(1, 101)
k_extended = np.arange(1, 1001)  # Extended range for SHA-256

# Case 1: N = 365 (birthday paradox)
print("=== BIRTHDAY PARADOX (N = 365) ===")
N_birthday = 365

# Calculate probabilities using different methods
prob_exact = collision_probability_exact(k_range, N_birthday)
prob_taylor_5 = collision_probability_taylor(k_range, N_birthday, terms=5)
prob_taylor_10 = collision_probability_taylor(k_range, N_birthday, terms=10)
prob_first_order = collision_probability_first_order(k_range, N_birthday)
prob_second_order = collision_probability_second_order(k_range, N_birthday)

# Find 50% threshold
threshold_idx = np.argmax(prob_exact >= 0.5)
threshold_k = k_range[threshold_idx]
print(f"50% threshold reached at k = {threshold_k} people")
print(f"Exact probability at k={threshold_k}: {prob_exact[threshold_idx]:.4f}")
print(f"First-order approx at k={threshold_k}: {prob_first_order[threshold_idx]:.4f}")
print(f"Second-order approx at k={threshold_k}: {prob_second_order[threshold_idx]:.4f}")

# Plot birthday paradox with Taylor approximations
plt.figure(figsize=(15, 10))

# Main comparison plot
plt.subplot(2, 2, 1)
plt.plot(k_range, prob_exact, 'b-', linewidth=2, label='Exact: 1-exp(-k(k-1)/(2N))')
plt.plot(k_range, prob_first_order, 'r--', linewidth=2, label='1st Order: k(k-1)/(2N)')
plt.plot(k_range, prob_second_order, 'g--', linewidth=2, label='2nd Order: x - x²/2')
plt.plot(k_range, prob_taylor_5, 'm:', linewidth=2, label='Taylor Series (5 terms)')
plt.axhline(0.5, color='gray', linestyle=':', alpha=0.7, label='50% Threshold')
plt.axvline(threshold_k, color='gray', linestyle=':', alpha=0.7)
plt.scatter(threshold_k, prob_exact[threshold_idx], color='red', s=100, zorder=5)
plt.annotate(f'50% at k={threshold_k}', 
             xy=(threshold_k, 0.5), xytext=(threshold_k+10, 0.3),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=10, color='red')
plt.title('Birthday Paradox: Exact vs Taylor Approximations')
plt.xlabel('Number of People (k)')
plt.ylabel('Collision Probability')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 100)
plt.ylim(0, 1)

# Error analysis
plt.subplot(2, 2, 2)
error_first = np.abs(prob_exact - prob_first_order)
error_second = np.abs(prob_exact - prob_second_order)
error_taylor = np.abs(prob_exact - prob_taylor_5)
plt.semilogy(k_range, error_first, 'r-', label='1st Order Error')
plt.semilogy(k_range, error_second, 'g-', label='2nd Order Error')
plt.semilogy(k_range, error_taylor, 'm-', label='Taylor Series Error')
plt.title('Approximation Errors (Log Scale)')
plt.xlabel('Number of People (k)')
plt.ylabel('Absolute Error')
plt.legend()
plt.grid(True, alpha=0.3)

# Case 2: SHA-256 analysis
print("\n=== SHA-256 HASH COLLISION (N = 2^256) ===")
N_sha256 = 2**256
print(f"SHA-256 hash space size: 2^256 ≈ {N_sha256:.2e}")

# For SHA-256, we need much larger k values to see meaningful probabilities
k_sha256 = np.logspace(0, 40, 1000)  # From 1 to 10^40

prob_sha256_exact = collision_probability_exact(k_sha256, N_sha256)
prob_sha256_first = collision_probability_first_order(k_sha256, N_sha256)

# Find where probability reaches various thresholds
thresholds = [1e-10, 1e-6, 0.01, 0.5]
threshold_ks = []
for thresh in thresholds:
    idx = np.argmax(prob_sha256_exact >= thresh)
    if prob_sha256_exact[idx] >= thresh:
        threshold_ks.append(k_sha256[idx])
        print(f"{thresh*100}% threshold at k ≈ {k_sha256[idx]:.2e}")
    else:
        threshold_ks.append(None)

# SHA-256 collision probability plot
plt.subplot(2, 2, 3)
plt.loglog(k_sha256, prob_sha256_exact, 'b-', linewidth=2, label='Exact Formula')
plt.loglog(k_sha256, prob_sha256_first, 'r--', linewidth=2, label='First-Order Approx')
for i, (thresh, k_thresh) in enumerate(zip(thresholds, threshold_ks)):
    if k_thresh is not None:
        plt.axhline(thresh, color='gray', linestyle=':', alpha=0.7)
        plt.axvline(k_thresh, color='gray', linestyle=':', alpha=0.7)
        plt.scatter(k_thresh, thresh, s=50, zorder=5)
plt.title('SHA-256: Collision Probability vs Number of Hashes')
plt.xlabel('Number of Hashes (k)')
plt.ylabel('Collision Probability')
plt.legend()
plt.grid(True, alpha=0.3)

# Practical comparison
plt.subplot(2, 2, 4)
# Show both on same scale for small k values
k_small = np.arange(1, 101)
prob_birthday_small = collision_probability_exact(k_small, N_birthday)
prob_sha256_small = collision_probability_exact(k_small, N_sha256)

plt.semilogy(k_small, prob_birthday_small, 'b-', linewidth=2, label='Birthday (N=365)')
plt.semilogy(k_small, prob_sha256_small, 'r-', linewidth=2, label='SHA-256 (N=2^256)')
plt.title('Collision Probability Comparison (Log Scale)')
plt.xlabel('Number of Items (k)')
plt.ylabel('Collision Probability (Log Scale)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Theoretical analysis
print("\n=== THEORETICAL ANALYSIS ===")
print("Taylor Series Expansion of 1 - e^(-x) around x=0:")
print("1 - e^(-x) = x - x²/2! + x³/3! - x⁴/4! + ...")
print("where x = k(k-1)/(2N)")
print("\nFor birthday paradox (N=365):")
print("- First-order approximation works well for small k")
print("- Second-order needed for k > 20")
print("- Full series converges rapidly")
print("\nFor SHA-256 (N=2^256):")
print("- First-order approximation excellent for reasonable k values")
print(f"- Need k ≈ 2^128 ≈ {2**128:.2e} for 50% collision probability")
print("- This is computationally infeasible")

# Calculate birthday paradox threshold more precisely
def find_exact_threshold(N, target_prob=0.5):
    """Find exact k where collision probability reaches target"""
    # Using the exact formula and solving numerically
    k = 1
    while collision_probability_exact(k, N) < target_prob:
        k += 1
    return k

exact_birthday_threshold = find_exact_threshold(N_birthday)
print(f"\nExact birthday paradox threshold: {exact_birthday_threshold} people")

# Show approximation quality at threshold
x_thresh = (exact_birthday_threshold * (exact_birthday_threshold - 1)) / (2 * N_birthday)
print(f"At threshold, x = k(k-1)/(2N) = {x_thresh:.4f}")
print(f"First-order approx: {x_thresh:.4f}")
print(f"Second-order approx: {x_thresh - x_thresh**2/2:.4f}")
print(f"Exact (1-e^(-x)): {1 - np.exp(-x_thresh):.4f}")

"""
=== BIRTHDAY PARADOX (N = 365) ===
50% threshold reached at k = 23 people
Exact probability at k=23: 0.5000
First-order approx at k=23: 0.6932
Second-order approx at k=23: 0.4529

=== SHA-256 HASH COLLISION (N = 2^256) ===
SHA-256 hash space size: 2^256 ≈ 1.16e+77
1e-08% threshold at k ≈ 5.17e+33
9.999999999999999e-05% threshold at k ≈ 5.20e+35
1.0% threshold at k ≈ 5.22e+37
50.0% threshold at k ≈ 4.35e+38

=== THEORETICAL ANALYSIS ===
Taylor Series Expansion of 1 - e^(-x) around x=0:
1 - e^(-x) = x - x²/2! + x³/3! - x⁴/4! + ...
where x = k(k-1)/(2N)

For birthday paradox (N=365):
- First-order approximation works well for small k
- Second-order needed for k > 20
- Full series converges rapidly

For SHA-256 (N=2^256):
- First-order approximation excellent for reasonable k values
- Need k ≈ 2^128 ≈ 3.40e+38 for 50% collision probability
- This is computationally infeasible

Exact birthday paradox threshold: 23 people
At threshold, x = k(k-1)/(2N) = 0.6932
First-order approx: 0.6932
Second-order approx: 0.4529
Exact (1-e^(-x)): 0.5000
""" 
