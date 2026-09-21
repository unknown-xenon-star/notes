---
title: "Stack"
date: 2026-09-21
tags:
  - concept
  - dsa
  - stack
  - linear-data-structures
aliases:
  - "LIFO"
  - "LIFO Structure"
  - "Stack Data Structure"
status: completed
---

# 🥞 Stack (Last In, First Out)

> [!NOTE] 💡 The Big Picture Intuition
> Think of a **stack of cafeteria plates**. You put a clean plate **on top** (push), and you always take the plate **from the top** (pop). The plate that went in **last** comes out **first** — *LIFO: Last In, First Out*. There is no reaching into the middle; the top is the only door in and out.
> Computer-science name-drops of the same idea: the browser **Back button** (most recent page first), the **Undo** shortcut ($\text{Ctrl+Z}$ un-does your latest action), and the **call stack** that tracks which function called which.

---

## 1. The Four Core Operations (all $O(1)$)

| Operation | What it does | Underflow / Overflow |
| :--- | :--- | :--- |
| `push(x)` | Insert $x$ at the **top** | Overflow if array is full |
| `pop()` | Remove and return the **top** element | **Underflow** if `isEmpty()` |
| `peek()` / `top()` | Read the top **without removing** | Underflow if empty |
| `isEmpty()` | `True` if the stack holds nothing | — |

```
push(10)      push(20)      push(30)      pop() → 30     peek() → 20
+----+        +----+        +----+        +----+         +----+
| 30 | ← top   | 30 |         | 30 |        | 30 |          | 20 | ← top
+----+        +----+        +----+        +----+         +----+
| 20 |        | 20 |         | 20 |        | 20 |          | 10 |
+----+        +----+        +----+        +----+         +----+
| 10 |        | 10 |         | 10 |        | 10 |
+----+        +----+        +----+        +----+
```

> [!IMPORTANT] 🎯 Exam Definition
> A **stack** is a linear data structure following the **LIFO** principle, where insertion (`push`) and deletion (`pop`) are restricted to **one end only**, called the **top**. All three core operations run in $O(1)$ time.

---

## 2. Two Implementations, One Interface

### 2.1 Array-Based Stack
Keep a `top` **index** (start at $-1$ = empty):

```
push:  top += 1; A[top] = x        pop:  x = A[top]; top -= 1; return x
```

- ✅ No per-element pointer overhead; excellent cache locality
- ❌ Fixed capacity → **overflow** possible (or a costly $O(n)$ resize)

### 2.2 Linked-List-Based Stack
The **head of a [[Linked List]] is the top**:

```
push:  new.next = head; head = new      pop:  x = head.data; head = head.next
```

- ✅ Grows forever, never overflows
- ❌ One pointer of memory per node

| Criterion | Array stack | Linked stack |
| :--- | :--- | :--- |
| push / pop / peek | $O(1)$ | $O(1)$ |
| Memory per element | data only | data + `next` pointer |
| Overflow risk | Yes (fixed capacity) | No (until RAM ends) |
| Best for | Known size limits | Unbounded growth |

