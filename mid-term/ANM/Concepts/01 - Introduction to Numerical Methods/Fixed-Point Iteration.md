---
title: "Fixed-Point Iteration"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - root-finding
  - open-methods
aliases:
  - "Successive Approximation Method"
  - "Simple Iteration Method"
status: completed
---

# 🔁 Fixed-Point Iteration (Successive Approximation)

> [!NOTE] 💡 The Big Picture Intuition (The "Calculator Game")
> Pick up any scientific calculator (in radians mode), enter any number (say $1.0$), and repeatedly press the $\cos$ button:
> $$1.0 \longrightarrow 0.5403 \longrightarrow 0.8575 \longrightarrow 0.6543 \longrightarrow \dots \longrightarrow 0.739085\dots$$
> After about 20 clicks, the display **freezes** at $0.739085$.
> You just discovered a **fixed point**! A fixed point of a function $g(x)$ is a number $\alpha$ where the output equals the input:
> $$\alpha = g(\alpha)$$
> By cleverly rewriting any equation $f(x) = 0$ into $x = g(x)$, we can solve difficult equations just by feeding the output back in as the next input!

---

## 1. Problem Formulation

Given an equation $f(x) = 0$, algebraically rearrange it to isolate a single $x$ on the left-hand side:
$$x = g(x)$$

Starting with an initial estimate $x_0$, generate the successive sequence:
$$x_{k+1} = g(x_k), \quad k = 0, 1, 2, \dots$$

```
   x_0 ----> g(x_0) = x_1 ----> g(x_1) = x_2 ----> ... ----> α  (Fixed Point)
```

Geometrically, finding a fixed point means finding the $x$-coordinate where the curve $y = g(x)$ intersects the $45^\circ$ line $y = x$.

---

## 2. Convergence Criterion (Lipschitz Condition)

> [!IMPORTANT] 🎯 The Fixed-Point Convergence Theorem
> Let $g(x)$ and $g'(x)$ be continuous on an interval $I = [a, b]$ containing the fixed point $\alpha = g(\alpha)$.
>
> 1. **Sufficient Condition for Convergence**:
>    If there exists a constant $k < 1$ such that:
>    $$|g'(x)| \le k < 1 \quad \forall x \in I$$
>    then the iteration $x_{k+1} = g(x_k)$ is **guaranteed to converge** to the unique fixed point $\alpha$ for any initial guess $x_0 \in I$.
>
> 2. **Condition for Divergence**:
>    If $|g'(x)| > 1$ everywhere on $I$, the iteration **diverges** (escapes to $\pm \infty$ or enters wild oscillations).

---

## 3. Cobweb Diagrams & Graphical Convergence Modes

The magnitude and sign of the slope $g'(x)$ dictate how the sequence behaves:

| Slope Value $|g'(x)|$ | Convergence Type | Visual Pattern (Cobweb Diagram) |
| :--- | :--- | :--- |
| **$0 < g'(x) < 1$** | **Monotonic Convergence** | Step-like staircase climbing/descending directly into the intersection $y=x$. |
| **$-1 < g'(x) < 0$** | **Oscillatory Convergence** | Inward spiral trapping the intersection point. |
| **$g'(x) > 1$** | **Monotonic Divergence** | Step-like staircase escaping outward away from the intersection. |
| **$g'(x) < -1$** | **Oscillatory Divergence** | Outward expanding spiral blowing up to infinity. |

---

## 4. Order of Convergence & Error Analysis

Expand $g(x_k)$ in a Taylor series around the exact root $\alpha$:
$$x_{k+1} = g(x_k) = g(\alpha) + g'(\xi_k)(x_k - \alpha), \quad \xi_k \in (x_k, \alpha)$$

Since $\alpha = g(\alpha)$ and defining the error as $e_k = x_k - \alpha$:
$$\alpha + e_{k+1} = \alpha + g'(\xi_k) e_k$$
$$e_{k+1} = g'(\xi_k) e_k \approx g'(\alpha) e_k$$

- **Order of Convergence ($p$)**: **$p = 1$ (Linear)**.
- **Asymptotic Error Constant ($C$)**: **$C = |g'(\alpha)|$**.
- *Remarkable Special Case*: If $g'(\alpha) = 0$ and $g''(\alpha) \neq 0$, the linear term vanishes and the error becomes quadratic ($p=2$). This is precisely the secret behind the [[Newton-Raphson Method]]!

---

## 5. How to Select the Winning $g(x)$ Rearrangement

> [!TIP] 💡 Exam Strategy for Choosing $g(x)$
> A single equation $f(x) = 0$ can be rearranged into dozens of different $x = g(x)$ formulas. **Always compute $|g'(x)|$ near the root** and choose the form where $|g'(x)| \ll 1$ (the flatter the slope, the faster it converges!).

### Candidate Screening Example: $f(x) = x^3 + x - 1 = 0$ near $x \approx 0.7$

1. **Rearrangement 1**: Isolate $x$ from the linear term:
   $$x = 1 - x^3 \implies g_1(x) = 1 - x^3$$
   $$g_1'(x) = -3x^2 \implies |g_1'(0.7)| = |-3(0.49)| = 1.47 > 1 \quad \text{❌ DIVERGES!}$$

2. **Rearrangement 2**: Factor $x(x^2 + 1) = 1 \implies x = \frac{1}{x^2 + 1}$:
   $$g_2(x) = (x^2 + 1)^{-1}$$
   $$g_2'(x) = \frac{-2x}{(x^2 + 1)^2} \implies |g_2'(0.7)| = \left| \frac{-2(0.7)}{(0.49 + 1)^2} \right| = \frac{1.4}{2.2201} \approx \mathbf{0.6306} < 1 \quad \text{✅ CONVERGES!}$$

