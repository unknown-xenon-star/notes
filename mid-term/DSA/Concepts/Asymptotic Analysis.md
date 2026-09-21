---
title: "Asymptotic Analysis"
date: 2026-09-21
tags:
  - concept
  - dsa
  - complexity-analysis
  - big-o
aliases:
  - "Big O Notation"
  - "Time Complexity Analysis"
  - "Order of Growth"
status: completed
---

# 📈 Asymptotic Analysis (How Fast Does Your Code Grow?)

> [!NOTE] 💡 The Big Picture Intuition
> Imagine **finding a name in a phone book**. You could flip page-by-page (a `for` loop), or open the middle, discard half, and repeat (binary search). Now the key question: what happens when the phone book gets **twice as thick**?
> - Page-by-page search: **twice the work**. Doubling input → doubling time.
> - Halving search: **just ONE extra step**. Doubling input → +1 step.
> Asymptotic analysis is the art of describing this **shape of growth**, not the exact seconds. A stopwatch would lie to you (it depends on the machine, the language, even the weather in the server room). Counting *how work scales with input size $n$* never lies.

---

## 1. Why Not Just Use a Stopwatch?

Measuring runtime in seconds is unreliable because it depends on:

| Factor | Why it lies |
| :-- | :-- |
| CPU speed | Same code, different chip → different time |
| Programming language | Python vs C can differ by $100\times$ |
| Compiler/interpreter | Optimization flags change everything |
| Background load | Other programs steal time slices |
| Input data | Sorted vs random input changes behaviour |

**The fix**: count **basic operations as a function of input size $n$**, and study what happens as $n \to \infty$. This is *asymptotic* analysis — the behaviour "at the far end" of the curve, where constants and hardware noise wash out.

---

## 2. The Three Asymptotic Notations

| Notation | Meaning | Formal Definition | Intuition |
| :---: | :--- | :--- | :--- |
| $O(g(n))$ | **Upper bound** (worst guarantee) | $f(n) \le c \cdot g(n)$ for all $n \ge n_0$ | A **ceiling** on runtime |
| $\Omega(g(n))$ | **Lower bound** (best guarantee) | $f(n) \ge c \cdot g(n)$ for all $n \ge n_0$ | A **floor** under runtime |
| $\Theta(g(n))$ | **Tight bound** (both) | $c_1 g(n) \le f(n) \le c_2 g(n)$ | An exact **corridor** |

> [!IMPORTANT] 🎯 The Rule of Thumb for Exams
> - When asked *"time complexity of X"*, give the **worst-case $O$** unless stated otherwise.
> - $O$ is about *growth shape*, not exact counts: $O(2n) = O(n)$, $O(n^2 + n) = O(n^2)$.
> - $\Theta$ is stronger: binary search is $\Theta(\log n)$ — it is *never* faster than that shape in the worst case.

---

## 3. The Complexity Ladder (Common Classes)

| Class | Name | Classic Example | $n=10$ | $n=100$ | $n=1000$ |
| :---: | :--- | :--- | :---: | :---: | :---: |
| $O(1)$ | Constant | Array index access | 1 | 1 | 1 |
| $O(\log n)$ | Logarithmic | Binary search | ~3 | ~7 | ~10 |
| $O(n)$ | Linear | Linear search | 10 | 100 | 1,000 |
| $O(n \log n)$ | Linearithmic | Merge sort | ~33 | ~664 | ~9,966 |
| $O(n^2)$ | Quadratic | Bubble/Selection sort | 100 | 10,000 | $10^6$ |
| $O(2^n)$ | Exponential | Enumerating subsets | 1,024 | $\approx 1.27 \times 10^{30}$ | astronomical |
| $O(n!)$ | Factorial | All permutations | 3,628,800 | $\approx 9.3 \times 10^{157}$ | meaningless |

> [!TIP] 🧠 Memory Hook
> Each rung of the ladder is "one nesting level worse": constant → loop → nested loop → loop with a built-in log → recursive branching. If $10^{12}$ operations ≈ 1 second, then $O(n^2)$ on $n = 10^5$ takes **~3 hours**, while $O(n \log n)$ takes **~0.2 seconds**.

---

## 4. Rules for Computing Big-O

1. **Drop constants**: $O(500) = O(1)$, $O(2n) = O(n)$, $O(n/2) = O(n)$.
2. **Drop lower-order terms**: $O(n^2 + n + 7) = O(n^2)$ (for huge $n$, the biggest term swallows the rest).
3. **Sequential blocks → ADD**: two independent loops = $O(n) + O(n) = O(n)$.
4. **Nested loops → MULTIPLY**: loop inside loop = $O(n) \times O(n) = O(n^2)$.
5. **Different inputs → different variables**: an algorithm taking two arrays is $O(a + b)$ if sequential, $O(a \cdot b)$ if nested — never just "$O(n)$".

---

## 5. Best, Average, and Worst Case

One algorithm can have three different growth shapes depending on the input:

**Example: Linear Search for target $t$ in an array of size $n$**

| Case | When | Complexity |
| :--- | :--- | :---: |
| **Best** | $t$ is the first element | $\Omega(1)$ |
| **Average** | $t$ is somewhere random (≈ $n/2$ comparisons) | $\Theta(n)$ |
| **Worst** | $t$ is last, or absent | $O(n)$ |

