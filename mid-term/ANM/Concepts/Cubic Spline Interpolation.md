---
title: "Cubic Spline Interpolation"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - interpolation
  - splines
aliases:
  - "Natural Cubic Splines"
  - "Clamped Cubic Splines"
  - "Piecewise Polynomial Interpolation"
status: completed
---

# 🌊 Cubic Spline Interpolation

> [!NOTE] 💡 The Big Picture Intuition
> High-degree Lagrange polynomials suffer from **Runge's Phenomenon** — they oscillate wildly between points when you add too many nodes. The **Cubic Spline** method solves this by breaking the problem into small pieces: instead of one big polynomial, we use **many small cubic polynomials** joined together at the data points (called **knots**).
> Think of it like a flexible ruler (a **spline**) used by shipbuilders and drafters: it passes through each point while bending smoothly, with no sudden kinks or sharp corners. Each segment is a simple cubic, but the whole curve looks smooth and natural!

---

## 1. Problem Statement & Setup

Given $n+1$ data points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$ with $x_0 < x_1 < \cdots < x_n$, a cubic spline $S(x)$ is a piecewise cubic polynomial:

$$S(x) = S_i(x) \quad \text{for } x \in [x_i, x_{i+1}], \quad i = 0, 1, \dots, n-1$$

where each $S_i(x)$ is a cubic polynomial:
$$S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$$

### Conditions for a Cubic Spline

For $S(x)$ to be a valid cubic spline:

1. **Interpolation Condition**: $S(x_i) = y_i$ for all $i = 0, 1, \dots, n$
2. **Continuity**: $S_i(x_{i+1}) = S_{i+1}(x_{i+1})$ for all $i$
3. **First Derivative Continuity**: $S_i'(x_{i+1}) = S_{i+1}'(x_{i+1})$ for all $i$
4. **Second Derivative Continuity**: $S_i''(x_{i+1}) = S_{i+1}''(x_{i+1})$ for all $i$

> [!IMPORTANT] 🎯 Key Insight
> A cubic spline with $n+1$ points uses $n$ cubic polynomials, giving $4n$ unknown coefficients. The interpolation, continuity, and smoothness conditions give us $4n - 2$ equations. We need **2 additional boundary conditions** to uniquely determine the spline!

---

## 2. Types of Cubic Splines

### A. Natural Cubic Spline
The second derivative is zero at the endpoints:
$$S_0''(x_0) = 0 \quad \text{and} \quad S_{n-1}''(x_n) = 0$$

This is the most common type — like a flexible ruler that is free to bend at the ends.

### B. Clamped Cubic Spline
The first derivatives at the endpoints are specified:
$$S_0'(x_0) = f'(x_0) \quad \text{and} \quad S_{n-1}'(x_n) = f'(x_n)$$

Used when we know the slope at the boundaries.

### C. Not-a-Knot Cubic Spline
The third derivative is continuous at the second and second-to-last knots:
$$S_0'''(x_1) = S_1'''(x_1) \quad \text{and} \quad S_{n-2}'''(x_{n-1}) = S_{n-1}'''(x_{n-1})$$

---

## 3. Derivation of the Cubic Spline

Let $h_i = x_{i+1} - x_i$ be the spacing between consecutive nodes.

Each cubic segment can be written as:
$$S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$$

### Step 1: Use the Interpolation Condition
At $x = x_i$:
$$S_i(x_i) = a_i = y_i$$

So: $a_i = y_i$ for all $i$.

### Step 2: Use the Second Derivative
The second derivative of $S_i(x)$ is:
$$S_i''(x) = 2c_i + 6d_i(x - x_i)$$

Let $M_i = S_i''(x_i)$ and $M_{i+1} = S_i''(x_{i+1})$. Then:
$$M_i = 2c_i$$
$$M_{i+1} = 2c_i + 6d_i h_i$$

Solving for $c_i$ and $d_i$:
$$c_i = \frac{M_i}{2}$$
$$d_i = \frac{M_{i+1} - M_i}{6h_i}$$

### Step 3: Use the First Derivative
The first derivative is:
$$S_i'(x) = b_i + 2c_i(x - x_i) + 3d_i(x - x_i)^2$$

The continuity of first derivatives gives us a system of equations. After algebraic manipulation, we get the **tridiagonal system**:

