# 📘 Birthday Paradox and Harmonic Bounce

On the Birthday Paradox and how it relates to harmonics, and then plot a harmonic graph (bouncing ball style) that intuitively visualizes the probability growth curve.

The Birthday Paradox refers to the counterintuitive probability that in a group of just 23 people, there's a > 50% chance that at least 2 share the same birthday.

Let:
- 𝑁: number of possible birthdays (or hash outputs) → e.g., 365 days or $$/ 2^{256} /$$ for SHA-256.
- 𝑘: number of samples (people/hashes).
- 𝑃(𝑘;𝑁): probability of no collision after 𝑘 samples:

$$\
P(k; N) = \prod_{i=0}^{k-1} \left(1 - \frac{i}{N}\right)
\$$

The probability of **at least 1 collision**:

$$\
P_{\text{collision}}(k; N) = 1 - \prod_{i=0}^{k-1} \left(1 - \frac{i}{N}\right)
\$$

---

## ⚡ Taylor Approximation

For large \( N \), we use a Taylor approximation:

$$\
P_{\text{collision}}(k; N) \approx 1 - e^{-\frac{k(k-1)}{2N}}
\$$

For \( N = 365 \), the probability exceeds **50%** at:

$$\
k \approx 23
\$$

---

## 🎯 Goal

We want to estimate the probability of a birthday collision using the Taylor expansion of the logarithm and exponential functions.

To prove the Birthday Paradox using a Taylor series and calculus, we'll approximate the probability of no collisions when selecting k samples uniformly at random from a set of size N, and use the Taylor expansion of the exponential function.

We aim to find:

$$\
P(\text{no collision}) \approx e^{-\frac{k(k-1)}{2N}}
\$$

and solve:

$$\
P(\text{collision}) = 1 - P(\text{no collision}) \approx 0.5 \Rightarrow k \approx \sqrt{2N \ln 2}
\$$

---

## 🎲 Setup

- Total possible values: `N` (e.g., 365 birthdays)
- We randomly select `k` values **without replacement**
- Interested in the **probability of no collisions**

---

## 🧮 Exact Expression

The probability of no collisions is:

$$\
P_{\text{no collision}} = \frac{N}{N} . \frac{N-1}{N} . \frac{N-2}{N} ... . \frac{N- k+1}{N} 
\$$

which is:

$$\
P_{\text{no collision}} = \prod_{i=0}^{k-1} \left(1 - \frac{i}{N} \right)
\$$

Take the natural logarithm:

$$\
\ln \ P_{\text{no collision}} = \sum_{i=0}^{k-1} \ln\left(1 - \frac{i}{N} \right)
\$$

---

## 🧩 Step 1: Taylor Expand `ln(1 - x)`

Using the Taylor series for \( \ln(1 - x) \):

