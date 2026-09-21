---
title: "Multi-dimensional Arrays"
date: 2026-09-21
tags:
  - concept
  - dsa
  - arrays
  - memory-layout
aliases:
  - "2D Array"
  - "3D Array"
  - "Row Major Order"
  - "Column Major Order"
status: completed
---

# 🧮 Multi-dimensional Arrays (Grids in a One-Dimensional Memory)

> [!NOTE] 💡 The Big Picture Intuition
> Memory is a **single street of numbered houses** — yet a spreadsheet is a **grid** with rows *and* columns. How does a 2D grid fit into a 1D street? Simple: you decide on a **reading order**. Read row-by-row like lines of text (*row-major*), or column-by-column like exam marks by subject (*column-major*). Once the reading order is fixed, any cell's address becomes a **formula**, not a search.
> That's the entire trick of multi-dimensional arrays: a convention for flattening + arithmetic for un-flattening. See [[Arrays]] for the 1D foundation: $\text{addr}(A[i]) = \text{base} + i \times w$.

---

## 1. The Two Flattening Conventions

```
Logical 3×4 grid:            Row-major (C/C++):         Column-major (Fortran/MATLAB):
[ [ a, b, c, d ],            a b c d e f g h i j k l    a e i b f j c g k d h l
  [ e, f, g, h ],    →       (rows end-to-end)          (columns end-to-end)
  [ i, j, k, l ] ]           memory ↓
                             a|b|c|d|e|f|g|h|i|j|k|l
```

> [!IMPORTANT] 🎯 Language Fact
> **C and C++ are row-major.** Fortran, MATLAB, and Julia are column-major. The convention changes *every* address formula below — and it's why looping over a C++ array row-by-row (inner index last) is cache-friendly.

---

## 2. Address Formulas (The Exam Heart)

For an $R \times C$ array $A$ with element width $w$ bytes, stored at **base** (address of $A[0][0]$):

### Row-Major (C/C++)

$$\text{addr}(A[i][j]) = \text{base} + (i \times C + j) \times w$$

*Reading*: skip $i$ complete rows ($i \times C$ elements), then walk $j$ more.

### Column-Major (Fortran/MATLAB)

$$\text{addr}(A[i][j]) = \text{base} + (j \times R + i) \times w$$

*Reading*: skip $j$ complete columns ($j \times R$ elements), then walk $i$ more.

### General $n$-D (Row-Major, "last index varies fastest")

$$\text{addr}(A[i_1][i_2]\dots[i_n]) = \text{base} + w \times \sum_{k=1}^{n} \Big( i_k \times \prod_{m=k+1}^{n} D_m \Big)$$

where $D_m$ is the size of dimension $m$. For 3D with dimensions $D_1 \times D_2 \times D_3$:

$$\text{addr}(A[i][j][k]) = \text{base} + (i \times D_2 \times D_3 + j \times D_3 + k) \times w$$

> [!WARNING] ⚠️ The #1 Exam Trap
> Multiply by the **number of columns $C$** in row-major (and rows $R$ in column-major) — *not* by $i$ or $j$ alone. If the problem says "array with 10 columns", the row stride is $10 \times w$ bytes. Mixing up $R$ and $C$ is the most common lost mark.

---

## 3. Lower-Bound Variants (When Indexes Start Elsewhere)

If row index runs $l_1 \dots u_1$ and column index $l_2 \dots u_2$ (common in older textbooks), each index contributes its *offset*:

$$\text{addr}(A[i][j]) = \text{base} + w \times \Big( (i - l_1) \times C + (j - l_2) \Big)$$

where $C = u_2 - l_2 + 1$. In C/C++ both lower bounds are $0$, so the offsets vanish — but read the question carefully!

---

## 4. Worked Examples

### Worked Example 1: Row-Major 2D Address

> [!EXAMPLE] Problem
> `int A[10][20]` starts at address **2000** ($w = 4$). Find the address of `A[3][5]` (row-major).

**Step 1: Identify parameters** — $R = 10$ (unused), $C = 20$, $i = 3$, $j = 5$, $w = 4$.

**Step 2: Count preceding elements** — complete rows skipped: $3 \times 20 = 60$; into the row: $5$. Total $= 65$.

**Step 3: Apply the formula**

$$\text{addr}(A[3][5]) = 2000 + 65 \times 4 = 2000 + 260 = \boxed{2260}$$

### Worked Example 2: Same Grid, Column-Major

> [!EXAMPLE] Problem
> Same array, but stored **column-major**. Find the address of `A[3][5]`.

**Step 1: Parameters** — $R = 10$, $j = 5$, $i = 3$.

**Step 2: Count preceding elements** — complete columns skipped: $5 \times 10 = 50$; into the column: $3$. Total $= 53$.

**Step 3: Apply the formula**