3. **Rearrangement 3**: Isolate $x^3 = 1 - x \implies x = (1 - x)^{1/3}$:
   $$g_3(x) = (1 - x)^{1/3}$$
   $$g_3'(x) = -\frac{1}{3(1 - x)^{2/3}} \implies |g_3'(0.7)| = \frac{1}{3(0.3)^{2/3}} \approx \frac{1}{3(0.4481)} \approx \mathbf{0.7438} < 1 \quad \text{✅ CONVERGES!}$$

**Conclusion**: Rearrangement 2 has the smallest derivative magnitude ($0.6306$), making it the fastest convergent choice.

---

## 6. Worked Step-by-Step Examples

### Worked Example 1: Full Iteration Table
> [!EXAMPLE] Problem
> Find a real root of $x^3 + x - 1 = 0$ using the iteration scheme $x_{k+1} = \frac{1}{x_k^2 + 1}$ starting from $x_0 = 0.5$ to $4$ decimal places.

- **Iteration 0**: $x_0 = 0.50000$
- **Iteration 1**:
  $$x_1 = g(x_0) = \frac{1}{(0.5)^2 + 1} = \frac{1}{0.25 + 1} = \frac{1}{1.25} = \mathbf{0.80000}$$
  Error: $|x_1 - x_0| = |0.80000 - 0.50000| = 0.30000$
- **Iteration 2**:
  $$x_2 = g(x_1) = \frac{1}{(0.8)^2 + 1} = \frac{1}{0.64 + 1} = \frac{1}{1.64} = \mathbf{0.60976}$$
  Error: $|x_2 - x_1| = |0.60976 - 0.80000| = 0.19024$
- **Iteration 3**:
  $$x_3 = g(x_2) = \frac{1}{(0.60976)^2 + 1} = \frac{1}{0.37180 + 1} = \frac{1}{1.37180} = \mathbf{0.72897}$$
- **Iteration 4**:
  $$x_4 = g(x_3) = \frac{1}{(0.72897)^2 + 1} = \frac{1}{0.53140 + 1} = \mathbf{0.65299}$$
- **Iteration 5**:
  $$x_5 = g(x_4) = \frac{1}{(0.65299)^2 + 1} = \mathbf{0.70104}$$
- **Iteration 6**:
  $$x_6 = g(x_5) = \frac{1}{(0.70104)^2 + 1} = \mathbf{0.67049}$$
- **Iteration 7**:
  $$x_7 = g(x_6) = \frac{1}{(0.67049)^2 + 1} = \mathbf{0.68986}$$

The sequence spirals inward toward the fixed point **$\alpha \approx 0.6823$**.

---

### Worked Example 2: Aitken's $\Delta^2$ Acceleration
> [!EXAMPLE] Accelerating Convergence
> Given the three consecutive iterates $x_0 = 0.50000, x_1 = 0.80000, x_2 = 0.60976$, use Aitken's $\Delta^2$ formula to compute an accelerated estimate $\hat{x}_0$.

**Step 1: Compute Differences**
- $\Delta x_0 = x_1 - x_0 = 0.80000 - 0.50000 = +0.30000$
- $\Delta x_1 = x_2 - x_1 = 0.60976 - 0.80000 = -0.19024$
- $\Delta^2 x_0 = \Delta x_1 - \Delta x_0 = -0.19024 - 0.30000 = -0.49024$

**Step 2: Apply Aitken's Acceleration Formula**
$$\hat{x}_0 = x_0 - \frac{(\Delta x_0)^2}{\Delta^2 x_0} = 0.50000 - \frac{(0.30000)^2}{-0.49024} = 0.50000 - \frac{0.09000}{-0.49024} = 0.50000 + 0.18358 = \mathbf{0.68358}$$

Notice that with just 2 basic iterations, Aitken's formula jumped directly to $\mathbf{0.68358}$ (accurate to 3 decimal places!), saving 5 iterations!

---

## 7. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Convergence Condition
> For what range of $x$ is the fixed-point iteration $x_{k+1} = \frac{1}{2}\left(x_k + \frac{2}{x_k}\right)$ guaranteed to converge?

> [!SUCCESS]- Step-by-Step Solution
> 1. Compute $g'(x)$ for $g(x) = \frac{1}{2}x + \frac{1}{x}$:
>    $$g'(x) = \frac{1}{2} - \frac{1}{x^2}$$
> 2. Set $|g'(x)| < 1$:
>    $$-1 < \frac{1}{2} - \frac{1}{x^2} < 1$$
> 3. Left inequality: $\frac{1}{2} - \frac{1}{x^2} > -1 \implies \frac{1}{x^2} < \frac{3}{2} \implies x^2 > \frac{2}{3} \implies |x| > \sqrt{\frac{2}{3}} \approx 0.816$.
> 4. Right inequality: $\frac{1}{2} - \frac{1}{x^2} < 1 \implies -\frac{1}{x^2} < \frac{1}{2}$ (always true for all real $x \neq 0$).
> 5. Convergence is guaranteed for all initial points $|x_0| > \sqrt{2/3} \approx 0.816$!

---

## 💻 Python Implementation

```python
def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for k in range(1, max_iter + 1):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, k
        x = x_new
    return x, max_iter
```

---

## 🔗 Related Notes
- [[Roots of Equations]] — Roots vs fixed points.
- [[Newton-Raphson Method]] — Optimal choice of $g(x) = x - \frac{f(x)}{f'(x)}$ where $g'(\alpha) = 0$.
- [[Errors and Convergence]] — Linear convergence proofs.
