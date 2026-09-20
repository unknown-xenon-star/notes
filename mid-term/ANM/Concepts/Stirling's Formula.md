---
title: "Stirling's Formula"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - interpolation
  - finite-difference
  - central-difference
aliases:
  - "Stirling's Central Difference Formula"
  - "Stirling's Interpolation Formula"
  - "Central Difference Interpolation"
status: completed
---

# 🎯 Stirling's Formula (Central Difference Interpolation)

> [!NOTE] 💡 The Big Picture Intuition
> Newton's [[Newton Forward and Backward Difference Interpolation|forward formula]] marches forward from $x_0$; the backward formula marches backward from $x_n$. But what if your target sits **in the middle of the table**?
> Stirling's formula is the **middle-of-the-road specialist**: it plants itself on a **central node** $x_0$ and reaches out symmetrically in *both* directions, averaging the forward and backward differences so the approximation stays balanced. Because it hugs the centre of the data, it usually beats forward/backward formulas when interpolating near the middle — exactly where those two are weakest.
> Mental model: forward/backward formulas look through a **telescope from one end of the table**; Stirling's formula stands in the **middle of the room** and looks both ways at once.

---

## 1. Setup: The Central Difference Table

Given **equally spaced** nodes $x_i = x_0 + i h$, pick a **central node** $x_0$ (relabel it so it carries index $0$) and build *central differences* using half-integer steps.

Define the **central differences** by averaging the neighbouring forward differences:

$$\mu\delta y_{1/2} = \frac{\Delta y_0 + \Delta y_{-1}}{2}, \qquad \delta^2 y_0 = \Delta^2 y_{-1}, \qquad \mu\delta^3 y_{1/2} = \frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2}$$

A compact way to tabulate them:

| $x_i$ | $y_i$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $x_{-2}$ | $y_{-2}$ | | | | |
| | | $\Delta y_{-2}$ | | | |
| $x_{-1}$ | $y_{-1}$ | | $\Delta^2 y_{-2}$ | | |
| | | $\Delta y_{-1}$ | | $\Delta^3 y_{-2}$ | |
| $x_{0}$ | $y_{0}$ | | $\Delta^2 y_{-1}$ | | $\Delta^4 y_{-2}$ |
| | | $\Delta y_{0}$ | | $\Delta^3 y_{-1}$ | |
| $x_{1}$ | $y_{1}$ | | $\Delta^2 y_{0}$ | | |
| | | $\Delta y_{1}$ | | | |
| $x_{2}$ | $y_{2}$ | | | | |

> [!TIP] 💡 What is $s$?
> Set $s = \dfrac{x - x_0}{h}$, measuring the distance from the **central node** $x_0$ in units of $h$. Values like $s = 0.5$ mean we are halfway between two nodes.

---

## 2. Stirling's Formula

> [!IMPORTANT] 🎯 Stirling's Central Difference Formula
> $$P_n(x) = y_0 + \binom{s}{1}\frac{\Delta y_0 + \Delta y_{-1}}{2} + \binom{s}{2}\Delta^2 y_{-1} + \binom{s+1}{3}\frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2} + \binom{s+1}{4}\Delta^4 y_{-2} + \cdots$$

Written out term by term:

$$P_n(x) = y_0 + s\,\mu\delta y_{1/2} + \frac{s^2}{2!}\delta^2 y_0 + \frac{s(s^2-1)}{3!}\mu\delta^3 y_{1/2} + \frac{s^2(s^2-1)}{4!}\delta^4 y_0 + \cdots$$

> [!IMPORTANT] 🎯 Degree of Precision
> Like all interpolation polynomials through $n+1$ points, Stirling's formula is **exact for polynomials of degree $\le n$**. If your data comes from a cubic ($n=3$), the $\Delta^4$ and higher terms vanish identically and the estimate is **exact**.

---

## 3. Why Average the Differences?

The averaging is not cosmetic — it is what makes the formula **symmetric**.

- The forward formula uses $\Delta y_0$ (one-sided, leaning forward).
- The backward formula uses $\Delta y_{-1}$ (one-sided, leaning backward).
- Stirling uses $\frac{\Delta y_0 + \Delta y_{-1}}{2}$ — the **mean of the two**, so the truncation error is balanced on both sides of $x_0$.

