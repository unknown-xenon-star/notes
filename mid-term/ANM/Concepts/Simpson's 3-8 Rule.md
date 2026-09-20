---
title: "Simpson's 3/8 Rule"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - numerical-integration
  - quadrature
aliases:
  - "Simpson 3/8 Rule"
  - "Second Simpson Rule"
  - "Composite Simpson's 3/8 Rule"
status: completed
---

# 📏 Simpson's 3/8 Rule (Numerical Integration)

> [!NOTE] 💡 The Big Picture Intuition
> Simpson's 1/3 Rule consumes strips **two at a time** (3 points per parabola). The 3/8 Rule is its sibling that consumes strips **three at a time** (4 points per panel) — fitting a **cubic** polynomial through each group of four consecutive ordinates.
> Why "3/8"? Because simplifying the integrated cubic leaves a leading coefficient of $\frac{3h}{8}$. The weight pattern becomes **1–3–3–1** per panel (the binomial coefficients — a lovely memory hook!). Its superpower: it integrates **quartics exactly** (degree of precision 3, same as 1/3), and its real exam value is flexibility — combining it with the 1/3 Rule handles tables with an **odd number of strips**.

---

## 1. Problem Statement & Setup

We want
$$I = \int_a^b f(x)\, dx$$
using equally spaced ordinates.

**Setup**: divide $[a, b]$ into $n$ equal subintervals of width
$$h = \frac{b - a}{n}, \qquad \boxed{n \text{ must be a MULTIPLE of } 3}$$
with nodes $x_0 = a, \dots, x_n = b$ and ordinates $y_i = f(x_i)$.

> [!WARNING] ⚠️ The Multiple-of-3 Requirement
> Each panel consumes **three strips (four points)** — a cubic needs 4 points. So $n$ must be divisible by $3$ (equivalently, the number of ordinates $n+1$ must be of the form $3k+1$).

---

## 2. Derivation via Cubic Interpolation

Fit the cubic through four consecutive points $(x_0,y_0),\dots,(x_3,y_3)$ using Newton's forward differences ($P_3(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{6}\Delta^3 y_0$, with $x = x_0 + ph$, $dx = h\,dp$) and integrate from $p = 0$ to $p = 3$:

$$\int_{x_0}^{x_3} f(x)\,dx \approx h\int_0^3 \left[ y_0 + p\,\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0 + \frac{p(p-1)(p-2)}{6}\Delta^3 y_0 \right] dp$$

Evaluating the three integrals: $\int_0^3 p\,dp = \frac{9}{2}$, $\int_0^3 \frac{p(p-1)}{2}dp = \frac{3}{2}$, $\int_0^3 \frac{p(p-1)(p-2)}{6}dp = \frac{9}{4}$, giving

$$h\left[ 3y_0 + \frac{9}{2}\Delta y_0 + \frac{3}{2}\Delta^2 y_0 + \frac{9}{4}\Delta^3 y_0 \right] = \frac{3h}{8}\Big[ y_0 + 3y_1 + 3y_2 + y_3 \Big]$$

> [!IMPORTANT] 🎯 Single Application (one cubic, 3 strips, 4 points)
> $$\int_{x_0}^{x_3} f(x)\,dx \approx \frac{3h}{8}\Big[ y_0 + 3y_1 + 3y_2 + y_3 \Big]$$

### Composite Rule ($n = 3k$ strips)
Applying the single-panel formula to each group of three strips and summing:

> [!IMPORTANT] 🎯 Composite Simpson's 3/8 Rule
> $$\int_a^b f(x)\,dx \approx \frac{3h}{8}\Big[ (y_0 + y_n) + 3(y_1 + y_2 + y_4 + y_5 + \dots + y_{n-2} + y_{n-1}) + 2(y_3 + y_6 + \dots + y_{n-3}) \Big]$$
>
> Pattern: ends get $1$, every **third interior point** (a panel boundary: $y_3, y_6, \dots, y_{n-3}$) gets $2$, and **all other interior points** get $3$.

