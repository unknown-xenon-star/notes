---
title: "Gauss-Seidel Iteration Method"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - linear-systems
  - iterative-solvers
aliases:
  - "Method of Successive Displacements"
  - "Liebmann's Method"
status: completed
---

# ⚡ Gauss-Seidel Iteration Method

> [!NOTE] 💡 The Big Picture Intuition (The "Fresh Ingredients" Analogy)
> In the [[Gauss-Jacobi Method]], all variables are updated using only "yesterday's" data, even if you just finished computing a fresher, more accurate value for $x$ a second ago!
> **Gauss-Seidel** fixes this inefficiency: the moment you calculate a new value $x^{(k+1)}$, you **immediately overwrite the old value and use the new one** in the very next line for $y^{(k+1)}$ and $z^{(k+1)}$!
> By always feeding the freshest available numbers into the next calculation, Gauss-Seidel converges **roughly twice as fast** as Jacobi and uses **half the computer memory**!

---

## 1. Mathematical Formulation

Given the linear system $A\mathbf{x} = \mathbf{b}$ with non-zero diagonal elements ($a_{ii} \neq 0$):

$$\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
&\vdots \\
a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &= b_n
\end{aligned}$$

> [!IMPORTANT] 🎯 Gauss-Seidel Component-wise Formula
> $$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} \mathbf{x_j^{(k+1)}} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)} \right), \quad i = 1, 2, \dots, n$$

### For a $3 \times 3$ Linear System:
$$\begin{aligned}
x^{(k+1)} &= \frac{1}{a_{11}}\left(b_1 - a_{12}y^{(k)} - a_{13}z^{(k)}\right) \\
y^{(k+1)} &= \frac{1}{a_{22}}\left(b_2 - a_{21}\mathbf{x^{(k+1)}} - a_{23}z^{(k)}\right) \\
z^{(k+1)} &= \frac{1}{a_{33}}\left(b_3 - a_{31}\mathbf{x^{(k+1)}} - a_{32}\mathbf{y^{(k+1)}}\right)
\end{aligned}$$

*Notice the bolded terms*: newly computed values $\mathbf{x^{(k+1)}}$ and $\mathbf{y^{(k+1)}}$ are immediately substituted within the same iteration pass!

---

## 2. Matrix Splitting Formulation

Split matrix $A$ into:
$$A = D - L - U$$
where:
- $D$ is diagonal,
- $-L$ is strictly lower triangular,
- $-U$ is strictly upper triangular.

Substitute into $A\mathbf{x} = \mathbf{b}$:
$$(D - L - U)\mathbf{x} = \mathbf{b} \implies (D - L)\mathbf{x}^{(k+1)} = U\mathbf{x}^{(k)} + \mathbf{b}$$

Multiplying both sides by $(D - L)^{-1}$:

> [!NOTE] Gauss-Seidel Matrix Iteration Scheme
> $$\mathbf{x}^{(k+1)} = (D - L)^{-1} U \mathbf{x}^{(k)} + (D - L)^{-1}\mathbf{b} = T_{GS} \mathbf{x}^{(k)} + \mathbf{c}_{GS}$$
> where:
> - $T_{GS} = (D - L)^{-1} U$ is the **Gauss-Seidel Iteration Matrix**.
> - $\mathbf{c}_{GS} = (D - L)^{-1}\mathbf{b}$ is the **load vector**.

---

## 3. Convergence & Speed Theorems

### Sufficient Conditions for Guaranteed Convergence:
Gauss-Seidel is guaranteed to converge for any starting guess $\mathbf{x}^{(0)}$ if $A$ satisfies **either** of the following:
1. $A$ is **Strictly Diagonally Dominant (SDD)**:
   $$|a_{ii}| > \sum_{j \neq i} |a_{ij}| \quad \forall i = 1, 2, \dots, n$$
2. $A$ is **Symmetric Positive Definite (SPD)**:
   $$A = A^T \quad \text{and} \quad \mathbf{x}^T A \mathbf{x} > 0 \quad \forall \mathbf{x} \neq \mathbf{0}$$

### Speed Comparison with Jacobi (Stein-Rosenberg Theorem):
For matrices where $a_{ij} \le 0$ for all $i \neq j$ (e.g. tridiagonal discretization matrices):
$$\rho(T_{GS}) \approx [\rho(T_J)]^2$$

> [!TIP] 💡 Exam Takeaway: The $2\times$ Speed Rule
> Because $[\rho(T_J)]^2 < \rho(T_J)$, **Gauss-Seidel requires roughly half the number of iterations** as Gauss-Jacobi to achieve the same precision!

---

## 4. Worked Step-by-Step Examples

### Worked Example 1: Full $3 \times 3$ Execution (Contrasted with Jacobi)
> [!EXAMPLE] Problem
> Solve the following system using the Gauss-Seidel method starting from $\mathbf{x}^{(0)} = (0, 0, 0)^T$ for 3 iterations:
> $$\begin{aligned}
> 10x - y + 2z &= 4 \\
> x + 10y - z &= 3 \\
> 2x + 3y + 10z &= 7
> \end{aligned}$$

**Step 1: Check Diagonal Dominance**
- Row 1: $|10| > 1 + 2 = 3$ ✅
- Row 2: $|10| > 1 + 1 = 2$ ✅
- Row 3: $|10| > 2 + 3 = 5$ ✅ (System is SDD!)

**Step 2: Write Gauss-Seidel Iteration Equations**
$$x^{(k+1)} = \frac{4 + y^{(k)} - 2z^{(k)}}{10}$$
$$y^{(k+1)} = \frac{3 - \mathbf{x^{(k+1)}} + z^{(k)}}{10}$$
$$z^{(k+1)} = \frac{7 - 2\mathbf{x^{(k+1)}} - 3\mathbf{y^{(k+1)}}}{10}$$

