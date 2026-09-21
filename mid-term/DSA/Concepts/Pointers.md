---
title: "Pointers"
date: 2026-09-21
tags:
  - concept
  - dsa
  - foundations
  - memory
aliases:
  - "Pointer Basics"
  - "Pointers in C/C++"
  - "Dynamic Memory"
status: completed
---

# 🎯 Pointers (Addresses as First-Class Data)

> [!NOTE] 💡 The Big Picture Intuition
> A normal variable is a **house**: it holds a value (a family). A **pointer** is a **scrap of paper with the house's address written on it**. The paper isn't the house — but hand someone the paper and they can walk there and *change what's inside*. Copying a huge house is expensive; copying a slip of paper costs nothing. That's why passing a pointer is cheap, and why "call by reference" works.
> Now the DSA payoff: houses in a street are fixed forever, but you can *build a new house anywhere in the city* and keep its address on paper. Chained slips of paper — each one pointing to the next house — are literally a **[[Linked List]]**. Every dynamic structure in DSA is built from this one trick.

> [!IMPORTANT] 🎯 Exam Definition
> A **pointer** is a variable that stores the **memory address** of another variable rather than a data value itself. For any type $T$, the type $T^*$ ("pointer to $T$") can hold the address of a $T$ object. Key operators: `&x` (*address-of*, gives $x$'s address), `*p` (*dereference/indirection*, accesses what $p$ points at), and `nullptr` (points at nothing, the safe "empty address").

---

## 1. The Four Operations You Must Know Cold

```cpp
int x = 10;        // a house with the value 10
int* p = &x;       // paper with x's address    (& = address-of)
*p = 20;           // walk to the house, change it — x is now 20  (* = dereference)
p = nullptr;       // the paper points at nothing
```

| Symbol | Name | Reads as | Example meaning |
| :-- | :-- | :-- | :-- |
| `&x` | address-of | "the address of $x$" | where the house is |
| `*p` | dereference | "the thing $p$ points at" | enter the house |
| `T* p` | declaration | "$p$ is a pointer to $T$" | the paper can only note $T$-houses |
| `p->f` | arrow | dereference + member | visit the house, open drawer `f` |
| `nullptr` | null pointer | "points nowhere" | blank paper |

> [!WARNING] ⚠️ The Two Classic Bugs
> **Dangling pointer**: `p` still holds an address after `delete p` — walking to a *demolished* house. Set `p = nullptr;` right after `delete`. **Null dereference**: `*p` when `p == nullptr` — entering a plot with no house; always test `if (p)` first. Both crash at runtime and both are exam favourites.

---

## 2. Pointer Arithmetic: The Array Connection

For `T* p`, the expression `p + k` advances the address by **$k \times \text{sizeof}(T)$ bytes**, not $k$ bytes:

$$\text{addr}(p + k) = \text{addr}(p) + k \times w, \qquad w = \text{sizeof}(T)$$

This is *exactly* the array address formula $\text{addr}(A[i]) = \text{base} + i \times w$ from [[Arrays]] — and it is no coincidence: **in C/C++, an array name decays to a pointer to its first element**, so `A[i]` is literally defined as `*(A + i)`.

```
int A[4] = {10, 20, 30, 40};     base = 2000, w = 4

p = A        → 2000      *p     → 10
p + 1        → 2004      *(p+1) → 20    (A[1])
p + 3        → 2012      *(p+3) → 40    (A[3])
```

> [!TIP] 🧠 Pointer ≈ Index
> `A[i]`, `*(A + i)`, and `*(p + i)` with `p = A` are the *same memory access*. Seeing an index as "address arithmetic" is the mental leap that makes linked structures, [[Multi-dimensional Arrays]], and buffer walks all click at once.

---

## 3. Dynamic Memory: `new` and `delete`

Static variables live on the **stack**: fixed size, freed automatically, gone at scope exit. **Heap** memory is requested at runtime — this is what makes structures that grow and shrink possible:

```cpp
int* p  = new int(5);      // one int on the heap
Node* n = new Node(v);     // a node born at runtime — the heart of linked structures

delete p;                  // return the memory (p now dangling!)
p = nullptr;               // cure the dangling pointer

int* arr = new int[n];     // runtime-sized array
delete[] arr;              // note the [] for arrays
```

| | Stack (static) | Heap (dynamic) |
| :-- | :-- | :-- |
| Size | Fixed at compile time | Requested at runtime |
| Lifetime | Scope-bound (auto-freed) | Until `delete` |
| Speed | Very fast | Slower allocation |
| Enables | Fixed buffers | Linked lists, growing stacks, trees |

Every `new` must be matched by exactly one `delete` — a missing one is a **memory leak**, a repeated one is **double-free corruption**.

---

## 4. Worked Example: Tracing Pointers by Hand

> [!EXAMPLE] Problem
> Trace the following fragment. What are the final values of $a$, $b$, and `*q`?

```cpp
int a = 5, b = 7;
int* p = &a;
int* q = &b;
*p = *q + 2;     // ?
q = p;
*q = 30;         // ?
```

**Step 1**: `p → a` (holds $a$'s address), `q → b`.

**Step 2**: `*p = *q + 2` → walk through $p$, write $7 + 2 = 9$ into $a$. Now $a = 9$.

**Step 3**: `q = p` → $q$ now carries the *same address as $p$*; both papers point at $a$. Note $b$ was never touched after Step 2.

**Step 4**: `*q = 30` → writes into $a$ (the shared target). 

**Final: $a = 30$, $b = 7$, `*q = 30`** — the classic insight: *assignment of pointers copies addresses, not values*; one dereference later, two pointers can touch one variable.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Swap Without References
> `void badSwap(int x, int y) { int t = x; x = y; y = t; }` fails to swap the caller's variables. Explain why, and write the pointer version that works.

> [!SUCCESS]- Step-by-Step Solution
> 1. `badSwap` receives **copies** of the values — rearranging the copies leaves the caller's originals untouched (pass-by-value).
> 2. Pointer version: `void swap(int* x, int* y) { int t = *x; *x = *y; *y = t; }` — parameters are *addresses*; `*x` and `*y` reach back into the caller's own variables.
> 3. Call: `swap(&a, &b);` — send the addresses, not the values.
> 4. Principle: to *modify* the caller's data, the function needs the data's location (address), not a photocopy of it.

---

## 6. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {          // the payoff: a node is pointers all the way down
    int data;
    Node* next;
    Node(int d, Node* n = nullptr) : data(d), next(n) {}
};

int main() {
    // 1) Basics: & and *
    int a = 5;
    int* p = &a;
    *p = 42;
    cout << "a=" << a << " via *p=" << *p << "\n";     // a=42

    // 2) Pointer arithmetic == array indexing
    int A[4] = {10, 20, 30, 40};
    int* q = A;                                        // decays to &A[0]
    cout << "*(q+2)=" << *(q + 2) << "  A[2]=" << A[2] << "\n";   // 30 30

    // 3) Dynamic memory: build a 3-node linked chain
    Node* head = new Node(10, new Node(20, new Node(30)));
    int sum = 0;
    for (Node* cur = head; cur; cur = cur->next) sum += cur->data;
    cout << "chain sum=" << sum << "\n";               // 60

    // 4) Clean up: delete exactly once, then null the pointer
    Node* cur = head;
    while (cur) { Node* nxt = cur->next; delete cur; cur = nxt; }
    head = nullptr;
    cout << "freed all nodes, head==" << (head == nullptr ? "nullptr" : "dangling!") << "\n";
    return 0;
}
```

**Output:**

```
a=42 via *p=42
*(q+2)=30  A[2]=30
chain sum=60
freed all nodes, head==nullptr
```

---

## 7. Related Notes
- [[Structure]] — pointers + structures = `->`; the node definition above is both ideas fused.
- [[Linked List]] — chains of pointers; the 3-pointer reversal is pure pointer manipulation.
- [[Arrays]] — pointer arithmetic is the array address formula wearing a different hat.
- [[Stack]] — a linked implementation is `new Node` on `push`, `delete` on `pop`.
