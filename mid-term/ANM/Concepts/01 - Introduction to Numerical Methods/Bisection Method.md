---
title: "Bisection Method"
date: 2026-09-19
tags:
  - concept
  - numerical-methods
  - root-finding
  - bracketing-methods
aliases:
  - "Interval Halving Method"
  - "Binary Search Method"
  - "Bolzano's Method"
status: completed
---

# ✂️ Bisection Method (Interval Halving)

> [!NOTE] 💡 The Big Picture Intuition
> Think of the classic **"Higher or Lower" number guessing game**. If you are told a secret number is between $1$ and $100$, your smartest first guess is $50$. If the host says "Lower", you throw away the entire range from $50$ to $100$ and test $25$.
> The **Bisection Method** is the mathematical equivalent: start with an interval $[a, b]$ where the curve starts underground ($f(a) < 0$) and ends above ground ($f(b) > 0$). Cut the interval right down the middle ($c = \frac{a+b}{2}$). By the **Intermediate Value Theorem**, the root is guaranteed to live in whichever half has opposite signs at its endpoints!

---

## 1. Visual & Geometric Workflow

```
Iteration 1:    a ---------------------- c ---------------------- b
                f(a) < 0               f(c) > 0                 f(b) > 0
                [ Root guaranteed here ]   x (Discard right half)

Iteration 2:    a ---------- c' ---------- b' (PREVIOUS c)
                f(a) < 0    f(c') < 0     f(b') > 0
                             [ Root here ]
```

---

## 2. Step-by-Step Algorithm

1. **Step 1: Check the Initial Bracket**
   Find two points $a_0$ and $b_0$ ($a_0 < b_0$) such that $f(x)$ is continuous on $[a_0, b_0]$ and has opposite signs at the endpoints:
   $$f(a_0) \cdot f(b_0) < 0$$

2. **Step 2: Calculate the Midpoint**
   $$c_k = \frac{a_k + b_k}{2}$$

3. **Step 3: Evaluate $f(c_k)$ and Check Stopping Criteria**
   - If $|f(c_k)| < \epsilon$ or $\frac{b_k - a_k}{2} < \epsilon$, **STOP**! The approximate root is $\alpha \approx c_k$.

4. **Step 4: Update the Bracket for the Next Step**
   - If $f(a_k) \cdot f(c_k) < 0$: The root is in the left half $[a_k, c_k]$. Set $a_{k+1} = a_k$ and $b_{k+1} = c_k$.
   - If $f(a_k) \cdot f(c_k) > 0$: The root is in the right half $[c_k, b_k]$. Set $a_{k+1} = c_k$ and $b_{k+1} = b_k$.
   - If $f(c_k) = 0$: $c_k$ is the exact root! **STOP**.

5. **Step 5: Repeat** until the desired tolerance $\epsilon$ is reached.

---

## 3. Error Analysis & Number of Iterations

Let the initial interval be $[a_0, b_0]$ with width $L_0 = b_0 - a_0$.

- **Interval width after $n$ iterations**:
  $$\Delta x_n = \frac{b_0 - a_0}{2^n}$$

- **Maximum error bound after $n$ iterations**:
  $$e_n = |\alpha - c_n| \le \frac{b_0 - a_0}{2^{n+1}}$$

- **Convergence Properties**:
  - **Order of Convergence ($p$)**: **$p = 1$ (Linear Convergence)**.
  - **Asymptotic Error Constant ($C$)**: **$C = 0.5$** (The uncertainty is strictly cut in half at every iteration).

> [!IMPORTANT] 🎯 Formula: Minimum Iterations Needed for Given Tolerance ($\epsilon$)
> To guarantee that the error $e_n \le \epsilon$, the required number of bisection iterations $n$ must satisfy:
> $$\frac{b_0 - a_0}{2^{n+1}} < \epsilon \implies 2^{n+1} > \frac{b_0 - a_0}{\epsilon}$$
> Taking natural logarithms:
> $$n > \frac{\ln(b_0 - a_0) - \ln(\epsilon)}{\ln 2} - 1 \quad \text{or for interval width: } n > \frac{\log_{10}(b_0 - a_0) - \log_{10}(\epsilon)}{\log_{10} 2}$$

---

## 4. Worked Step-by-Step Examples

### Worked Example 1: Full Numerical Execution
> [!EXAMPLE] Problem
> Find the real root of $f(x) = x^3 - x - 2 = 0$ in the interval $[1, 2]$ using the Bisection Method until the error bound is less than $\epsilon = 0.05$.

**Step 1: Check Initial Bracket**
- $f(1) = (1)^3 - (1) - 2 = 1 - 1 - 2 = -2 < 0$
- $f(2) = (2)^3 - (2) - 2 = 8 - 2 - 2 = +4 > 0$
- $f(1) \cdot f(2) = (-2)(+4) = -8 < 0$ ✅ Bracket is valid!

**Step 2: Iteration Calculations**

- **Iteration 1**:
  - Midpoint: $c_1 = \frac{1 + 2}{2} = \mathbf{1.5000}$
  - Evaluate: $f(1.5) = (1.5)^3 - 1.5 - 2 = 3.375 - 1.5 - 2 = \mathbf{-0.1250} < 0$
  - Check signs: $f(a_1) \cdot f(c_1) = f(1) \cdot f(1.5) = (-2)(-0.1250) = +0.25 > 0$.
  - Update: Replace left boundary $\implies a_2 = 1.5, b_2 = 2.0$.
  - Current Error Bound: $\frac{2 - 1.5}{2} = \frac{0.5}{2} = 0.2500$.

