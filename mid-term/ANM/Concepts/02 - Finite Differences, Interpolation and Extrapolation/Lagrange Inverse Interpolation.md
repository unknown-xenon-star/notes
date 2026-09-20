---
title: "Lagrange's Inverse Interpolation"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - interpolation
  - inverse-interpolation
aliases:
  - "Inverse Interpolation"
  - "Lagrange Inverse Interpolation"
  - "Reverse Interpolation"
status: completed
---

# 🔄 Lagrange's Inverse Interpolation

> [!NOTE] 💡 The Big Picture Intuition
> Ordinary interpolation answers: *"Given $x$, what is $y$?"* Inverse interpolation flips the question: *"Given $y$, what is $x$?"*
> Picture a vending machine price list: forward interpolation finds the price of item #7; inverse interpolation finds **which item number costs ₹50**. The trick is beautifully simple — **swap the roles of $x$ and $y$**: instead of fitting $y = P(x)$, fit $x = P(y)$ and evaluate it at the given value of $y$.
> The killer exam application: **root-finding without iteration** — since a root of $f(x) = 0$ is just the $x$ where $y = 0$, inverse interpolation directly extracts the root from a small table of $(x_i, f(x_i))$ values in a single shot!

---

## 1. Problem Statement & Setup

Given a tabulated function known at points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$ where $y_i = f(x_i)$, find the value of $x$ corresponding to a given (non-tabulated) value of $y$:

$$\text{Find } x \text{ such that } f(x) = y, \quad \text{given the table } (x_i, y_i)$$

> [!IMPORTANT] 🎯 The Core Idea: Swap the Variables
> Instead of constructing $y = P_n(x)$ and solving the equation $P_n(x) = y$ (which would itself require an iterative root-finder!), we construct the **inverse polynomial**:
> $$x = P_n(y)$$
> This is exactly [[Lagrange Interpolation]] applied with $x$ and $y$ interchanged — the $y_i$ act as the "nodes" and the $x_i$ as the "values."

---

## 2. The Inverse Lagrange Formula

Treating $y$ as the independent variable, the Lagrange basis polynomials are built on the $y$-nodes:

$$L_j(y) = \prod_{\substack{k=0 \\ k \neq j}}^{n} \frac{y - y_k}{y_j - y_k}$$

> [!IMPORTANT] 🎯 Lagrange's Inverse Interpolation Formula
> $$x = P_n(y) = \sum_{j=0}^{n} x_j \, L_j(y) = \sum_{j=0}^{n} x_j \prod_{\substack{k=0 \\ k \neq j}}^{n} \frac{y - y_k}{y_j - y_k}$$
> The formula is **identical in structure** to the forward Lagrange formula — only the roles of $x$ and $y$ are exchanged.

**Why it works**:
- When $y = y_j$: every basis factor becomes $\frac{y_j - y_k}{y_j - y_k} = 1$, so $x = x_j$ ✅
- The formula exactly reproduces every tabulated pair $(x_i, y_i)$ ✅

### Special Case: Finding a Root of $f(x) = 0$ (set $y = 0$)

The most important exam application. Substituting $y = 0$ into the three-point inverse formula gives the closed-form root estimate:

> [!IMPORTANT] 🎯 Three-Point Root Formula (Inverse Interpolation at $y = 0$)
> $$x = x_0 \cdot \frac{y_1 y_2}{(y_0 - y_1)(y_0 - y_2)} + x_1 \cdot \frac{y_0 y_2}{(y_1 - y_0)(y_1 - y_2)} + x_2 \cdot \frac{y_0 y_1}{(y_2 - y_0)(y_2 - y_1)}$$
> Valid whenever the three $y$-values are distinct (each term's denominator is non-zero).

> [!TIP] 💡 Exam Shortcut: Degenerates to the Secant Formula
> With only **two** points $(x_0, y_0), (x_1, y_1)$ and target $y = 0$, the inverse formula collapses to
> $$x = \frac{x_0 y_1 - x_1 y_0}{y_1 - y_0}$$
> which is exactly the secant / [[Regula Falsi Method]] root estimate. Inverse interpolation is thus the **natural generalization** of the secant idea to three or more points.

---

## 3. When Is Inverse Interpolation Valid?

> [!WARNING] ⚠️ The Monotonicity Requirement
> Strictly speaking, $f$ must be **one-to-one (monotonic)** near the data — otherwise one $y$-value could correspond to several $x$-values and the "inverse" becomes ambiguous.
> **Exam rule of thumb**: apply the method **locally**, using points that bracket the target $y$-value within a region where $f$ does not turn around. All the classic uses (finding roots, finding $x$ at a specified $y$ in monotonic tables) satisfy this.

---

## 4. Worked Step-by-Step Examples

### Worked Example 1: Finding $x$ for a Given $y$
> [!EXAMPLE] Problem
> Given the tabulated function:
> | $x$ | $3$ | $4$ | $5$ |
> | :---: | :---: | :---: | :---: |
> | $y = f(x)$ | $0.50$ | $0.25$ | $0.20$ |
>
> Find the value of $x$ for which $y = \dfrac{1}{3}$ using Lagrange inverse interpolation.

**Step 1: Identify the swapped nodes and the target**
- $y_0 = 0.50,\ x_0 = 3$
- $y_1 = 0.25,\ x_1 = 4$
- $y_2 = 0.20,\ x_2 = 5$
- Target: $y = \frac{1}{3} \approx 0.333333$

**Step 2: Compute each basis term at $y = \frac{1}{3}$**

$$\text{Term}_0 = x_0 \cdot \frac{(y - y_1)(y - y_2)}{(y_0 - y_1)(y_0 - y_2)} = 3 \cdot \frac{(0.333333 - 0.25)(0.333333 - 0.20)}{(0.50 - 0.25)(0.50 - 0.20)} = 3 \cdot \frac{(0.083333)(0.133333)}{(0.25)(0.30)} = 3 \cdot \frac{0.011111}{0.075} = 0.444444$$

$$\text{Term}_1 = x_1 \cdot \frac{(y - y_0)(y - y_2)}{(y_1 - y_0)(y_1 - y_2)} = 4 \cdot \frac{(0.333333 - 0.50)(0.333333 - 0.20)}{(0.25 - 0.50)(0.25 - 0.20)} = 4 \cdot \frac{(-0.166667)(0.133333)}{(-0.25)(0.05)} = 4 \cdot \frac{-0.022222}{-0.0125} = 7.111111$$

$$\text{Term}_2 = x_2 \cdot \frac{(y - y_0)(y - y_1)}{(y_2 - y_0)(y_2 - y_1)} = 5 \cdot \frac{(0.333333 - 0.50)(0.333333 - 0.25)}{(0.20 - 0.50)(0.20 - 0.25)} = 5 \cdot \frac{(-0.166667)(0.083333)}{(-0.30)(-0.05)} = 5 \cdot \frac{-0.013889}{0.015} = -4.629630$$

**Step 3: Sum the terms**

$$x = 0.444444 + 7.111111 - 4.629630 = \mathbf{2.925926} \approx \mathbf{2.9259}$$

**Step 4: Comment on accuracy**
The data comes from $f(x) = \frac{1}{x}$, for which the true answer is $x = 3$. The estimate $2.9259$ has an absolute error of $\approx 0.074$ — the inverse of a quadratic in $x$ is **not** a quadratic in $y$, so some error is expected. The estimate improves rapidly as the tabulated points are taken closer together around the target $y$.

---

### Worked Example 2: Finding a Root of $f(x) = 0$ (Classic Exam Pattern)
> [!EXAMPLE] Problem
> The function $f(x) = x^3 - 3x + 1$ is tabulated at three points:
> | $x$ | $1.4$ | $1.5$ | $1.6$ |
> | :---: | :---: | :---: | :---: |
> | $f(x)$ | $-0.456$ | $-0.125$ | $0.296$ |
>
> Find the root of $f(x) = 0$ lying in $[1.4,\ 1.6]$ by Lagrange inverse interpolation.

**Step 1: Setup** — target $y = 0$, with $y_0 = -0.456,\ y_1 = -0.125,\ y_2 = 0.296$ and $x_0 = 1.4,\ x_1 = 1.5,\ x_2 = 1.6$.

**Step 2: Apply the three-point root formula**

$$x = x_0 \cdot \frac{y_1 y_2}{(y_0 - y_1)(y_0 - y_2)} + x_1 \cdot \frac{y_0 y_2}{(y_1 - y_0)(y_1 - y_2)} + x_2 \cdot \frac{y_0 y_1}{(y_2 - y_0)(y_2 - y_1)}$$

**Step 3: Evaluate each term**

$$\text{Term}_0 = 1.4 \times \frac{(-0.125)(0.296)}{(-0.331)(-0.752)} = 1.4 \times \frac{-0.037000}{0.248912} = -0.208106$$

$$\text{Term}_1 = 1.5 \times \frac{(-0.456)(0.296)}{(0.331)(-0.421)} = 1.5 \times \frac{-0.134976}{-0.139351} = 1.452907$$

$$\text{Term}_2 = 1.6 \times \frac{(-0.456)(-0.125)}{(0.752)(0.421)} = 1.6 \times \frac{0.057000}{0.316592} = 0.288068$$

**Step 4: Sum**

$$x = -0.208106 + 1.452907 + 0.288068 = \mathbf{1.532869} \approx \mathbf{1.5329}$$

**Step 5: Verify against the true root**
The true root of $x^3 - 3x + 1 = 0$ in $[1.4, 1.6]$ is $x \approx 1.5321$.

- Absolute error: $|1.5321 - 1.5329| \approx \mathbf{0.0008}$ ✅ — excellent for a single shot!
- Residual check: $f(1.5329) \approx +0.003$, essentially zero on the scale of the tabulated values ✅
- The estimate lies inside the sign-change bracket $[1.4, 1.6]$ ✅

> [!SUCCESS] ✅ Why This Beats Naive Methods
> One evaluation, no iteration, no derivatives — and it already beats a couple of steps of bisection. Adding a **fourth point** (cubic inverse interpolation) pushes the error even lower. Compare: two-point inverse interpolation = [[Secant Method]] ($p \approx 1.618$); the three-point version gains accuracy by using curvature information of the inverse function.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why not just solve $P_n(x) = y$ directly?
> Forward interpolation gives $y = P_n(x)$. Given $y$, why do we build $x = P_n(y)$ instead of solving the forward polynomial equation?

> [!SUCCESS]- Step-by-Step Solution
> 1. Solving $P_n(x) = y$ means finding roots of a degree-$n$ polynomial — an **iterative** problem (Newton-Raphson, etc.).
> 2. Building $x = P_n(y)$ is a **direct, one-shot formula** — no iteration, no derivatives, no convergence worries.
> 3. The cost: the inverse polynomial is only a good approximation of the true inverse when $f$ is smooth and locally monotonic (see the monotonicity warning above).
> 4. Hence inverse interpolation trades a root-finding problem for a single evaluation — ideal for quick hand computation in exams.

---

> [!QUESTION] Practice Question: Connection to the Secant Method
> Show that inverse interpolation with **two** points and target $y = 0$ yields exactly the secant estimate.

> [!SUCCESS]- Step-by-Step Solution
> 1. Two-point inverse Lagrange formula with target $y = 0$:
>    $$x = x_0 \cdot \frac{(0 - y_1)}{(y_0 - y_1)} + x_1 \cdot \frac{(0 - y_0)}{(y_1 - y_0)}$$
> 2. Simplify:
>    $$x = \frac{-x_0 y_1}{y_0 - y_1} + \frac{-x_1 y_0}{y_1 - y_0} = \frac{x_0 y_1 - x_1 y_0}{y_1 - y_0}$$
> 3. This is exactly the **[[Regula Falsi Method]] / [[Secant Method]]** interpolation estimate for the root.
> 4. Conclusion: inverse interpolation **generalizes** the secant idea to three or more points.

---

## 💻 Python Implementation

```python
def inverse_lagrange(x_data, y_data, y):
    """
    Estimate x such that f(x) = y, using Lagrange inverse interpolation.

    Parameters:
        x_data: list of x-values [x0, x1, ..., xn]
        y_data: list of corresponding y-values [y0, y1, ..., yn]
        y:      the target y-value (e.g., 0 to find a root)

    Returns:
        x estimate such that f(x) ≈ y
    """
    n = len(x_data)
    result = 0.0

    for j in range(n):
        # Basis polynomial in the SWAPPED variable (built on y-nodes)
        term = x_data[j]
        for k in range(n):
            if k != j:
                term *= (y - y_data[k]) / (y_data[j] - y_data[k])
        result += term

    return result


# Example usage: root of f(x) = x^3 - 3x + 1 from three tabulated points
x_points = [1.4, 1.5, 1.6]
y_points = [-0.456, -0.125, 0.296]

print(f"Root x = {inverse_lagrange(x_points, y_points, 0.0):.4f}")  # Output: 1.5329
```

---

## 🔗 Related Notes
- [[Lagrange Interpolation]] — The forward version this method is built from
- [[Secant Method]] — Degenerates to inverse interpolation with two points
- [[Regula Falsi Method]] — Same two-point root estimate inside a bracket
- [[Newton Divided Difference Interpolation]] — Alternative forward construction
