---
title: "Graeffe's Root-Squaring Method"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - polynomial-roots
aliases:
  - "Root-Squaring Method"
  - "Graeffe's Method"
status: completed
---

# 🔲 Graeffe's Root-Squaring Method

> [!NOTE] 💡 The Big Picture Intuition (The "Amplifying the Loudest Voice" Analogy)
> Imagine three people speaking in a room at volumes $3, 2, 1$. The difference is noticeable, but everyone is still audible.
> Now suppose we pass their voices through a **repeated squaring machine** ($x^2, x^4, x^8, x^{16}$):
> - $3^{16} \approx 43,046,721$
> - $2^{16} = 65,536$
> - $1^{16} = 1$
> 
> The largest number $3$ now completely dwarfs $2$ by a factor of $650\times$, and dwarfs $1$ by millions!
> **Graeffe's Method** uses this algebraic trick: by repeatedly squaring the roots of a polynomial, the roots become vastly separated in magnitude. Each polynomial coefficient then isolates and exposes **one specific root**, allowing you to calculate **ALL roots simultaneously without any initial guess**!

---

## 1. The Root-Squaring Transformation

Consider an $n$-th degree polynomial with real coefficients:
$$P_n(x) = a_0 x^n + a_1 x^{n-1} + a_2 x^{n-2} + \dots + a_n = 0 \quad (a_0 \neq 0)$$

To construct a new polynomial whose roots are the squares ($x^2$) of the original roots, multiply $P(x)$ by $P(-x)$:
$$P(x) \cdot P(-x) = (-1)^n Q(x^2) = 0$$

Let $y = x^2$. The transformed polynomial is:
$$Q(y) = A_0 y^n + A_1 y^{n-1} + A_2 y^{n-2} + \dots + A_n = 0$$

> [!IMPORTANT] 🎯 Formula for Squared Coefficients ($A_k$)
> $$A_k = (-1)^k \left[ a_k^2 - 2a_{k-1}a_{k+1} + 2a_{k-2}a_{k+2} - 2a_{k-3}a_{k+3} + \dots \right]$$
> 
> Specifically for each term:
> - $A_0 = a_0^2$
> - $A_1 = a_1^2 - 2a_0 a_2$
> - $A_2 = a_2^2 - 2a_1 a_3 + 2a_0 a_4$
> - $A_3 = a_3^2 - 2a_2 a_4 + 2a_1 a_5 - 2a_0 a_6$
> - $A_n = a_n^2$

---

## 2. Root Magnitude Extraction Formula

Let the original roots be $\alpha_1, \alpha_2, \dots, \alpha_n$ ordered by descending magnitude:
$$|\alpha_1| > |\alpha_2| > |\alpha_3| > \dots > |\alpha_n|$$

After $m$ successive root-squarings ($N = 2^m$, where $m=1 \implies N=2$, $m=2 \implies N=4$, $m=3 \implies N=8$):

> [!IMPORTANT] 🎯 Root Magnitude Formula
> $$|\alpha_1| = \left( \frac{A_1}{A_0} \right)^{1/N}, \quad |\alpha_2| = \left( \frac{A_2}{A_1} \right)^{1/N}, \quad \dots, \quad |\alpha_n| = \left( \frac{A_n}{A_{n-1}} \right)^{1/N}$$

---

## 3. Determining the Signs ($\pm$) of the Roots

Because the magnitude formulas yield absolute values $|\alpha_i|$, the sign ($\pm$) of each root is determined using:
1. **Direct Substitution**: Test $+\alpha_i$ and $-\alpha_i$ in original $P_n(x) = 0$. Whichever yields near zero is the correct sign.
2. **Descartes' Rule of Signs**: Count the sign changes in $P_n(x)$ (gives maximum number of positive real roots) and $P_n(-x)$ (gives maximum number of negative real roots).
3. **Vieta's Relations**:
   $$\sum_{i=1}^n \alpha_i = -\frac{a_1}{a_0}, \quad \prod_{i=1}^n \alpha_i = (-1)^n \frac{a_n}{a_0}$$

---

## 4. Special Root Structures & Symptoms

| Case | Symptom during Squaring | Root Structure | Extraction Formula |
| :--- | :--- | :--- | :--- |
| **Distinct Real Roots** | Cross terms become negligible ($A_k \approx a_k^2$) | All real and distinct | Standard: $|\alpha_i| = (A_i / A_{i-1})^{1/N}$ |
| **Equal Magnitude Real Roots** ($\alpha_k = -\alpha_{k+1}$) | Middle coefficient $A_k$ vanishes or stays near $0$ | Pair with opposite signs $\pm \alpha$ | $|\alpha| = \left(\frac{A_{k+1}}{A_{k-1}}\right)^{1/(2N)}$ |
| **Complex Conjugate Roots** ($\rho e^{\pm i \theta}$) | Coefficient $A_k$ oscillates in sign | Pair $u \pm iv = \rho(\cos\theta \pm i\sin\theta)$ | Modulus: $\rho = \left(\frac{A_{k+1}}{A_{k-1}}\right)^{1/(2N)}$ |

