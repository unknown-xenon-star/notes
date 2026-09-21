---
title: "Arrays"
date: 2026-09-21
tags:
  - concept
  - dsa
  - arrays
  - linear-data-structures
aliases:
  - "Static Array"
  - "Dynamic Array"
  - "1D Array"
  - "2D Array"
status: completed
---

# 🧺 Arrays (Contiguous Memory Blocks)

> [!NOTE] 💡 The Big Picture Intuition
> Think of an **egg carton**: a fixed row of numbered slots, all the same size, glued side-by-side. Because slot #0 starts at a known position and every egg takes the same space, you can *calculate* where egg #7 lives instantly — you never have to open the carton and count.
> That is the array superpower: **contiguous memory + uniform element size = instant address arithmetic**. The price? The carton is rigid — inserting an egg in the middle means shuffling every egg after it one slot over.

---

## 1. Memory Layout & the Magic Formula

An array occupies **one unbroken block** of memory:

```
Index:        0        1        2        3        4
            +--------+--------+--------+--------+--------+
Elements:   |   42   |   17   |   93   |    5   |   28   |
            +--------+--------+--------+--------+--------+
Address:    2000     2004     2008     2012     2016      (4-byte ints)
```

Because the slots touch, the address of any element is pure arithmetic:

$$\text{addr}(A[i]) = \text{base} + i \times w$$

where **base** = address of $A[0]$ and **$w$** = size of one element in bytes.

> [!IMPORTANT] 🎯 Why Random Access Is $O(1)$
> The CPU computes `base + i × w` in a single step, *regardless of how big the array is*. Finding $A[1{,}000{,}000]$ costs exactly as much as finding $A[0]$. This is the fundamental advantage arrays hold over [[Linked List]]s.

---

## 2. Operations & Complexity Table

| Operation | Complexity | Why |
| :--- | :---: | :--- |
| Access / Update `A[i]` | $O(1)$ | Direct address arithmetic |
| Search (unsorted) | $O(n)$ | Must scan linearly |
| Search (sorted) | $O(\log n)$ | Binary search on the order |
| Insert / Delete **at end** | $O(1)$ | No shifting needed* |
| Insert / Delete at **front or middle** | $O(n)$ | Must shift up to $n$ elements |
| Grow beyond capacity (static) | Rebuild | Copy everything into a bigger block |

\* *Amortized $O(1)$ for dynamic arrays (see Section 4).*

---

## 3. Insertion & Deletion — The Shifting Tax

Arrays keep elements packed, so order must be preserved at all costs:

```
INSERT 15 at index 1:
Before:  [ 10 | 20 | 30 | 40 | __ ]      (one empty slot at the end)
Shift →: [ 10 | __ | 20 | 30 | 40 ]      (40→4, 30→3, 20→2)
Write:   [ 10 | 15 | 20 | 30 | 40 ]      ✅ 3 shifts for n=5

DELETE element at index 1:
Before:  [ 10 | 20 | 30 | 40 ]
Shift ←: [ 10 | 30 | 40 ]                (30→1, 40→2, n -= 1) ✅
```

> [!TIP] 🧠 Cost Rule
> Inserting/deleting at position $i$ costs $O(n - i)$ shifts. Front operations are the most expensive ($O(n)$); end operations are free. If your workload is "insert at front" all day, you want a [[Linked List]] or a [[Stack]] pushed from the other end.

---

## 4. Static vs Dynamic Arrays

| Property | Static Array | Dynamic Array (C++ `vector`, Python `list`) |
| :--- | :--- | :--- |
| Capacity | Fixed at creation | Grows automatically |
| Size stored | Reserved upfront | Doubles when full: 1 → 2 → 4 → 8 → … |
| Append cost | $O(1)$ | $O(1)$ **amortized** (occasional $O(n)$ resize + copy) |
| Memory | Exactly what's reserved | May over-allocate (typically ~1.5–2× the used size) |

**How growth works**: when the array is full, a new block **double the size** is allocated, all elements are copied over ($O(n)$), and the old block is freed. Because doublings become rarer as $n$ grows, the *total* cost of $n$ appends is $O(n)$ — hence **amortized $O(1)$ per append**.

---

## 5. 2D Arrays & Row-Major Order

A 2D array is stored as one flat row of memory, row after row:

$$\text{addr}(A[i][j]) = \text{base} + (i \times C + j) \times w$$

where **$C$** = number of columns. (In *column-major* storage — used by Fortran/MATLAB — the formula becomes $\text{base} + (j \times R + i) \times w$.)

```
Logical view (3×4):        Memory layout (row-major):
[ [ a, b, c, d ],          a b c d | e f g h | i j k l
  [ e, f, g, h ],    →     (rows laid end-to-end)
  [ i, j, k, l ] ]
```

---

## 6. Worked Examples

### Worked Example 1: 1D Address Calculation
> [!EXAMPLE] Problem
> An integer array `A` starts at address **2000**, and each `int` occupies **4 bytes**. Find the address of `A[7]`.

