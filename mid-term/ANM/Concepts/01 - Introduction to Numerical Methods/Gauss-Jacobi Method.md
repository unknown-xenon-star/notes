---
title: "Gauss-Jacobi Iteration Method"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - linear-systems
  - iterative-solvers
aliases:
  - "Jacobi Iteration"
  - "Method of Simultaneous Displacements"
status: completed
---

# 🔢 Gauss-Jacobi Iteration Method

> [!NOTE] 💡 The Big Picture Intuition (The "Batch Processing" Analogy)
> Imagine three cooks working in a kitchen trying to balance a recipe with 3 ingredients: $x, y, z$.
> At the start of step $k$, all three cooks look at the status of yesterday's ingredients $\mathbf{x}^{(k)} = (x^{(k)}, y^{(k)}, z^{(k)})$.
> - Cook 1 computes the new $x^{(k+1)}$ using only yesterday's $y^{(k)}$ and $z^{(k)}$.
> - Cook 2 computes the new $y^{(k+1)}$ using only yesterday's $x^{(k)}$ and $z^{(k)}$.
> - Cook 3 computes the new $z^{(k+1)}$ using only yesterday's $x^{(k)}$ and $y^{(k)}$.
>
> Because all calculations happen **simultaneously in parallel** without using any fresh results from the current round, it is called the **Method of Simultaneous Displacements**!

---

## 1. Mathematical Formulation

Consider a system of $n$ linear algebraic equations with $n$ unknowns, $A\mathbf{x} = \mathbf{b}$:

$$\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
&\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &= b_n
\end{aligned}$$

Assuming non-zero diagonal entries ($a_{ii} \neq 0$), solve each equation for its corresponding diagonal variable $x_i$:

> [!IMPORTANT] 🎯 Gauss-Jacobi Component-wise Formula
> $$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1, j \neq i}^{n} a_{ij} x_j^{(k)} \right), \quad i = 1, 2, \dots, n$$

### For a $3 \times 3$ Linear System:
$$\begin{aligned}
x^{(k+1)} &= \frac{1}{a_{11}}\left(b_1 - a_{12}y^{(k)} - a_{13}z^{(k)}\right) \\
y^{(k+1)} &= \frac{1}{a_{22}}\left(b_2 - a_{21}x^{(k)} - a_{23}z^{(k)}\right) \\
z^{(k+1)} &= \frac{1}{a_{33}}\left(b_3 - a_{31}x^{(k)} - a_{32}y^{(k)}\right)
\end{aligned}$$

---

## 2. Matrix Splitting Formulation

Split the coefficient matrix $A$ into three component matrices:
$$A = D - L - U$$
where:
- $D$ is the diagonal matrix containing $a_{ii}$,
- $-L$ is the strictly lower triangular part of $A$,
- $-U$ is the strictly upper triangular part of $A$.

Substitute this into $A\mathbf{x} = \mathbf{b}$:
$$(D - L - U)\mathbf{x} = \mathbf{b} \implies D\mathbf{x} = (L + U)\mathbf{x} + \mathbf{b}$$

Multiplying by $D^{-1}$ yields the matrix iteration scheme:

> [!NOTE] Jacobi Matrix Iteration Scheme
> $$\mathbf{x}^{(k+1)} = D^{-1}(L + U)\mathbf{x}^{(k)} + D^{-1}\mathbf{b} = T_J \mathbf{x}^{(k)} + \mathbf{c}_J$$
> where:
> - $T_J = D^{-1}(L + U)$ is the **Jacobi Iteration Matrix**.
> - $\mathbf{c}_J = D^{-1}\mathbf{b}$ is the **load vector**.

---

## 3. Convergence Criterion (Strict Diagonal Dominance)

> [!IMPORTANT] 🎯 The Strict Diagonal Dominance (SDD) Theorem
> An iterative solver is **guaranteed to converge** for ANY starting vector $\mathbf{x}^{(0)}$ if the matrix $A$ is **Strictly Diagonally Dominant (SDD)**:
> $$|a_{ii}| > \sum_{j=1, j \neq i}^{n} |a_{ij}| \quad \text{for every row } i = 1, 2, \dots, n$$
>
> *General Necessary & Sufficient Condition*: The spectral radius of the iteration matrix must be less than unity:
> $$\rho(T_J) = \max_i |\lambda_i(T_J)| < 1$$

> [!TIP] 💡 Exam Tip: Rearranging Equations (Pivoting)
> If a system is not diagonally dominant as written in the exam prompt, **swap the order of equations** (row pivoting) so that the largest coefficient in each column/variable sits right on the main diagonal before computing iteration 1!

---

## 4. Worked Step-by-Step Examples

### Worked Example 1: Full $3 \times 3$ System Execution
> [!EXAMPLE] Problem
> Solve the following system of linear equations using the Gauss-Jacobi method starting with initial vector $\mathbf{x}^{(0)} = (0, 0, 0)^T$ for 3 iterations:
> $$\begin{aligned}
> 10x - y + 2z &= 4 \\
> x + 10y - z &= 3 \\
> 2x + 3y + 10z &= 7
> \end{aligned}$$

**Step 1: Verify Strict Diagonal Dominance (SDD)**
- **Row 1**: $|10| > |-1| + |2| = 3$ ($10 > 3$) ✅
- **Row 2**: $|10| > |1| + |-1| = 2$ ($10 > 2$) ✅
- **Row 3**: $|10| > |2| + |3| = 5$ ($10 > 5$) ✅
The system is SDD, guaranteeing convergence!

