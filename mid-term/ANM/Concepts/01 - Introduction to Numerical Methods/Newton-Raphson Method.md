---
title: "Newton-Raphson Method"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - root-finding
  - open-methods
aliases:
  - "Newton's Method"
  - "Tangent Method"
status: completed
---

# 🚀 Newton-Raphson Method (Newton's Method)

> [!NOTE] 💡 The Big Picture Intuition (The Ski Slope Analogy)
> Imagine standing on a hilly curve $y = f(x)$ at your current guess $(x_k, f(x_k))$. You want to find where the hill meets the ground ($y = 0$). 
> Instead of walking blindly, you look down at the slope beneath your feet (the derivative $f'(x_k)$) and shoot a straight laser beam down that **tangent line**. Wherever that beam strikes the ground is your next guess $x_{k+1}$! 
> Because tangent lines fit smooth curves exceptionally well, this method hurtles toward the root with **quadratic speed ($p=2$)**, approximately **doubling the number of correct decimal digits on every single step**!

---

## 1. Mathematical Derivations

### Derivation 1: Tangent Line Geometry
Consider the tangent line to the curve $y = f(x)$ passing through the point $(x_k, f(x_k))$ with slope $m = f'(x_k)$.
The point-slope equation of the tangent line is:
$$y - f(x_k) = f'(x_k)(x - x_k)$$

To find the $x$-intercept $x_{k+1}$, set $y = 0$:
$$0 - f(x_k) = f'(x_k)(x_{k+1} - x_k)$$
$$-f(x_k) = f'(x_k) x_{k+1} - f'(x_k) x_k$$

```
       y ^            . (x_k, f(x_k))
         |           /|
         |          / |  Tangent Line (slope = f'(x_k))
---------+-------x_{k+1}----+--------> x
         |      /     |    x_k
         |     /      |
```

> [!IMPORTANT] 🎯 Newton-Raphson Iteration Formula
> $$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}, \quad f'(x_k) \neq 0$$

---

### Derivation 2: Taylor Series Truncation
Expand $f(x)$ in a Taylor series about the current estimate $x_k$:
$$f(x) = f(x_k) + f'(x_k)(x - x_k) + \frac{f''(\xi)}{2!}(x - x_k)^2 + \dots$$

Setting $x = x_{k+1}$ where $f(x_{k+1}) \approx 0$ and dropping second and higher-order terms:
$$0 \approx f(x_k) + f'(x_k)(x_{k+1} - x_k) \implies x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$

---

## 2. Rigorous Proof of Quadratic Convergence ($p = 2$)

Let $\alpha$ be a simple root ($f(\alpha) = 0$ and $f'(\alpha) \neq 0$), and define the error at step $k$ as $e_k = x_k - \alpha$.
Express Newton-Raphson as a fixed-point iteration $x_{k+1} = g(x_k)$ where:
$$g(x) = x - \frac{f(x)}{f'(x)}$$

### Step 1: Differentiate $g(x)$ using the Quotient Rule
$$g'(x) = 1 - \frac{[f'(x)]^2 - f(x)f''(x)}{[f'(x)]^2} = 1 - 1 + \frac{f(x)f''(x)}{[f'(x)]^2} = \frac{f(x)f''(x)}{[f'(x)]^2}$$

### Step 2: Evaluate $g'(x)$ at the True Root $x = \alpha$
Since $f(\alpha) = 0$ and $f'(\alpha) \neq 0$:
$$g'(\alpha) = \frac{0 \cdot f''(\alpha)}{[f'(\alpha)]^2} = 0$$

### Step 3: Expand $g(x_k)$ in a Taylor Series about $\alpha$
$$x_{k+1} = g(x_k) = g(\alpha) + g'(\alpha)(x_k - \alpha) + \frac{g''(\alpha)}{2!}(x_k - \alpha)^2 + \mathcal{O}((x_k - \alpha)^3)$$
$$\alpha + e_{k+1} = \alpha + 0 \cdot e_k + \frac{g''(\alpha)}{2} e_k^2 + \dots$$
$$e_{k+1} \approx \frac{g''(\alpha)}{2} e_k^2$$

