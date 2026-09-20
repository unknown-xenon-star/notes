---
title: "Newton Forward and Backward Difference Interpolation"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - interpolation
  - finite-difference
aliases:
  - "Newton's Forward Difference Formula"
  - "Newton's Backward Difference Formula"
  - "Finite Difference Interpolation"
status: completed
---

# 📊 Newton's Forward & Backward Difference Interpolation

> [!NOTE] 💡 The Big Picture Intuition
> The general Newton Divided Difference method works for **any** data points, but when the $x$-values are **equally spaced** (e.g., $x_0, x_0+h, x_0+2h, \dots$), something magical happens!
> The divided differences simplify dramatically into **forward/backward differences** — simple subtractions of $y$-values without any division by $h$! This yields **Newton's Forward Difference Formula** (for interpolating near the **beginning** of the data) and **Newton's Backward Difference Formula** (for interpolating near the **end**).
> Think of it like using a specialized tool: if your nodes are on a perfect grid, you don't need the general-purpose divided difference wrench — you can use the precision forward/backward difference screwdriver that's faster and simpler!

---

## 1. Setup: Equally Spaced Nodes

Given data points with **constant spacing** $h$:
$$x_i = x_0 + i h \quad \text{for } i = 0, 1, 2, \dots, n$$

| $x$ | $x_0$ | $x_0+h$ | $x_0+2h$ | $\dots$ | $x_0+nh$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | $y_0$ | $y_1$ | $y_2$ | $\dots$ | $y_n$ |

---

## 2. Forward Differences

The **first forward difference** at $x_i$ is: $\Delta y_i = y_{i+1} - y_i$

The **second forward difference**: $\Delta^2 y_i = \Delta y_{i+1} - \Delta y_i = y_{i+2} - 2y_{i+1} + y_i$

The **k-th forward difference** (recursive): $\Delta^k y_i = \Delta^{k-1} y_{i+1} - \Delta^{k-1} y_i$

### Forward Difference Table

| $x_i$ | $y_i$ | $\Delta$ | $\Delta^2$ | $\Delta^3$ | $\Delta^4$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $x_0$ | $y_0$ | | | | |
| | | $\Delta y_0$ | | | |
| $x_1$ | $y_1$ | | $\Delta^2 y_0$ | | |
| | | $\Delta y_1$ | | $\Delta^3 y_0$ | |
| $x_2$ | $y_2$ | | $\Delta^2 y_1$ | | $\Delta^4 y_0$ |
---

## 3. Newton's Forward Difference Formula

Let $s$ be the **normalized variable** measuring how far we are from $x_0$:
$$s = \frac{x - x_0}{h}$$

> [!IMPORTANT] 🎯 Newton's Forward Difference Formula
> $$P_n(x) = y_0 + \binom{s}{1} \Delta y_0 + \binom{s}{2} \Delta^2 y_0 + \cdots + \binom{s}{n} \Delta^n y_0$$

where the binomial coefficients are:
$$\binom{s}{k} = \frac{s(s-1)(s-2)\cdots(s-k+1)}{k!}$$

### Expanded Form
$$P_n(x) = y_0 + s \Delta y_0 + \frac{s(s-1)}{2!} \Delta^2 y_0 + \frac{s(s-1)(s-2)}{3!} \Delta^3 y_0 + \cdots$$

---

## 4. Backward Differences

The **first backward difference** at $x_i$ is: $\nabla y_i = y_i - y_{i-1}$

The **k-th backward difference**: $\nabla^k y_i = \nabla^{k-1} y_i - \nabla^{k-1} y_{i-1}$

### Backward Difference Table

| $x_i$ | $y_i$ | $\nabla$ | $\nabla^2$ | $\nabla^3$ |
| :---: | :---: | :---: | :---: | :---: |
| $x_0$ | $y_0$ | | | |
| | | $\nabla y_1$ | | |
| $x_1$ | $y_1$ | | $\nabla^2 y_2$ | |
| | | $\nabla y_2$ | | $\nabla^3 y_3$ |
| $x_2$ | $y_2$ | | $\nabla^2 y_3$ | |
| $x_3$ | $y_3$ | | | |

---

## 5. Newton's Backward Difference Formula

Let $s$ be the **normalized variable** measuring how far we are from $x_n$:
$$s = \frac{x - x_n}{h}$$

> [!IMPORTANT] 🎯 Newton's Backward Difference Formula
> $$P_n(x) = y_n + \binom{s}{1} \nabla y_n + \binom{s+1}{2} \nabla^2 y_n + \cdots + \binom{s+n-1}{n} \nabla^n y_n$$

where the generalized binomial coefficients are:
$$\binom{s}{k} = \frac{s(s+1)(s+2)\cdots(s+k-1)}{k!}$$

### When to Use Which?
| Situation | Recommended Formula |
| :--- | :--- |
| Interpolating **near $x_0$** (beginning of table) | **Forward Differences** |
| Interpolating **near $x_n$** (end of table) | **Backward Differences** |
| Interpolating **in the middle** | Either works; use Stirling's or Bessel's formula |

---

## 6. Worked Step-by-Step Example

> [!EXAMPLE] Problem
> Given the following equally spaced data:
> | $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
> | :---: | :---: | :---: | :---: | :---: | :---: |
> | $y$ | $1$ | $3$ | $7$ | $13$ | $21$ |
>
> Use Newton's Forward Difference formula to estimate $f(1.5)$ and $f(3.5)$.

**Step 1: Identify Parameters**
- $x_0 = 0$, $h = 1$
- $y_0 = 1, y_1 = 3, y_2 = 7, y_3 = 13, y_4 = 21$