> [!IMPORTANT] 🎯 Cubic Spline Tridiagonal System (Natural Spline)
> $$h_{i-1}M_{i-1} + 2(h_{i-1} + h_i)M_i + h_i M_{i+1} = 6\left(\frac{y_{i+1} - y_i}{h_i} - \frac{y_i - y_{i-1}}{h_{i-1}}\right)$$
> for $i = 1, 2, \dots, n-1$

With boundary conditions for a **natural spline**:
$$M_0 = 0 \quad \text{and} \quad M_n = 0$$

---

## 4. Algorithm for Natural Cubic Spline

1. **Compute** $h_i = x_{i+1} - x_i$ for $i = 0, 1, \dots, n-1$
2. **Set up** the tridiagonal system for $M_1, M_2, \dots, M_{n-1}$
3. **Apply** boundary conditions $M_0 = M_n = 0$
4. **Solve** the tridiagonal system using the Thomas algorithm
5. **Compute** coefficients:
   - $a_i = y_i$
   - $b_i = \frac{y_{i+1} - y_i}{h_i} - \frac{h_i}{6}(M_{i+1} + 2M_i)$
   - $c_i = \frac{M_i}{2}$
   - $d_i = \frac{M_{i+1} - M_i}{6h_i}$

---

## 5. Worked Step-by-Step Example

> [!EXAMPLE] Problem
> Given the data points:
> | $x$ | $0$ | $1$ | $2$ | $3$ |
> | :---: | :---: | :---: | :---: | :---: |
> | $y$ | $1$ | $2$ | $5$ | $10$ |
>
> Construct the **natural cubic spline** and estimate $S(1.5)$.

**Step 1: Identify Parameters**
- $x_0 = 0, x_1 = 1, x_2 = 2, x_3 = 3$
- $y_0 = 1, y_1 = 2, y_2 = 5, y_3 = 10$
- $h_0 = 1, h_1 = 1, h_2 = 1$ (equally spaced)

**Step 2: Set up the Tridiagonal System**

For $i = 1$:
$$h_0 M_0 + 2(h_0 + h_1)M_1 + h_1 M_2 = 6\left(\frac{y_2 - y_1}{h_1} - \frac{y_1 - y_0}{h_0}\right)$$

$$M_0 + 4M_1 + M_2 = 6\left(\frac{5 - 2}{1} - \frac{2 - 1}{1}\right) = 6(3 - 1) = 12$$

For $i = 2$:
$$h_1 M_1 + 2(h_1 + h_2)M_2 + h_2 M_3 = 6\left(\frac{y_3 - y_2}{h_2} - \frac{y_2 - y_1}{h_1}\right)$$

$$M_1 + 4M_2 + M_3 = 6\left(\frac{10 - 5}{1} - \frac{5 - 2}{1}\right) = 6(5 - 3) = 12$$

**Step 3: Apply Boundary Conditions**
- $M_0 = 0$
- $M_3 = 0$

So the system becomes:
$$4M_1 + M_2 = 12$$
$$M_1 + 4M_2 = 12$$

**Step 4: Solve the System**
From the first equation: $M_2 = 12 - 4M_1$

Substitute into the second:
$$M_1 + 4(12 - 4M_1) = 12$$
$$M_1 + 48 - 16M_1 = 12$$
$$-15M_1 = -36$$
$$M_1 = \frac{36}{15} = 2.4$$

Then: $M_2 = 12 - 4(2.4) = 12 - 9.6 = 2.4$

So: $M_0 = 0, M_1 = 2.4, M_2 = 2.4, M_3 = 0$

**Step 5: Compute Coefficients**

For $i = 0$:
- $a_0 = y_0 = 1$
- $b_0 = \frac{2-1}{1} - \frac{1}{6}(2.4 + 2(0)) = 1 - 0.4 = 0.6$
- $c_0 = \frac{0}{2} = 0$
- $d_0 = \frac{2.4 - 0}{6} = 0.4$

$$S_0(x) = 1 + 0.6x + 0x^2 + 0.4x^3 = 1 + 0.6x + 0.4x^3$$

For $i = 1$:
- $a_1 = y_1 = 2$
- $b_1 = \frac{5-2}{1} - \frac{1}{6}(2.4 + 2(2.4)) = 3 - 1.2 = 1.8$
- $c_1 = \frac{2.4}{2} = 1.2$
- $d_1 = \frac{2.4 - 2.4}{6} = 0$

$$S_1(x) = 2 + 1.8(x-1) + 1.2(x-1)^2$$

