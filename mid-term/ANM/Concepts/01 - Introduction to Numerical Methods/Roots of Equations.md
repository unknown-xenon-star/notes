---
title: "Roots of Equations"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - root-finding
aliases:
  - "Root of an Equation"
  - "Zero of a Function"
status: completed
---

# 🎯 Roots of Equations (Zeros of Functions)

> [!NOTE] 💡 The Big Picture Intuition
> Imagine a submarine descending into the ocean. The surface of the ocean is altitude $y = 0$. A **root** (or zero) of an equation $f(x) = 0$ is the exact moment or position $x = \alpha$ where the submarine crosses sea level:
> $$f(\alpha) = 0$$
> In physical terms, roots represent equilibrium states, break-even points, resonance frequencies, or critical structural thresholds.

---

## 1. Geometric & Physical Meaning

Geometrically, a real root of $f(x) = 0$ is the $x$-coordinate of any point where the graph of $y = f(x)$ touches or slices through the horizontal $x$-axis.

```
       y ^
         |             + (Positive altitude: f(x) > 0)
         |            /
---------+-----------α------------> x  (Sea Level: y = 0)
         |          /
         |         - (Negative altitude: f(x) < 0)
```

---

## 2. Classification of Equations

Equations generally fall into two broad categories:

### A. Algebraic Equations (Polynomials)
An equation formed solely by finite additions, subtractions, and integer powers of $x$:
$$P_n(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 = 0, \quad a_n \neq 0$$

- By the **Fundamental Theorem of Algebra**, an $n$-th degree polynomial has **exactly $n$ roots** (which may be real, complex, or repeated).
- *Specialized Solvers*: [[Graeffe's Root-Squaring Method]], [[Lin-Bairstow Method]].

### B. Transcendental Equations
Equations containing non-algebraic operations like trigonometric ($\sin x, \cos x$), exponential ($e^x$), or logarithmic ($\ln x$) terms.
- *Examples*: $x e^x - 2 = 0$, $x - \tan x = 0$, $\cos x - x = 0$.
- These rarely have closed-form algebraic solutions and must be solved iteratively.
- *General Solvers*: [[Bisection Method]], [[Regula Falsi Method]], [[Newton-Raphson Method]], [[Secant Method]].

---

## 3. Multiplicity of Roots

A root $\alpha$ has **multiplicity $m$** ($m \ge 1$) if we can factor $f(x)$ as:
$$f(x) = (x - \alpha)^m g(x), \quad \text{where } g(\alpha) \neq 0$$

### How to Detect Multiplicity with Derivatives:
1. **Simple Root ($m = 1$)**:
   $$f(\alpha) = 0 \quad \text{and} \quad f'(\alpha) \neq 0$$
   *Visual behavior*: The curve cuts cleanly across the $x$-axis with a non-zero slope.
2. **Double Root ($m = 2$)**:
   $$f(\alpha) = 0, \quad f'(\alpha) = 0, \quad \text{and} \quad f''(\alpha) \neq 0$$
   *Visual behavior*: The curve bounces off (touches tangentially) the $x$-axis without crossing.
3. **General Multiple Root ($m > 1$)**:
   $$f(\alpha) = f'(\alpha) = f''(\alpha) = \dots = f^{(m-1)}(\alpha) = 0, \quad \text{and} \quad f^{(m)}(\alpha) \neq 0$$

> [!WARNING] The Multiple-Root Trap
> Standard algorithms like the [[Newton-Raphson Method]] assume simple roots ($m=1$). When applied to multiple roots ($m > 1$), their speed drops drastically from **quadratic ($p=2$)** to **linear ($p=1$)** unless a multiplicity modification is applied.

---

## 4. Existence & Uniqueness: Intermediate Value Theorem (IVT)

> [!IMPORTANT] Bolzano's Theorem (Existence of a Root)
> Let $f(x)$ be a continuous function on a closed interval $[a, b]$. If $f(a)$ and $f(b)$ have opposite signs:
> $$f(a) \cdot f(b) < 0$$
> then there exists **at least one real root** $\alpha \in (a, b)$ such that $f(\alpha) = 0$.

```
       y ^
         |      + f(b) > 0
         |     /
---------+----+--------> x
       a |   /  b
         |  /
  f(a) < 0 | v
```

### Condition for Uniqueness:
If in addition to $f(a) \cdot f(b) < 0$, the first derivative $f'(x)$ maintains a strictly constant sign on $[a, b]$ (i.e., $f'(x) > 0$ strictly strictly increasing, or $f'(x) < 0$ strictly decreasing):
$$\text{Sign of } f'(x) = \text{constant } \forall x \in [a, b] \implies \text{The root } \alpha \in (a, b) \text{ is unique!}$$

---

## 5. Master Taxonomy of Root-Finding Methods

| Category | Typical Methods | Prerequisites | Guarantee | Convergence Rate |
| :--- | :--- | :--- | :--- | :--- |
| **Bracketing (Closed)** | [[Bisection Method]], [[Regula Falsi Method]] | Two points $a, b$ where $f(a)f(b) < 0$ | **$100\%$ Guaranteed** | Linear ($p = 1$) |
| **Open Methods** | [[Fixed-Point Iteration]], [[Newton-Raphson Method]], [[Secant Method]] | $1$ or $2$ initial guesses near root | May diverge if guess is poor | Superlinear ($p \approx 1.618$) to Quadratic ($p = 2$) |
| **Polynomial Methods** | [[Graeffe's Root-Squaring Method]], [[Lin-Bairstow Method]] | Polynomial coefficients $a_0, a_1, \dots, a_n$ | Finds all roots simultaneously | Depends on squarings / iteration |

---

## 6. Worked Step-by-Step Examples

### Worked Example 1: Root Existence & Uniqueness
> [!EXAMPLE] Problem
> Prove that the equation $f(x) = x e^x - 2 = 0$ has a unique real root in the interval $[0, 1]$.

**Step 1: Check Continuity**
- The function $f(x) = x e^x - 2$ is composed of continuous elementary functions ($x$, $e^x$, and constants). Hence, $f(x)$ is continuous for all $x \in [0, 1]$.

**Step 2: Apply the Intermediate Value Theorem**
- Evaluate at the left endpoint $a = 0$:
  $$f(0) = (0) e^0 - 2 = 0 - 2 = -2 < 0$$
- Evaluate at the right endpoint $b = 1$:
  $$f(1) = (1) e^1 - 2 = e - 2 \approx 2.7183 - 2 = +0.7183 > 0$$
- Compute the product of endpoint signs:
  $$f(0) \cdot f(1) = (-2) \cdot (+0.7183) = -1.4366 < 0$$
- **Conclusion from IVT**: Since $f(0) \cdot f(1) < 0$, at least one real root $\alpha$ exists in $(0, 1)$.

**Step 3: Prove Uniqueness using First Derivative**
- Compute the derivative $f'(x)$ using the product rule:
  $$f'(x) = \frac{d}{dx}(x e^x - 2) = 1 \cdot e^x + x \cdot e^x = (x + 1)e^x$$
- For all $x \in [0, 1]$, $(x + 1) \ge 1 > 0$ and $e^x \ge 1 > 0$.
- Therefore, $f'(x) > 0$ strictly for all $x \in [0, 1]$.
- Because $f(x)$ is strictly increasing across $[0, 1]$, the curve can cross sea level $y=0$ **only once**.
- **Final Result**: There is **exactly one unique real root** in $[0, 1]$.

---

### Worked Example 2: Determining Root Multiplicity
> [!EXAMPLE] Problem
> Determine all roots and their multiplicities for the polynomial $f(x) = x^3 - 3x + 2 = 0$.

**Step 1: Test Rational Candidates**
- By the Rational Root Theorem, potential integer roots are factors of $+2$, namely $\pm 1, \pm 2$.
- Test $x = 1$:
  $$f(1) = 1^3 - 3(1) + 2 = 1 - 3 + 2 = 0 \implies x = 1 \text{ is a root!}$$
- Test $x = -2$:
  $$f(-2) = (-2)^3 - 3(-2) + 2 = -8 + 6 + 2 = 0 \implies x = -2 \text{ is a root!}$$

**Step 2: Check Derivatives at $x = 1$**
- First derivative:
  $$f'(x) = 3x^2 - 3$$
  $$f'(1) = 3(1)^2 - 3 = 0$$
- Second derivative:
  $$f''(x) = 6x$$
  $$f''(1) = 6(1) = 6 \neq 0$$
- Since $f(1) = 0$, $f'(1) = 0$, and $f''(1) \neq 0$, the root **$x = 1$ has multiplicity $m = 2$ (Double Root)**.

**Step 3: Check Derivatives at $x = -2$**
- Evaluate $f'(-2)$:
  $$f'(-2) = 3(-2)^2 - 3 = 3(4) - 3 = 9 \neq 0$$
- Since $f(-2) = 0$ and $f'(-2) \neq 0$, the root **$x = -2$ has multiplicity $m = 1$ (Simple Root)**.

---

## 7. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Locating Root Intervals
> Without graphing, find an integer interval $[k, k+1]$ of length $1$ containing a real root of the transcendental equation:
> $$f(x) = \cos x - x = 0$$

> [!SUCCESS]- Step-by-Step Solution
> 1. Ensure calculator is in **radians** mode!
> 2. Test $x = 0$:
>    $$f(0) = \cos(0) - 0 = 1 - 0 = +1 > 0$$
> 3. Test $x = 1$:
>    $$f(1) = \cos(1) - 1 \approx 0.5403 - 1 = -0.4597 < 0$$
> 4. Since $f(0) > 0$ and $f(1) < 0$, $f(0) \cdot f(1) < 0$.
> 5. By the Intermediate Value Theorem, a real root lies in the interval **$[0, 1]$**. (Known as the Dottie Number, $\alpha \approx 0.739085$).

---

## 🔗 Related Notes
- [[Errors and Convergence]] — How numerical error and iteration speed are defined.
- [[Bisection Method]] — The fundamental bracketing algorithm built on Bolzano's Theorem.
- [[Newton-Raphson Method]] — High-speed root finder utilizing $f'(x)$.
- [[Fixed-Point Iteration]] — Converting $f(x)=0$ to $x=g(x)$.
