---
title: "Lagrange Interpolation"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - interpolation
  - polynomial-interpolation
aliases:
  - "Lagrange Polynomial"
  - "Lagrange Formula"
  - "Method of Undetermined Coefficients"
status: completed
---

# 📐 Lagrange Interpolation (Method of Undetermined Coefficients)

> [!NOTE] 💡 The Big Picture Intuition
> Imagine you are handed a set of data points from a mysterious experiment — maybe temperature readings at specific hours, or position measurements at discrete time steps. You want to find a smooth curve that passes **exactly through every single data point** so you can estimate values between them.
> The **Lagrange Interpolation** method is a brilliant, self-contained formula that constructs the unique polynomial of degree $n-1$ passing through $n$ given data points **without** needing to solve a system of equations! Instead of building the polynomial from scratch by solving a linear system, Lagrange gives you a direct, elegant formula using "basis polynomials" that each do the heavy lifting individually.
> Think of it like building a bridge out of individual pre-fabricated arches — each arch supports exactly one data point, and when you combine them all, the full bridge passes through every point perfectly!

---

## 1. Problem Statement & Setup

Given $n+1$ distinct data points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$ where all $x_i$ are distinct, find the polynomial $P_n(x)$ of degree at most $n$ such that:

$$P_n(x_i) = y_i \quad \text{for } i = 0, 1, \dots, n$$

> [!IMPORTANT] 🎯 Uniqueness Theorem
> There exists a **unique** polynomial of degree $\le n$ passing through $n+1$ distinct points. Lagrange's formula provides an explicit construction of this polynomial.

---

## 2. Construction of Lagrange Basis Polynomials

The key idea is to construct $n+1$ **basis polynomials** $L_0(x), L_1(x), \dots, L_n(x)$, each of degree $n$, with the special property:

$$L_j(x_i) = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$

Each basis polynomial $L_j(x)$ is constructed by taking the product of terms that are zero at every data point **except** $x_j$:

> [!IMPORTANT] 🎯 Lagrange Basis Polynomial Formula
> $$L_j(x) = \prod_{\substack{k=0 \\ k \neq j}}^{n} \frac{x - x_k}{x_j - x_k}$$

**Why this works**:
- When $x = x_j$: every numerator term is $(x_j - x_k) \neq 0$, giving $L_j(x_j) = \prod_{k \neq j} 1 = 1$ ✅
- When $x = x_i$ (where $i \neq j$): one numerator factor is $(x_i - x_i) = 0$, making $L_j(x_i) = 0$ ✅

---

## 3. The Lagrange Interpolation Formula

The interpolating polynomial is the **weighted sum** of all basis polynomials, each weighted by its corresponding $y$-value:

> [!IMPORTANT] 🎯 Lagrange Interpolation Formula
> $$P_n(x) = \sum_{j=0}^{n} y_j \, L_j(x) = \sum_{j=0}^{n} y_j \prod_{\substack{k=0 \\ k \neq j}}^{n} \frac{x - x_k}{x_j - x_k}$$

**Geometric Interpretation**: Each basis polynomial $L_j(x)$ acts like a "selector" — at $x = x_j$ it picks out $y_j$, and at every other data point it contributes nothing. Summing them all constructs the exact interpolant.
---

## 5. Error Analysis & Remainder Term

If $f(x)$ is the original (unknown) function and $P_n(x)$ is its interpolating polynomial through $n+1$ points, the **interpolation error** at any point $x$ in $[a, b]$ containing all nodes is:

> [!IMPORTANT] 🎯 Lagrange Interpolation Error Formula
> $$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod_{i=0}^{n} (x - x_i)$$
> where $\xi \in (a, b)$ is some point that depends on $x$.

**Consequence**: For a polynomial $f(x)$ of degree $\le n$, the error is exactly **zero** — the interpolating polynomial reproduces the function perfectly!

### Error Bound
If $|f^{(n+1)}(x)| \le M_{n+1}$ for all $x \in [a, b]$, then:
$$|f(x) - P_n(x)| \le \frac{M_{n+1}}{(n+1)!} \max_{x \in [a,b]} \left| \prod_{i=0}^{n} (x - x_i) \right|$$
---

## 6. Worked Step-by-Step Examples

### Worked Example 1: Lagrange Interpolation with 3 Points
> [!EXAMPLE] Problem
> Given the data points:
> | $x$ | $0$ | $1$ | $3$ |
> | :---: | :---: | :---: | :---: |
> | $y = f(x)$ | $1$ | $2$ | $4$ |
>
> Find the quadratic Lagrange interpolating polynomial $P_2(x)$ and estimate $f(2)$.

**Step 1: Identify Nodes and Values**
- $x_0 = 0, \; y_0 = 1$
- $x_1 = 1, \; y_1 = 2$
- $x_2 = 3, \; y_2 = 4$

**Step 2: Construct Basis Polynomials**

$$L_0(x) = \frac{(x - 1)(x - 3)}{(0 - 1)(0 - 3)} = \frac{(x-1)(x-3)}{3}$$

$$L_1(x) = \frac{(x - 0)(x - 3)}{(1 - 0)(1 - 3)} = \frac{x(x-3)}{-2}$$

$$L_2(x) = \frac{(x - 0)(x - 1)}{(3 - 0)(3 - 1)} = \frac{x(x-1)}{6}$$

**Step 3: Assemble the Interpolating Polynomial**

$$P_2(x) = 1 \cdot \frac{(x-1)(x-3)}{3} + 2 \cdot \frac{x(x-3)}{-2} + 4 \cdot \frac{x(x-1)}{6}$$