**Step 2: Build Forward Difference Table**

| $x_i$ | $y_i$ | $\Delta$ | $\Delta^2$ | $\Delta^3$ | $\Delta^4$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $1$ | | | | |
| | | $2$ | | | |
| $1$ | $3$ | | $2$ | | |
| | | $4$ | | $0$ | |
| $2$ | $7$ | | $2$ | | $0$ |
| | | $6$ | | $0$ | |
| $3$ | $13$ | | $2$ | | |
| | | $8$ | | | |
| $4$ | $21$ | | | | |

**Step 3: Extract Forward Differences from Top Row**
- $\Delta y_0 = 2$
- $\Delta^2 y_0 = 2$
- $\Delta^3 y_0 = 0$
- $\Delta^4 y_0 = 0$

**Step 4: Write Forward Formula**
Since $\Delta^3 = \Delta^4 = 0$, the polynomial is degree 2:
$$P_2(x) = y_0 + s \Delta y_0 + \frac{s(s-1)}{2} \Delta^2 y_0$$
$$P_2(x) = 1 + 2s + s(s-1) = 1 + s + s^2$$

Since $s = \frac{x - 0}{1} = x$, we get $P_2(x) = x^2 + x + 1$.

**Step 5: Evaluate**

- **$f(1.5)$**: $s = 1.5$
  $$P_2(1.5) = 1 + 1.5 + (1.5)^2 = 1 + 1.5 + 2.25 = \mathbf{4.75}$$

- **$f(3.5)$**: $s = 3.5$
  $$P_2(3.5) = 1 + 3.5 + (3.5)^2 = 1 + 3.5 + 12.25 = \mathbf{16.75}$$

**Verification**:
- $f(2) = 2^2 + 2 + 1 = 7$ ✅
- $f(3) = 3^2 + 3 + 1 = 13$ ✅
- $f(4) = 4^2 + 4 + 1 = 21$ ✅

---

## 7. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: For the data in the example above, what is the true function?
> 
> > [!SUCCESS]- Step-by-Step Solution
> > 1. The forward difference table shows $\Delta^3 = 0$ and $\Delta^4 = 0$.
> > 2. This means the data comes from a **degree-2 polynomial** (since 3rd differences vanish).
> > 3. The polynomial we found: $P_2(x) = x^2 + x + 1$.
> > 4. Check: $f(x) = x^2 + x + 1$ gives $f(0)=1, f(1)=3, f(2)=7, f(3)=13, f(4)=21$ ✅

---

> [!QUESTION] Practice Question: What is the relationship between divided differences and forward differences?
> 
> > [!SUCCESS]- Step-by-Step Solution
> > For equally spaced nodes with spacing $h$:
> > $$f[x_0, x_1, \dots, x_k] = \frac{\Delta^k y_0}{k! \cdot h^k}$$
> > 
> > **Proof**: The k-th divided difference equals the k-th forward difference divided by $k! h^k$.
> > This is why the Newton forward formula looks like the divided difference formula but with binomial coefficients instead of divided differences!

---

## 💻 Python Implementation

```python
import math

def newton_forward_difference(x_data, y_data, x):
    """
    Evaluate using Newton's Forward Difference formula.
    Requires equally spaced x_data.
    """
    n = len(x_data)
    h = x_data[1] - x_data[0]
    
    # Verify equal spacing
    for i in range(1, n):
        if abs(x_data[i] - x_data[i-1] - h) > 1e-10:
            raise ValueError("x_data must be equally spaced!")
    
    # Build forward difference table
    diff = [y_data[:]]  # diff[0] = y values
    for level in range(1, n):
        prev = diff[level - 1]
        curr = [prev[i+1] - prev[i] for i in range(len(prev) - 1)]
        diff.append(curr)
    
    # Evaluate using s = (x - x0) / h
    s = (x - x_data[0]) / h
    
    result = diff[0][0]
    s_term = 1.0
    for k in range(1, n):
        s_term *= (s - (k - 1))
        result += (s_term / math.factorial(k)) * diff[k][0]
    
    return result


def newton_backward_difference(x_data, y_data, x):
    """
    Evaluate using Newton's Backward Difference formula.
    Requires equally spaced x_data.
    """
    n = len(x_data)
    h = x_data[1] - x_data[0]
    
    # Verify equal spacing
    for i in range(1, n):
        if abs(x_data[i] - x_data[i-1] - h) > 1e-10:
            raise ValueError("x_data must be equally spaced!")
    
    # Build backward difference table
    diff = [y_data[:]]
    for level in range(1, n):
        prev = diff[level - 1]
        curr = [prev[i] - prev[i-1] for i in range(len(prev) - 1, 0, -1)]
        curr.reverse()
        diff.append(curr)
    
    # Evaluate using s = (x - x_n) / h
    s = (x - x_data[-1]) / h
    
    result = diff[0][-1]  # y_n
    s_term = 1.0
    for k in range(1, n):
        s_term *= (s + (k - 1))
        result += (s_term / math.factorial(k)) * diff[k][-1]
    
    return result


# Example usage:
x_points = [0, 1, 2, 3, 4]
y_points = [1, 3, 7, 13, 21]

print(f"f(1.5) = {newton_forward_difference(x_points, y_points, 1.5)}")  # 4.75
print(f"f(3.5) = {newton_backward_difference(x_points, y_points, 3.5)}")  # 16.75
```

---

## 🔗 Related Notes
- [[Newton Divided Difference Interpolation]] — General case for arbitrary nodes
- [[Lagrange Interpolation]] — Alternative polynomial interpolation
- [[Cubic Spline Interpolation]] — Piecewise approach for large datasets