For $i = 2$:
- $a_2 = y_2 = 5$
- $b_2 = \frac{10-5}{1} - \frac{1}{6}(0 + 2(2.4)) = 5 - 0.8 = 4.2$
- $c_2 = \frac{2.4}{2} = 1.2$
- $d_2 = \frac{0 - 2.4}{6} = -0.4$

$$S_2(x) = 5 + 4.2(x-2) + 1.2(x-2)^2 - 0.4(x-2)^3$$

**Step 6: Estimate $S(1.5)$**

Since $1.5 \in [1, 2]$, we use $S_1(x)$:
$$S_1(1.5) = 2 + 1.8(0.5) + 1.2(0.5)^2 = 2 + 0.9 + 0.3 = \mathbf{3.2}$$

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why do we need boundary conditions for cubic splines?
> 
> > [!SUCCESS]- Step-by-Step Solution
> > 1. With $n+1$ data points, we have $n$ cubic polynomials, each with 4 coefficients, giving $4n$ unknowns.
> > 2. The interpolation conditions give $n+1$ equations.
> > 3. The continuity conditions at interior knots give $3(n-1)$ equations.
> > 4. Total: $(n+1) + 3(n-1) = 4n - 2$ equations.
> > 5. We have $4n$ unknowns but only $4n - 2$ equations, so we need **2 more conditions**.
> > 6. These are provided by the boundary conditions (natural, clamped, or not-a-knot).

---

> [!QUESTION] Practice Question: What makes a cubic spline better than a high-degree Lagrange polynomial?
> 
> > [!SUCCESS]- Step-by-Step Solution
> > 1. High-degree Lagrange polynomials suffer from **Runge's Phenomenon** — oscillations near the endpoints.
> > 2. Cubic splines use low-degree (cubic) polynomials on small intervals, avoiding wild oscillations.
> > 3. Splines maintain smoothness ($C^2$ continuity) at the knots while being locally controlled.
> > 4. Changing one data point only affects nearby segments, not the entire curve.
> > 5. This makes splines much more stable and reliable for large datasets.

---

## 💻 Python Implementation

```python
import numpy as np

def natural_cubic_spline(x_data, y_data, x):
    """
    Evaluate the natural cubic spline interpolant at x.
    """
    x_data = np.array(x_data, dtype=float)
    y_data = np.array(y_data, dtype=float)
    x = float(x)
    
    n = len(x_data) - 1
    h = np.diff(x_data)
    
    # Build tridiagonal system for M (second derivatives)
    A = np.zeros((n - 1, n - 1))
    b = np.zeros(n - 1)
    
    for i in range(n - 1):
        if i > 0:
            A[i, i - 1] = h[i]
        A[i, i] = 2 * (h[i] + h[i + 1])
        if i < n - 2:
            A[i, i + 1] = h[i + 1]
        
        b[i] = 6 * ((y_data[i + 2] - y_data[i + 1]) / h[i + 1] - (y_data[i + 1] - y_data[i]) / h[i])
    
    # Natural boundary conditions: M_0 = M_n = 0
    M = np.zeros(n + 1)
    M[1:n] = np.linalg.solve(A, b)
    
    # Find which segment contains x
    idx = np.searchsorted(x_data, x) - 1
    idx = max(0, min(idx, n - 1))
    
    # Compute coefficients
    a = y_data[idx]
    b_coeff = (y_data[idx + 1] - y_data[idx]) / h[idx] - h[idx] * (M[idx + 1] + 2 * M[idx]) / 6
    c_coeff = M[idx] / 2
    d_coeff = (M[idx + 1] - M[idx]) / (6 * h[idx])
    
    dx = x - x_data[idx]
    return a + b_coeff * dx + c_coeff * dx**2 + d_coeff * dx**3


# Example usage:
x_points = [0, 1, 2, 3]
y_points = [1, 2, 5, 10]

print(f"S(1.5) = {natural_cubic_spline(x_points, y_points, 1.5)}")  # 3.2
```

---

## 🔗 Related Notes
- [[Lagrange Interpolation]] — Global polynomial interpolation (Runge's Phenomenon)
- [[Newton Divided Difference Interpolation]] — Polynomial interpolation alternative
- [[Newton Forward and Backward Difference Interpolation]] — Equally spaced nodes
- [[Errors and Convergence]] — Error analysis and convergence behavior