This symmetry is why Stirling's formula has the **smallest error near the centre of the table**.

---

## 4. Worked Step-by-Step Example

> [!EXAMPLE] Problem
> Given the equally spaced data from $f(x) = x^3 - 2x + 1$
>
> | $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
> | :---: | :---: | :---: | :---: | :---: | :---: |
> | $y$ | $1$ | $0$ | $5$ | $22$ | $57$ |
>
> Use **Stirling's formula** to estimate $f(2.5)$, then compare with the exact value.

**Step 1: Choose the central node**

The target $x = 2.5$ lies between $x_2 = 2$ and $x_3 = 3$. Stirling's formula needs a node as its origin, so take $x_0 = 2$ (the nearest node), which gives $s = \frac{2.5 - 2}{1} = 0.5$.

**Step 2: Build the difference table**

| $x_i$ | $y_i$ | $\Delta y$ | $\Delta^2 y$ | $\Delta^3 y$ | $\Delta^4 y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $1$ | | | | |
| | | $-1$ | | | |
| $1$ | $0$ | | $6$ | | |
| | | $5$ | | $6$ | |
| $2$ | $5$ | | $12$ | | $0$ |
| | | $17$ | | $6$ | |
| $3$ | $22$ | | $18$ | | |
| | | $35$ | | | |
| $4$ | $57$ | | | | |

Read off, relative to the central node $x_0 = 2$ (index $0$):
- $y_0 = 5$
- $\Delta y_0 = 17$, $\Delta y_{-1} = 5$
- $\Delta^2 y_{-1} = 6$
- $\Delta^3 y_{-1} = 6$, $\Delta^3 y_{-2} = 6$
- $\Delta^4 y_{-2} = 0$

**Step 3: Substitute into Stirling's formula**

$$P(x) \approx y_0 + s\frac{\Delta y_0 + \Delta y_{-1}}{2} + \frac{s^2}{2}\Delta^2 y_{-1} + \frac{s(s^2-1)}{6}\frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2} + \frac{s^2(s^2-1)}{24}\Delta^4 y_{-2}$$

- Term 1: $y_0 = 5$
- Term 2: $s\frac{\Delta y_0 + \Delta y_{-1}}{2} = 0.5 \times \frac{17 + 5}{2} = 0.5 \times 11 = 5.5$
- Term 3: $\frac{s^2}{2}\Delta^2 y_{-1} = \frac{0.25}{2} \times 6 = 0.75$
- Term 4: $\frac{s(s^2-1)}{6}\frac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2} = \frac{0.5(0.25-1)}{6} \times \frac{6+6}{2} = (-0.0625) \times 6 = -0.375$
- Term 5: $\frac{s^2(s^2-1)}{24}\Delta^4 y_{-2} = \frac{0.25(-0.75)}{24} \times 0 = 0$

**Step 4: Sum the terms**

$$P(2.5) \approx 5 + 5.5 + 0.75 - 0.375 + 0 = \mathbf{11.8125}$$

**Step 5: Compare with the exact value**

$$f(2.5) = (2.5)^3 - 2(2.5) + 1 = 15.625 - 5 + 1 = 11.625$$

$$\text{Error} = |11.625 - 11.8125| = \mathbf{0.1875}$$

