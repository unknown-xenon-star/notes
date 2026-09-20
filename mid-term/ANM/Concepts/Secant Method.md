---
title: "Secant Method"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - root-finding
  - open-methods
aliases:
  - "Secant Algorithm"
  - "Interpolation Method"
status: completed
---

# 📐 Secant Method

> [!NOTE] 💡 The Big Picture Intuition
> [[Newton-Raphson Method]] is extremely fast, but it has a major drawback: you must analytically calculate the derivative $f'(x)$. In real-world engineering (like CFD simulations or financial models), $f'(x)$ might be impossible or computationally painful to find!
> The **Secant Method** is Newton's method with a clever shortcut: instead of calculating the exact derivative slope, it estimates the slope using your **two most recent footsteps**:
> $$\text{Slope } \approx \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}$$
> It shoots a line through those two recent points to find the next ground hit $x_{k+1}$!

---

## 1. Derivation of the Secant Formula

```
       y ^            (x_k, f(x_k))
         |           /
         |          /  Secant Line through 2 most recent points
---------+-------x_{k+1}----+--------> x
         |      /     |    x_k
  (x_{k-1}, f(x_{k-1}))
```

In Newton-Raphson:
$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$

Replace the derivative $f'(x_k)$ with the backward finite difference slope:
$$f'(x_k) \approx \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}$$

Substitute this into Newton's formula:

> [!IMPORTANT] 🎯 Secant Iteration Formula
> $$x_{k+1} = x_k - f(x_k) \left[ \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})} \right] = \frac{x_{k-1}f(x_k) - x_k f(x_{k-1})}{f(x_k) - f(x_{k-1})}$$
> 
> *Key Operational Rule*: You **always** use the two latest computed points ($x_k$ and $x_{k-1}$). You do **not** check for sign changes or keep an interval bracket!

---

## 2. The Golden Ratio Convergence Proof ($p \approx 1.618$)

