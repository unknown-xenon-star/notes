---
title: "Weddle's Rule"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - numerical-integration
  - quadrature
aliases:
  - "Weddle Rule"
  - "Weddle's Sixth-Order Rule"
  - "Sixth Difference Rule"
status: completed
---

# 🎯 Weddle's Rule (Numerical Integration)

> [!NOTE] 💡 The Big Picture Intuition
> Every rule so far has been "keep the first few terms of Newton's differences": the [[Trapezoidal Rule]] keeps $\Delta$, [[Simpson's One-Third Rule]] keeps up to $\Delta^2$, [[Simpson's Three-Eighths Rule]] up to $\Delta^3$. **Weddle's Rule** goes further: integrate the 6th-degree interpolating polynomial, then apply a dash of numerical cleverness — **replace the stubborn coefficient $\frac{41}{140}$ by the clean $\frac{3}{10}$** (they differ by only $\approx 2.4\%$, but the swap makes the formula memorable while keeping the same high order of accuracy!).
> The result: a sixth-order rule with the weight pattern **1–5–1–6–1–5–1** over **six strips (seven points)** — the most accurate classic rule in the syllabus, exact for every polynomial up to degree 5.

---

## 1. Problem Statement & Setup

We want
$$I = \int_a^b f(x)\, dx$$
using equally spaced ordinates.

**Setup**: divide $[a, b]$ into $n$ equal subintervals of width
$$h = \frac{b - a}{n}, \qquad \boxed{n \text{ must be a MULTIPLE of } 6}$$
with nodes $x_0 = a, \dots, x_n = b$ and ordinates $y_i = f(x_i)$.

> [!WARNING] ⚠️ The Multiple-of-6 Requirement
> Each panel consumes **six strips (seven points)**. So $n$ must be divisible by $6$ (equivalently, the number of ordinates $n + 1$ must be a multiple of $7$).

---

## 2. Derivation (in Two Moves)

**Move 1 — Integrate the degree-6 Newton polynomial.** Integrating the full Newton forward formula through 7 points from $p = 0$ to $p = 6$ (with $x = x_0 + ph$, $dx = h\,dp$) gives the exact 7-point (sixth-order) closed Newton–Cotes form:

$$C_6 = \frac{h}{140}\Big[ 41y_0 + 216y_1 + 27y_2 + 272y_3 + 27y_4 + 216y_5 + 41y_6 \Big]$$

**Move 2 — Weddle's simplification.** Noting that $216 \approx 5 \times 41$ and $272 \approx 6 \times 41$ (within $1.2\%$), Weddle factorized and replaced $\frac{41}{140}$ by the clean $\frac{3}{10}$:

> [!IMPORTANT] 🎯 Weddle's Rule (Single Panel: 6 strips, 7 points)
> $$\int_{x_0}^{x_6} f(x)\,dx \approx \frac{3h}{10}\Big[ y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6 \Big]$$

> [!TIP] 💡 Why the "sloppy" swap is nearly free
> Algebraically one can show the exact relation
> $$C_6 = \frac{3h}{10}S - \frac{h}{140}\Delta^6 y_0 \quad\Longleftrightarrow\quad \text{Weddle} = C_6 + \frac{h}{140}\Delta^6 y_0$$
> where $S = y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6$. The extra term $\frac{h}{140}\Delta^6 y_0$ is $O(h^7 f^{(6)})$ — the **same order** as $C_6$'s own truncation error. So the swap costs exactness at degree 6 (Weddle is exact for degree $\le 5$, $C_6$ for degree $\le 6$) but keeps the same $O(h^7)$ single-panel error — a tiny price for the memorable **1–5–1–6–1–5–1** pattern. Multiplier: $\frac{3h}{10}$.
> Memory hook: the pattern is symmetric, with $6$ at the center.

### Composite Rule ($n = 6k$ strips)
Apply the single-panel formula to each block of six strips ($y_0..y_6$, then $y_6..y_{12}$, …) and sum:

> [!IMPORTANT] 🎯 Composite Weddle's Rule
> $$I \approx \frac{3h}{10}\sum_{\text{panels}} \Big[ y_{\text{first}} + 5y_{\text{first}+1} + y_{\text{first}+2} + 6y_{\text{first}+3} + y_{\text{first}+4} + 5y_{\text{first}+5} + y_{\text{last}} \Big]$$
> Shared panel boundaries get counted once per panel (unlike Simpson's rules, no doubling is applied — each panel is simply summed with its own 1–5–1–6–1–5–1 pattern).

---

## 3. Accuracy & Degree of Precision

- **Exact** for every polynomial of degree $\le 5$ (degree of precision $= 5$).
- Single-panel error: $-\dfrac{h^7}{140} f^{(6)}(\xi)$ — sixth-order accuracy, two orders better than the Simpson rules' $O(h^4)$.
- Composite error: $O(h^6)$; see [[Error in Quadrature Formulas – Trapezoidal, Simpson's]] for the full comparison ladder.

> [!SUCCESS] ✅ Quick degree-6 check
> For $f(x) = x^6$ on $[0, 6]$ with $h = 1$: exact $= \frac{6^7}{7} = 39990.857$, Weddle $= 0.3 \times 133320 = 39996$ — a small but **non-zero** error, confirming precision stops at degree 5.

---

## 4. Worked Step-by-Step Examples

### Worked Example 1: Single-Panel Weddle's Rule
> [!EXAMPLE] Problem
> Evaluate $\displaystyle\int_0^6 \frac{dx}{1 + x}$ (i.e., $\ln 7$) using Weddle's Rule with $h = 1$ ($n = 6$ strips).

**Step 1: Step size** — $h = \frac{6-0}{6} = 1$ ✅ ($n = 6$)

**Step 2: Tabulate $y_i = \dfrac{1}{1 + x_i}$**

| $i$ | $x_i$ | $y_i$ | Coefficient |
| :---: | :---: | :---: | :---: |
| 0 | $0$ | $1.000000$ | $1$ |
| 1 | $1$ | $0.500000$ | $5$ |
| 2 | $2$ | $0.333333$ | $1$ |
| 3 | $3$ | $0.250000$ | $6$ |
| 4 | $4$ | $0.200000$ | $1$ |
| 5 | $5$ | $0.166667$ | $5$ |
| 6 | $6$ | $0.142857$ | $1$ |

**Step 3: Apply the formula**

$$I \approx \frac{3h}{10}\Big[ y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6 \Big]$$
$$I \approx 0.3 \times \Big[ 1.000000 + 2.500000 + 0.333333 + 1.500000 + 0.200000 + 0.833333 + 0.142857 \Big]$$
$$I \approx 0.3 \times 6.509524 = \mathbf{1.952857}$$

**Step 4: Compare with exact**
$$\int_0^6 \frac{dx}{1+x} = \ln 7 \approx 1.945910 \implies \text{Error} \approx \mathbf{0.006947}$$
Compare [[Simpson's Three-Eighths Rule]] on $[0,3]$: relative accuracy is far superior here for the same strip width.

### Worked Example 2: Weddle vs Simpson on the Same Data ($n = 6$)
> [!EXAMPLE] Problem
> Evaluate $\displaystyle\int_0^1 \frac{dx}{1 + x^2}$ using Weddle's Rule with $n = 6$ strips, and compare with the Simpson's 1/3 result.

**Step 1:** $h = \frac{1}{6}$; ordinates (as in the [[Simpson's One-Third Rule]] table):
$y_0 = 1.000000,\ y_1 = 0.972973,\ y_2 = 0.900000,\ y_3 = 0.800000,\ y_4 = 0.692308,\ y_5 = 0.590164,\ y_6 = 0.500000$

**Step 2: Apply the single-panel Weddle formula**

$$I \approx \frac{3h}{10}\Big[ y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6 \Big]$$
$$I \approx 0.05 \times \Big[ 1.000000 + 4.864865 + 0.900000 + 4.800000 + 0.692308 + 2.950820 + 0.500000 \Big]$$
$$I \approx 0.05 \times 15.707992 = \mathbf{0.785400}$$

**Step 3: Compare with exact**
$$\text{Exact} = \frac{\pi}{4} = 0.785398 \implies \text{Error} \approx \mathbf{0.0000015}$$

> [!SUCCESS] ✅ Sanity Check
> Weight sum $= 1 + 5 + 1 + 6 + 1 + 5 + 1 = 20$, and $20 \times \frac{3h}{10} = 6h = b - a$ ✅. Weddle's error ($\approx 1.5 \times 10^{-6}$) is the same order as Simpson 1/3's on this data — Weddle's sixth-order advantage becomes decisive as $h$ shrinks, since $O(h^6)$ beats $O(h^4)$ in the limit.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: What exactly did Weddle change?
> The exact 7-point Newton–Cotes rule has coefficients $\frac{h}{140}(41, 216, 27, 272, 27, 216, 41)$. What modification produces Weddle's rule, and what does it cost/gain?

> [!SUCCESS]- Step-by-Step Solution
> 1. Weddle replaces $\frac{41}{140}$ by $\frac{3}{10}$ after factorizing: $216 = 5 \times 41 + 11$ and $272 = 6 \times 41 + 26$ — approximating $216 \approx 5 \times 41$, $272 \approx 6 \times 41$.
> 2. Dividing through by 41 gives $\frac{41h}{140}\left[ y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6 \right]$, and $\frac{41}{140} \to \frac{3}{10}$ completes the swap.
> 3. **Cost**: the rule is no longer the exact Newton–Cotes $C_6$ (drops exactness at degree 6).
> 4. **Gain**: the induced error $-\frac{h}{140}\Delta^6 y_0$ merges with the existing truncation error, yielding a cleaner formula that is exact for degree $\le 5$ with error $-\frac{h^7}{140}f^{(6)}(\xi)$.

---

> [!QUESTION] Practice Question: Choosing the right rule
> A table gives 13 equally spaced ordinates ($n = 12$ strips). Which composite rule(s) can be applied directly, and which is most accurate?

> [!SUCCESS]- Step-by-Step Solution
> 1. $n = 12$ is even → composite [[Simpson's One-Third Rule]] applies (6 panels) ✅
> 2. $n = 12$ is a multiple of 3 → composite [[Simpson's Three-Eighths Rule]] applies (4 panels) ✅
> 3. $n = 12$ is a multiple of 6 → composite **Weddle's Rule** applies (2 panels) ✅ — the most accurate choice ($O(h^6)$).
> 4. If $n$ were, say, 10: Simpson 1/3 alone works (even); Weddle would need a hybrid split.

---

## 💻 Python Implementation

```python
def weddle_rule(f, a, b, n):
    """
    Composite Weddle's Rule (n must be a multiple of 6).

    Parameters:
        f: function to integrate
        a, b: integration limits
        n: number of subintervals (must be divisible by 6)

    Returns:
        Approximation of the integral of f from a to b.
    """
    if n % 6 != 0:
        raise ValueError("Weddle's rule requires n to be a multiple of 6.")
    h = (b - a) / n
    weights = [1, 5, 1, 6, 1, 5, 1]              # 1-5-1-6-1-5-1 pattern
    total = 0.0
    for panel_start in range(0, n, 6):
        for w, i in zip(weights, range(panel_start, panel_start + 7)):
            total += w * f(a + i * h)
    return total * 3 * h / 10


# Example usage:
import math

approx = weddle_rule(lambda x: 1 / (1 + x**2), 0, 1, 6)
exact = math.atan(1)  # pi/4

print(f"Weddle (n=6):     {approx:.6f}")   # Output: 0.785400
print(f"Exact (pi/4):     {exact:.6f}")    # Output: 0.785398
```

---

## 🔗 Related Notes
- [[Trapezoidal Rule]] — $O(h^2)$ baseline
- [[Simpson's One-Third Rule]] — $O(h^4)$, even strips
- [[Simpson's Three-Eighths Rule]] — $O(h^4)$, strips in multiples of 3
- [[Error in Quadrature Formulas – Trapezoidal, Simpson's]] — The full accuracy ladder across all rules
- [[Newton Forward and Backward Difference Interpolation]] — Finite-difference machinery behind the derivation