> [!TIP] 💡 The "1 3 3 2 3 3 2 … 3 3 1" Memory Hook
> Each panel carries the binomial pattern **1–3–3–1**; adjacent panels share a boundary point, so shared boundaries accumulate $1 + 1 = 2$, while the outer ends stay $1$. Multiplier out front: $\frac{3h}{8}$.
> (Arithmetic check: for $n = 3k$ strips there are $k$ panels, each contributing a total weight of $8$, so the weight sum is $\frac{8n}{3}$ and indeed $\frac{3h}{8} \cdot \frac{8n}{3} = nh = b - a$ ✅)

---

## 3. Accuracy & Degree of Precision

- Like Simpson's 1/3, it integrates every polynomial of degree $\le 3$ **exactly** — its error term contains $f^{(4)}(\xi)$ (see [[Error in Quadrature Formulas – Trapezoidal, Simpson's]]).
- Single-panel error: $-\frac{3h^5}{80}f^{(4)}(\xi)$ — actually slightly *smaller* than the 1/3 rule's $-\frac{h^5}{90}f^{(4)}(\xi)$ per panel, but per **unit length** they are essentially equivalent ($\frac{3}{80}h^5$ over width $3h$ vs. $\frac{1}{90}h^5$ over width $2h$).
- Composite error: $O(h^4)$, same order as the 1/3 Rule.

---

## 4. Worked Step-by-Step Example

### Worked Example 1: Single-Panel 3/8 Rule
> [!EXAMPLE] Problem
> Evaluate $\displaystyle\int_0^3 \frac{dx}{1 + x}$ (i.e., $\ln 4$) using Simpson's 3/8 Rule with $h = 1$ ($n = 3$ strips).

**Step 1: Step size** — $h = \frac{3-0}{3} = 1$ ✅ ($n = 3$ is a multiple of 3)

**Step 2: Tabulate $y_i = \dfrac{1}{1 + x_i}$**

| $i$ | $x_i$ | $y_i$ | Coefficient |
| :---: | :---: | :---: | :---: |
| 0 | $0$ | $1.000000$ | $1$ |
| 1 | $1$ | $0.500000$ | $3$ |
| 2 | $2$ | $0.333333$ | $3$ |
| 3 | $3$ | $0.250000$ | $1$ |

**Step 3: Apply the formula**
$$I \approx \frac{3h}{8}\Big[ y_0 + 3y_1 + 3y_2 + y_3 \Big] = \frac{3}{8}\Big[ 1.000000 + 1.500000 + 0.999999 + 0.250000 \Big]$$
$$I \approx 0.375 \times 3.749999 = \mathbf{1.406250}$$

**Step 4: Compare with exact**
$$\int_0^3 \frac{dx}{1+x} = \big[\ln(1+x)\big]_0^3 = \ln 4 \approx 1.386294$$
$$\text{Error} = |1.386294 - 1.406250| \approx \mathbf{0.019956}$$

### Worked Example 2: Composite 3/8 Rule ($n = 6$)
> [!EXAMPLE] Problem
> Evaluate $\displaystyle\int_0^1 \frac{dx}{1 + x^2}$ using the composite Simpson's 3/8 Rule with $n = 6$ strips.