**Step 2: Formulate the Jacobi Iteration Equations**
$$x^{(k+1)} = \frac{4 + y^{(k)} - 2z^{(k)}}{10}$$
$$y^{(k+1)} = \frac{3 - x^{(k)} + z^{(k)}}{10}$$
$$z^{(k+1)} = \frac{7 - 2x^{(k)} - 3y^{(k)}}{10}$$

**Step 3: Line-by-Line Iterations**

- **Iteration 1 ($k=0 \implies \mathbf{x}^{(1)}$):**
  Using $x^{(0)} = 0, y^{(0)} = 0, z^{(0)} = 0$:
  $$x^{(1)} = \frac{4 + 0 - 2(0)}{10} = \frac{4}{10} = \mathbf{0.4000}$$
  $$y^{(1)} = \frac{3 - 0 + 0}{10} = \frac{3}{10} = \mathbf{0.3000}$$
  $$z^{(1)} = \frac{7 - 2(0) - 3(0)}{10} = \frac{7}{10} = \mathbf{0.7000}$$

- **Iteration 2 ($k=1 \implies \mathbf{x}^{(2)}$):**
  Using $x^{(1)} = 0.4000, y^{(1)} = 0.3000, z^{(1)} = 0.7000$:
  $$x^{(2)} = \frac{4 + 0.3000 - 2(0.7000)}{10} = \frac{4 + 0.3000 - 1.4000}{10} = \frac{2.9000}{10} = \mathbf{0.2900}$$
  $$y^{(2)} = \frac{3 - 0.4000 + 0.7000}{10} = \frac{3.3000}{10} = \mathbf{0.3300}$$
  $$z^{(2)} = \frac{7 - 2(0.4000) - 3(0.3000)}{10} = \frac{7 - 0.8000 - 0.9000}{10} = \frac{5.3000}{10} = \mathbf{0.5300}$$

- **Iteration 3 ($k=2 \implies \mathbf{x}^{(3)}$):**
  Using $x^{(2)} = 0.2900, y^{(2)} = 0.3300, z^{(2)} = 0.5300$:
  $$x^{(3)} = \frac{4 + 0.3300 - 2(0.5300)}{10} = \frac{4 + 0.3300 - 1.0600}{10} = \frac{3.2700}{10} = \mathbf{0.3270}$$
  $$y^{(3)} = \frac{3 - 0.2900 + 0.5300}{10} = \frac{3.2400}{10} = \mathbf{0.3240}$$
  $$z^{(3)} = \frac{7 - 2(0.2900) - 3(0.3300)}{10} = \frac{7 - 0.5800 - 0.9900}{10} = \frac{5.4300}{10} = \mathbf{0.5430}$$

### Iteration Table:

| Iteration ($k$) | $x^{(k)}$ | $y^{(k)}$ | $z^{(k)}$ | Step Error $\|\mathbf{x}^{(k)} - \mathbf{x}^{(k-1)}\|_\infty$ |
| :---: | :---: | :---: | :---: | :---: |
| **0** | $0.0000$ | $0.0000$ | $0.0000$ | — |
| **1** | **$0.4000$** | **$0.3000$** | **$0.7000$** | $0.7000$ |
| **2** | **$0.2900$** | **$0.3300$** | **$0.5300$** | $0.1700$ |
| **3** | **$0.3270$** | **$0.3240$** | **$0.5430$** | $0.0370$ |

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Row Pivoting for SDD
> Consider the system:
> $$\begin{aligned}
> x + 5y + z &= 7 \\
> 4x + y - z &= 4 \\
> x - y + 6z &= 6
> \end{aligned}$$
> Is it diagonally dominant? How should it be rearranged for Jacobi iteration?

> [!SUCCESS]- Step-by-Step Solution
> 1. Check Row 1: $|1| < |5| + |1| = 6$ ❌ Not dominant ($x$ has small coefficient).
> 2. Look down column 1 for the largest coefficient: $4x$ in equation 2.
> 3. Look down column 2 for the largest coefficient: $5y$ in equation 1.
> 4. Look down column 3 for the largest coefficient: $6z$ in equation 3.
> 5. **Rearranged System**:
>    - Equation 1 (new): $4x + y - z = 4 \implies |4| > |1| + |-1| = 2$ ✅
>    - Equation 2 (new): $x + 5y + z = 7 \implies |5| > |1| + |1| = 2$ ✅
>    - Equation 3 (new): $x - y + 6z = 6 \implies |6| > |1| + |-1| = 2$ ✅
> 6. Now the matrix is strictly diagonally dominant and ready for Jacobi iteration!

---

## 💻 Python Implementation

```python
import numpy as np

def gauss_jacobi(A, b, x0=None, tol=1e-5, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
        
    x = x0.copy()
    x_new = np.zeros(n)
    
    for k in range(1, max_iter + 1):
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i, i]
            
        if np.max(np.abs(x_new - x)) < tol:
            return x_new, k
            
        x = x_new.copy()
        
    return x, max_iter
```

---

## 🔗 Related Notes
- [[Gauss-Seidel Method]] — Immediate in-place updating variant that converges twice as fast.
- [[Errors and Convergence]] — Matrix condition numbers and stopping rules.