Convention: complexity quoted without qualification = **worst case**.

---

## 6. Worked Examples: Analyzing Loops

### Worked Example 1: Counting Operations Exactly
> [!EXAMPLE] Problem
> Find the time complexity of:
> ```cpp
> long long total = 0;             // 1 operation
> for (int i = 0; i < n; ++i) {    // loop control: n+1 checks
>     total += i;                  // body: n operations
> }
> cout << total << "\n";           // 1 operation
> ```

**Step 1: Count every operation** → $f(n) = 1 + (n+1) + n + 1 = 2n + 3$
**Step 2: Drop constants inside terms** → $2n$ → $n$
**Step 3: Drop the constant term** → $+3$ vanishes

$$\boxed{f(n) = 2n + 3 \implies O(n)}$$

### Worked Example 2: The Doubling Loop → Logarithmic
> [!EXAMPLE] Problem
> Find the complexity of:
> ```cpp
> int i = 1;
> while (i < n) {
>     i *= 2;
> }
> ```

**Step 1**: After $k$ iterations, $i = 2^k$.
**Step 2**: The loop stops when $2^k \ge n$.
**Step 3**: Solve for $k$: $k = \lceil \log_2 n \rceil$.

$$\boxed{O(\log n)} \quad \text{(input size doubles} \Rightarrow \text{just one more iteration)}$$

### Worked Example 3: The Triangle Loop → Quadratic (Gauss Sum)
> [!EXAMPLE] Problem
> Find the complexity of:
> ```cpp
> for (int i = 0; i < n; ++i) {
>     for (int j = 0; j < i; ++j)     // inner runs i times, not n times!
>         cout << i << " " << j << "\n";
> }
> ```

**Step 1**: Total inner iterations $= 0 + 1 + 2 + \dots + (n-1)$.
**Step 2**: Gauss's formula gives $\frac{n(n-1)}{2} = \frac{n^2 - n}{2}$.
**Step 3**: Drop constants and lower-order terms → $\frac{n^2}{2}$ → $n^2$.

$$\boxed{O(n^2)}$$

---

## 7. Space Complexity (Memory as a Function of $n$)

Same asymptotic logic, applied to **auxiliary memory** (extra memory beyond the input):

| Pattern | Extra Space |
| :--- | :---: |
| A few variables (`total`, `i`, `max`) | $O(1)$ |
| Building a copy / result list of size $n$ | $O(n)$ |
| A 2D table of $n \times n$ entries | $O(n^2)$ |
| Recursion with depth $d$ (each call = one stack frame) | $O(d)$ |

> [!WARNING] ⚠️ Recursion Isn't Free
> A recursive function that makes $n$ nested calls consumes $O(n)$ **call-stack memory**, even if it uses no arrays. An "in-place" recursive solution can still blow the memory limit.

---

## 8. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: The Constant-Offender Trap
> Your friend claims an algorithm taking $100n$ steps is *always worse* than one taking $n^2$ steps, "because 100 > 1". For which inputs is your friend accidentally right, and why is the claim still wrong?

> [!SUCCESS]- Step-by-Step Solution
> 1. Compare: $100n$ vs $n^2$ → the crossover happens when $n^2 = 100n$, i.e. $n = 100$.
> 2. For **$n > 100$**, $n^2$ truly is worse — the friend is right on large inputs.
> 3. But asymptotic notation describes behaviour **as $n \to \infty$**, so the constant 100 is dropped: $O(100n) = O(n)$.
> 4. Growth shape wins in the limit: linear always beats quadratic eventually, no matter how big the constant.
> 5. (For tiny inputs like $n = 10$, the "constant-heavy" linear version is indeed faster — which is why real libraries switch to insertion sort for small subarrays.)

---

## 9. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

long long linearSearchOps(long long n) {
    return n;                                             // worst case: O(n)
}

long long binarySearchOps(long long n) {
    return n > 0 ? (long long)ceil(log2((double)n)) : 0;  // worst case: O(log n)
}

int main() {
    cout << setw(15) << "n" << " | "
         << setw(15) << "linear O(n)" << " | "
         << setw(15) << "binary O(log n)" << "\n";
    for (long long n : {10LL, 1000LL, 1000000LL, 1000000000LL}) {
        cout << setw(15) << n << " | "
             << setw(15) << linearSearchOps(n) << " | "
             << setw(15) << binarySearchOps(n) << "\n";
    }
    return 0;
}
```

**Output** — watch binary search barely move while linear search explodes:

```
              n |     linear O(n) | binary O(log n)
             10 |              10 |               4
           1000 |            1000 |              10
        1000000 |         1000000 |              20
     1000000000 |      1000000000 |              30
```

---

## 10. Related Notes
- [[Algorithm Evaluation]] — the bigger judging framework: apriori vs apostiori, correctness, optimality.
- [[Introduction to Data Structures]] — the subject this notation measures end to end.
- [[Arrays]] — the $O(1)$ random access that address arithmetic buys you.
- [[Linked List]] — trades $O(1)$ access for $O(1)$ insertion at the front.
- [[Stack]] — all core operations run in $O(1)$; recursion depth = stack depth.