**Step 1:** $h = \frac{1}{6} \approx 0.166667$; ordinates as in the [[Simpson's 1/3 Rule]] table:
$y_0 = 1.000000,\ y_1 = 0.972973,\ y_2 = 0.900000,\ y_3 = 0.800000,\ y_4 = 0.692308,\ y_5 = 0.590164,\ y_6 = 0.500000$

**Step 2: Identify weights** — ends $y_0, y_6$: coefficient $1$; panel boundary $y_3$: coefficient $2$; all other interiors $y_1, y_2, y_4, y_5$: coefficient $3$.

**Step 3: Apply the composite formula**

$$I \approx \frac{3h}{8}\Big[ (y_0 + y_6) + 3(y_1 + y_2 + y_4 + y_5) + 2y_3 \Big]$$
$$I \approx 0.0625 \times \Big[ 1.500000 + 3(0.972973 + 0.900000 + 0.692308 + 0.590164) + 1.600000 \Big]$$
$$I \approx 0.0625 \times \Big[ 1.500000 + 3(3.155445) + 1.600000 \Big] = 0.0625 \times 12.566335 = \mathbf{0.785396}$$

**Step 4: Compare with exact**
$$\text{Exact} = \frac{\pi}{4} = 0.785398 \implies \text{Error} \approx \mathbf{0.000002}$$

> [!SUCCESS] ✅ Sanity Check
> Weight sum $= (1 + 1) + 2 + 3 \times 4 = 16 = \dfrac{8n}{3}$ for $n = 6$ ✅, and $16 \times \dfrac{3h}{8} = 6h = b - a$ ✅. Accuracy is superb — error $\sim 2\times10^{-6}$, same $O(h^4)$ class as the 1/3 Rule on identical data.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: When should you prefer 3/8 over 1/3?
> Given a table with $n = 7$ strips, how do you build a high-accuracy composite rule?

> [!SUCCESS]- Step-by-Step Solution
> 1. $n = 7$ is odd → the 1/3 Rule cannot cover everything; $n$ is not a multiple of 3 → pure 3/8 fails too.
> 2. Standard hybrid: apply **Simpson's 1/3 on the first 4 strips** ($n = 4$, even ✅) and **Simpson's 3/8 on the last 3 strips** ($n = 3$ ✅): $4 + 3 = 7$.
> 3. Both rules have error $O(h^4)$, so the hybrid preserves fourth-order accuracy overall — far better than appending a trapezoidal strip ($O(h^2)$).

---

> [!QUESTION] Practice Question: Deriving the weight pattern
> Why do the interior weights of the composite 3/8 rule take only the values 2 and 3?

> [!SUCCESS]- Step-by-Step Solution
> 1. Each panel contributes weights $(1, 3, 3, 1)$ on its four ordinates.
> 2. Interior panel boundaries (every third point) belong to **two adjacent panels**, receiving $1 + 1 = 2$.
> 3. Non-boundary interior points belong to a single panel at weight $3$.
> 4. Only the global ends belong to one panel at weight $1$.

---

## 💻 Python Implementation

```python
def simpson_three_eighth(f, a, b, n):
    """
    Composite Simpson's 3/8 Rule (n must be a multiple of 3).

    Parameters:
        f: function to integrate
        a, b: integration limits
        n: number of subintervals (must be divisible by 3)

    Returns:
        Approximation of the integral of f from a to b.
    """
    if n % 3 != 0:
        raise ValueError("Simpson's 3/8 rule requires n to be a multiple of 3.")
    h = (b - a) / n
    total = f(a) + f(b)                          # ends: coefficient 1
    for i in range(1, n):
        weight = 2 if i % 3 == 0 else 3          # panel boundaries -> 2, else 3
        total += weight * f(a + i * h)
    return total * 3 * h / 8


# Example usage:
import math

approx = simpson_three_eighth(lambda x: 1 / (1 + x**2), 0, 1, 6)
exact = math.atan(1)  # pi/4

print(f"Simpson 3/8 (n=6): {approx:.6f}")   # Output: 0.785396
print(f"Exact (pi/4):      {exact:.6f}")   # Output: 0.785398
```

---

## 🔗 Related Notes
- [[Simpson's 1/3 Rule]] — The even-strip sibling with identical accuracy order
- [[Trapezoidal Rule]] — $O(h^2)$ baseline
- [[Weddle's Rule]] — Sixth-difference rule for $n$ a multiple of 6
- [[Error in Quadrature Formulas – Trapezoidal, Simpson's]] — Exact error terms and comparison table
- [[Newton Forward and Backward Difference Interpolation]] — Finite-difference derivation source
