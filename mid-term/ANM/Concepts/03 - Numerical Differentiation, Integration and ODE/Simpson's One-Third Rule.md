---
title: "Simpson's 1/3 Rule"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - numerical-integration
  - quadrature
aliases:
  - "Simpson 1/3 Rule"
  - "Simpson's Rule"
  - "Composite Simpson's 1/3 Rule"
  - "Simpson's 1/3 Rule"
status: completed
---

# 📐 Simpson's 1/3 Rule (Numerical Integration)

> [!NOTE] 💡 The Big Picture Intuition
> The [[Trapezoidal Rule]] connects data points with **straight lines**, throwing away all curvature. Simpson's 1/3 Rule upgrades each pair of strips from a flat chord to a **parabola** — a curve that bends through three consecutive points at once.
> Why "1/3"? Because after simplifying, the formula's leading coefficient is $\frac{h}{3}$. The odd-numbered ordinates get weight $4$ ("odds are four"), the remaining interior points get weight $2$, and the two ends get $1$ — the famous **1–4–2–4–…–4–1 coefficient pattern**. This tiny change quadruples the accuracy: error drops from $O(h^2)$ to $O(h^4)$, and the rule integrates **cubics exactly**, not just lines!

---

## 1. Problem Statement & Setup

We want
$$I = \int_a^b f(x)\, dx$$
using only function values (tabulated or computed).

**Setup**: divide $[a, b]$ into $n$ equal subintervals of width
$$h = \frac{b - a}{n}, \qquad \boxed{n \text{ must be EVEN}}$$
with nodes $x_0 = a, \dots, x_n = b$ and ordinates $y_i = f(x_i)$.

> [!WARNING] ⚠️ The Even-Strips Requirement
> Each application of the rule consumes **two strips (three points)** — a parabola needs 3 points. So the total number of strips $n$ must be **even** (equivalently, the number of ordinates $n+1$ must be **odd**). If your table has an even number of ordinates, pair Simpson's 1/3 with the [[Trapezoidal Rule]] or [[Simpson's Three-Eighths Rule]] for the leftover strip(s).

---

## 2. Derivation via Parabolic Interpolation

Fit the unique quadratic through three consecutive points $(x_0,y_0),(x_1,y_1),(x_2,y_2)$ using Newton's forward differences ($P_2(x) = y_0 + p\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0$, with $x = x_0 + ph$, $dx = h\,dp$) and integrate from $p = 0$ to $p = 2$:

$$\int_{x_0}^{x_2} f(x)\,dx \approx h\int_0^2 \left[ y_0 + p\,\Delta y_0 + \frac{p(p-1)}{2}\Delta^2 y_0 \right] dp = h\left[ 2y_0 + 2\Delta y_0 + \frac{\Delta^2 y_0}{3} \right]$$

Since $2y_0 + 2\Delta y_0 + \frac{\Delta^2 y_0}{3} = 2y_0 + 2(y_1 - y_0) + \frac{y_2 - 2y_1 + y_0}{3} = \frac{y_0 + 4y_1 + y_2}{3}$:

> [!IMPORTANT] 🎯 Single Application (one parabola, 2 strips, 3 points)
> $$\int_{x_0}^{x_2} f(x)\,dx \approx \frac{h}{3}\Big[ y_0 + 4y_1 + y_2 \Big]$$

### Composite Rule ($n$ even, $n+1$ points)
Applying the single-panel formula to each pair of strips $(y_0..y_2), (y_2..y_4), \dots, (y_{n-2}..y_n)$ and summing:

> [!IMPORTANT] 🎯 Composite Simpson's 1/3 Rule
> $$\int_a^b f(x)\,dx \approx \frac{h}{3}\Big[ (y_0 + y_n) + 4(y_1 + y_3 + \dots + y_{n-1}) + 2(y_2 + y_4 + \dots + y_{n-2}) \Big]$$

> [!TIP] 💡 The "1 4 2 4 2 … 4 1" Memory Hook
> - **Ends** ($y_0, y_n$): coefficient $1$
> - **Odd-indexed interiors** ($y_1, y_3, \dots$): coefficient $4$
> - **Even-indexed interiors** ($y_2, y_4, \dots$): coefficient $2$
>
> Multiplier out front: $\frac{h}{3}$. (The sum of all coefficients $\times \frac{h}{3}$ must equal $nh$ — a fast arithmetic check!)

---

## 3. Why It's Exact for Cubics (The Superpower)

A parabola has 3 parameters, so intuitively it should be exact only up to degree 2. But Simpson's rule has a hidden symmetry: for $f(x) = x^3$ over $[-1, 1]$ (the standard symmetry argument),

$$\int_{-1}^{1} x^3\,dx = 0 \quad \text{and} \quad \frac{h}{3}\big[ (-1)^3 + 4(0)^3 + (1)^3 \big] = \frac{1}{3}[-1 + 0 + 1] = 0 ✅$$

The cubic's odd part integrates to zero on both sides symmetrically, and the even part is captured exactly by the parabola. Hence:

> [!IMPORTANT] 🎯 Degree of Precision: 3
> Simpson's 1/3 rule integrates every polynomial of degree $\le 3$ **exactly**, and its error term contains $f^{(4)}(\xi)$ (see [[Error in Quadrature Formulas – Trapezoidal, Simpson's]]). This is why it vastly outperforms the Trapezoidal Rule for smooth functions.

---

## 4. Worked Step-by-Step Example

### Worked Example 1: Composite Simpson's 1/3 Rule
> [!EXAMPLE] Problem
> Evaluate $\displaystyle\int_0^1 \frac{dx}{1 + x^2}$ using Simpson's 1/3 Rule with $n = 6$ subintervals. Give the answer to 6 decimal places.