Let $\alpha$ be the exact root and $e_k = x_k - \alpha$. Using Taylor series expansions of $f(x_k)$ and $f(x_{k-1})$ about $\alpha$, we obtain the error relation:
$$e_{k+1} \approx C \cdot e_k \cdot e_{k-1}, \quad \text{where } C = \frac{f''(\alpha)}{2 f'(\alpha)}$$

To find the order of convergence $p$, assume the asymptotic relation $e_{k+1} \sim A e_k^p$.
Then $e_k \sim A e_{k-1}^p \implies e_{k-1} \sim (e_k / A)^{1/p}$.

Substitute this into the error product:
$$e_{k+1} \approx C e_k (e_k^{1/p}) = C e_k^{1 + 1/p}$$

Equating the exponents of $e_k$:
$$p = 1 + \frac{1}{p} \implies p^2 - p - 1 = 0$$

Solving the quadratic equation for $p > 0$:
$$p = \frac{1 + \sqrt{5}}{2} \approx \mathbf{1.6180339887\dots} \quad \text{(The Golden Ratio } \phi \text{!)}$$

> [!IMPORTANT] 🎯 Summary of Convergence Properties
> - **Order of Convergence ($p$)**: **$p \approx 1.618$ (Superlinear)**.
> - Faster than linear methods ($p=1$), slightly slower per iteration than Newton ($p=2$).

---

## 3. Computational Efficiency Index ($I = p^{1/n}$)

Why do many professional software packages use the Secant Method instead of Newton-Raphson? Because of the **Efficiency Index**:

Let $p$ be the order of convergence, and $n$ be the number of function evaluations required per iteration:
$$I = p^{1/n}$$

| Algorithm | Order $p$ | Evaluations / Step ($n$) | Efficiency Index ($I = p^{1/n}$) |
| :--- | :---: | :---: | :---: |
| **[[Newton-Raphson Method]]** | $p = 2.000$ | $2$ ($f$ and $f'$) | $I = 2^{1/2} = \sqrt{2} \approx \mathbf{1.414}$ |
| **[[Secant Method]]** | $p \approx 1.618$ | **$1$** (re-uses $f(x_{k-1})$, evaluates only $f(x_k)$) | $I = 1.618^{1/1} \approx \mathbf{1.618}$ |

> [!TIP] 💡 Exam Takeaway
> Per function evaluation, the **Secant Method is computationally more efficient** than Newton's method ($1.618 > 1.414$)!

---

## 4. Master 3-Way Comparison: Secant vs. Newton vs. Regula Falsi

| Metric | [[Newton-Raphson Method]] | [[Secant Method]] | [[Regula Falsi Method]] |
| :--- | :--- | :--- | :--- |
| **Class** | Open Method | Open Method | Bracketing Method |
| **Required Starting Points** | $1$ initial guess ($x_0$) | $2$ initial guesses ($x_0, x_1$) | $2$ bracket points ($a, b$ where $f(a)f(b)<0$) |
| **Requires $f'(x)$?** | **Yes** (analytical derivative) | **No** | **No** |
| **Formula Used** | $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$ | $x_{k+1} = \frac{x_{k-1}f(x_k) - x_k f(x_{k-1})}{f(x_k)-f(x_{k-1})}$ | $c = \frac{a f(b) - b f(a)}{f(b)-f(a)}$ |
| **Point Replacement** | Overwrites single value | Always uses 2 newest points | Replaces point with matching sign |
| **Order of Convergence** | $p = 2.000$ (Quadratic) | $p \approx 1.618$ (Superlinear) | $p = 1.000$ (Linear) |
| **Convergence Guarantee** | Local (can diverge) | Local (can diverge) | **Global (always converges)** |

---

## 5. Worked Step-by-Step Examples

### Worked Example 1: Full Numerical Calculation
> [!EXAMPLE] Problem
> Find a real root of $f(x) = x^3 - 2x - 5 = 0$ using the Secant Method with initial guesses $x_0 = 2$ and $x_1 = 3$ for 3 iterations.

**Step 1: Evaluate Initial Points**
- $f(x_0) = f(2) = (2)^3 - 2(2) - 5 = 8 - 4 - 5 = \mathbf{-1.000000}$
- $f(x_1) = f(3) = (3)^3 - 2(3) - 5 = 27 - 6 - 5 = \mathbf{+16.000000}$

**Step 2: Line-by-Line Iterations**

- **Iteration 1 ($k=1 \implies$ Compute $x_2$):**
  $$x_2 = x_1 - f(x_1) \left[ \frac{x_1 - x_0}{f(x_1) - f(x_0)} \right] = 3 - (16) \left[ \frac{3 - 2}{16 - (-1)} \right] = 3 - \frac{16}{17} \approx \mathbf{2.058824}$$
  Evaluate $f(x_2)$:
  $$f(2.058824) = (2.058824)^3 - 2(2.058824) - 5 = 8.726396 - 4.117648 - 5 = \mathbf{-0.391252}$$

- **Iteration 2 ($k=2 \implies$ Compute $x_3$):**
  Use $x_1 = 3$ and $x_2 = 2.058824$:
  $$x_3 = x_2 - f(x_2) \left[ \frac{x_2 - x_1}{f(x_2) - f(x_1)} \right] = 2.058824 - (-0.391252) \left[ \frac{2.058824 - 3}{-0.391252 - 16} \right]$$
  $$x_3 = 2.058824 - (-0.391252) \left[ \frac{-0.941176}{-16.391252} \right] = 2.058824 - (-0.391252)(0.057419) = 2.058824 + 0.022465 = \mathbf{2.081289}$$
  Evaluate $f(x_3)$:
  $$f(2.081289) = (2.081289)^3 - 2(2.081289) - 5 = 9.015141 - 4.162578 - 5 = \mathbf{-0.147437}$$

- **Iteration 3 ($k=3 \implies$ Compute $x_4$):**
  Use $x_2 = 2.058824$ and $x_3 = 2.081289$:
  $$x_4 = x_3 - f(x_3) \left[ \frac{x_3 - x_2}{f(x_3) - f(x_2)} \right] = 2.081289 - (-0.147437) \left[ \frac{2.081289 - 2.058824}{-0.147437 - (-0.391252)} \right]$$
  $$x_4 = 2.081289 - (-0.147437) \left[ \frac{0.022465}{0.243815} \right] = 2.081289 - (-0.147437)(0.092140) = 2.081289 + 0.013585 = \mathbf{2.094874}$$
  Evaluate $f(x_4)$:
  $$f(2.094874) = (2.094874)^3 - 2(2.094874) - 5 \approx \mathbf{+0.003608}$$

### Iteration Summary Table:

| Iteration ($k$) | $x_{k-1}$ | $x_k$ | $f(x_{k-1})$ | $f(x_k)$ | Next Iterate $x_{k+1}$ | $f(x_{k+1})$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $2.000000$ | $3.000000$ | $-1.000000$ | $+16.000000$ | **$2.058824$** | $-0.391252$ |
| **2** | $3.000000$ | $2.058824$ | $+16.000000$ | $-0.391252$ | **$2.081289$** | $-0.147437$ |
| **3** | $2.058824$ | $2.081289$ | $-0.391252$ | $-0.147437$ | **$2.094874$** | $+0.003608$ |

Notice how quickly $f(x)$ plummeted to $+0.0036$! The root is **$\alpha \approx 2.0948$**.

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Secant vs Regula Falsi Difference
> Suppose during an iteration $k$, both $f(x_k) > 0$ and $f(x_{k-1}) > 0$. Can the Secant method proceed? Can Regula Falsi proceed?

> [!SUCCESS]- Step-by-Step Solution
> 1. **Secant Method**: **YES**. Secant does not care about signs. It only uses the algebraic values of the two most recent points to draw the secant line.
> 2. **Regula Falsi**: **NO**. Regula Falsi is a bracketing method that strictly requires $f(a) \cdot f(b) < 0$. If both endpoints have the same sign, the bracket is broken and Regula Falsi cannot execute.

---

## 💻 Python Implementation

```python
def secant_method(f, x0, x1, tol=1e-6, max_iter=50):
    for k in range(1, max_iter + 1):
        f0, f1 = f(x0), f(x1)
        if abs(f1 - f0) < 1e-12:
            raise ZeroDivisionError("Denominator too close to zero!")
            
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        
        if abs(x2 - x1) < tol or abs(f(x2)) < tol:
            return x2, k
            
        x0, x1 = x1, x2
        
    return x1, max_iter
```

---

## 🔗 Related Notes
- [[Newton-Raphson Method]] — Tangent baseline.
- [[Regula Falsi Method]] — Bracketing version of the secant formula.
- [[Errors and Convergence]] — Superlinear convergence proofs.
