---
title: "Sparse Matrices"
date: 2026-09-21
tags:
  - concept
  - dsa
  - arrays
  - matrices
  - memory-optimization
aliases:
  - "Sparse Matrix Representation"
  - "Triplet Representation"
  - "Sparse Matrix Addition"
status: completed
---

# 🕸️ Sparse Matrices (Storing Only What Exists)

> [!NOTE] 💡 The Big Picture Intuition
> Picture a **stadium seating chart of 100,000 seats** where only 400 are sold. Would you really keep a full grid with 99,600 repeated "empty" cells? No — you'd keep a **list of the 400 sold seats**: *seat (row 12, col 30) → Mr. Sharma*.
> A **sparse matrix** is that grid: mostly zeros, few non-zeros. Storing it densely wastes memory *and* time (multiplying by 0 is wasted work). The fix: store **only the non-zero elements**, each tagged with its position. The trade-off: positions must now be *stored* alongside values, so sparsity must be worth that overhead — typically worthwhile when non-zeros are under ~⅓ of all entries.

> [!IMPORTANT] 🎯 Exam Definition
> A matrix of size $m \times n$ with $t$ non-zero elements is **sparse** when $t \ll m \times n$. It is stored using a **triplet (3-tuple) representation**: each non-zero element becomes a row $(row,\ col,\ value)$, preceded by a header triplet $(m,\ n,\ t)$ giving dimensions and the non-zero count.

---

## 1. From Grid to Triplets

$$A = \begin{bmatrix} 0 & 0 & 3 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 5 & 0 & 0 & 0 & 8 \\ 0 & 0 & 0 & 2 & 0 \end{bmatrix} \quad (m{=}4,\ n{=}5,\ t{=}4)$$

Dense storage: $4 \times 5 = 20$ cells. Triplet storage: $t + 1 = 5$ rows $\times$ 3 columns:

```
row  col  val
 4    5    4      ← header: dimensions + non-zero count
 0    2    3
 2    0    5
 2    4    8
 3    3    2
```

Memory comparison: dense $= 20 \times w$ bytes; triplet $= 3(t+1) \times w$ bytes. Here $20w$ vs $15w$ — already cheaper, and the gap explodes for realistic sparsity (a $10^4 \times 10^4$ matrix with $10^4$ non-zeros: $10^8 w$ vs $3 \times 10^4 w$ — **over 3000× smaller**).

> [!TIP] 🧠 Sparsity Threshold
> Triplet form wins when $3(t+1) < mn$, i.e. roughly when non-zeros fill **less than $\frac{1}{3}$** of the grid. That's why the exam definition says $t \ll mn$ — the overhead of storing $(row, col)$ must be repaid by the zeros you skip.

---

## 2. Core Operations on the Triplet Form

| Operation | Method | Cost |
| :-- | :-- | :--: |
| **Transpose** | Swap $(row, col)$ of each triplet, re-sort by row (or fast in-place by column counting) | $O(t \log t)$ naive, $O(nc + t)$ fast |
| **Addition $A + B$** | Merge the two sorted triplet lists like a 2-way merge; equal positions add values (drop if $0$) | $O(t_A + t_B)$ |
| **Multiplication $A \times B$** | For each non-zero $A_{ij}$, fetch non-zeros of row $j$ of $B$ | $O(t_A \times \text{avg nnz/row of } B)$ |
| **Search value / position** | Scan triplets | $O(t)$ |

The constant win: every cost is proportional to $t$ (non-zeros), *never* to $mn$.

---

## 3. Worked Example: Adding Two Sparse Matrices

> [!EXAMPLE] Problem
> Add $A$ (above) and $B$ below, both $4 \times 5$, using triplet form.

$$B = \begin{bmatrix} 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 5 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 2 & 0 \end{bmatrix} \quad (t_B = 3)$$

**Step 1: Merge the two sorted triplet lists** (position order: $(0,2), (2,0), (2,4), (3,3)$ for $A$; $(0,3), (2,0), (3,3)$ for $B$).

| Position | $A$ value | $B$ value | Sum | Keep? |
| :--: | :--: | :--: | :--: | :--: |
| $(0,2)$ | 3 | 0 | 3 | ✅ |
| $(0,3)$ | 0 | 1 | 1 | ✅ (new) |
| $(2,0)$ | 5 | 5 | 10 | ✅ |
| $(2,4)$ | 8 | 0 | 8 | ✅ |
| $(3,3)$ | 2 | 2 | 4 | ✅ |

