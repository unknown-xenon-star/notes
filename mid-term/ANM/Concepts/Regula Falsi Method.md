---
title: "Regula Falsi Method (False Position)"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - root-finding
  - bracketing-methods
aliases:
  - "False Position Method"
  - "Linear Interpolation Method"
status: completed
---

# 📐 Regula Falsi Method (Method of False Position)

> [!NOTE] 💡 The Big Picture Intuition
> In the [[Bisection Method]], we blindly cut the interval at the exact midpoint ($50\%$), even if $f(a) = -0.001$ (whispering distance from zero) and $f(b) = +1000$ (miles away).
> **Regula Falsi** is smarter: it connects the two points $(a, f(a))$ and $(b, f(b))$ with a tight string (a straight **secant line**) and picks where that line hits the ground ($y = 0$). If $f(a)$ is very close to zero, the string naturally intersects the axis much closer to $a$!

---

## 1. Geometric Derivation of the Formula

```
       y ^            B (b, f(b))
         |           /
         |          /  Secant Line connecting A and B
---------+---------c----+--------> x
       a |        /     b
         |       /
A (a, f(a))    v
```

Let $A = (a, f(a))$ and $B = (b, f(b))$ with $f(a) \cdot f(b) < 0$.
The two-point equation of the straight line joining $A$ and $B$ is:
$$\frac{y - f(a)}{x - a} = \frac{f(b) - f(a)}{b - a}$$

Setting $y = 0$ to locate the $x$-intercept $x = c$:
$$\frac{0 - f(a)}{c - a} = \frac{f(b) - f(a)}{b - a}$$
$$c - a = -\frac{f(a)(b - a)}{f(b) - f(a)}$$

> [!IMPORTANT] Regula Falsi Formula
> $$c = a - \frac{f(a)(b - a)}{f(b) - f(a)} = \frac{a f(b) - b f(a)}{f(b) - f(a)}$$
> Alternatively, expanding from $b$:
> $$c = b - \frac{f(b)(b - a)}{f(b) - f(a)}$$

---

## 2. Step-by-Step Algorithm

1. **Step 1: Bracket Verification**: Choose $a, b$ such that $f(a) \cdot f(b) < 0$.
2. **Step 2: Linear Interpolation**: Compute:
   $$c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$$
3. **Step 3: Evaluate & Check Convergence**:
   - If $|f(c)| < \epsilon$ or $|c_{\text{new}} - c_{\text{old}}| < \epsilon$, **STOP**; $\alpha \approx c$.
4. **Step 4: Update Bracket**:
   - If $f(a) \cdot f(c) < 0$: The root lies in $[a, c]$. Set $b = c$.
   - If $f(a) \cdot f(c) > 0$: The root lies in $[c, b]$. Set $a = c$.
5. **Step 5: Repeat** until satisfied.

---

## 3. The "Stagnant Endpoint" Trap & The Illinois Fix

> [!WARNING] The Stagnant Endpoint Problem
> When the function $f(x)$ is strictly convex or strictly concave (like $f(x) = x^4 - 10$ or $e^x - 2$), the secant line consistently underestimates the root from the same side.
> - As a result, **one endpoint never changes** (it stays "stagnant" forever), and the interval $[a, b]$ never shrinks to zero!
> - This slows convergence to a sluggish linear crawl.

```
       y ^           B (Stagnant endpoint that never moves!)
         |          /|
         |         /.|
         |        / .|
---------+-------c1-c2--+--------> x
       a |      / .  |  b
         |     / .   |
```

### The Illinois Algorithm Remedy:
If an endpoint remains stagnant for **two consecutive steps**, artificially halve its function value:
$$f(a_{\text{stagnant}}) \leftarrow \frac{f(a_{\text{stagnant}})}{2}$$
This forces the next secant line to swing across the root, instantly unstucking the stagnant endpoint!

---

## 4. Worked Step-by-Step Examples

### Worked Example 1: Standard Polynomial Root
> [!EXAMPLE] Problem
> Find a real root of $f(x) = x^3 - 2x - 5 = 0$ in the interval $[2, 3]$ using Regula Falsi for 3 iterations.

**Step 1: Check Bracket**
- $f(2) = (2)^3 - 2(2) - 5 = 8 - 4 - 5 = -1 < 0$
- $f(3) = (3)^3 - 2(3) - 5 = 27 - 6 - 5 = +16 > 0$
- $f(2) \cdot f(3) = (-1)(16) = -16 < 0$ ✅ ($a = 2, b = 3$).

**Step 2: Iterations Breakdown**