- **Iteration 2**:
  - Midpoint: $c_2 = \frac{1.5 + 2.0}{2} = \mathbf{1.7500}$
  - Evaluate: $f(1.75) = (1.75)^3 - 1.75 - 2 = 5.3594 - 1.75 - 2 = \mathbf{+1.6094} > 0$
  - Check signs: $f(a_2) \cdot f(c_2) = f(1.5) \cdot f(1.75) = (-0.1250)(+1.6094) < 0$.
  - Update: Replace right boundary $\implies a_3 = 1.5, b_3 = 1.75$.
  - Current Error Bound: $\frac{1.75 - 1.5}{2} = \frac{0.25}{2} = 0.1250$.

- **Iteration 3**:
  - Midpoint: $c_3 = \frac{1.5 + 1.75}{2} = \mathbf{1.6250}$
  - Evaluate: $f(1.625) = (1.625)^3 - 1.625 - 2 = 4.2910 - 1.625 - 2 = \mathbf{+0.6660} > 0$
  - Update: Replace right boundary $\implies a_4 = 1.5, b_4 = 1.625$.
  - Current Error Bound: $\frac{1.625 - 1.5}{2} = \frac{0.125}{2} = 0.0625$.

- **Iteration 4**:
  - Midpoint: $c_4 = \frac{1.5 + 1.625}{2} = \mathbf{1.5625}$
  - Evaluate: $f(1.5625) = (1.5625)^3 - 1.5625 - 2 = 3.8147 - 1.5625 - 2 = \mathbf{+0.2522} > 0$
  - Update: Replace right boundary $\implies a_5 = 1.5, b_5 = 1.5625$.
  - Current Error Bound: $\frac{1.5625 - 1.5}{2} = \frac{0.0625}{2} = \mathbf{0.03125} < 0.05$ ✅

### Complete Iteration Table:

| Iteration ($k$) | $a_k$ | $b_k$ | Midpoint $c_k$ | $f(c_k)$ | Sign Check $f(a_k)f(c_k)$ | Next Bracket | Error Bound $\frac{b-a}{2}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $1.0000$ | $2.0000$ | **$1.5000$** | $-0.1250$ | $(-) \times (-) > 0$ | $[1.5, 2.0]$ | $0.2500$ |
| **2** | $1.5000$ | $2.0000$ | **$1.7500$** | $+1.6094$ | $(-) \times (+) < 0$ | $[1.5, 1.75]$ | $0.1250$ |
| **3** | $1.5000$ | $1.7500$ | **$1.6250$** | $+0.6660$ | $(-) \times (+) < 0$ | $[1.5, 1.625]$ | $0.0625$ |
| **4** | $1.5000$ | $1.6250$ | **$1.5625$** | $+0.2522$ | $(-) \times (+) < 0$ | $[1.5, 1.5625]$ | **$0.03125$** |

**Final Approximate Root**: **$x \approx 1.5625$** (with error $< 0.03125$).

---

### Worked Example 2: Calculating Required Iterations Ahead of Time
> [!EXAMPLE] Problem
> How many bisection iterations are required to find a root of an equation in the interval $[1, 5]$ with an accuracy of $\epsilon = 10^{-4}$?

**Step 1: Identify Parameters**
- Initial interval: $a_0 = 1, b_0 = 5 \implies b_0 - a_0 = 5 - 1 = 4$.
- Desired tolerance: $\epsilon = 10^{-4} = 0.0001$.

**Step 2: Apply the Formula**
$$n > \frac{\log_{10}(b_0 - a_0) - \log_{10}(\epsilon)}{\log_{10} 2}$$
$$\log_{10}(4) \approx 0.60206$$
$$\log_{10}(10^{-4}) = -4$$
$$\log_{10}(2) \approx 0.30103$$

$$n > \frac{0.60206 - (-4)}{0.30103} = \frac{4.60206}{0.30103} \approx 15.288$$

**Step 3: Round up to Next Integer**
- Since $n$ must be an integer, **$n = 16$ iterations** are required.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why can't Bisection find the root of $f(x) = (x-2)^2 = 0$?
> Explain conceptually why the Bisection method fails to find the root of $f(x) = (x-2)^2 = 0$.

> [!SUCCESS]- Step-by-Step Solution
> 1. The root $\alpha = 2$ is a **double root** ($m=2$).
> 2. For any real $x \neq 2$, $(x-2)^2 > 0$ strictly.
> 3. Therefore, $f(x) \ge 0$ everywhere on the real line.
> 4. It is impossible to find two numbers $a$ and $b$ such that $f(a) \cdot f(b) < 0$ (there is no sign change across the axis).
> 5. Consequently, the initial prerequisite for Bisection cannot be satisfied!

---

## 💻 Python Implementation

```python
def bisection(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs!")
    
    for k in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)
        
        # Check stopping criteria
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            return c, k
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    return (a + b) / 2.0, max_iter
```

---

## 🔗 Related Notes
- [[Roots of Equations]] — Intermediate Value Theorem and bracket definitions.
- [[Regula Falsi Method]] — Uses linear interpolation instead of midpoint halving.
- [[Errors and Convergence]] — Linear convergence rates and error formulas.