**Step 1: Step size** — $h = \frac{1 - 0}{6} = \frac{1}{6} \approx 0.166667$ (check: $n = 6$ is even ✅)

**Step 2: Tabulate the ordinates $y_i = \dfrac{1}{1 + x_i^2}$** (same table as the [[Trapezoidal Rule]] example)

| $i$ | $x_i$ | $y_i$ | Coefficient |
| :---: | :---: | :---: | :---: |
| 0 | $0$ | $1.000000$ | $1$ |
| 1 | $1/6$ | $0.972973$ | $4$ |
| 2 | $1/3$ | $0.900000$ | $2$ |
| 3 | $1/2$ | $0.800000$ | $4$ |
| 4 | $2/3$ | $0.692308$ | $2$ |
| 5 | $5/6$ | $0.590164$ | $4$ |
| 6 | $1$ | $0.500000$ | $1$ |

**Step 3: Group the weighted sums**
- Ends: $y_0 + y_6 = 1.000000 + 0.500000 = 1.500000$
- Odd sum: $y_1 + y_3 + y_5 = 0.972973 + 0.800000 + 0.590164 = 2.363137$
- Even sum: $y_2 + y_4 = 0.900000 + 0.692308 = 1.592308$

**Step 4: Apply the composite formula**

$$I \approx \frac{h}{3}\Big[ (y_0 + y_6) + 4(\text{odd sum}) + 2(\text{even sum}) \Big]$$
$$I \approx \frac{0.166667}{3}\Big[ 1.500000 + 4(2.363137) + 2(1.592308) \Big]$$
$$I \approx 0.055556 \times \big[ 1.500000 + 9.452548 + 3.184616 \big] = 0.055556 \times 14.137164 = \mathbf{0.785398}$$

**Step 5: Compare with the exact value**
$$\int_0^1 \frac{dx}{1+x^2} = \frac{\pi}{4} = 0.785398$$
$$\text{Error} = |0.785398 - 0.785398| \approx \mathbf{0.000000}$$

> [!SUCCESS] ✅ Sanity Check
> The weighted sum of coefficients is $1 + 4 + 2 + 4 + 2 + 4 + 1 = 18$, and $18 \times \frac{h}{3} = 18 \times \frac{1/6}{3} = 1 = b - a$ ✅. The result matches $\pi/4$ to all 6 displayed decimals — the weighted error contribution $\frac{(b-a)h^4}{180}f^{(4)}(\xi)$ nearly cancels for this integrand, whose $f^{(4)}$ changes sign on $[0,1]$ (see [[Error in Quadrature Formulas – Trapezoidal, Simpson's]]), giving a dramatically better result than the Trapezoidal Rule's $0.784241$ on identical data.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why is $n$ required to be even?
> Explain precisely why Simpson's 1/3 rule cannot be applied with an odd number of strips.

> [!SUCCESS]- Step-by-Step Solution
> 1. The rule fits **one parabola per two strips**; a parabola is determined by exactly **3 points**.
> 2. With $n$ odd, after pairing strips ($2 + 2 + \dots$) there is **one unpaired strip** left over — only 2 points, which define a line, not a parabola.
> 3. Remedies: integrate the last strip with the Trapezoidal Rule (losing accuracy there), or restructure with [[Simpson's Three-Eighths Rule]] (which consumes strips in threes).

---

> [!QUESTION] Practice Question: Exactness for cubics
> Simpson's rule fits a *quadratic*, yet integrates *cubic* polynomials exactly. Explain.

> [!SUCCESS]- Step-by-Step Solution
> 1. On a symmetric panel $[-1, 1]$, write $f = f_{\text{even}} + f_{\text{odd}}$.
> 2. The odd part (e.g., $x^3$) integrates to exactly $0$ on $[-1,1]$ **and** the Simpson sum of any odd function is also $0$ (since $y_0 = -y_2$, $y_1 = 0$ at the symmetric nodes).
> 3. The even part of a cubic is a quadratic, which the parabola reproduces exactly.
> 4. Hence $\text{error} \propto f^{(4)}$ — the rule's degree of precision is **3**, not 2.

---

## 💻 Python Implementation

```python
def simpson_one_third(f, a, b, n):
    """
    Composite Simpson's 1/3 Rule (n must be even).

    Parameters:
        f: function to integrate
        a, b: integration limits
        n: number of subintervals (must be even)

    Returns:
        Approximation of the integral of f from a to b.
    """
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requires an EVEN number of strips.")
    h = (b - a) / n
    total = f(a) + f(b)                       # ends: coefficient 1
    for i in range(1, n):
        weight = 4 if i % 2 == 1 else 2       # odd -> 4, even -> 2
        total += weight * f(a + i * h)
    return total * h / 3


# Example usage:
import math

approx = simpson_one_third(lambda x: 1 / (1 + x**2), 0, 1, 6)
exact = math.atan(1)  # pi/4

print(f"Simpson 1/3 (n=6): {approx:.6f}")   # Output: 0.785398
print(f"Exact (pi/4):      {exact:.6f}")   # Output: 0.785398
```

---

## 🔗 Related Notes
- [[Trapezoidal Rule]] — The $O(h^2)$ baseline this rule improves upon
- [[Simpson's Three-Eighths Rule]] — Cubic-panel variant for $n$ divisible by 3
- [[Weddle's Rule]] — Sixth-difference rule for $n$ a multiple of 6
- [[Error in Quadrature Formulas – Trapezoidal, Simpson's]] — Exact error terms and comparison
- [[Newton Forward and Backward Difference Interpolation]] — Source of the finite-difference derivation