**Step 3: Line-by-Line Calculations**

- **Iteration 1 ($k=0 \implies \mathbf{x}^{(1)}$):**
  - Compute $x^{(1)}$ using $y^{(0)} = 0, z^{(0)} = 0$:
    $$x^{(1)} = \frac{4 + 0 - 2(0)}{10} = \mathbf{0.4000}$$
  - Compute $y^{(1)}$ using updated $x^{(1)} = \mathbf{0.4000}$ and $z^{(0)} = 0$:
    $$y^{(1)} = \frac{3 - (0.4000) + 0}{10} = \frac{2.6000}{10} = \mathbf{0.2600}$$
  - Compute $z^{(1)}$ using updated $x^{(1)} = \mathbf{0.4000}$ and updated $y^{(1)} = \mathbf{0.2600}$:
    $$z^{(1)} = \frac{7 - 2(0.4000) - 3(0.2600)}{10} = \frac{7 - 0.8000 - 0.7800}{10} = \frac{5.4200}{10} = \mathbf{0.5420}$$

- **Iteration 2 ($k=1 \implies \mathbf{x}^{(2)}$):**
  - Compute $x^{(2)}$ using $y^{(1)} = 0.2600, z^{(1)} = 0.5420$:
    $$x^{(2)} = \frac{4 + 0.2600 - 2(0.5420)}{10} = \frac{4 + 0.2600 - 1.0840}{10} = \frac{3.1760}{10} = \mathbf{0.3176}$$
  - Compute $y^{(2)}$ using updated $x^{(2)} = \mathbf{0.3176}$ and $z^{(1)} = 0.5420$:
    $$y^{(2)} = \frac{3 - (0.3176) + 0.5420}{10} = \frac{3.2244}{10} = \mathbf{0.3224}$$
  - Compute $z^{(2)}$ using updated $x^{(2)} = \mathbf{0.3176}$ and updated $y^{(2)} = \mathbf{0.3224}$:
    $$z^{(2)} = \frac{7 - 2(0.3176) - 3(0.3224)}{10} = \frac{7 - 0.6352 - 0.9672}{10} = \frac{5.3976}{10} = \mathbf{0.5398}$$

- **Iteration 3 ($k=2 \implies \mathbf{x}^{(3)}$):**
  - Compute $x^{(3)}$ using $y^{(2)} = 0.3224, z^{(2)} = 0.5398$:
    $$x^{(3)} = \frac{4 + 0.3224 - 2(0.5398)}{10} = \frac{4 + 0.3224 - 1.0796}{10} = \frac{3.2428}{10} = \mathbf{0.3243}$$
  - Compute $y^{(3)}$ using updated $x^{(3)} = \mathbf{0.3243}$ and $z^{(2)} = 0.5398$:
    $$y^{(3)} = \frac{3 - (0.3243) + 0.5398}{10} = \frac{3.2155}{10} = \mathbf{0.3216}$$
  - Compute $z^{(3)}$ using updated $x^{(3)} = \mathbf{0.3243}$ and updated $y^{(3)} = \mathbf{0.3216}$:
    $$z^{(3)} = \frac{7 - 2(0.3243) - 3(0.3216)}{10} = \frac{7 - 0.6486 - 0.9648}{10} = \frac{5.3866}{10} = \mathbf{0.5387}$$

### Side-by-Side Comparison: Jacobi vs. Gauss-Seidel

| $k$ | Jacobi $x^{(k)}$ | Gauss-Seidel $x^{(k)}$ | Jacobi $y^{(k)}$ | Gauss-Seidel $y^{(k)}$ | Jacobi $z^{(k)}$ | Gauss-Seidel $z^{(k)}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ | $0.0000$ |
| **1** | $0.4000$ | **$0.4000$** | $0.3000$ | **$0.2600$** | $0.7000$ | **$0.5420$** |
| **2** | $0.2900$ | **$0.3176$** | $0.3300$ | **$0.3224$** | $0.5300$ | **$0.5398$** |
| **3** | $0.3270$ | **$0.3243$** | $0.3240$ | **$0.3216$** | $0.5430$ | **$0.5387$** |

*Observation*: Gauss-Seidel at $k=2$ is already more accurate than Jacobi at $k=3$!

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Memory & Parallelism Trade-off
> Why is Gauss-Jacobi preferred over Gauss-Seidel on supercomputers (GPUs/multicore clusters), even though Gauss-Seidel takes fewer mathematical iterations?

> [!SUCCESS]- Step-by-Step Solution
> 1. **Gauss-Jacobi**: Each component $x_i^{(k+1)}$ depends only on values from the *previous* iteration step $k$. Thus, all $n$ equations can be computed **simultaneously in parallel** across thousands of GPU threads with zero synchronization lock.
> 2. **Gauss-Seidel**: Component $x_2$ strictly requires the updated $x_1$, and $x_3$ strictly requires $x_1$ and $x_2$. This **sequential dependency** prevents massive parallelization across threads.

---

## 💻 Python Implementation

```python
import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-5, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
        
    x = x0.copy()
    for k in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            s1 = sum(A[i, j] * x[j] for j in range(i))
            s2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i, i]
            
        if np.max(np.abs(x - x_old)) < tol:
            return x, k
            
    return x, max_iter
```

---

## 🔗 Related Notes
- [[Gauss-Jacobi Method]] — Simultaneous displacement foundation.
- [[Errors and Convergence]] — Matrix condition numbers and stopping rules.