> [!TIP] 🧠 Where to Push on an Array?
> Always use the **end** of the array as the top. [[Arrays]] make end-operations $O(1)$ and front-operations $O(n)$ — so "top = tail" gets you a free constant-time stack. (The textbook memory trick "insert at head" is the linked-list habit; for arrays it's backwards.)

---

## 3. Applications — Where LIFO Shines

1. **Function calls** — the runtime **call stack**: each call pushes a frame (locals, return address); each `return` pops it. Infinite recursion = *stack overflow*, literally.
2. **Balanced parentheses** — push openers `(`, `[`, `{`; every closer must match the most recent opener (the top). Mismatch or leftover = invalid. $O(n)$.
3. **Expression conversion** — infix → postfix (Reverse Polish) / prefix using an operator stack; operators wait on the stack until their turn to be output.
4. **Postfix evaluation** — push operands; on each operator, pop two, apply, push result.
5. **Undo/Redo & browser history** — each action/page is pushed; "back/undo" pops.
6. **Backtracking** — mazes, N-queens, DFS: push choices as you descend; pop when you hit a dead end.
7. **Tower of Hanoi** — the rods *are* stacks (only the top disc may move).

---

## 4. Worked Examples

### Worked Example 1: Postfix Evaluation
> [!EXAMPLE] Problem
> Evaluate the postfix expression `5 6 2 + * 12 4 / -`.

**Step 1**: Scan left to right. Operand → push. Operator → pop twice, compute, push back.

| Token | Action | Stack (bottom → top) |
| :--: | :--- | :-- |
| 5 | push | `5` |
| 6 | push | `5, 6` |
| 2 | push | `5, 6, 2` |
| `+` | $6 + 2 = 8$, push | `5, 8` |
| `*` | $5 \times 8 = 40$, push | `40` |
| 12 | push | `40, 12` |
| 4 | push | `40, 12, 4` |
| `/` | $12 \div 4 = 3$, push | `40, 3` |
| `-` | $40 - 3 = 37$, push | `37` |

**Answer: $37$** — note the pop order matters for `-` and `/`: the **first pop is the right operand**.

### Worked Example 2: Infix → Postfix Conversion (Shunting-Yard, by hand)
> [!EXAMPLE] Problem
> Convert `A + B * C - D` to postfix.

**Step 1**: Operands `A, B, C, D` go straight to output. Operators wait in the stack, higher-precedence operators leaving first.

| Token | Stack | Output |
| :--: | :--: | :-- |
| A | — | `A` |
| `+` | `+` | `A` |
| B | `+` | `A B` |
| `*` | `+ *` | `A B` (`*` > `+`, push) |
| C | `+ *` | `A B C` |
| `-` | `-` | `A B C * +` (pop `*` then `+`: equal-or-higher precedence) |
| D | `-` | `A B C * + D` |
| end | — | **`A B C * + -`** |

**Postfix: `A B C * + D -`** — which evaluates to $A + B \times C - D$. ✔

### Worked Example 3: Balanced Parentheses Trace
> [!EXAMPLE] Problem
> Is `{ [ ( ) ] }` balanced?

| Token | Action | Stack |
| :--: | :-- | :--: |
| `{` | push | `{` |
| `[` | push | `{ [` |
| `(` | push | `{ [ (` |
| `)` | top `(` matches → pop | `{ [` |
| `]` | top `[` matches → pop | `{` |
| `}` | top `{` matches → pop | *(empty)* |

Ends empty with no mismatches → **Balanced ✅**. Failure modes: closer with wrong top (e.g. `( ]`), or a non-empty stack at the end (unclosed opener).

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: The Pop-Order Trap
> In postfix evaluation, when you meet `-`, you pop two values. Which one is the left operand — and what error would swapping them cause? Predict the wrong answer for `8 3 -` before checking.

> [!SUCCESS]- Step-by-Step Solution
> 1. Pops come off in **reverse** order: the **second** pop is the left operand.
> 2. Correct: `left − right = 8 − 3 = 5`.
> 3. Swapped: `3 − 8 = −5` — the negation bug. For `/` the swapped version computes a reciprocal instead of a quotient.
> 4. General rule: for non-commutative operators (`-`, `/`, `^`), op $= \text{second pop} \;\text{op}\; \text{first pop}$.

---

## 6. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

template <typename T>
class ArrayStack {
    vector<T> items;                    // top = end of the vector
public:
    void push(const T& x) { items.push_back(x); }        // O(1) amortized

    T pop() {                                            // O(1)
        if (items.empty())
            throw underflow_error("Stack underflow: pop from empty stack");
        T top = items.back();
        items.pop_back();
        return top;
    }

    T peek() const {                                     // O(1)
        if (items.empty())
            throw underflow_error("Stack underflow: peek at empty stack");
        return items.back();
    }

    bool isEmpty() const { return items.empty(); }
    int  size()    const { return (int)items.size(); }
};

bool isOperand(const string& t) {
    size_t start = (t[0] == '+' || t[0] == '-') ? 1 : 0;
    return start < t.size() &&
           t.find_first_not_of("0123456789", start) == string::npos;
}

double evaluatePostfix(const string& expr) {   // O(n)
    ArrayStack<double> st;
    istringstream in(expr);
    string token;
    while (in >> token) {
        if (isOperand(token)) {
            st.push(stod(token));             // operand
        } else {                              // operator
            double right = st.pop();          // FIRST pop = right operand!
            double left  = st.pop();
            switch (token[0]) {
                case '+': st.push(left + right); break;
                case '-': st.push(left - right); break;
                case '*': st.push(left * right); break;
                case '/': st.push(left / right); break;
            }
        }
    }
    return st.pop();
}

bool isBalanced(const string& s) {             // O(n) time, O(n) space
    unordered_map<char, char> pairs = {{')', '('}, {']', '['}, {'}', '{'}};
    ArrayStack<char> st;
    for (char ch : s) {
        if (ch == '(' || ch == '[' || ch == '{') {
            st.push(ch);
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (st.isEmpty() || st.pop() != pairs[ch]) return false;
        }
    }
    return st.isEmpty();       // leftover openers => unbalanced
}

// Demos -------------------------------------------------------------
int main() {
    ArrayStack<int> s;
    for (int x : {10, 20, 30}) s.push(x);
    cout << s.pop() << " " << s.peek() << " " << s.size() << "\n";  // 30 20 2

    cout << evaluatePostfix("5 6 2 + * 12 4 / -") << "\n";          // 37

    cout << boolalpha << isBalanced("{[()]}") << " "
         << isBalanced("(]") << "\n";                              // true false
    return 0;
}
```

---

## 7. Related Notes
- [[Infix, Postfix and Prefix Notations]] — the deep dive behind Section 3's conversion and evaluation applications.
- [[Linked List]] — the second stack implementation: head-of-list as top.
- [[Arrays]] — the array-backed stack; top at the cheap (end) side.
- [[Asymptotic Analysis]] — why every stack operation is labelled $O(1)$.
