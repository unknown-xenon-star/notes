---
title: "Numerical Methods - High-Yield Formula Sheet"
date: 2026-09-19
tags:
  - summary
  - cheat-sheet
  - numerical-methods
  - exam-prep
aliases:
  - "Formula Sheet"
  - "Numerical Analysis Quick Reference"
status: completed
---

# ⚡ Numerical Methods: Mid-Term Revision Cheat Sheet

> [!SUMMARY] 🎯 Master Cheat Sheet
> A high-yield reference guide containing all essential formulas, convergence rates, stopping criteria, matrix splitting relations, and exam tips.

---

## 📌 1. Master Comparison: Single Equation Root-Finding

| Method | Type | Iteration Formula | Order of Convergence ($p$) | Conditions / Exam Notes |
| :--- | :---: | :--- | :---: | :--- |
| **[[Bisection Method]]** | Bracketing | $c = \frac{a+b}{2}$ | **$p = 1$** (Linear, $C=0.5$) | Guaranteed to converge if $f(a)f(b) < 0$. Error strictly halves every step. |
| **[[Regula Falsi Method]]** | Bracketing | $c = \frac{a f(b) - b f(a)}{f(b) - f(a)}$ | **$p = 1$** (Linear) | Faster than Bisection initially; prone to one-sided stagnant endpoint. |
| **[[Fixed-Point Iteration]]** | Open | $x_{k+1} = g(x_k)$ | **$p = 1$** (Linear) | Converges iff $\vert g'(x) \vert < 1$ near root $\alpha$. If $g'(\alpha) = 0 \implies p=2$. |
| **[[Newton-Raphson Method]]** | Open | $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$ | **$p = 2$** (Quadratic) | Requires $f'(x_k) \neq 0$. Simple roots only. Digits double each step. |
| **[[Secant Method]]** | Open | $x_{k+1} = \frac{x_{k-1}f(x_k) - x_k f(x_{k-1})}{f(x_k) - f(x_{k-1})}$ | **$p \approx 1.618$** (Superlinear) | No derivative required. 1 evaluation/step $\implies$ higher efficiency index than Newton. |

---

## 📌 2. High-Speed Special Newton Formulas

| Target Calculation | Objective Equation | Dedicated Iteration Formula |
| :--- | :--- | :--- |
| **Square Root ($\sqrt{N}$)** | $f(x) = x^2 - N = 0$ | $x_{k+1} = \frac{1}{2}\left(x_k + \frac{N}{x_k}\right)$ |
| **$p$-th Root ($\sqrt[p]{N}$)** | $f(x) = x^p - N = 0$ | $x_{k+1} = \frac{1}{p}\left((p-1)x_k + \frac{N}{x_k^{p-1}}\right)$ |
| **Reciprocal ($\frac{1}{N}$)** | $f(x) = \frac{1}{x} - N = 0$ | $x_{k+1} = x_k(2 - Nx_k)$ *(No division needed)* |
| **Multiple Root (Multiplicity $m$)** | $f(\alpha) = f'(\alpha) = 0$ | $x_{k+1} = x_k - m \frac{f(x_k)}{f'(x_k)}$ |

---

## 📌 3. Linear Systems of Equations ($A\mathbf{x} = \mathbf{b}$)

### Strict Diagonal Dominance (SDD) Condition
Iterative linear solvers are guaranteed to converge for **any** starting vector $\mathbf{x}^{(0)}$ if:
$$|a_{ii}| > \sum_{j=1, j \neq i}^{n} |a_{ij}| \quad \forall i = 1, 2, \dots, n$$

| Solver | Updating Scheme | Component Iteration Formula | Matrix Iteration Scheme |
| :--- | :--- | :--- | :--- |
| **[[Gauss-Jacobi Method]]** | Simultaneous Displacement | $x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j \neq i} a_{ij}x_j^{(k)}\right)$ | $\mathbf{x}^{(k+1)} = D^{-1}(L+U)\mathbf{x}^{(k)} + D^{-1}\mathbf{b}$ |
| **[[Gauss-Seidel Method]]** | Successive Displacement (In-Place) | $x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j<i} a_{ij}x_j^{(k+1)} - \sum_{j>i} a_{ij}x_j^{(k)}\right)$ | $\mathbf{x}^{(k+1)} = (D-L)^{-1}U\mathbf{x}^{(k)} + (D-L)^{-1}\mathbf{b}$ |

> [!TIP] 💡 Exam Takeaway
> For tridiagonal and consistently ordered matrices, **Gauss-Seidel converges twice as fast as Gauss-Jacobi** ($\rho(T_{GS}) \approx [\rho(T_J)]^2$).

---

## 📌 4. Polynomial Root-Finding

### A. [[Graeffe's Root-Squaring Method]]
- **Squaring Step**:
  $$A_k = (-1)^k \left[ a_k^2 - 2a_{k-1}a_{k+1} + 2a_{k-2}a_{k+2} - 2a_{k-3}a_{k+3} + \dots \right]$$
- **Root Magnitudes after $m$ squarings ($N = 2^m$)**:
  $$|\alpha_i| = \left( \frac{A_i}{A_{i-1}} \right)^{1/N}$$
- Direct, non-iterative method that extracts **all roots simultaneously**.

