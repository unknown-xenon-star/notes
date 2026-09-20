---
title: "Newton Divided Difference Interpolation"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - interpolation
  - divided-difference
aliases:
  - "Newton's Divided Difference Formula"
  - "Divided Difference Method"
status: completed
---

# 🔢 Newton's Divided Difference Interpolation

> [!NOTE] 💡 The Big Picture Intuition
> Lagrange interpolation is powerful but has a major drawback: if you want to **add a new data point**, you must **recompute the entire polynomial from scratch** — every basis polynomial changes!
> Newton's Divided Difference method is the clever alternative: it builds the interpolating polynomial **incrementally**. Each new data point only requires adding **one new term** to the existing polynomial. It's like upgrading a house — you add a new room without rebuilding the whole structure!
> The method uses **divided differences** — a systematic way to compute the slopes between all pairs of points — to construct the polynomial in a form that's both elegant and efficient:
> $$P_n(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \cdots + a_n(x-x_0)\cdots(x-x_{n-1})$$

---

## 1. Problem Statement & Setup

Given $n+1$ distinct data points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, Newton's Divided Difference method constructs the unique polynomial $P_n(x)$ of degree at most $n$ passing through all points.

The polynomial is written in **Newton form**:

> [!IMPORTANT] 🎯 Newton's Divided Difference Form
> $$P_n(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \cdots + a_n(x-x_0)(x-x_1)\cdots(x-x_{n-1})$$

where the coefficients $a_0, a_1, \dots, a_n$ are the **divided differences**.

---

## 2. Definition of Divided Differences

### Zeroth-Order Divided Differences
These are simply the $y$-values:

$$f[x_i] = y_i$$

### First-Order Divided Differences
These are the slopes between consecutive points:

> [!IMPORTANT] 🎯 First Divided Difference
> $$f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i} = \frac{y_{i+1} - y_i}{x_{i+1} - x_i}$$

### Second-Order Divided Differences
These measure how the first differences change:

$$f[x_i, x_{i+1}, x_{i+2}] = \frac{f[x_{i+1}, x_{i+2}] - f[x_i, x_{i+1}]}{x_{i+2} - x_i}$$

### k-th Order Divided Differences (General)

> [!IMPORTANT] 🎯 k-th Divided Difference Formula
> $$f[x_i, x_{i+1}, \dots, x_{i+k}] = \frac{f[x_{i+1}, x_{i+2}, \dots, x_{i+k}] - f[x_i, x_{i+1}, \dots, x_{i+k-1}]}{x_{i+k} - x_i}$$

---

## 3. The Divided Difference Table

The most efficient way to organize the computation is a **divided difference table**:

| $x_i$ | $y_i$ | $f[.,.]$ | $f[.,.,.]$ | $f[.,.,.,.]$ |
| :---: | :---: | :---: | :---: | :---: |
| $x_0$ | $y_0$ | | | |
| | | $f[x_0,x_1]$ | | |
| $x_1$ | $y_1$ | | $f[x_0,x_1,x_2]$ | |
| | | $f[x_1,x_2]$ | | $f[x_0,x_1,x_2,x_3]$ |
| $x_2$ | $y_2$ | | $f[x_1,x_2,x_3]$ | |
| | | $f[x_2,x_3]$ | | |
| $x_3$ | $y_3$ | | | |

**Reading the table**: The coefficients $a_0, a_1, \dots, a_n$ are the **top diagonal** of the table:
$$a_0 = f[x_0], \quad a_1 = f[x_0,x_1], \quad a_2 = f[x_0,x_1,x_2], \quad \dots, \quad a_n = f[x_0,x_1,\dots,x_n]$$

> [!TIP] 💡 The coefficients are the **top-left to top-right diagonal** of the table!

---

## 4. Derivation of the Newton Form

The Newton form polynomial is:
$$P_n(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \cdots + a_n(x-x_0)\cdots(x-x_{n-1})$$

### Step 1: Evaluate at $x = x_0$
$$P_n(x_0) = a_0$$
Since $P_n(x_0) = y_0$, we get:
$$a_0 = y_0 = f[x_0]$$

### Step 2: Evaluate at $x = x_1$
$$P_n(x_1) = a_0 + a_1(x_1 - x_0) = y_1$$
$$a_1 = \frac{y_1 - y_0}{x_1 - x_0} = f[x_0, x_1]$$

### Step 3: General Pattern
Continuing this process for all points, we get:
$$a_k = f[x_0, x_1, \dots, x_k]$$

Therefore:
> [!IMPORTANT] 🎯 Final Newton Interpolation Formula
> $$P_n(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots + f[x_0,x_1,\dots,x_n](x-x_0)\cdots(x-x_{n-1})$$

---

## 5. Worked Step-by-Step Example

> [!EXAMPLE] Problem
> Given the data points:
> | $x$ | $0$ | $1$ | $2$ | $4$ |
> | :---: | :---: | :---: | :---: | :---: |
> | $y$ | $1$ | $3$ | $5$ | $11$ |
>
> Use Newton's Divided Difference method to find $P_3(x)$ and estimate $f(3)$.

**Step 1: Build the Divided Difference Table**

| $x_i$ | $y_i$ | $f[.,.]$ | $f[.,.,.]$ | $f[.,.,.,.]$ |
| :---: | :---: | :---: | :---: | :---: |
| $0$ | $1$ | | | |
| | | $2$ | | |
| $1$ | $3$ | | $0$ | |
| | | $2$ | | $\frac{1}{12}$ |
| $2$ | $5$ | | $\frac{1}{3}$ | |
| | | $3$ | | |
| $4$ | $11$ | | | |

**Step 2: Extract Coefficients from the Top Diagonal**
- $a_0 = f[x_0] = 1$
- $a_1 = f[x_0,x_1] = 2$
- $a_2 = f[x_0,x_1,x_2] = 0$
- $a_3 = f[x_0,x_1,x_2,x_3] = \frac{1}{12}$

**Step 3: Write the Interpolating Polynomial**

$$P_3(x) = 1 + 2(x-0) + 0(x-0)(x-1) + \frac{1}{12}(x-0)(x-1)(x-2)$$

$$P_3(x) = 1 + 2x + \frac{1}{12}x(x-1)(x-2)$$

**Step 4: Estimate $f(3)$**

$$P_3(3) = 1 + 2(3) + \frac{1}{12}(3)(3-1)(3-2)$$

$$P_3(3) = 1 + 6 + \frac{1}{12}(6) = 1 + 6 + 0.5 = \mathbf{7.5}$$

**Step 5: Verify at Known Points**
- $P_3(0) = 1 + 0 + 0 = 1$ ✅
- $P_3(1) = 1 + 2 + 0 = 3$ ✅
- $P_3(2) = 1 + 4 + 0 = 5$ ✅
- $P_3(4) = 1 + 8 + \frac{1}{12}(4)(3)(2) = 1 + 8 + 2 = 11$ ✅

**Final Answer**: $f(3) \approx \mathbf{7.5}$

---

## 6. Error Analysis

The error for Newton's Divided Difference interpolation is identical to Lagrange's:

> [!IMPORTANT] 🎯 Interpolation Error
> $$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod_{i=0}^{n} (x - x_i)$$

where $\xi$ lies in the interval containing all nodes and $x$.

---

## 7. Advantages Over Lagrange

1. **Incremental Construction**: Adding a new data point requires only **one additional term** in the Newton form — no recalculation needed!
2. **Computational Efficiency**: Building the divided difference table requires only $\frac{n(n+1)}{2}$ operations (additions and divisions).
3. **Natural Extension**: The Newton form makes it easy to compare with **Taylor polynomials** — both have a nested structure.

---

## 8. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: What happens to the divided differences when the data points are generated by a polynomial of degree $m < n$?
> 
> > [!SUCCESS]- Step-by-Step Solution
> > 1. If $f(x)$ is a polynomial of degree $m$, then $f^{(m+1)}(x) = 0$ for all $x$.
> > 2. For the $(m+1)$-th order divided difference: $f[x_0, x_1, \dots, x_{m+1}] = \frac{f^{(m+1)}(\xi)}{(m+1)!} = 0$.
> > 3. **All divided differences of order $> m$ are zero!**
> > 4. The interpolating polynomial $P_n(x)$ reduces to $P_m(x)$ — it matches the true polynomial exactly.

---

> [!QUESTION] Practice Question: Compute the first and second divided differences for $f(x) = x^2$ at $x_0=0, x_1=1, x_2=3$.
> 
> > [!SUCCESS]- Step-by-Step Solution
> > 1. $f[x_0] = 0^2 = 0$, $f[x_1] = 1$, $f[x_2] = 9$.
> > 2. First-order: $f[x_0,x_1] = \frac{1-0}{1-0} = 1$, $f[x_1,x_2] = \frac{9-1}{3-1} = 4$.
> > 3. Second-order: $f[x_0,x_1,x_2] = \frac{4-1}{3-0} = 1$.
> > 4. Verify: For $f(x)=x^2$, $f''(x)=2$, so $\frac{f''(\xi)}{2!} = \frac{2}{2} = 1$ ✅

---

## 💻 Python Implementation

```python
def newton_divided_difference(x_data, y_data, x):
    """
    Evaluate the Newton interpolating polynomial at x.
    
    Parameters:
        x_data: list of distinct x-values [x0, x1, ..., xn]
        y_data: list of corresponding y-values [y0, y1, ..., yn]
        x: the point at which to evaluate the polynomial
    
    Returns:
        P_n(x): the interpolated value
    """
    n = len(x_data)
    
    # Build divided difference table
    # dd[i][j] = f[x_i, x_{i+1}, ..., x_{i+j}]
    dd = [[0.0] * n for _ in range(n)]
    for i in range(n):
        dd[i][0] = y_data[i]
    
    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (x_data[i+j] - x_data[i])
    
    # Extract diagonal coefficients: dd[0][0], dd[0][1], ..., dd[0][n-1]
    coefficients = [dd[0][j] for j in range(n)]
    
    # Evaluate Newton polynomial using nested multiplication
    result = coefficients[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_data[i]) + coefficients[i]
    
    return result


# Example usage:
x_points = [0, 1, 2, 4]
y_points = [1, 3, 5, 11]

print(f"P_3(3) = {newton_divided_difference(x_points, y_points, 3)}")  # 7.5
print(f"P_3(4) = {newton_divided_difference(x_points, y_points, 4)}")  # 11.0 (exact)
```

---

## 🔗 Related Notes
- [[Lagrange Interpolation]] — Basis polynomial approach (equivalent result)
- [[Newton Forward and Backward Difference Interpolation]] — Simplified for equally spaced nodes
- [[Cubic Spline Interpolation]] — Piecewise alternative avoiding Runge's phenomenon