$$\
\ln(1 - x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \dots \quad \text{(for } |x| < 1)
\$$

Apply to each term:

$$\
\ln\left(1 - \frac{i}{N} \right) \approx -\frac{i}{N} - \frac{1}{2} \left( \frac{i}{N} \right)^2 + \dots
\$$

Summing over all `i`:

$$\
\ln P_{\text{no collision}} \approx -\sum_{i=0}^{k-1} \frac{i}{N} = -\frac{1}{N} \sum_{i=0}^{k-1} i = -\frac{k(k-1)}{2N}
\$$

Exponentiating both sides:

$$\
P_{\text{no collision}} \approx e^{-\frac{k(k-1)}{2N}} \approx e^{-\frac{k^2}{2N}}
\$$

(for large `k`, we approximate \( k(k-1) \approx k^2 \))

---

## 📐 Step 2: Find When Collision Probability is ~50%

We want:

$$\
1 - e^{-k^2 / (2N)} \approx 0.5 \Rightarrow e^{-k^2 / (2N)} = 0.5
\$$

Taking logarithm:

$$\
-\frac{k^2}{2N} = \ln(0.5) = -\ln 2
\Rightarrow \frac{k^2}{2N} = \ln 2
\Rightarrow k = \sqrt{2N \ln 2}
\$$

---

## ✅ 

- The **birthday paradox** arises because collision probability grows quickly
- Using Taylor series on `ln(1 - x)`, we derived:

$$\
P_{\text{no collision}} \approx e^{-k^2 / (2N)} \Rightarrow k \approx \sqrt{2N \ln 2}
\$$

---

## 📌 Real-World Example

For `N = 365` (days in a year):

$$\
k \approx \sqrt{2 \cdot 365 \cdot \ln 2} \approx \sqrt{505.6} \approx 22.5
\$$

So, **only 23 people** are needed for a **50% chance** that two share the same birthday.


For SHA-256:

We often hear: 
$$\ 𝑘 \approx \sqrt{2^n} = 2^{n/2} \$$

$$\ 𝑘 ≈ 2^{256/2} = 2^{128} \$$

This is a rule-of-thumb estimate and comes from ignoring constants.

🧮 The Exact Formula:
The more precise version is:

For $$\ N = 2^{256} \$$ (SHA 256):

$$\
k \approx \sqrt{2 \cdot 2^{256} \cdot \ln 2} \approx 4.006518692980012e+38
\$$

bits: $$\ \ln \ k \approx 88.88615624166214 \$$

| Concept               | Value                                                           |
| --------------------- | --------------------------------------------------------------- |
| Approx birthday bound | $k \approx 2^{128}$                                             |
| Exact birthday bound  | $k = \sqrt{2^{256} \cdot 2\ln 2} = 2^{128} \cdot \sqrt{2\ln 2}$ |
| Extra multiplier      | $\sqrt{2 \ln 2} \approx 1.177$                                  |
| So log becomes        | $\ln(k) \approx 128 \cdot \ln 2 + \ln(1.177) \approx 89.82$     |



## 🔁 Diminishing Harmonic Bounce

To simulate a “bouncing ball” decay effect, we define:

$$\
\text{bounce}(k) = |\sin(k / 5)| \cdot \frac{1}{\sqrt{k}}
\$$

This is illustrative only and does **not** reflect real collision probability—it’s used for visualizing intuition fluctuation as probability grows.



> ⚠️ Note: This is **not** the actual birthday paradox probability—just a visualization aid for intuition.

### 🔁 Intuition: Fluctuating Probability and Harmonic Decay

- The sine term `sin(k/5)` introduces **oscillations**. These simulate the mental "surprise bounce" we feel as the probability of a birthday collision increases.
- The `(1/√k)` term introduces **decay**, reflecting that as `k` (number of people) increases, each new person adds **less new information** or surprise – the more people you add, the smaller the per-person contribution to your feeling of uncertainty. This is like a diminishing bounce—each new addition is less surprising.
- Together, these form a **damped oscillation**: a gradually flattening wave.

Think of this function as simulating a mental "bounce"—your intuitive surprise at a match increases sharply early on, then levels off.
- Early on, each new person significantly increases the chance of a collision.
- Later additions contribute less — the surprise “bounces” fade.

### 🧮 Taylor Series Expansion

We use Taylor series to examine the sine component:
```
sin(x) = x - x³/3! + x⁵/5! - ...
```

Substitute `x = k/5`:
```
sin(k/5) ≈ (k/5) - (k/5)³/6 + ...
= (k/5) - (k³ / 125) / 6 + ...
= (k/5) - (k³ / 750) + ...
```

Now multiply this by `1/√k` (the decay term). This implies the bounce function is approximately:

$$\
bounce(k) ≈ \lvert \frac{k}{5} - \frac{ (k/5)^3 }{6}  + ... \rvert . ​\frac{1}{ \sqrt {k}}
\$$

```
bounce(k) ≈ |(k/5 - k³/750 + …) * (1/√k)|
= |(√k / 5) - (k^(5/2) / 750) + …|
```

So as `k` grows:

- The `√k` term grows slowly.
- But the `k^(5/2)` term grows faster and **subtracts**, leading to **damping**.
- This mirrors how the **intuition** for collisions starts large but **diminishes** as we expect duplicates.

### 🔍 Conceptual Summary

| Component             | Meaning                                                       |
|-----------------------|---------------------------------------------------------------|
| `|sin(k/5)|`           | Oscillates — models surprise or intuitive “collision bounces” |
| `(1 / √k)`            | Damps the amplitude — each new person adds less surprise      |
| Taylor of `sin(x)`    | Helps show how bounce grows then flattens                    |
| Bounce curve shape     | Mimics intuition: rising surprise → flattening expectation    |

This function is **not** rigorous probability, but gives a **calculus-based visualization** of how our **intuition** behaves across increasing `k` in the birthday paradox.

---


| Concept                             | Purpose                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| **Taylor series of $\ln(1 - x)$**   | Used to approximate collision probability in the birthday paradox            |
| **Taylor series of $\sin(x)$**      | Used to simulate oscillating intuition as people are added                   |
| **$\frac{1}{\sqrt{k}}$**            | Models diminishing intuition — newer additions matter less                   |
| **Product of terms vs sum of logs** | Switch from discrete product to continuous approximation                     |
| **Bounce function**                 | An **illustrative model** for how our intuition “bounces” before stabilizing |


## 🔐 SHA-256 and the Birthday Bound

For a cryptographic hash function like **SHA-256**, the number of unique outputs is:

$$\
N = 2^{256}
\$$

To estimate the number of hashes \( k \) needed for a **50% chance of at least one collision**, we use the birthday bound:

$$\
P_{\text{collision}}(k; N) \approx 1 - e^{-k^2 / (2N)}
\$$

Setting \( P_{\text{collision}} = 0.5 \):

$$\
0.5 = 1 - e^{-k^2 / (2N)} \Rightarrow e^{-k^2 / (2N)} = 0.5
\$$

$$\
-\frac{k^2}{2N} = \ln(0.5) = -\ln(2) \Rightarrow \frac{k^2}{2N} = \ln(2)
\$$

$$\
k = \sqrt{2N \ln(2)} \approx 1.1774 \cdot \sqrt{N}
\$$

### ✅ For SHA-256:

$$\
k \approx 1.1774 \cdot \sqrt{2^{256}} = 1.1774 \cdot 2^{128}
\$$

$$\
k \approx 1.1774 \cdot 3.4 \times 10^{38} \approx 4.0 \times 10^{38}
\$$

---

### 🔐 Insight:

- You would need to compute **~\( $$\ 2^{128} \$$ \)** SHA-256 hashes to reach a 50% probability of collision.
- This number is **astronomically large**, making SHA-256 **collision-resistant** in practical scenarios.

---

## 📈 Combined Visualization

The combined plot includes:

- ✅ **Green Line**: Approximate collision probability.
- 🔁 **Purple Dashed Line**: Diminishing harmonic bounce.
- 📍 **Red Dot**: First point where probability exceeds 50% (at \( k \approx 23 \)).
- 🔹 **Gray Lines**: Horizontal (at 50%) and vertical (at \( k = 23 \)) threshold markers.

![birthday_paradox](birthday_paradox.png)


![birthday_paradox_365](birthday_paradox_365.png)

![birthday_paradox_sha256_00](birthday_paradox_sha256_00.png)

![birthday_paradox_sha256_01](birthday_paradox_sha256_01.png)

---
## Mathematical Insights:
- The Taylor series for 1 - e^(-x) is: x - x²/2 + x³/6 - x⁴/24 + ...
- For the birthday paradox, x = k(k-1)/(2N)
- The 50% threshold occurs when k ≈ √(2N ln(2))
- For N=365: ~23 people (code identified this)
- For SHA-256: ~2^128 hashes (practically infeasible to find the collision)

## Key Findings:

- Birthday Paradox: Taylor series works well for small k values but diverges for larger groups
- SHA-256: The collision probability is so astronomically small that even with 100 hashes, it's effectively 0
- Approximation Quality: Higher-order Taylor terms dramatically improve accuracy, especially for larger k values

The visualization shows how the different approximation methods compare and provides insight into when each approach is most appropriate. The SHA-256 analysis demonstrates why cryptographic hash functions are considered secure against collision attacks.


