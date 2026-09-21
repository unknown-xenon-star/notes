---
title: "Infix, Postfix and Prefix Notations"
date: 2026-09-21
tags:
  - concept
  - dsa
  - stack
  - expressions
aliases:
  - "Polish Notation"
  - "Reverse Polish Notation"
  - "Expression Conversion"
  - "Infix to Postfix"
status: completed
---

# 🔀 Infix, Postfix and Prefix Notations (Three Ways to Write One Expression)

> [!NOTE] 💡 The Big Picture Intuition
> When you write $A + B \times C$, the operators sit **between** their operands — that's *infix*, and it forces you to play a precedence game: parentheses, then $\times\ /\$, then $+\ -$. Computers find that game awkward — they'd rather be told the order **outright**.
> Put the operator **after** its operands ($A\ B\ C\ \times\ +$) and order becomes unambiguous with *zero parentheses* — *postfix* (Reverse Polish). Put it **before** ($+\ A\ \times\ B\ C$) and you get *prefix* (Polish). Both are parenthesis-free, precedence-free, and readable in **one left-to-right pass** with a [[Stack]] — which is exactly why compilers convert your infix code into one of them.
> The stack is the perfect referee: it remembers operators that are *waiting* for their right operand, and its LIFO order naturally respects precedence. See [[Stack]] for the core operations.

> [!IMPORTANT] 🎯 Exam Definitions
> For binary operators between operands $A$ and $B$:
> - **Infix**: $A + B$ — operator between operands; needs precedence + parentheses.
> - **Postfix (Reverse Polish)**: $A\ B\ +$ — operator follows operands; evaluation stack-driven.
> - **Prefix (Polish)**: $+\ A\ B$ — operator precedes operands; evaluation right-to-left or stack-driven.

---

## 1. Precedence and Associativity (The Rules of the Game)

| Operator | Precedence | Associativity |
| :-- | :--: | :--: |
| `^` (power) | 3 (highest) | **Right** to left |
| `*` `/` `%` | 2 | Left to right |
| `+` `-` | 1 (lowest) | Left to right |

Higher precedence = leaves the stack **later** (i.e. is popped first). Associativity breaks ties: for equal precedence in infix→postfix, pop the stack operator first **except** for right-associative `^`.

---

## 2. Infix → Postfix (Shunting-Yard Algorithm)

**Scan left to right. Operands → output immediately. Operators → wait on the stack, leaving when precedence says so.**

1. **Operand** → append to output.
2. **`(`** → push (acts as a "floor" that blocks pops).
3. **`)`** → pop to output until `(` appears; discard both parentheses.
4. **Operator $o$** → while stack top is an operator with **precedence ≥ $o$'s** (for left-assoc $o$; **>** for right-assoc), pop it to output. Then push $o$.
5. **End** → pop everything to output.

### Worked Example 1: `A + B * C - D`

| Token | Stack | Output | Why |
| :--: | :--: | :-- | :-- |
| A | — | `A` | operand straight out |
| + | `+` | `A` | stack empty → push |
| B | `+` | `A B` | operand |
| * | `+ *` | `A B` | `*` > `+` → no pop, push |
| C | `+ *` | `A B C` | operand |
| - | `-` | `A B C * +` | `-` ≤ `*`, `-` ≤ `+` → pop both, push `-` |
| D | `-` | `A B C * + D` | operand |
| end | — | **`A B C * + D -`** | flush stack |

$$A + B \times C - D \;\Rightarrow\; A\,B\,C\,\times\,+\,D\,-$$

### Worked Example 2: Parentheses + Power — `(A + B) ^ C * D`

| Token | Stack | Output | Why |
| :--: | :--: | :-- | :-- |
| ( | `(` | — | push the floor |
| A | `(` | `A` | |
| + | `( +` | `A` | `(` blocks pops |
| B | `( +` | `A B` | |
| ) | — | `A B +` | pop to `(`, discard the pair |
| ^ | `^` | `A B +` | push |
| C | `^` | `A B + C` | |
| * | `*` | `A B + C ^` | `*` < `^` → pop `^`; push `*` |
| D | `*` | `A B + C ^ D` | |
| end | — | **`A B + C ^ D *`** | flush |

---

## 3. Infix → Prefix (Reverse the Trick)

1. **Reverse** the infix string, **swapping `(` ↔ `)`**.
2. Convert that "reversed-infix" to postfix — but for equal precedence, pop only when the stack top is **strictly greater** (this preserves left-associativity after the flip).
3. **Reverse the output** → prefix.

### Worked Example 3: `(A + B) ^ C * D` → Prefix

**Step 1: Reverse & swap** → `D * C ^ ) B + A (` becomes `D * C ^ ( B + A )`.

**Step 2: Shunting-yard on it** → postfix: `D C B A + ^ *`.

**Step 3: Reverse the output** → **`* ^ + A B C D`**

$$((A+B)^{C}) \times D \;\Rightarrow\; *\; \hat{}\; +\,A\,B\;C\;D$$

---

## 4. Evaluating Postfix — One Pass, One Stack

> [!EXAMPLE] Problem
> Evaluate `5 6 2 + * 12 4 / -`.

