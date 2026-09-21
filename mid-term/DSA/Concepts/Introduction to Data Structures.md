---
title: "Introduction to Data Structures"
date: 2026-09-21
tags:
  - concept
  - dsa
  - foundations
  - data-structures
aliases:
  - "Data Structures Basics"
  - "DS Introduction"
  - "Classification of Data Structures"
status: completed
---

# 🏛️ Introduction to Data Structures (Organizing Information for Speed)

> [!NOTE] 💡 The Big Picture Intuition
> Imagine a **library with no organizing system**: ten thousand books dumped in one pile. Finding any book means digging through the pile. Now add *structure* — shelves by genre, alphabetically ordered — and the same search takes seconds. The books never changed; the **organization** did.
> A data structure is exactly that: a deliberate way of **organizing data in memory** so that specific operations (search, insert, delete, update) become fast or cheap. There is no "best" data structure — only a *best fit* for the operations your program performs most.

---

## 1. What Is a Data Structure?

> [!IMPORTANT] 🎯 Exam Definition
> A **data structure** is a way of organizing, storing, and relating data in memory so that it can be accessed and modified **efficiently**. Formally it is a triplet: **(D, A, F)** — a set of data objects **D**, the allowed **relationships (A)** among them, and the **operations (F)** permitted on them.

A useful slogan to remember (from Niklaus Wirth, author of Pascal):

$$\text{Program} = \text{Algorithms} + \text{Data Structures}$$

- The **algorithm** is the recipe (what steps to take).
- The **data structure** is the kitchen layout (where the ingredients are, how fast you can grab them).
- Change the layout, and the same recipe takes a totally different time.

---

## 2. Primitive vs Non-Primitive Data

| Kind | Meaning | Examples |
| :-- | :-- | :-- |
| **Primitive** | Directly operated on by machine instructions | `int`, `float`, `char`, `double`, `bool` |
| **Non-primitive** | Built by *combining* primitives into organized collections | Array, Linked List, Stack, Queue, Tree, Graph |

All non-primitive structures are ultimately built from primitives glued together by **arrays** (contiguous) or **pointers** (scattered) — see [[Pointers]] and [[Structure]] for the two glue mechanisms in C/C++.

---

## 3. Classification of Data Structures

```
                      Data Structures
                     /               \
             Linear                    Non-Linear
        (one predecessor,          (element can connect
         one successor)             to many others)
       /     |        \              /        \
   Array   Linked    Stack,       Tree       Graph
           List      Queue
```

| Axis | Option A | Option B |
| :-- | :-- | :-- |
| **Arrangement** | **Linear** — elements in a sequence: array, linked list, stack, queue | **Non-linear** — hierarchy or network: tree, graph |
| **Memory** | **Static** — size fixed at compile time (C array) | **Dynamic** — grows/shrinks at runtime (linked list, `vector`) |
| **Homogeneity** | **Homogeneous** — all elements same type (array) | **Non-homogeneous** — mixed types (structure) |

> [!TIP] 🧠 Memory Hook
> **Linear = a queue of people** (each person has exactly one neighbour behind and one ahead). **Non-linear = a family tree** (a parent has several children; a child has siblings). Every structure in this vault is either a queue of people or a family tree in disguise.

---

## 4. Abstract Data Types (ADT): Interface vs Implementation

An **ADT** is a *mathematical contract*: it lists **what** operations exist and what they do — while hiding **how** they are implemented.

- **Stack ADT**: `push`, `pop`, `peek`, `isEmpty` — obeying LIFO (see [[Stack]]).
- The ADT says nothing about whether the stack is stored in an array or a linked list.

| Layer | Question it answers | Example (Stack) |
| :-- | :-- | :-- |
| **ADT (interface)** | *What* can I do? | `push(x)`, `pop()` — all $O(1)$ |
| **Implementation** | *How* is it stored? | Array with `top` index, or linked list with head |

This separation is why the same ADT can have multiple competing implementations — and why [[Asymptotic Analysis]] is the tool that referees between them.

---

## 5. The Core Operations Every Structure Offers

| Operation | Meaning | Array cost | Linked List cost |
| :-- | :-- | :--: | :--: |
| **Traversal** | Visit every element once | $O(n)$ | $O(n)$ |
| **Search** | Locate an element by value | $O(n)$ | $O(n)$ |
| **Insertion** | Add a new element | $O(n)$ middle | $O(1)$ at known node |
| **Deletion** | Remove an element | $O(n)$ middle | $O(1)$ at known node |
| **Access by index** | Read the $i$-th element | $O(1)$ ✅ | $O(n)$ ❌ |
| **Sorting / Merging** | Reorder / combine | varies | varies |

**The whole game of DSA**: pick the structure whose *cheap* operations are the ones your program performs *most often*.

---

## 6. Worked Example: Choosing the Right Structure

> [!EXAMPLE] Problem
> A text editor must (1) undo the last $k$ actions, (2) jump instantly to character position $i$ of a 1-million-character document. Which structures fit?

**Step 1: List the hot operations.** Undo → "most recent action first". Jump-to-$i$ → random access.

**Step 2: Match operations to structures.**
- "Most recent first" is **LIFO** → a **stack** of actions gives $O(1)$ undo.
- "Instant access to position $i$" is $O(1)$ addressing → an **array** (contiguous memory, $\text{base} + i \times w$).

**Step 3: Check the trade-off.** A stack *could* be array-based — and here both hot operations want contiguity, so **one array-backed design can serve both** (the editor's buffer *is* an array; the undo history *is* a stack of edit records).

**Decision: array-backed stack + array buffer.** ✅

---

## 7. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: The Misfit Structure
> A program spends 95% of its time inserting items **at the front** of a 100,000-element container and almost never searches it. The team uses an array. Diagnose the performance bug and prescribe the fix, with complexities.

> [!SUCCESS]- Step-by-Step Solution
> 1. Array front-insertion shifts all $n$ existing elements → $O(n)$ per insert, × 95% of runtime = the bottleneck.
> 2. A **linked list** inserts at the head by rewiring two pointers → $O(1)$, no shifting.
> 3. The rare searches degrade from $O(1)$ (array index) to $O(n)$ (list walk) — acceptable, because searches are only 5% of the workload.
> 4. Principle: **optimize for the dominant operation**, not for the one that looks scary.

---

## 8. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

// One traversal that simultaneously performs three core operations:
// traversal + search (max) + update-by-index — all on a static array.
int main() {
    int scores[6] = {72, 91, 85, 64, 99, 88};   // static, homogeneous, linear

    int sum = 0, maxVal = scores[0], maxIdx = 0;
    for (int i = 0; i < 6; ++i) {               // traversal: O(n)
        sum += scores[i];                       // aggregation
        if (scores[i] > maxVal) {               // search for maximum
            maxVal = scores[i];
            maxIdx = i;
        }
    }
    scores[maxIdx] += 5;                        // update by index: O(1)

    cout << "sum=" << sum << " max=" << maxVal
         << " at index " << maxIdx << "\n";
    cout << "after bonus, top score=" << scores[maxIdx] << "\n";
    return 0;
}
```

**Output:**

```
sum=499 max=99 at index 4
after bonus, top score=104
```

---

## 9. Related Notes
- [[Asymptotic Analysis]] — the measuring stick for every "cost" quoted above.
- [[Algorithm Evaluation]] — how algorithms (the other half of Wirth's equation) are judged.
- [[Arrays]] — the first and most fundamental linear structure.
- [[Pointers]] — the second building block every dynamic structure stands on.