---

## 5. Worked Step-by-Step Examples

### Worked Example 1: Full Root Extraction for a Cubic Polynomial
> [!EXAMPLE] Problem
> Find all roots of $P(x) = x^3 - 6x^2 + 11x - 6 = 0$ using Graeffe's Root-Squaring Method with 2 squarings ($m=2 \implies N = 2^2 = 4$).

**Step 1: Identify Original Coefficients ($m=0, N=1$)**
- $a_0 = 1$
- $a_1 = -6$
- $a_2 = 11$
- $a_3 = -6$

**Step 2: First Root-Squaring ($m=1, N=2$)**
- $A_0 = a_0^2 = 1^2 = \mathbf{1}$
- $A_1 = a_1^2 - 2a_0 a_2 = (-6)^2 - 2(1)(11) = 36 - 22 = \mathbf{14}$
- $A_2 = a_2^2 - 2a_1 a_3 = (11)^2 - 2(-6)(-6) = 121 - 72 = \mathbf{49}$
- $A_3 = a_3^2 = (-6)^2 = \mathbf{36}$

The squared polynomial is $Q_1(y) = y^3 - 14y^2 + 49y - 36 = 0$.

**Step 3: Second Root-Squaring ($m=2, N=4$)**
Using coefficients of $Q_1(y)$: $A_0 = 1, A_1 = 14, A_2 = 49, A_3 = 36$:
- $B_0 = A_0^2 = 1^2 = \mathbf{1}$
- $B_1 = A_1^2 - 2A_0 A_2 = (14)^2 - 2(1)(49) = 196 - 98 = \mathbf{98}$
- $B_2 = A_2^2 - 2A_1 A_3 = (49)^2 - 2(14)(36) = 2401 - 1008 = \mathbf{1393}$
- $B_3 = A_3^2 = (36)^2 = \mathbf{1296}$

The 4-th power polynomial is $Q_2(z) = z^3 - 98z^2 + 1393z - 1296 = 0$.

**Step 4: Extract Root Magnitudes ($N = 4$)**
- $|\alpha_1| = \left( \frac{B_1}{B_0} \right)^{1/4} = (98)^{1/4} = (98)^{0.25} \approx \mathbf{3.146}$ *(Approaching true root $3$)*
- $|\alpha_2| = \left( \frac{B_2}{B_1} \right)^{1/4} = \left( \frac{1393}{98} \right)^{1/4} = (14.214286)^{0.25} \approx \mathbf{1.941}$ *(Approaching true root $2$)*
- $|\alpha_3| = \left( \frac{B_3}{B_2} \right)^{1/4} = \left( \frac{1296}{1393} \right)^{1/4} = (0.930366)^{0.25} \approx \mathbf{0.982}$ *(Approaching true root $1$)*

**Step 5: Determine Signs**
- Original signs of $P(x) = +x^3 - 6x^2 + 11x - 6$:
  - Sign sequence: $+ \longrightarrow - \longrightarrow + \longrightarrow -$ ($3$ sign changes $\implies 3$ positive real roots).
- Sum of roots check: $\alpha_1 + \alpha_2 + \alpha_3 = 3 + 2 + 1 = 6 = -(-6)/1$.
- **Final Result**: The roots are **$\alpha_1 \approx 3, \alpha_2 \approx 2, \alpha_3 \approx 1$**.

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why is Graeffe called a "Direct" method?
> Why is Graeffe's method categorized as a direct method rather than an open iterative method?

> [!SUCCESS]- Step-by-Step Solution
> 1. Unlike open iterative methods (such as Newton-Raphson) that require an initial guess $x_0$ and only converge to **one single root** at a time, Graeffe's method requires **no initial guess**.
> 2. It directly operates on the full coefficient array of the polynomial and simultaneously computes approximations to **all $n$ roots** at once!

---

## 💻 Python Implementation

```python
import numpy as np

def graeffe_step(a):
    n = len(a) - 1
    A = np.zeros(n + 1)
    for k in range(n + 1):
        s = a[k]**2
        j = 1
        while (k - j >= 0) and (k + j <= n):
            s += 2 * ((-1)**j) * a[k - j] * a[k + j]
            j += 1
        A[k] = s
    return A
```

---

## 🔗 Related Notes
- [[Roots of Equations]] — Polynomial properties and Descartes' Rule of Signs.
- [[Lin-Bairstow Method]] — Quadratic factor extraction method.
