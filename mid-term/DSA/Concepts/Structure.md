---
title: "Structure"
date: 2026-09-21
tags:
  - concept
  - dsa
  - foundations
  - user-defined-types
aliases:
  - "C Structure"
  - "struct"
  - "Structures in C"
status: completed
---

# 📦 Structure (Grouping Unlike Things Together)

> [!NOTE] 💡 The Big Picture Intuition
> An **array** is an egg carton: twelve identical slots, all the same size. But a *student* is not twelve identical things — it's a **name** (text), a **roll number** (int), and a **CGPA** (float) bundled into one card. A **structure** is that index card: a fixed set of *differently-typed* fields travelling together under one name.
> Arrays organize *many of the same thing*; structures organize *one thing made of many parts*. Combine them — an array of structures — and you can store a whole classroom of index cards, addressable by index like [[Arrays]] but readable field-by-field.

> [!IMPORTANT] 🎯 Exam Definition
> A **structure** is a user-defined, **heterogeneous** data type that groups one or more members of possibly different types under a single name. Declaration reserves no memory; **defining a variable** of that type does. Members are accessed with the **dot operator** (`s.member`), or the **arrow operator** (`p->member`) when working through a pointer.

---

## 1. Declaring, Defining, Accessing

```cpp
struct Student {              // 1) declaration: a blueprint, no memory
    int   roll;
    char  name[20];
    float cgpa;
};

Student s1 = {42, "Aditi", 9.1f};   // 2) definition + init: memory allocated
s1.cgpa += 0.2f;                    // 3) access: dot operator
```

| Concept | Syntax | Memory? |
| :-- | :-- | :-- |
| Declaration | `struct Student { ... };` | ❌ blueprint only |
| Variable definition | `Student s1;` | ✅ all members allocated |
| Member access | `s1.roll` | — |
| Access via pointer | `ptr->roll` (≡ `(*ptr).roll`) | — |
| Nested member | `s1.dob.day` | — |

---

## 2. Size of a Structure: Padding

Each member must sit at an address aligned to its type, so the compiler inserts invisible **padding bytes**:

```cpp
struct Example {
    char  c;    // 1 byte  + 3 pad
    int   i;    // 4 bytes
    char  d;    // 1 byte  + 3 pad (tail)
};              // sizeof = 12, not 6!
```

> [!TIP] 🧠 Ordering Rule
> Order members **largest-first** to minimize padding. `{int, char, char}` packs into 8 bytes; `{char, int, char}` inflates to 12. Same data, 33% less memory — free lunch by reordering.

---

## 3. Structure vs Array — The Complementary Pair

| Criterion | Array | Structure |
| :-- | :-- | :-- |
| Element types | Homogeneous (all same) | Heterogeneous (mixed) |
| Access style | Index `a[i]` | Member name `s.roll` |
| Memory layout | Contiguous, no overhead | Contiguous, possible padding |
| Typical use | Many copies of one thing | One thing with many attributes |
| Arithmetic on base | `a+i` walks elements | Pointer cast + offset (rare) |

And they compose: `Student class[60]` is an array of structures — the classic "records table" of C, and the direct ancestor of the *objects* that [[Linked List]] nodes and [[Stack]] elements wrap.

---

## 4. Worked Example: Offset Arithmetic

> [!EXAMPLE] Problem
> A `struct Student { int roll; char name[20]; float cgpa; };` variable starts at address **3000**. Find the address of `cgpa` (no padding between members; `int` = 4, `float` = 4).

**Step 1: Lay out members in order**
- `roll`: offset $0$ → bytes 3000–3003
- `name`: offset $4$ → bytes 3004–3023 ($20$ chars)
- `cgpa`: offset $24$ → bytes 3024–3027

**Step 2: Formula**

$$\text{addr}(\text{member}) = \text{base} + \text{offset} = 3000 + 24 = \boxed{3024}$$

**Step 3: Sanity check with `sizeof`** — total $= 4 + 20 + 4 = 28$ bytes, so the next `Student` in an array would start at 3028. *(With real alignment, `sizeof` may round up to a multiple of 4 — here 28 already is.)*

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: The Swollen Struct
> `struct S { char a; double b; char c; };` reports `sizeof(S) == 24`, yet the members need only $1 + 8 + 1 = 10$ bytes. Where did 14 bytes go, and how would you shrink the struct to 16?

> [!SUCCESS]- Step-by-Step Solution
> 1. `double` needs 8-byte alignment: 7 padding bytes after `a` (offset 1–7), `b` at offset 8–15.
> 2. `c` at offset 16, then 7 tail bytes so the *next* struct in an array is also aligned → $16 + 7 = 23$, rounded to $24$.
> 3. Reorder largest-first: `struct S { double b; char a; char c; };` → `b` at 0–7, `a` at 8, `c` at 9, tail padding to 16.
> 4. **24 → 16 bytes (33% saving) with zero code changes** — same members, same logic.

---

## 6. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Student {
    int   roll;
    char  name[20];
    float cgpa;
};

int main() {
    Student cls[4] = {                 // array of structures: a "records table"
        {42, "Aditi", 9.1f},
        {17, "Bilal", 8.4f},
        {93, "Chen",  9.4f},
        {58, "Divya", 7.9f},
    };

    // search by member: linear scan for the topper — O(n)
    Student* top = &cls[0];
    for (Student* p = cls; p != cls + 4; ++p)
        if (p->cgpa > top->cgpa) top = p;      // arrow operator

    cout << "Topper: " << top->name << " (roll " << top->roll
         << ", cgpa " << top->cgpa << ")\n";

    // structure padding, measured:
    cout << "sizeof(Student) = " << sizeof(Student)
         << " bytes (4 + 20 + 4 = 28, aligned to "
         << alignof(Student) << ")\n";

    // member offset via offsetof — the worked example, verified
    cout << "offset of cgpa = " << offsetof(Student, cgpa) << "\n";
    return 0;
}
```

**Output:**

```
Topper: Chen (roll 93, cgpa 9.4)
sizeof(Student) = 28 bytes (4 + 20 + 4 = 28, aligned to 4)
offset of cgpa = 24
```

The offset 24 matches the hand calculation in Section 4 exactly. ✅

---

## 7. Related Notes
- [[Pointers]] — `->` is pointer + structure working together; `new`/`delete` complete the picture.
- [[Arrays]] — the homogeneous sibling; together they build *arrays of structures*.
- [[Linked List]] — every node *is* a structure holding data + pointers.
- [[Introduction to Data Structures]] — structures as the primary non-primitive building block.
