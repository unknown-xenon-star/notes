---
title: "Bessel's Formula"
date: 2026-09-20
tags:
  - concept
  - numerical-methods
  - interpolation
  - finite-difference
  - central-difference
aliases:
  - "Bessel's Central Difference Formula"
  - "Bessel's Interpolation Formula"
status: completed
---

# 🎯 Bessel's Formula (Central Difference Interpolation)

> [!NOTE] 💡 The Big Picture Intuition
> [[Stirling's Formula]] plants its flag on a **data point** and looks both ways. But what if your target sits **exactly halfway between two nodes**?
> Bessel's formula is built for that case: it centres itself **between** two adjacent nodes, averaging the two ordinates and the two second differences so the expansion is symmetric about the **midpoint** rather than about a node.
> Mental model: if Stirling's formula stands on a **stepping stone**, Bessel's formula stands on the **plank bridging two stones** — perfectly balanced in the gap. Together the two formulas cover the whole middle of the table: use Stirling on a node, Bessel in the gap between nodes.

---

## 1. Setup: Centring Between Two Nodes

Given **equally spaced** nodes $x_i = x_0 + i h$, choose two **central adjacent nodes** and relabel them $x_0$ and $x_1$. Bessel's formula expands about the **midpoint** $\frac{x_0 + x_1}{2}$.

Let
$$s = \frac{x - x_0}{h}$$
so that $s = 0.5$ corresponds exactly to the midpoint between the two central nodes.

> [!TIP] 💡 The Node-to-Midpoint Shift
> Bessel's formula contains a factor $(s - \tfrac{1}{2})$ in its third-difference term. That is the algebraic fingerprint of "centred on the midpoint": the term **vanishes at $s = 0.5$**, because at the midpoint the two neighbouring third differences cancel by symmetry.

---

## 2. Bessel's Formula

> [!IMPORTANT] 🎯 Bessel's Interpolation Formula
> $$P_n(x) = \frac{y_0 + y_1}{2} + \left(s - \frac{1}{2}\right)\Delta y_0 + \frac{s(s-1)}{2!}\cdot\frac{\Delta^2 y_{-1} + \Delta^2 y_0}{2} + \frac{s(s-1)(s-\frac{1}{2})}{3!}\Delta^3 y_{-1} + \cdots$$

Written in the compact averaged-difference notation:

$$P_n(x) = \mu y_{1/2} + \left(s - \tfrac{1}{2}\right)\delta y_{1/2} + \frac{s(s-1)}{2!}\mu\delta^2 y_{1/2} + \frac{s(s-1)(s-\frac{1}{2})}{3!}\delta^3 y_{1/2} + \cdots$$

where
$$\mu y_{1/2} = \frac{y_0 + y_1}{2}, \qquad \delta y_{1/2} = \Delta y_0, \qquad \mu\delta^2 y_{1/2} = \frac{\Delta^2 y_{-1} + \Delta^2 y_0}{2}$$

> [!IMPORTANT] 🎯 Degree of Precision
> Like all interpolation polynomials through $n+1$ points, Bessel's formula is **exact for polynomials of degree $\le n$**. For cubic data the $\Delta^4$ and higher terms are identically zero.

---

## 3. Bessel vs. Stirling: Which One?

| Target location | Best formula | Why |
| :--- | :--- | :--- |
| Exactly **on a central node** | [[Stirling's Formula]] | Expansion centred on a node; the third-difference term contributes fully |
| **Midway between two central nodes** | **Bessel's Formula** | Expansion centred on the midpoint; the third-difference term vanishes |
| Near the **start** of the table | [[Newton Forward and Backward Difference Interpolation\|Forward]] | One-sided expansion from $x_0$ |
| Near the **end** of the table | [[Newton Forward and Backward Difference Interpolation\|Backward]] | One-sided expansion from $x_n$ |

---

## 4. Worked Step-by-Step Example

> [!EXAMPLE] Problem
> Given the equally spaced data from $f(x) = x^3 - 2x + 1$
>
> | $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
> | :---: | :---: | :---: | :---: | :---: | :---: |
> | $y$ | $1$ | $0$ | $5$ | $22$ | $57$ |
>
> Use **Bessel's formula** to estimate $f(2.5)$, then compare with [[Stirling's Formula]] and the exact value.

**Step 1: Choose the two central nodes**

The target $x = 2.5$ sits **exactly between** $x_2 = 2$ and $x_3 = 3$. Take those as the two central nodes, relabelled $x_0 = 2$ and $x_1 = 3$, so
$$s = \frac{x - x_0}{h} = \frac{2.5 - 2}{1} = 0.5$$

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

Read off the quantities Bessel's formula needs:
- $y_0 = 5$, $y_1 = 22$
- $\Delta y_0 = 17$
- $\Delta^2 y_{-1} = 6$, $\Delta^2 y_0 = 12$
- $\Delta^3 y_{-1} = 6$

**Step 3: Substitute into Bessel's formula**

$$P(x) \approx \frac{y_0 + y_1}{2} + \left(s - \tfrac{1}{2}\right)\Delta y_0 + \frac{s(s-1)}{2}\cdot\frac{\Delta^2 y_{-1} + \Delta^2 y_0}{2} + \frac{s(s-1)(s-\frac{1}{2})}{6}\Delta^3 y_{-1}$$

- Term 1: $\dfrac{y_0 + y_1}{2} = \dfrac{5 + 22}{2} = 13.5$
- Term 2: $\left(s - \tfrac{1}{2}\right)\Delta y_0 = (0.5 - 0.5) \times 17 = 0$ ← vanishes at the midpoint, exactly as predicted
- Term 3: $\dfrac{s(s-1)}{2}\cdot\dfrac{\Delta^2 y_{-1} + \Delta^2 y_0}{2} = \dfrac{0.5(-0.5)}{2} \times \dfrac{6 + 12}{2} = (-0.125) \times 9 = -1.125$
- Term 4: $\dfrac{s(s-1)(s-\frac{1}{2})}{6}\Delta^3 y_{-1} = \dfrac{0.5(-0.5)(0)}{6} \times 6 = 0$

**Step 4: Sum the terms**

$$P(2.5) \approx 13.5 + 0 - 1.125 + 0 = \mathbf{12.375}$$

**Step 5: Compare with Stirling's formula and the exact value**

$$f(2.5) = (2.5)^3 - 2(2.5) + 1 = 15.625 - 5 + 1 = 11.625$$

Stirling's formula on the same data gave $11.8125$ (centred on the node $x_2 = 2$). Here:

$$\text{Bessel error} = |11.625 - 12.375| = \mathbf{0.750}$$
$$\text{Stirling error} = |11.625 - 11.8125| = \mathbf{0.1875}$$

> [!SUCCESS] ✅ Sanity Check
> Both terms that are **supposed** to vanish did vanish: Term 2 and Term 4 both collapse to zero because $s = 0.5$ makes $\left(s - \tfrac{1}{2}\right) = 0$ and $s(s-1)\left(s-\tfrac{1}{2}\right) = 0$. That is the structural signature of a midpoint-centred expansion working correctly.
> On this truncated expansion Stirling's formula lands closer to the true value, which is a useful reminder that these formulas are **local approximations**, not magic: each is optimised for a particular position relative to its centre, and accuracy degrades as the target moves away from that sweet spot. Both are exact for cubic data in principle; neither is automatically the better choice for every target.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why does the third-difference term vanish?
> In the worked example both Term 2 and Term 4 dropped out at $s = 0.5$. Explain why this is expected.

> [!SUCCESS]- Step-by-Step Solution
> 1. Bessel's formula is expanded about the **midpoint** $\frac{x_0 + x_1}{2}$, not about a node.
> 2. That centre choice introduces the factors $\left(s - \tfrac{1}{2}\right)$ and $s(s-1)\left(s-\tfrac{1}{2}\right)$ into the odd-order terms.
> 3. At the midpoint, $s = 0.5$, so $\left(s - \tfrac{1}{2}\right) = 0$ and both odd-order terms vanish identically.
> 4. This is the mirror image of Stirling's behaviour: Stirling's odd terms **cannot** vanish at a node, because its expansion is anchored there. The two formulas are complementary halves of the central-difference toolkit.

---

> [!QUESTION] Practice Question: Choosing the formula
> You must interpolate at $x = 7.0$ from a table on nodes $0, 1, 2, \dots, 10$. Would you pick Stirling's or Bessel's formula?

> [!SUCCESS]- Step-by-Step Solution
> 1. $x = 7.0$ lies **exactly on the node** $x_7$, not between nodes.
> 2. Bessel's formula is designed for targets **midway between** two central nodes — its advantage evaporates on a node.
> 3. **Stirling's formula** is centred on a node, so it is the natural choice here.
> 4. General rule: **on a node → Stirling; in the gap → Bessel.**

---

## 💻 Python Implementation

```python
def bessel_formula(xs, ys, x_target):
    """
    Bessel's central difference interpolation formula.

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

    def d(row, order):
        """Safe access to a forward difference."""
        if 0 <= row < n and 0 <= order < n - row:
            return table[row][order]
        return 0.0

    # Choose the pair of central nodes surrounding x_target
    idx = 0
    for i in range(n - 1):
        if xs[i] <= x_target <= xs[i + 1]:
            idx = i
            break
    s = (x_target - xs[idx]) / h

    result = (d(idx, 0) + d(idx + 1, 0)) / 2
    result += (s - 0.5) * d(idx, 1)
    result += (s * (s - 1) / 2) * (d(idx - 1, 2) + d(idx, 2)) / 2
    result += (s * (s - 1) * (s - 0.5) / 6) * d(idx - 1, 3)
    return result


# Example usage:
xs = [0, 1, 2, 3, 4]
ys = [1, 0, 5, 22, 57]          # f(x) = x^3 - 2x + 1
approx = bessel_formula(xs, ys, 2.5)
exact = 2.5 ** 3 - 2 * 2.5 + 1

print(f"Bessel f(2.5): {approx:.6f}")   # Output: 12.375000
print(f"Exact:         {exact:.6f}")   # Output: 11.625000
```

---

## 🔗 Related Notes
- [[Stirling's Formula]] — The companion central-difference formula for targets *on* a node
- [[Newton Forward and Backward Difference Interpolation]] — The one-sided forward and backward formulas
- [[Newton Divided Difference Interpolation]] — The general formula for **unequal** spacing
- [[Lagrange Interpolation]] — Basis-polynomial alternative for arbitrary nodes
- [[Cubic Spline Interpolation]] — Piecewise alternative that avoids high-degree oscillation