- **Iteration 1 ($k=1$):**
  $$c_1 = \frac{a f(b) - b f(a)}{f(b) - f(a)} = \frac{2(16) - 3(-1)}{16 - (-1)} = \frac{32 + 3}{17} = \frac{35}{17} \approx \mathbf{2.058824}$$
  Evaluate $f(c_1)$:
  $$f(2.058824) = (2.058824)^3 - 2(2.058824) - 5 = 8.726396 - 4.117648 - 5 = \mathbf{-0.391252} < 0$$
  Sign check: $f(a) \cdot f(c_1) = (-1)(-0.391252) > 0 \implies$ Replace left endpoint $a$:
  $$a_2 = 2.058824, \quad b_2 = 3.000000$$

- **Iteration 2 ($k=2$):**
  $$c_2 = \frac{(2.058824)(16) - (3)(-0.391252)}{16 - (-0.391252)} = \frac{32.941184 + 1.173756}{16.391252} = \frac{34.114940}{16.391252} \approx \mathbf{2.081264}$$
  Evaluate $f(c_2)$:
  $$f(2.081264) = (2.081264)^3 - 2(2.081264) - 5 = 9.014815 - 4.162528 - 5 = \mathbf{-0.147713} < 0$$
  Sign check: $f(a_2) \cdot f(c_2) > 0 \implies$ Replace left endpoint $a$:
  $$a_3 = 2.081264, \quad b_3 = 3.000000$$

- **Iteration 3 ($k=3$):**
  $$c_3 = \frac{(2.081264)(16) - (3)(-0.147713)}{16 - (-0.147713)} = \frac{33.300224 + 0.443139}{16.147713} = \frac{33.743363}{16.147713} \approx \mathbf{2.089640}$$
  Evaluate $f(c_3)$:
  $$f(2.089640) = (2.089640)^3 - 2(2.089640) - 5 = \mathbf{-0.05474} < 0$$

### Iteration Table:

| Iteration ($k$) | $a_k$ | $b_k$ | $f(a_k)$ | $f(b_k)$ | Approximation $c_k$ | $f(c_k)$ | Next Bracket |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $2.000000$ | $3.000000$ | $-1.000000$ | $+16.000000$ | **$2.058824$** | $-0.391252$ | $[2.058824, 3.0]$ |
| **2** | $2.058824$ | $3.000000$ | $-0.391252$ | $+16.000000$ | **$2.081264$** | $-0.147713$ | $[2.081264, 3.0]$ |
| **3** | $2.081264$ | $3.000000$ | $-0.147713$ | $+16.000000$ | **$2.089640$** | $-0.054740$ | $[2.089640, 3.0]$ |

Notice how $b = 3.0$ remained stagnant while $a$ marched steadily toward the exact root $\alpha \approx 2.094551$.

---

## 5. Comparison: Bisection vs. Regula Falsi

| Feature | [[Bisection Method]] | [[Regula Falsi Method]] |
| :--- | :--- | :--- |
| **Formula** | $c = \frac{a+b}{2}$ | $c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$ |
| **Philosophy** | Blind geometric halving | Function-value weighted interpolation |
| **Order of Convergence** | Linear ($p = 1$, $C = 0.5$) | Linear ($p = 1$, variable $C$) |
| **Interval Behavior** | Interval size strictly halves | Interval size may freeze due to stagnant endpoint |
| **Predictability** | Exact number of steps known in advance | Step count varies based on curve shape |

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Derivation Memory Check
> How can you easily write the Regula Falsi formula without memorization by using cross-multiplication?

> [!SUCCESS]- Step-by-Step Solution
> 1. Remember the two endpoint pairs: $(a, f(a))$ and $(b, f(b))$.
> 2. Cross-multiply $a$ with the opposite function value $f(b)$, and $b$ with the opposite function value $f(a)$.
> 3. Subtract them in the numerator: $a f(b) - b f(a)$.
> 4. Divide by the difference of the function values: $f(b) - f(a)$.
> 5. Result:
>    $$c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$$

---

## 💻 Python Implementation

```python
def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
        
    c = a
    for k in range(1, max_iter + 1):
        fa, fb = f(a), f(b)
        c_new = (a * fb - b * fa) / (fb - fa)
        fc = f(c_new)
        
        if abs(fc) < tol or abs(c_new - c) < tol:
            return c_new, k
            
        c = c_new
        if fa * fc < 0:
            b = c
        else:
            a = c
            
    return c, max_iter
```

---

## 🔗 Related Notes
- [[Bisection Method]] — Midpoint bracketing baseline.
- [[Secant Method]] — Uses the same interpolation formula without requiring bracket preservation.
- [[Newton-Raphson Method]] — Replaces secants with tangents.