$$\text{addr}(A[3][5]) = 2000 + 53 \times 4 = 2000 + 212 = \boxed{2212}$$

*Same element, two addresses — the storage convention changes the arithmetic, never the logic.*

### Worked Example 3: 3D Address

> [!EXAMPLE] Problem
> `int B[4][5][6]` starts at **5000** ($w = 4$). Find the address of `B[2][3][4]` (row-major).

**Step 1: Formula setup** — $D_2 = 5$, $D_3 = 6$:

$$\text{offset} = (i \cdot D_2 D_3 + j \cdot D_3 + k) = (2 \times 30) + (3 \times 6) + 4 = 60 + 18 + 4 = 82$$

**Step 2: Multiply by width**

$$\text{addr}(B[2][3][4]) = 5000 + 82 \times 4 = 5000 + 328 = \boxed{5328}$$

---

## 5. C++ Implementation: Watch the Layout Prove Itself

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int A[3][4] = {
        {100, 101, 102, 103},
        {104, 105, 106, 107},
        {108, 109, 110, 111}
    };

    // 1) Row-major proof: A[1][2] sits exactly 6 ints after A[0][0].
    const int* base = &A[0][0];
    ptrdiff_t flat = &A[1][2] - base;                 // (1*4 + 2) = 6
    cout << "flat offset of A[1][2] = " << flat << " ints\n";

    // 2) The formula predicts it: base + (i*C + j)
    const int* predicted = base + (1 * 4 + 2);
    cout << "formula matches?  " << boolalpha << (predicted == &A[1][2]) << "\n";

    // 3) Traversal order matters for cache: row-wise vs column-wise.
    // Warm the memory first (touch every page) so BOTH loops run hot —
    // otherwise the first loop pays one-time page-fault costs that swamp
    // the cache effect we want to measure.
    const int N = 1024;
    static int big[N][N];               // 4 MB: exceeds L2, fits DRAM easily
    memset(big, 0, sizeof(big));
    long long sw = 0;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) sw += big[i][j];   // warm-up pass
    (void)sw;

    // best-of-5 for each pattern, to shed scheduler noise
    double rowMs = 1e9, colMs = 1e9;
    long long s1 = 0, s2 = 0;
    for (int rep = 0; rep < 5; ++rep) {
        auto a0 = chrono::steady_clock::now();
        long long s = 0;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j) s += big[i][j];   // row-major: cache-friendly
        auto a1 = chrono::steady_clock::now();
        s1 = s;
        rowMs = min(rowMs, chrono::duration<double, milli>(a1 - a0).count());
    }
    for (int rep = 0; rep < 5; ++rep) {
        auto a0 = chrono::steady_clock::now();
        long long s = 0;
        for (int j = 0; j < N; ++j)
            for (int i = 0; i < N; ++i) s += big[i][j];   // column: 1 useful int/line
        auto a1 = chrono::steady_clock::now();
        s2 = s;
        colMs = min(colMs, chrono::duration<double, milli>(a1 - a0).count());
    }
    cout << "row-wise:    " << rowMs << " ms\n";
    cout << "column-wise: " << colMs << " ms\n";
    cout << "sums equal? " << (s1 == s2) << "\n";
    return 0;
}
```

**Sample output** (absolute times vary by machine — the *ratio* is the lesson):

```
flat offset of A[1][2] = 6 ints
formula matches?  true
row-wise:    2.3 ms
column-wise: 3.4 ms
sums equal? true
```

> [!TIP] 🧠 Same Work, Slower in Reality
> Both loops touch the same 4 MB and do identical arithmetic — only the *order* differs. Row-wise walks memory in its natural flattened order (every 64-byte cache line delivers 16 useful ints); column-wise jumps $N \times 4$ bytes each step (one useful int per line). On typical desktop hardware this costs 1.5–8× more time — the gap widens as the array outgrows the cache (try $N = 4096$). Data layout is performance.

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: The Missing Column Count
> A row-major `char` array ($w = 1$) starts at address **1000**, and `A[4][7]` sits at **1047**. How many columns does it have? Predict before computing.

> [!SUCCESS]- Step-by-Step Solution
> 1. Offset of the element $= 1047 - 1000 = 47$ elements.
> 2. Row-major offset formula: $\text{offset} = i \times C + j = 4C + 7$.
> 3. Solve: $4C + 7 = 47 \Rightarrow 4C = 40 \Rightarrow C = 10$.
> 4. **10 columns** — run the formula backwards, the same equation answers "guess-the-dimension" questions too.

---

## 7. Related Notes
- [[Arrays]] — the 1D address formula and dynamic-array behaviour.
- [[Sparse Matrices]] — grids whose non-zeros are too few to store densely.
- [[Introduction to Data Structures]] — where arrays sit in the classification.
- [[Asymptotic Analysis]] — why traversal order changes constants but not $O(n^2)$.
