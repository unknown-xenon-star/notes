---
title: "Algorithm Evaluation"
date: 2026-09-21
tags:
  - concept
  - dsa
  - foundations
  - algorithm-analysis
aliases:
  - "Evaluating Algorithms"
  - "Algorithm Analysis Criteria"
  - "Performance Measurement"
status: completed
---

# ⚖️ Algorithm Evaluation (Judging Recipes Before You Cook)

> [!NOTE] 💡 The Big Picture Intuition
> Two chefs can both "make pasta". One uses a 10-step recipe, the other 40 steps — yet the 40-step one might finish *first* because it boils water while chopping, and wastes nothing. Which recipe is *better*? The honest answer is: **better at what?** Fewer steps? Less gas? Easier for a beginner to follow?
> Algorithm evaluation is the discipline of answering that question with **criteria instead of opinions** — and the two big criteria are *time* (how many basic steps) and *space* (how much memory), measured in a way that doesn't depend on which machine runs the code.

---

## 1. What Is an Algorithm? (Definition First)

> [!IMPORTANT] 🎯 Exam Definition
> An **algorithm** is a finite, well-defined sequence of unambiguous instructions that transforms a valid **input** into the correct **output** in a finite amount of time.

Five essential properties (a classic exam list):

| Property | Meaning | What fails without it |
| :-- | :-- | :-- |
| **Input** | Zero or more externally supplied quantities | Nothing to work on |
| **Output** | At least one quantity produced | Pointless computation |
| **Definiteness** | Every step is precise and unambiguous | Two machines "interpret" differently |
| **Finiteness** | Terminates after a finite number of steps | Infinite loop |
| **Effectiveness** | Each step is basic enough to be carried out exactly | Step like "solve this equation" is not executable |

Note the contrast with a **program**: a program is an algorithm expressed in a programming language — but a program may loop forever, while an *algorithm* by definition must terminate.

---

## 2. The Evaluation Criteria

### 2.1 Primary (Performance) Criteria

| Criterion | Question | Measured by |
| :-- | :-- | :-- |
| **Time complexity** | How does the step count grow with input size $n$? | $O$, $\Omega$, $\Theta$ (see [[Asymptotic Analysis]]) |
| **Space complexity** | How does auxiliary memory grow with $n$? | Extra variables, buffers, recursion depth |

### 2.2 Secondary Criteria

- **Correctness** — does it produce the right output for *every* valid input, including edge cases (empty, single element, duplicates)?
- **Simplicity / readability** — a simple algorithm is easier to verify, debug, and maintain.
- **Optimality** — is it the *best possible* for the problem? (e.g. comparison-based sorting cannot beat $\Omega(n \log n)$, so merge sort is asymptotically optimal.)
- **Robustness** — graceful behaviour on unexpected input.

> [!TIP] 🧠 The Trade-off Triangle
> **Time ↔ Space ↔ Simplicity** usually fight each other. Counting sort is blazing $O(n)$ but devours memory; bubble sort is trivially simple but $O(n^2)$. Evaluation means deciding *which axis your application can afford to lose on*.

---

## 3. Apriori vs Apostiori Analysis

This is the classic two-mark exam question:

| | **Apriori ("before the fact")** | **Apostiori ("after the fact")** |
| :-- | :-- | :-- |
| **When** | At design time, before running | After running, by profiling |
| **Method** | Count operations as a function of $n$; asymptotic bounds | Stopwatch, profiler, hardware counters |
| **Depends on** | Algorithm logic only — machine/compiler/language independent | Hardware, compiler, load, even room temperature |
| **Result** | $O(n^2)$, $O(n \log n)$, … | "1.37 s on this laptop today" |
| **Used for** | Comparing algorithms fairly | Tuning a chosen implementation |

**Why asymptotic wins for comparison**: a stopwatch on machine A vs machine B is meaningless — but "$O(n \log n)$ beats $O(n^2)$ for large $n$" is a *mathematical truth* valid on every machine.

---

## 4. Algorithm Design Techniques (The Toolbox)

Most algorithms descend from a handful of master strategies:

| Technique | Idea | Flagship examples |
| :-- | :-- | :-- |
| **Brute force** | Try everything directly | Linear search, bubble sort |
| **Divide & conquer** | Split, solve halves, combine | Merge sort, binary search |
| **Greedy** | Take the locally best choice | Dijkstra, Huffman coding |
| **Dynamic programming** | Cache overlapping subproblems | Fibonacci, 0/1 knapsack |
| **Backtracking** | Explore, abandon dead ends | N-queens, maze solving |

---

## 5. Worked Example: Evaluating Three Searches

> [!EXAMPLE] Problem
> Evaluate linear search, binary search, and hash lookup for a 1,000,000-element sorted table with 10⁶ lookups. Which do you choose?

**Step 1: Establish complexities** (apriori). Linear: $O(n)$. Binary: $O(\log n)$. Hash: $O(1)$ average.

**Step 2: Count actual comparisons for one lookup** ($n = 10^6$):
- Linear: $n = 1{,}000{,}000$
- Binary: $\lceil \log_2 10^6 \rceil = 20$
- Hash: $1$ (average)

**Step 3: Scale to the workload** (10⁶ lookups):

$$\text{Linear: } 10^6 \times 10^6 = 10^{12} \quad \text{Binary: } 10^6 \times 20 = 2 \times 10^{7} \quad \text{Hash: } \approx 10^{6}$$

**Step 4: Apply the ≈10⁹ ops/second rule of thumb**: linear ≈ **1000 s**, binary ≈ **0.02 s**, hash ≈ **0.001 s**.

**Step 5: Weigh secondary criteria.** The table is already sorted, data is numeric and dense → binary search needs no extra memory and no hash function design.

**Decision: binary search** — 50,000× faster than linear, zero memory overhead, trivially correct. Hash only wins if constant-factor speed matters more than memory/simplicity. ✅

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Apriori or Apostiori?
> "Implementation A took 2.1 s and implementation B took 1.8 s on the lab PC, therefore B's algorithm is better." State *two* flaws in this reasoning and name the correct evaluation method.

> [!SUCCESS]- Step-by-Step Solution
> 1. **Flaw 1 — apostiori results are machine-relative**: 0.3 s difference may vanish (or invert) on different hardware, compilers, or background load.
> 2. **Flaw 2 — no input-size context**: for the tested $n$ a constant factor dominates; growth *shape* (asymptotics) decides behaviour as $n$ grows.
> 3. **Correct method**: *apriori asymptotic analysis* — count basic operations as $f(n)$ and compare growth rates ($O$-notation), independent of machine.
> 4. Profiling (apostiori) is still useful — but only to *tune the chosen algorithm*, never to *choose between algorithms*.

---

## 7. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;
using Clock = chrono::steady_clock;

// Same task, two algorithms: evaluation in action.
long long sumFormula(long long n)   { return n * (n + 1) / 2; }        // O(1)

long long sumLoop(long long n) {                                       // O(n)
    long long s = 0;
    for (long long i = 1; i <= n; ++i) s += i;
    return s;
}

template <typename F>
double timed(F f, long long n) {
    auto t0 = Clock::now();
    volatile long long r = f(n);        // volatile: prevent optimizing away
    (void)r;
    return chrono::duration<double, micro>(Clock::now() - t0).count();
}

int main() {
    long long n = 10000000;
    cout << "formula: " << timed(sumFormula, n) << " us   (O(1))\n";
    cout << "loop   : " << timed(sumLoop,   n) << " us   (O(n))\n";
    cout << "both return " << sumFormula(n) << " == " << sumLoop(n) << "\n";
    return 0;
}
```

**Sample output** (yours will vary — that's exactly the apostiori caveat!):

```
formula: 0.15 us   (O(1))
loop   : 26248.5 us   (O(n))
both return 50000005000000 == 50000005000000
```

The *apriori* verdict ($O(1)$ vs $O(n)$) predicts the winner on every machine; the *apostiori* numbers only confirm it locally.

The *apriori* verdict ($O(1)$ vs $O(n)$) predicts the winner on every machine; the *apostiori* numbers only confirm it locally.

---

## 8. Related Notes
- [[Asymptotic Analysis]] — the notation toolkit ($O/\Omega/\Theta$) this evaluation rests on.
- [[Introduction to Data Structures]] — the other half of Wirth's equation.
- [[Arrays]] — first structure to evaluate these criteria on.
- [[Stack]] — a case study: same ADT, two implementations, one evaluation.