Differentiating $g'(x)$ to find $g''(\alpha)$:
$$g''(\alpha) = \frac{f''(\alpha)}{f'(\alpha)}$$

> [!IMPORTANT] 🎯 Conclusion: Quadratic Convergence Law
> $$e_{k+1} \approx \frac{f''(\alpha)}{2 f'(\alpha)} e_k^2$$
> - **Order of Convergence**: **$p = 2$ (Quadratic)** for simple roots.
> - **Asymptotic Error Constant**: **$C = \left| \frac{f''(\alpha)}{2 f'(\alpha)} \right|$**.

---

## 3. High-Yield Special Formulas Derived from Newton's Method

Newton's method is the secret engine powering hardware math co-processors for division and root extraction:

### A. Square Root Extraction ($\sqrt{N}$)
Solve $f(x) = x^2 - N = 0 \implies f'(x) = 2x$:
$$x_{k+1} = x_k - \frac{x_k^2 - N}{2x_k} = \frac{2x_k^2 - x_k^2 + N}{2x_k} = \mathbf{\frac{1}{2}\left(x_k + \frac{N}{x_k}\right)} \quad \text{(Heron's Formula / Babylonian Method)}$$

### B. $p$-th Root Extraction ($\sqrt[p]{N}$)
Solve $f(x) = x^p - N = 0 \implies f'(x) = p x^{p-1}$:
$$x_{k+1} = \mathbf{\frac{1}{p}\left((p-1)x_k + \frac{N}{x_k^{p-1}}\right)}$$

### C. Reciprocal Calculation ($\frac{1}{N}$ without hardware division)
Solve $f(x) = \frac{1}{x} - N = 0 \implies f'(x) = -\frac{1}{x^2}$:
$$x_{k+1} = x_k - \frac{\frac{1}{x_k} - N}{-1/x_k^2} = x_k + x_k^2\left(\frac{1}{x_k} - N\right) = \mathbf{x_k(2 - N x_k)}$$

---

## 4. Failure Modes & Exam Traps

```
   1. Horizontal Tangent          2. Cycle / Oscillation Trap         3. Local Extrema Shootoff
      f'(x_k) = 0                   f(x) = x^3 - 5x near x_0 = 1         Shoots iterate to ±∞
```

> [!WARNING] Common Failure Cases
> 1. **Zero Derivative ($f'(x_k) = 0$)**: Division by zero! Tangent is horizontal and never touches the $x$-axis.
> 2. **Inflection Point Oscillations**: The tangents bounce back and forth between two points forever.
> 3. **Multiple Roots ($m > 1$)**: When $f(\alpha) = 0$ and $f'(\alpha) = 0$, $g'(\alpha) \neq 0$, causing convergence to degrade to **slow linear ($p=1$)**.

### Remedies for Multiple Roots:
1. **If multiplicity $m$ is known**:
   $$x_{k+1} = x_k - m \frac{f(x_k)}{f'(x_k)}$$
2. **If multiplicity is unknown (Schröder's Method)**: Define $u(x) = \frac{f(x)}{f'(x)}$ and apply Newton:
   $$x_{k+1} = x_k - \frac{f(x_k)f'(x_k)}{[f'(x_k)]^2 - f(x_k)f''(x_k)}$$

---

## 5. Worked Step-by-Step Examples

### Worked Example 1: Standard Polynomial Root
> [!EXAMPLE] Problem
> Find the real root of $f(x) = x^3 - 2x - 5 = 0$ starting from $x_0 = 2$ correct to 5 decimal places using Newton-Raphson.

**Step 1: Compute Derivatives**
- $f(x) = x^3 - 2x - 5$
- $f'(x) = 3x^2 - 2$

**Step 2: Formulate Specific Iteration Scheme**
$$x_{k+1} = x_k - \frac{x_k^3 - 2x_k - 5}{3x_k^2 - 2} = \frac{3x_k^3 - 2x_k - (x_k^3 - 2x_k - 5)}{3x_k^2 - 2} = \frac{2x_k^3 + 5}{3x_k^2 - 2}$$

**Step 3: Line-by-Line Calculations**

- **Iteration 0 ($x_0 = 2$):**
  $$x_1 = \frac{2(2)^3 + 5}{3(2)^2 - 2} = \frac{2(8) + 5}{3(4) - 2} = \frac{16 + 5}{12 - 2} = \frac{21}{10} = \mathbf{2.100000}$$

- **Iteration 1 ($x_1 = 2.1$):**
  $$f(2.1) = (2.1)^3 - 2(2.1) - 5 = 9.261 - 4.2 - 5 = 0.061000$$
  $$f'(2.1) = 3(2.1)^2 - 2 = 3(4.41) - 2 = 13.23 - 2 = 11.230000$$
  $$x_2 = 2.1 - \frac{0.061000}{11.230000} = 2.1 - 0.00543188 = \mathbf{2.094568}$$

- **Iteration 2 ($x_2 = 2.094568$):**
  $$f(2.094568) = (2.094568)^3 - 2(2.094568) - 5 = 0.000185$$
  $$f'(2.094568) = 3(2.094568)^2 - 2 = 11.161435$$
  $$x_3 = 2.094568 - \frac{0.000185}{11.161435} = 2.094568 - 0.00001657 = \mathbf{2.094551}$$

- **Iteration 3 ($x_3 = 2.094551$):**
  $$f(2.094551) \approx 0.000000$$
  $$x_4 = \mathbf{2.094551}$$

**Final Result**: The root is **$\alpha \approx 2.09455$** (achieved full 5-digit accuracy in just 3 steps!).

---

### Worked Example 2: Lightning-Fast Square Root ($\sqrt{12}$)
> [!EXAMPLE] Problem
> Compute $\sqrt{12}$ using Heron's formula starting from $x_0 = 3$.

- **Iteration 0**: $x_0 = 3$
- **Iteration 1**:
  $$x_1 = \frac{1}{2}\left(3 + \frac{12}{3}\right) = \frac{1}{2}(3 + 4) = \frac{7}{2} = \mathbf{3.500000}$$
- **Iteration 2**:
  $$x_2 = \frac{1}{2}\left(3.5 + \frac{12}{3.5}\right) = \frac{1}{2}(3.5 + 3.428571) = \frac{6.928571}{2} = \mathbf{3.464286}$$
- **Iteration 3**:
  $$x_3 = \frac{1}{2}\left(3.464286 + \frac{12}{3.464286}\right) = \frac{1}{2}(3.464286 + 3.463917) = \mathbf{3.464102}$$

Exact value: $\sqrt{12} \approx 3.464101615$. Notice how $x_3$ is accurate to 6 decimal places!

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Reciprocal without Division
> Use Newton's reciprocal formula to compute $\frac{1}{7}$ starting with $x_0 = 0.1$ for 2 iterations.

> [!SUCCESS]- Step-by-Step Solution
> 1. Formula: $x_{k+1} = x_k(2 - 7x_k)$.
> 2. Iteration 1 ($x_0 = 0.1$):
>    $$x_1 = 0.1(2 - 7(0.1)) = 0.1(2 - 0.7) = 0.1(1.3) = \mathbf{0.1300}$$
> 3. Iteration 2 ($x_1 = 0.13$):
>    $$x_2 = 0.13(2 - 7(0.13)) = 0.13(2 - 0.91) = 0.13(1.09) = \mathbf{0.1417}$$
> 4. True value: $\frac{1}{7} \approx 0.142857$. $x_2$ has already captured the first 3 digits without ever performing division!

---

## 💻 Python Implementation

```python
def newton_raphson(f, df, x0, tol=1e-7, max_iter=50):
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            raise ZeroDivisionError(f"Zero derivative encountered at x = {x}")
        
        x_new = x - fx / dfx
        if abs(x_new - x) < tol or abs(fx) < tol:
            return x_new, k
        x = x_new
    return x, max_iter
```

---

## 🔗 Related Notes
- [[Secant Method]] — Eliminates the need for derivative computation.
- [[Fixed-Point Iteration]] — Theoretical umbrella for $x_{k+1} = g(x_k)$.
- [[Errors and Convergence]] — Quadratic error analysis.
