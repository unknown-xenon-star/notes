---
title: "Lin-Bairstow Method"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - polynomial-roots
  - quadratic-factor
aliases:
  - "Bairstow's Method"
  - "Lin's Method"
  - "Quadratic Factor Method"
status: completed
---

# 🧬 Lin-Bairstow Method (Quadratic Factor Extraction)

> [!NOTE] 💡 The Big Picture Intuition (The "Real Arithmetic" Secret)
> Finding complex roots ($u \pm iv$) of high-degree polynomials is normally painful because you have to calculate with imaginary numbers ($\sqrt{-1}$).
> **Bairstow's Method** uses a brilliant mathematical truth: **any pair of complex conjugate roots multiplies together to form a pure REAL quadratic factor**:
> $$(x - (u + iv))(x - (u - iv)) = x^2 - 2ux + (u^2 + v^2) = x^2 - rx - s$$
> where $r = 2u$ and $s = -(u^2 + v^2)$ are **pure real numbers**!
> By iteratively tuning $r$ and $s$ using **double synthetic division**, Bairstow peels off quadratic factors using only ordinary real numbers, and then finds both real or complex roots instantly with the standard quadratic formula!

---

## 1. Mathematical Formulation

Let an $n$-th degree polynomial with real coefficients be:
$$P_n(x) = a_0 x^n + a_1 x^{n-1} + a_2 x^{n-2} + \dots + a_n = 0 \quad (a_0 \neq 0)$$

Divide $P_n(x)$ by a trial quadratic factor $(x^2 - rx - s)$:
$$P_n(x) = (x^2 - rx - s) Q_{n-2}(x) + R(x)$$

where the quotient polynomial is:
$$Q_{n-2}(x) = b_0 x^{n-2} + b_1 x^{n-3} + \dots + b_{n-2}$$
and the linear remainder is:
$$R(x) = b_{n-1}(x - r) + b_n$$

For $(x^2 - rx - s)$ to be an exact factor of $P_n(x)$, the remainder must vanish completely:
$$b_{n-1}(r, s) = 0 \quad \text{and} \quad b_n(r, s) = 0$$

---

## 2. Double Synthetic Division Recurrence Relations

### A. First Synthetic Division (Quotient & Remainder Coefficients $b_k$)

> [!IMPORTANT] 🎯 Recurrence for $b_k$
> $$\begin{aligned}
> b_0 &= a_0 \\
> b_1 &= a_1 + r b_0 \\
> b_k &= a_k + r b_{k-1} + s b_{k-2}, \quad \text{for } k = 2, 3, \dots, n
> \end{aligned}$$
> - The remainder terms are $R_1 = b_{n-1}$ and $R_0 = b_n$.

---

### B. Second Synthetic Division (Partial Derivatives $c_k$)
To compute the sensitivity derivatives $\frac{\partial b_k}{\partial r}$ and $\frac{\partial b_k}{\partial s}$, we divide the newly calculated $b$-array by the exact same trial factor $(x^2 - rx - s)$:

> [!IMPORTANT] 🎯 Recurrence for $c_k$
> $$\begin{aligned}
> c_0 &= b_0 \\
> c_1 &= b_1 + r c_0 \\
> c_k &= b_k + r c_{k-1} + s c_{k-2}, \quad \text{for } k = 2, 3, \dots, n-1
> \end{aligned}$$

---

## 3. Newton-Raphson Corrections ($\Delta r, \Delta s$)

We set up a $2 \times 2$ Taylor series linear system to find the adjustments $\Delta r$ and $\Delta s$ that drive the remainders $b_{n-1}$ and $b_n$ to zero:

$$\begin{bmatrix}
c_{n-2} & c_{n-3} \\
c_{n-1} & c_{n-2}
\end{bmatrix}
\begin{bmatrix}
\Delta r \\
\Delta s
\end{bmatrix}
=
\begin{bmatrix}
-b_{n-1} \\
-b_n
\end{bmatrix}$$

Using Cramer's Rule:
$$\text{Determinant: } D = c_{n-2}^2 - c_{n-1} c_{n-3}$$

> [!IMPORTANT] 🎯 Parameter Update Formulas
> $$\Delta r = \frac{b_n c_{n-3} - b_{n-1} c_{n-2}}{D}$$
> $$\Delta s = \frac{b_{n-1} c_{n-1} - b_n c_{n-2}}{D}$$
> 
> $$r_{\text{new}} = r + \Delta r, \quad s_{\text{new}} = s + \Delta s$$

---

## 4. Root Extraction & Polynomial Deflation

Iterate until $|\Delta r| < \epsilon$ and $|\Delta s| < \epsilon$.
Once converged, solve the quadratic factor $x^2 - rx - s = 0$:

> [!IMPORTANT] 🎯 Extracted Roots Formula
> $$x_{1, 2} = \frac{r \pm \sqrt{r^2 + 4s}}{2}$$
> - If $r^2 + 4s \ge 0$: Two **real roots**.
> - If $r^2 + 4s < 0$: Pair of **complex conjugate roots** $u \pm iv = \frac{r}{2} \pm i \frac{\sqrt{-(r^2+4s)}}{2}$.

### Polynomial Deflation:
The remaining $n-2$ roots are found by taking the quotient coefficients $b_0, b_1, \dots, b_{n-2}$ as the new polynomial and repeating Bairstow's process!

---