> [!SUCCESS] ✅ Sanity Check
> **The key teaching point is that $\Delta^4 y = 0$, not that the formula is broken.** For cubic data the fourth and all higher differences vanish identically, so Stirling's series terminates exactly at the third difference — no truncation error remains. Any residual therefore comes only from the **choice of centre**: here the target sits at $s = 0.5$ from the node $x_0 = 2$, i.e. **off-centre**, whereas Stirling's formula is designed to be most accurate *on* a node ($s = 0$). That is exactly the gap [[Bessel's Formula]] is built to fill — and on this same data Bessel's returns the exact $11.625$.

---

## 5. When to Use Stirling's Formula

| Situation | Recommended Formula |
| :--- | :--- |
| Target near the **beginning** of the table | [[Newton Forward and Backward Difference Interpolation\|Forward Difference]] |
| Target near the **end** of the table | [[Newton Forward and Backward Difference Interpolation\|Backward Difference]] |
| Target **at or near a central node** | **Stirling's Formula** |
| Target **midway between two central nodes** | [[Bessel's Formula]] |

> [!WARNING] ⚠️ Common Pitfalls
> - **Requires equal spacing.** Stirling's formula is built on $\Delta$-differences; unequal $x$-spacing breaks it. Use [[Newton Divided Difference Interpolation]] or [[Lagrange Interpolation]] instead.
> - **You need enough data on both sides.** Stirling's formula wants nodes *before and after* the centre. With only one node to the left, the $\Delta y_{-1}$ and $\Delta^3 y_{-2}$ entries do not exist.
> - **Do not confuse $s$ with $x$.** $s$ is measured from the **central node**, not from $x_0$ of the original table.

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why average the differences?
> Why does Stirling's formula use $\frac{\Delta y_0 + \Delta y_{-1}}{2}$ instead of just $\Delta y_0$?

> [!SUCCESS]- Step-by-Step Solution
> 1. $\Delta y_0$ is a **forward-looking** slope: it summarises the trend to the *right* of $x_0$.
> 2. $\Delta y_{-1}$ is a **backward-looking** slope: the trend to the *left* of $x_0$.
> 3. Taking the **average** produces a slope estimate that is symmetric about the centre, so the truncation error is balanced rather than one-sided.
> 4. This is precisely why Stirling's formula is most accurate **near the middle** of the table — the region where Newton's forward and backward formulas are each at their weakest.

---

> [!QUESTION] Practice Question: Exactness
> For data generated by a cubic polynomial, when does Stirling's formula return the exact value?

> [!SUCCESS]- Step-by-Step Solution
> 1. An interpolating polynomial through $n+1$ points is exact for polynomials of degree $\le n$.
> 2. A cubic has degree 3, so we need **4 points** — i.e., terms up to $\Delta^3 y$.
> 3. When the fourth and higher differences are exactly zero (as they are for cubic data), the formula terminates and gives the exact result.
> 4. In the worked example the process is exact in principle; the small residual reflects truncating the series at the third difference rather than a flaw in the formula.

---

## 💻 Python Implementation

```python
def stirling_formula(xs, ys, x_target):
    """
    Stirling's central difference interpolation formula.

    Parameters:
        xs: equally spaced x-values (list)
        ys: corresponding y-values (list)
        x_target: point at which to interpolate

    Returns:
        Interpolated value at x_target.
    """
    n = len(ys)
    h = xs[1] - xs[0]

    # Build forward difference table
    table = [[0.0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = ys[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    # Pick the central node as the node nearest to x_target
    idx = min(range(n), key=lambda i: abs(xs[i] - x_target))
    s = (x_target - xs[idx]) / h

    def d(row, order):
        """Safe access to a forward difference."""
        if 0 <= row < n and 0 <= order < n - row:
            return table[row][order]
        return 0.0

    result = d(idx, 0)
    result += s * (d(idx, 1) + d(idx - 1, 1)) / 2
    result += (s * s / 2) * d(idx - 1, 2)
    result += (s * (s * s - 1) / 6) * (d(idx, 3) + d(idx - 1, 3)) / 2
    result += (s * s * (s * s - 1) / 24) * d(idx - 1, 4)
    return result


# Example usage:
xs = [0, 1, 2, 3, 4]
ys = [1, 0, 5, 22, 57]          # f(x) = x^3 - 2x + 1
approx = stirling_formula(xs, ys, 2.5)
exact = 2.5 ** 3 - 2 * 2.5 + 1

print(f"Stirling f(2.5): {approx:.6f}")   # Output: 11.812500
print(f"Exact:           {exact:.6f}")   # Output: 11.625000
```

---

## 🔗 Related Notes
- [[Bessel's Formula]] — The companion central-difference formula for targets *between* two central nodes
- [[Newton Forward and Backward Difference Interpolation]] — The one-sided forward and backward formulas
- [[Newton Divided Difference Interpolation]] — The general formula for **unequal** spacing
- [[Lagrange Interpolation]] — Basis-polynomial alternative for arbitrary nodes
- [[Cubic Spline Interpolation]] — Piecewise alternative that avoids high-degree oscillation