$$P_2(x) = \frac{(x-1)(x-3)}{3} - x(x-3) + \frac{2x(x-1)}{3}$$

Expanding each term:
- $\frac{(x-1)(x-3)}{3} = \frac{x^2 - 4x + 3}{3}$
- $-x(x-3) = -x^2 + 3x$
- $\frac{2x(x-1)}{3} = \frac{2x^2 - 2x}{3}$

Combining over common denominator $3$:
$$P_2(x) = \frac{x^2 - 4x + 3 - 3x^2 + 9x + 2x^2 - 2x}{3} = \frac{3x + 3}{3} = x + 1$$

**Verification**:
- $P_2(0) = 0 + 1 = 1$ ✅
- $P_2(1) = 1 + 1 = 2$ ✅
- $P_2(3) = 3 + 1 = 4$ ✅

**Step 4: Estimate $f(2)$**

$$f(2) \approx P_2(2) = 2 + 1 = \mathbf{3}$$

> [!WARNING] ⚠️ Runge's Phenomenon
> Increasing $n$ (adding more nodes) does **NOT** always improve accuracy! For equidistant nodes, high-degree Lagrange interpolation can oscillate wildly near the endpoints of the interval — this is called **Runge's Phenomenon**. Using **Chebyshev nodes** or **piecewise polynomials** (splines) avoids this issue.
Given $(x_0, y_0)$ and $(x_1, y_1)$:

$$P_1(x) = y_0 \cdot \frac{x - x_1}{x_0 - x_1} + y_1 \cdot \frac{x - x_0}{x_1 - x_0}$$

> [!TIP] 💡 This is just the standard **two-point linear interpolation formula** from algebra!

### Quadratic Interpolation ($n = 2$, 3 data points)
Given $(x_0, y_0), (x_1, y_1), (x_2, y_2)$:

$$P_2(x) = y_0 \cdot \frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)} + y_1 \cdot \frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)} + y_2 \cdot \frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}$$
---

## 2. Construction of Lagrange Basis Polynomials

---

## 7. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why does Lagrange interpolation fail if two $x$-values are identical?
> Explain what happens to the basis polynomial formula when $x_i = x_j$ for some $i \neq j$.

> [!SUCCESS]- Step-by-Step Solution
> 1. The denominator of $L_j(x)$ contains the factor $(x_j - x_i)$.
> 2. If $x_j = x_i$, then $(x_j - x_i) = 0$, making the denominator **zero**.
> 3. Division by zero is undefined, so the Lagrange formula **breaks down**.
> 4. Physically, two points with the same $x$-coordinate but different $y$-values cannot lie on the graph of a function, so interpolation is impossible.
> 5. **Key Assumption**: All $x$-values must be distinct for Lagrange interpolation to work.

---

> [!QUESTION] Practice Question: What is the degree of $P_n(x)$ if we have $n+1$ data points?
> Can the degree ever be less than $n$?

> [!SUCCESS]- Step-by-Step Solution
> 1. The Lagrange formula constructs a polynomial of degree **at most** $n$.
> 2. The degree can be **less than** $n$ if the data happens to lie on a lower-degree polynomial.
> 3. For example, if the data points lie exactly on a line ($y = mx + b$), then with 3 points, $P_2(x)$ will simplify to a degree-1 polynomial (the $x^2$ coefficient cancels to zero).
> 4. Therefore, $\deg(P_n) \le n$, with equality when the data does not lie on a lower-degree curve.

---

## 💻 Python Implementation

```python
def lagrange_interpolation(x_data, y_data, x):
    """
    Evaluate the Lagrange interpolating polynomial at x.
    
    Parameters:
        x_data: list of distinct x-values [x0, x1, ..., xn]
        y_data: list of corresponding y-values [y0, y1, ..., yn]
        x: the point at which to evaluate the polynomial
    
    Returns:
        P_n(x): the interpolated value
    """
    n = len(x_data)
    result = 0.0
    
    for j in range(n):
        # Compute Lagrange basis polynomial L_j(x)
        term = y_data[j]
        for k in range(n):
            if k != j:
                term *= (x - x_data[k]) / (x_data[j] - x_data[k])
        result += term
    
    return result


# Example usage:
x_points = [0, 1, 3]
y_points = [1, 2, 4]

print(f"P_2(2) = {lagrange_interpolation(x_points, y_points, 2)}")  # Output: 3.0
```

---

## 🔗 Related Notes
- [[Newton Divided Difference Interpolation]] — Alternative approach with incremental construction
- [[Newton Forward and Backward Difference Interpolation]] — Special case for equally spaced nodes
- [[Errors and Convergence]] — Interpolation error analysis and Runge's phenomenon
- [[Cubic Spline Interpolation]] — Piecewise approach avoiding Runge's phenomenon
The key idea is to construct $n+1$ **basis polynomials** $L_0(x), L_1(x), \dots, L_n(x)$, each of degree $n$, with the special property:

$$L_j(x_i) = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$

Each basis polynomial $L_j(x)$ is constructed by taking the product of terms that are zero at every data point **except** $x_j$:

> [!IMPORTANT] 🎯 Lagrange Basis Polynomial Formula
> $$L_j(x) = \prod_{\substack{k=0 \\ k \neq j}}^{n} \frac{x - x_k}{x_j - x_k}$$

**Why this works**:
- When $x = x_j$: every numerator term is $(x_j - x_k) \neq 0$, giving $L_j(x_j) = \prod_{k \neq j} 1 = 1$ ✅
- When $x = x_i$ (where $i \neq j$): one numerator factor is $(x_i - x_i) = 0$, making $L_j(x_i) = 0$ ✅