## 5. Worked Step-by-Step Examples

### Worked Example 1: Full Iteration on a 4th-Degree Polynomial
> [!EXAMPLE] Problem
> Perform one complete iteration of Bairstow's method on the polynomial:
> $$P(x) = x^4 - 3x^3 + 20x^2 - 44x + 54 = 0$$
> using initial trial guesses $r_0 = 2, s_0 = -2$.

**Step 1: Identify Given Coefficients**
- Degree $n = 4$.
- $a_0 = 1, a_1 = -3, a_2 = 20, a_3 = -44, a_4 = 54$.
- Initial guesses: $r = 2, s = -2$.

**Step 2: First Synthetic Division (Compute $b$-array)**
$$\begin{aligned}
b_0 &= a_0 = \mathbf{1} \\
b_1 &= a_1 + r b_0 = -3 + (2)(1) = \mathbf{-1} \\
b_2 &= a_2 + r b_1 + s b_0 = 20 + (2)(-1) + (-2)(1) = 20 - 2 - 2 = \mathbf{16} \\
b_3 &= a_3 + r b_2 + s b_1 = -44 + (2)(16) + (-2)(-1) = -44 + 32 + 2 = \mathbf{-10} \quad (= b_{n-1}) \\
b_4 &= a_4 + r b_3 + s b_2 = 54 + (2)(-10) + (-2)(16) = 54 - 20 - 32 = \mathbf{2} \quad (= b_n)
\end{aligned}$$

**Step 3: Second Synthetic Division (Compute $c$-array up to $n-1 = 3$)**
$$\begin{aligned}
c_0 &= b_0 = \mathbf{1} \\
c_1 &= b_1 + r c_0 = -1 + (2)(1) = \mathbf{1} \quad (= c_{n-3}) \\
c_2 &= b_2 + r c_1 + s c_0 = 16 + (2)(1) + (-2)(1) = 16 + 2 - 2 = \mathbf{16} \quad (= c_{n-2}) \\
c_3 &= b_3 + r c_2 + s c_1 = -10 + (2)(16) + (-2)(1) = -10 + 32 - 2 = \mathbf{20} \quad (= c_{n-1})
\end{aligned}$$

**Step 4: Solve for Corrections $\Delta r$ and $\Delta s$**
- Determinant:
  $$D = c_2^2 - c_3 c_1 = (16)^2 - (20)(1) = 256 - 20 = \mathbf{236}$$
- Compute $\Delta r$:
  $$\Delta r = \frac{b_4 c_1 - b_3 c_2}{D} = \frac{(2)(1) - (-10)(16)}{236} = \frac{2 + 160}{236} = \frac{162}{236} \approx \mathbf{+0.6864}$$
- Compute $\Delta s$:
  $$\Delta s = \frac{b_3 c_3 - b_4 c_2}{D} = \frac{(-10)(20) - (2)(16)}{236} = \frac{-200 - 32}{236} = \frac{-232}{236} \approx \mathbf{-0.9831}$$

**Step 5: Compute Updated Parameters**
$$r_1 = r_0 + \Delta r = 2 + 0.6864 = \mathbf{2.6864}$$
$$s_1 = s_0 + \Delta s = -2 - 0.9831 = \mathbf{-2.9831}$$

*(Note: The exact quadratic factor is $x^2 - 2x + 2 = 0 \implies r = 2, s = -2$, giving roots $1 \pm i$).*

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Extracting Complex Conjugate Roots
> If Bairstow's method converges to the quadratic factor $x^2 - 4x + 13 = 0$, what are the two roots?

> [!SUCCESS]- Step-by-Step Solution
> 1. Identify parameters: $r = 4, s = -13$.
> 2. Discriminant: $\Delta = r^2 + 4s = 4^2 + 4(-13) = 16 - 52 = -36 < 0$.
> 3. Apply the quadratic formula:
>    $$x_{1, 2} = \frac{4 \pm \sqrt{-36}}{2} = \frac{4 \pm 6i}{2} = \mathbf{2 \pm 3i}$$
> 4. The roots are the complex conjugate pair **$x = 2 + 3i$** and **$x = 2 - 3i$**!

---

## 💻 Python Implementation

```python
import numpy as np

def bairstow_step(a, r, s):
    n = len(a) - 1
    b = np.zeros(n + 1)
    c = np.zeros(n + 1)
    
    b[0] = a[0]
    b[1] = a[1] + r * b[0]
    for k in range(2, n + 1):
        b[k] = a[k] + r * b[k - 1] + s * b[k - 2]
        
    c[0] = b[0]
    c[1] = b[1] + r * c[0]
    for k in range(2, n):
        c[k] = b[k] + r * c[k - 1] + s * c[k - 2]
        
    D = c[n - 2]**2 - c[n - 1] * c[n - 3]
    dr = (b[n] * c[n - 3] - b[n - 1] * c[n - 2]) / D
    ds = (b[n - 1] * c[n - 1] - b[n] * c[n - 2]) / D
    
    return r + dr, s + ds, abs(dr), abs(ds)
```

---

## 🔗 Related Notes
- [[Roots of Equations]] — Fundamental Theorem of Algebra.
- [[Graeffe's Root-Squaring Method]] — Alternative direct polynomial solver.
- [[Newton-Raphson Method]] — Theoretical foundation for the $2 \times 2$ Jacobian parameter updates.