### B. [[Lin-Bairstow Method]]
- **Extracts Quadratic Factor**: $x^2 - rx - s = 0 \implies x_{1, 2} = \frac{r \pm \sqrt{r^2 + 4s}}{2}$
- **Double Synthetic Recurrences**:
  - $b_0 = a_0, \quad b_1 = a_1 + rb_0, \quad b_k = a_k + rb_{k-1} + sb_{k-2}$
  - $c_0 = b_0, \quad c_1 = b_1 + rc_0, \quad c_k = b_k + rc_{k-1} + sc_{k-2}$
- **Corrections & Updates**:
  $$D = c_{n-2}^2 - c_{n-1}c_{n-3}$$
  $$\Delta r = \frac{b_n c_{n-3} - b_{n-1} c_{n-2}}{D}, \quad \Delta s = \frac{b_{n-1} c_{n-1} - b_n c_{n-2}}{D}$$
  $$r_{\text{new}} = r + \Delta r, \quad s_{\text{new}} = s + \Delta s$$

---

## 🎯 5. Numerical Integration (Quadrature)

| Rule | Composite Formula | Strips $n$ | Composite Error | Precision |
| :--- | :--- | :---: | :--- | :---: |
| **[[Trapezoidal Rule]]** | $\frac{h}{2}\big[y_0 + 2(y_1+\dots+y_{n-1}) + y_n\big]$ | any | $-\frac{(b-a)h^2}{12}f''(\xi)$ | 1 |
| **[[Simpson's One-Third Rule]]** | $\frac{h}{3}\big[(y_0+y_n) + 4\Sigma y_{\text{odd}} + 2\Sigma y_{\text{even}}\big]$ | even | $-\frac{(b-a)h^4}{180}f^{(4)}(\xi)$ | 3 |
| **[[Simpson's Three-Eighths Rule]]** | $\frac{3h}{8}\big[(y_0+y_n) + 3\Sigma y_{\text{non-boundary}} + 2\Sigma y_{3,6,\dots}\big]$ | $\equiv 0 \pmod 3$ | $-\frac{(b-a)h^4}{80}f^{(4)}(\xi)$ | 3 |
| **[[Weddle's Rule]]** | $\frac{3h}{10}\big[y_0+5y_1+y_2+6y_3+y_4+5y_5+y_6\big]$ per panel | $\equiv 0 \pmod 6$ | $-\frac{(b-a)h^6}{840}f^{(6)}(\xi)$ | 5 |

> [!TIP] 💡 Quadrature Exam Takeaways
> - Strip-doubling shrinkage: error ÷ **4** (Trapezoidal), ÷ **16** (Simpson), ÷ **64** (Weddle).
> - $n$ compatibility cheatsheet: $n = 12$ → all rules apply; $n = 7$ → Simpson 1/3 on 4 strips + Simpson 3/8 on 3 strips.
> - Romberg idea: $\frac{4I_{h/2} - I_h}{3}$ cancels the trapezoidal $h^2$ error (→ Simpson accuracy).
> - **[[Lagrange Inverse Interpolation]]** (companion topic): to find $x$ given $y$, swap variables — $x = \sum_j x_j \prod_{k \neq j} \frac{y - y_k}{y_j - y_k}$; at $y = 0$ it is a one-shot root finder reducing to the secant formula for two points.

---

## 🎯 6. Error & Stopping Criteria Quick Reference

| Measure | Mathematical Formula | Purpose / Meaning |
| :--- | :--- | :--- |
| **Absolute Error ($E_a$)** | $E_a = \vert x_{\text{true}} - x_{\text{approx}} \vert$ | Raw numerical distance |
| **Relative Error ($E_r$)** | $E_r = \frac{\vert x_{\text{true}} - x_{\text{approx}} \vert}{\vert x_{\text{true}} \vert}$ | Scale-free error fraction |
| **Percentage Error ($E_p$)** | $E_p = E_r \times 100\%$ | Error as a percentage |
| **Approximate Relative Error ($\epsilon_a$)** | $\epsilon_a = \left\vert \frac{x_{k+1} - x_k}{x_{k+1}} \right\vert \times 100\%$ | Iterative error without knowing true root |
| **Scarborough Criterion** | $\epsilon_a \le 0.5 \times 10^{2-m}\%$ | Guarantees $m$ correct significant digits |
| **Bisection Iteration Count** | $n > \frac{\log_{10}(b_0 - a_0) - \log_{10}(\epsilon)}{\log_{10} 2}$ | Exact steps needed to achieve tolerance $\epsilon$ |
| **Aitken's $\Delta^2$ Acceleration** | $\hat{x}_0 = x_0 - \frac{(x_1 - x_0)^2}{x_2 - 2x_1 + x_0}$ | Accelerates linear sequences |

---

## 🔗 Quick Links to Full Modules
- [[00 - Numerical Methods Index|🏠 Master Hub]]
- [[Roots of Equations]] | [[Errors and Convergence]]
- [[Bisection Method]] | [[Regula Falsi Method]]
- [[Fixed-Point Iteration]] | [[Newton-Raphson Method]] | [[Secant Method]]
- [[Gauss-Jacobi Method]] | [[Gauss-Seidel Method]]
- [[Graeffe's Root-Squaring Method]] | [[Lin-Bairstow Method]]
- [[Lagrange Interpolation]] | [[Lagrange Inverse Interpolation]] | [[Cubic Spline Interpolation]]
- [[Newton Forward and Backward Difference Interpolation]] | [[Stirling's Formula]] | [[Bessel's Formula]]
- [[Trapezoidal Rule]] | [[Simpson's One-Third Rule]] | [[Simpson's Three-Eighths Rule]] | [[Weddle's Rule]] | [[Error in Quadrature Formulas – Trapezoidal, Simpson's]]