**Step 1: Identify parameters** — base $= 2000$, $w = 4$, $i = 7$.
**Step 2: Apply the formula**

$$\text{addr}(A[7]) = 2000 + 7 \times 4 = 2000 + 28 = \boxed{2028}$$

(Check: `A[0]` = 2000, `A[1]` = 2004, … each step of the index costs exactly one element width.)

### Worked Example 2: 2D Row-Major Address Calculation
> [!EXAMPLE] Problem
> A 2D array `A` with **10 columns** is stored row-major starting at address **1000**. Each element is a 4-byte int. Find the address of `A[3][5]`.

**Step 1: Count the elements that precede it**
- Complete rows before row 3: $3 \times 10 = 30$ elements
- Elements into row 3: $5$ elements
- Total preceding: $30 + 5 = 35$ elements

**Step 2: Apply the row-major formula**

$$\text{addr}(A[3][5]) = 1000 + (3 \times 10 + 5) \times 4 = 1000 + 35 \times 4 = 1000 + 140 = \boxed{1140}$$

### Worked Example 3: Counting the Shifting Tax
> [!EXAMPLE] Problem
> Inserting a value at the **front** of a 5-element array with one free slot — how many element moves occur?

**Step 1**: All 5 existing elements must move one slot right: $40{\to}4,\ 30{\to}3,\ 20{\to}2,\ 10{\to}1$, plus the write.
**Step 2**: That is $\ge n$ operations regardless of position → $\boxed{O(n)}$. At the *end* it would have been exactly 1 write → $O(1)$.

---

## 7. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why can't a linked list do $O(1)$ random access?
> An array finds `A[7]` instantly. Why must a [[Linked List]] walk node-by-node to reach its 8th element, even though both "store 8 things"?

> [!SUCCESS]- Step-by-Step Solution
> 1. Array nodes are **contiguous and uniform**: address of slot 7 = base + 7 × w — one arithmetic expression.
> 2. Linked-list nodes live at **arbitrary, scattered addresses**; the only way to find node #7 is to start at the head and follow the `next` pointers seven times.
> 3. No address arithmetic is possible because there is no mathematical relation between a node's index and its memory address.
> 4. Hence arrays: access $O(1)$, insert $O(n)$; linked lists: access $O(n)$, insert-at-known-node $O(1)$ — a perfect trade-off, not a strict improvement.

---

## 8. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

// 1) Watch a dynamic array double its capacity as it grows
void showDynamicGrowth() {
    vector<int> arr;
    int prevCap = 0;
    for (int i = 0; i < 30; ++i) {
        arr.push_back(i);                        // amortized O(1)
        if ((int)arr.capacity() != prevCap) {    // a resize just happened!
            cout << "len=" << setw(2) << arr.size()
                 << "  allocated=" << arr.capacity() << " ints\n";
            prevCap = arr.capacity();
        }
    }
}

// 2) Manual shifting insert (what vector::insert does under the hood) — O(n)
vector<int> insertAt(vector<int> arr, int index, int value) {
    arr.push_back(0);                            // make room
    for (int i = (int)arr.size() - 1; i > index; --i)
        arr[i] = arr[i - 1];                     // shift right
    arr[index] = value;
    return arr;
}

// 3) In-place two-pointer reverse — O(n) time, O(1) extra space
void reverseInPlace(vector<int>& arr) {
    int left = 0, right = (int)arr.size() - 1;
    while (left < right)
        swap(arr[left++], arr[right--]);
}

int main() {
    showDynamicGrowth();

    vector<int> a = insertAt({10, 20, 30, 40}, 1, 15);
    vector<int> b = {1, 2, 3, 4, 5};
    reverseInPlace(b);

    for (int x : a) cout << x << ' ';            // 10 15 20 30 40
    cout << '\n';
    for (int x : b) cout << x << ' ';            // 5 4 3 2 1
    cout << '\n';
    return 0;
}
```

**Sample output** (GCC/libstdc++ — capacities are implementation-defined, but the doubling pattern 1→2→4→8→16→32 is typical):

```
len= 1  allocated=1 ints
len= 2  allocated=2 ints
len= 3  allocated=4 ints
len= 5  allocated=8 ints
len= 9  allocated=16 ints
len=17  allocated=32 ints
10 15 20 30 40
5 4 3 2 1
```

---

## 9. Related Notes
- [[Multi-dimensional Arrays]] — the 2D/3D sequel: row-major formulas for grids in flat memory.
- [[Sparse Matrices]] — when most 2D cells are zero, store only the non-zeros as triplets.
- [[Structure]] — heterogeneous records: the other way to bundle data besides arrays.
- [[Asymptotic Analysis]] — where the $O(1)$ / $O(n)$ / $O(\log n)$ labels come from.
- [[Linked List]] — the scattered-memory alternative: fast inserts, slow access.
- [[Stack]] — usually built on top of an array; pushes at the cheap (end) side.