**Step 2: Write the result triplet** ($t = 5$):

```
row  col  val
 4    5    5
 0    2    3
 0    3    1
 2    0   10
 2    4    8
 3    3    4
```

**Step 3: Verify against the dense sum** — $A+B$ at $(2,0)$ is $5+5=10$ ✓, at $(0,3)$ is $0+1=1$ ✓. Total work: one merge of $7$ triplets, not $4 \times 5 = 20$ cell additions.

---

## 4. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: When Is Sparse Worse?
> A $10 \times 10$ matrix has 40 non-zero entries. A classmate insists on triplet representation "because sparse = efficient". Compute the memory of both schemes and give the correct verdict.

> [!SUCCESS]- Step-by-Step Solution
> 1. Dense: $mn = 100$ elements.
> 2. Triplet: $3(t+1) = 3 \times 41 = 123$ elements — **more** than dense!
> 3. Verdict: with 40% fill, the matrix is *not* sparse enough; the $(row, col)$ overhead per element outweighs the skipped zeros.
> 4. Rule: use triplets only when $3(t+1) < mn$ (here $123 > 100$, so dense wins). Sparsity is a *quantitative* decision, not a label.

---

## 5. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Triplet { int row, col, val; };

// Build the triplet table from a dense matrix
vector<Triplet> toTriplet(const vector<vector<int>>& M) {
    vector<Triplet> T = { { (int)M.size(), (int)M[0].size(), 0 } };  // header
    for (int i = 0; i < (int)M.size(); ++i)
        for (int j = 0; j < (int)M[i].size(); ++j)
            if (M[i][j] != 0) T.push_back({i, j, M[i][j]});
    T[0].val = (int)T.size() - 1;              // header: non-zero count
    return T;
}

// Merge-add two position-sorted triplet tables: O(tA + tB)
vector<Triplet> addSparse(const vector<Triplet>& A, const vector<Triplet>& B) {
    vector<Triplet> C = { { A[0].row, A[0].col, 0 } };
    size_t p = 1, q = 1;
    while (p < A.size() && q < B.size()) {
        if (A[p].row == B[q].row && A[p].col == B[q].col) {
            int s = A[p].val + B[q].val;
            if (s != 0) C.push_back({A[p].row, A[p].col, s});
            ++p; ++q;
        } else if (A[p].row < B[q].row ||
                  (A[p].row == B[q].row && A[p].col < B[q].col)) {
            C.push_back(A[p++]);
        } else {
            C.push_back(B[q++]);
        }
    }
    while (p < A.size()) C.push_back(A[p++]);
    while (q < B.size()) C.push_back(B[q++]);
    C[0].val = (int)C.size() - 1;
    return C;
}

int main() {
    vector<vector<int>> A = {{0,0,3,0,0}, {0,0,0,0,0}, {5,0,0,0,8}, {0,0,0,2,0}};
    vector<vector<int>> B = {{0,0,0,1,0}, {0,0,0,0,0}, {5,0,0,0,0}, {0,0,0,2,0}};

    vector<Triplet> TA = toTriplet(A), TB = toTriplet(B), TC = addSparse(TA, TB);

    cout << "A triplets: " << TA[0].val << "  B triplets: " << TB[0].val << "\n";
    cout << "sum header: " << TC[0].row << "x" << TC[0].col
         << " nnz=" << TC[0].val << "\n";
    for (int k = 1; k < (int)TC.size(); ++k)
        cout << "(" << TC[k].row << "," << TC[k].col << ") -> " << TC[k].val << "\n";
    return 0;
}
```

**Output:**

```
A triplets: 4  B triplets: 3
sum header: 4x5 nnz=5
(0,2) -> 3
(0,3) -> 1
(2,0) -> 10
(2,4) -> 8
(3,3) -> 4
```

Exactly the table computed by hand in Section 3. ✅

---

## 6. Related Notes
- [[Arrays]] — the dense layout whose waste sparse representation avoids.
- [[Multi-dimensional Arrays]] — the row/column addressing that triplets replace with explicit tags.
- [[Linked List]] — the alternative storage: non-zeros chained as nodes.
- [[Introduction to Data Structures]] — representation choice as a memory/time decision.