| Token | Action | Stack (bottom → top) |
| :--: | :-- | :-- |
| 5 | push | `5` |
| 6 | push | `5, 6` |
| 2 | push | `5, 6, 2` |
| `+` | $6+2=8$ | `5, 8` |
| `*` | $5\times8=40$ | `40` |
| 12 | push | `40, 12` |
| 4 | push | `40, 12, 4` |
| `/` | $12\div4=3$ | `40, 3` |
| `-` | $40-3=37$ | `37` |

**Answer: $37$** — and the golden pop-order rule: for non-commutative operators, $\text{result} = (\text{second pop})\ op\ (\text{first pop})$. Swap it and $8-3$ becomes $3-8=-5$.

**Prefix evaluation** mirrors this: scan **right to left**, push operands; on an operator pop two and compute (first pop = left operand). Evaluating `* ^ + A B C D` with $A{=}1,B{=}2,C{=}3,D{=}4$: $+AB=3$, $3^3=27$, $27\times4=108$.

---

## 5. Why Bother? (The Compiler's Motive)

| Property | Infix | Postfix / Prefix |
| :-- | :--: | :--: |
| Parentheses needed | ✅ yes | ❌ never |
| Precedence rules needed | ✅ yes | ❌ baked in |
| Evaluation passes | multiple (or recursion) | **one left-to-right** |
| Machine-friendly | ❌ | ✅ |
| Human-friendly | ✅ | ❌ |

Compilers parse your infix source once, convert to postfix/prefix (or an expression tree), and generate code — evaluation order is then fixed forever, no precedence table consulted at runtime.

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Convert Under Pressure
> Convert `A * (B + C) / D - E` to postfix and to prefix. Then evaluate the postfix with $A{=}8, B{=}2, C{=}3, D{=}5, E{=}1$.

> [!SUCCESS]- Step-by-Step Solution
> 1. **Postfix** (shunting-yard): `A B C + * D / E -`
>    (`*` waits; `(` blocks; `+` pops at `)`; `/` pops `*` (equal precedence, left-assoc) then pushes; `-` pops `/` and pushes.)
> 2. **Prefix**: reverse+swap → `E - / D ) C + B ( * A` → postfix `E D C B A + * / -` → reverse → **`- / * A + B C D E`**
> 3. **Evaluate postfix**: push 8, 2, 3; `+` → 5; `*` → 40; push 5; `/` → $40/5=8$; push 1; `-` → $8-1=7$.
> 4. **Answer: $7$** — and note `*` was popped by `/` despite equal precedence because left-to-right associativity demands the earlier operator leave first.

---

## 7. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

int prec(char op) {
    switch (op) { case '^': return 3; case '*': case '/': return 2;
                  case '+': case '-': return 1; }
    return 0;
}

// Infix -> Postfix (shunting-yard). Single-token operands (A, B, ...).
string infixToPostfix(const string& in) {
    string out;  vector<char> st;                    // ArrayStack for operators
    for (char t : in) {
        if (isspace((unsigned char)t)) continue;
        if (isalnum((unsigned char)t)) out += t;     // operand -> output
        else if (t == '(') st.push_back(t);
        else if (t == ')') {
            while (!st.empty() && st.back() != '(') { out += st.back(); st.pop_back(); }
            st.pop_back();                           // discard '('
        } else {                                     // operator
            while (!st.empty() && st.back() != '(' &&
                   (prec(st.back()) > prec(t) ||
                    (prec(st.back()) == prec(t) && t != '^'))) {
                out += st.back(); st.pop_back();     // pop higher/equal (left-assoc)
            }
            st.push_back(t);
        }
    }
    while (!st.empty()) { out += st.back(); st.pop_back(); }
    return out;
}

// Postfix evaluation with an operand stack. Space-separated tokens. O(n).
double evalPostfix(const string& expr) {
    vector<double> st;
    istringstream in(expr);
    string tok;
    while (in >> tok) {
        if (isdigit(tok[0])) {
            st.push_back(stod(tok));                 // multi-digit number
        } else {                                     // single-char operator
            double right = st.back(); st.pop_back();  // FIRST pop = right operand!
            double left  = st.back(); st.pop_back();
            switch (tok[0]) {
                case '+': st.push_back(left + right); break;
                case '-': st.push_back(left - right); break;
                case '*': st.push_back(left * right); break;
                case '/': st.push_back(left / right); break;
                case '^': st.push_back(pow(left, right)); break;
            }
        }
    }
    return st.back();
}

int main() {
    cout << infixToPostfix("A+B*C-D")     << "\n";   // ABC*+D-
    cout << infixToPostfix("(A+B)^C*D")   << "\n";   // AB+C^D*
    cout << infixToPostfix("A*(B+C)/D-E") << "\n";   // ABC+*D/E-
    cout << evalPostfix("5 6 2 + * 12 4 / -") << "\n"; // 37 (Worked Example 4)
    // self-test operands: A=8, B=2, C=3, D=5, E=1
    cout << evalPostfix("8 2 3 + * 5 / 1 -") << "\n";  // 7
    return 0;
}
```

**Output:**

```
ABC*+D-
AB+C^D*
ABC+*D/E-
37
7
```

Every line matches the hand-traced worked examples above. ✅

---

## 8. Related Notes
- [[Stack]] — the data structure doing all the work: operator waiting-room and operand machine.
- [[Postfix Evaluation]]-style demos in [[Stack]] — the $37$ example shared between notes.
- [[Arrays]] / [[Pointers]] — how the stack itself is implemented under the hood.
- [[Asymptotic Analysis]] — everything here is a single $O(n)$ scan.
