---
title: "Linked List"
date: 2026-09-21
tags:
  - concept
  - dsa
  - linked-list
  - linear-data-structures
aliases:
  - "Singly Linked List"
  - "Doubly Linked List"
  - "Circular Linked List"
status: completed
---

# 🔗 Linked Lists (Train Cars of Memory)

> [!NOTE] 💡 The Big Picture Intuition
> Think of a **train**: each car holds cargo and is coupled only to its neighbours. To board the train you must enter at the engine (the **head**) and walk car-by-car — but you can attach a new car to the front in **one move** (recouple two couplings), no matter how long the train is.
> That's the linked list bargain versus [[Arrays]]: the nodes live at *scattered* addresses in memory, so no address arithmetic is possible — you pay $O(n)$ to reach element $i$, but gain $O(1)$ insertion/deletion *once you're standing at the right spot*, because nothing has to be physically shifted.

---

## 1. Anatomy of a Node

Every linked list is built from nodes, each holding **data + at least one pointer**:

```
Singly:   +--------+--------+      +--------+--------+
          |  data  |  next ●+----->|  data  |  next ●+----> NULL
          +--------+--------+      +--------+--------+

Doubly:   NULL<--●prev+------+--------+--●next-->  (each node has both arrows)
                    | data  |  data  |

Circular: the last node's next pointer loops back to the first node
```

| Field | Purpose |
| :-- | :-- |
| `data` | The stored value (int, object, …) |
| `next` | Address of the next node — **this arrow IS the list's order** |
| `prev` (doubly only) | Address of the previous node — enables backward walking |

---

## 2. The Three Flavours

### 2.1 Singly Linked List
Each node points only **forward**. One entry point (`head`); traversal is one-way; ends at `NULL`.

```
head ──> [10|●]──>[20|●]──>[30|●]──>[40|NULL]
```

- ✅ Least memory per node (one pointer)
- ✅ Simplest to implement
- ❌ Cannot step backwards; deleting a node needs its *predecessor*

### 2.2 Doubly Linked List (DLL)
Each node points **forward and backward**. Usually kept with a `head` and a `tail`.

```
NULL <──[⇄ 10 ⇄]⇌[⇄ 20 ⇄]⇌[⇄ 30 ⇄]──> NULL
              head          tail
```

- ✅ Two-way traversal; deletion of a known node in $O(1)$ (its `prev` is on-board!)
- ✅ $O(1)$ access to both ends
- ❌ Extra `prev` pointer = more memory; more pointer bookkeeping (two fields to fix per operation)

### 2.3 Circular Linked List
The last node's `next` points back to the **first** node — no `NULL` terminator, the chain forms a ring. Works with both singly and doubly variants.

```
      ┌──────────────────────────────┐
      ▼                              │
head ──>[10|●]──>[20|●]──>[30|●]─────┘
```

- ✅ From any node you can reach every node (round-robin scheduling, multiplayer turn-taking)
- ✅ `tail.next = head` gives $O(1)$ access to **both ends** of the logical list
- ❌ No natural `NULL` — **every traversal needs a stop condition** (`do…while` until you return to the start node), otherwise infinite loop

> [!WARNING] ⚠️ The Infinite-Loop Trap
> In a circular list, `while (temp != nullptr)` never terminates. Always use a **sentinel stop**: remember the starting node and loop `while (true) { …; if (temp->next == start) break; }`, or use `do…while` semantics.

---

## 3. Operations & Complexity

| Operation | Singly | Doubly | Circular (singly) |
| :--- | :---: | :---: | :---: |
| Search by value | $O(n)$ | $O(n)$ | $O(n)$ |
| Access $i$-th element | $O(n)$ | $O(n/2) = O(n)$ | $O(n)$ |
| Insert at **head** | $O(1)$ | $O(1)$ | $O(1)$ (via tail) |
| Insert at **tail** | $O(n)$ (walk) / $O(1)$ with tail ptr | $O(1)$ | $O(1)$ |
| Delete at **head** | $O(1)$ | $O(1)$ | $O(1)$ |
| Delete a **given node** | $O(n)$ (need predecessor) | $O(1)$ | $O(n)$ |
| Reverse traversal | ❌ (needs reversal) | ✅ $O(n)$ | ❌ / ✅ (doubly circular) |

> [!TIP] 🧠 The Golden Rule of Pointers
> **Reconnect before you disconnect.** When inserting or deleting, always wire up the new/remaining links *first*, and only then drop the old ones — otherwise you orphan part of the chain with no way back to it.

---

## 4. Core Algorithms, Step by Step

### 4.1 Insert at Head (singly) — $O(1)$
```cpp
// Step 1: create the node
Node* newNode = new Node(value);
// Step 2: new node adopts the old first node
newNode->next = head;
// Step 3: crown the newcomer
head = newNode;
```
```
Before:   head ──>[20]──>[30]
Insert10: [10]──>[20]──>[30]   (2 pointer writes — never touch the rest)
```

### 4.2 Insert at Tail with Tail Pointer (singly) — $O(1)$
```cpp
Node* newNode = new Node(value);
tail->next = newNode;
tail = newNode;
```
Without a tail pointer you must first walk $n$ nodes → $O(n)$.

### 4.3 Delete a Node by Value (singly) — $O(n)$
```cpp
Node *prev = nullptr, *curr = head;
while (curr != nullptr && curr->data != target) {   // walk
    prev = curr; curr = curr->next;
}
if (prev == nullptr) head = curr->next;             // deleting the head
else                 prev->next = curr->next;       // bypass the node
delete curr;                                        // C++ frees the node manually
```
The walk to find the *predecessor* is the cost. A DLL deletes in $O(1)$ because the node carries its own `prev`.

### 4.4 Insert into a Sorted List (singly) — walk + splice
```cpp
if (head == nullptr || head->data >= value) {
    newNode->next = head; head = newNode; return;
}
while (curr->next != nullptr && curr->next->data < value)   // walk
    curr = curr->next;
newNode->next = curr->next;  curr->next = newNode;          // reconnect before disconnect
```

### 4.5 Reverse a Singly List — the 3-pointer dance, $O(n)$
```
        prev    curr    nxt
NULL ← [ 1 ] ← [ 2 ]    [ 3 ] → …   (flip one arrow at a time)
```
```cpp
Node *prev = nullptr, *curr = head;          // 1. start
while (curr != nullptr) {                    // 2. loop
    Node* nxt = curr->next;   // save the road ahead
    curr->next = prev;        // flip the arrow
    prev = curr; curr = nxt;  // march both pointers forward
}
head = prev;                                 // 3. prev ends on the last node
```

### 4.6 Josephus / Round-Robin (circular) — elimination walk
People stand in a circle; every $k$-th person is eliminated; continue from the next person until one remains. The circular list models the circle natively: after eliminating node `curr`, resume from `curr->next` — no need to "restart" from the head each round.

---

## 5. Linked List vs Array — The Trade-off Table

| Criterion | [[Arrays]] | Linked List |
| :--- | :---: | :---: |
| Memory layout | Contiguous block | Scattered nodes + pointers |
| Random access `A[i]` | $O(1)$ ✅ | $O(n)$ ❌ |
| Insert/delete at **front** | $O(n)$ (shift) | $O(1)$ ✅ |
| Insert/delete at **end** | $O(1)$ | $O(1)$ only with tail pointer |
| Memory overhead | None (pure data) | 1–2 pointers per node |
| Cache performance | Excellent (locality) | Poor (pointer chasing) |
| Size flexibility | Fixed / resize copies all | Grows/shrinks node-by-node |

**Rule of thumb**: read-heavy → array; write-at-front-heavy → linked list.

---

## 6. Worked Examples

### Worked Example 1: Address-Chain Trace
> [!EXAMPLE] Problem
> Nodes live at addresses: head→**100** `[5|next]`, →**300** `[7|next]`, →**200** `[9|NULL]`. Print the list.

**Step 1**: Read node at 100 → data `5`, `next = 300`.
**Step 2**: Read node at 300 → data `7`, `next = 200`.
**Step 3**: Read node at 200 → data `9`, `next = NULL` → stop.

**Output: `5 → 7 → 9`** — note the addresses (100, 300, 200) are in *no arithmetic order*; only the pointers define sequence. This is exactly why $O(1)$ indexing is impossible.

### Worked Example 2: Pointer Rewiring Trace (delete 20)
> [!EXAMPLE] Problem
> `head → [10] → [20] → [30] → NULL`. Delete the node containing 20 using only `head`.

**Step 1**: `prev = head (10)`, `curr = head.next (20)`.
**Step 2**: Found target. Bypass: `prev->next = curr->next` → node 10 now points at node 30.
**Step 3**: Node 20 is unreachable; `delete curr` reclaims its memory.

```
Before:  [10] ──> [20] ──> [30]      After:   [10] ──────> [30]
                (orphaned ↑)                   (20 deleted with `delete`)
```

Cost = the search walk ($O(n)$) + **one** pointer write. In a DLL this is $O(1)$: `curr->prev->next = curr->next` and `curr->next->prev = curr->prev`.

### Worked Example 3: Reversal Dry-Run
> [!EXAMPLE] Problem
> Reverse `10 → 20 → 30 → NULL` by hand using the 3-pointer method.

| Step | `prev` | `curr` | `nxt` | List state (`curr` onward) |
| :--: | :--: | :--: | :--: | :-- |
| start | `NULL` | `10` | — | `10 → 20 → 30` |
| 1 | `10` | `20` | `20` | `10→NULL ‖ 20 → 30` |
| 2 | `20` | `30` | `30` | `20 → 10 → NULL ‖ 30` |
| 3 | `30` | `NULL` | `NULL` | `30 → 20 → 10 → NULL` ✅ |

Return `prev = 30` as the new head. Time $O(n)$, space $O(1)$.

---

## 7. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: The Tail-Insert Surprise
> A singly linked list has only a `head` pointer (no `tail`). What is the complexity of appending a node at the end — and which flavour fixes it?

> [!SUCCESS]- Step-by-Step Solution
> 1. With only `head`, you must walk all $n$ nodes to find the last one → **$O(n)$**.
> 2. Fix A: maintain a `tail` pointer permanently → append becomes $O(1)$ (`tail.next = new; tail = new`).
> 3. Fix B: a **circular** list where you keep only the tail — `tail.next` is the head, so you get both ends in $O(1)$.
> 4. Fix C: a **doubly** list with `tail` — also $O(1)$, plus $O(1)$ deletion of any known node.

---

## 8. C++ Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d, Node* n = nullptr) : data(d), next(n) {}
};

class SinglyLinkedList {
    Node* head = nullptr;
    Node* tail = nullptr;                    // tail pointer => O(1) append
public:
    ~SinglyLinkedList() {                    // free every node
        while (head) { Node* nxt = head->next; delete head; head = nxt; }
    }

    void insertHead(int value) {             // O(1)
        head = new Node(value, head);
        if (!tail) tail = head;
    }

    void insertTail(int value) {             // O(1) thanks to tail
        Node* node = new Node(value);
        if (!tail) { head = tail = node; }
        else       { tail->next = node; tail = node; }
    }

    bool remove(int value) {                 // O(n)
        Node *prev = nullptr, *curr = head;
        while (curr && curr->data != value) { prev = curr; curr = curr->next; }
        if (!curr) return false;
        if (!prev) head = curr->next;
        else       prev->next = curr->next;
        if (curr == tail) tail = prev;
        delete curr;
        return true;
    }

    int search(int value) const {            // O(n), returns index or -1
        int i = 0;
        for (Node* curr = head; curr; curr = curr->next, ++i)
            if (curr->data == value) return i;
        return -1;
    }

    void reverse() {                         // O(n) time, O(1) space
        Node *prev = nullptr, *curr = head;
        tail = head;
        while (curr) {
            Node* nxt = curr->next;
            curr->next = prev;
            prev = curr; curr = nxt;
        }
        head = prev;
    }

    friend ostream& operator<<(ostream& os, const SinglyLinkedList& lst) {
        for (Node* curr = lst.head; curr; curr = curr->next)
            os << curr->data << " -> ";
        return os << "NULL";
    }
};

int main() {
    SinglyLinkedList lst;
    for (int x : {10, 20, 30}) lst.insertHead(x);   // 30 -> 20 -> 10 -> NULL
    lst.remove(20);                                 // 30 -> 10 -> NULL
    lst.reverse();                                  // 10 -> 30 -> NULL
    cout << lst << "\n";
    return 0;
}
```

---

*(Full runnable circular version below — kept separate for clarity.)*

```cpp
#include <bits/stdc++.h>
using namespace std;

// Circular list in action: every k-th player loses their turn (Josephus).
vector<int> roundRobin(const vector<string>& names, int k) {
    struct Player { string name; Player* next; };
    int n = names.size();

    // build the ring: last node's next loops back to the first
    vector<Player> pool;  pool.reserve(n);
    for (const string& s : names) pool.push_back({s, nullptr});
    for (int i = 0; i < n; ++i) pool[i].next = &pool[(i + 1) % n];

    Player* curr = &pool[n - 1];             // stand just before the first player
    vector<int> out;                         // elimination order (indices)
    while (n > 1) {
        for (int step = 0; step < k - 1; ++step) curr = curr->next;
        Player* out_ = curr->next;           // the k-th player is eliminated
        curr->next = out_->next;             // bypass — reconnect before disconnect
        out.push_back(out_ - &pool[0]);
        --n;
    }
    out.push_back(curr - &pool[0]);          // survivor
    return out;
}

int main() {
    vector<string> names = {"A", "B", "C", "D", "E"};
    vector<int> order = roundRobin(names, 3);
    cout << "Elimination order: ";
    for (int i = 0; i + 1 < (int)order.size(); ++i)
        cout << names[order[i]] << " ";
    cout << " | survivor: " << names[order.back()] << "\n";
    // Elimination order: C A E B  →  survivor: D
    return 0;
}
```

---

## 9. Related Notes
- [[Pointers]] — every `next`/`prev` field *is* a pointer; this note is pointers in action.
- [[Structure]] — a node is a struct: heterogeneous members (data + links) under one name.
- [[Arrays]] — the contiguous rival: $O(1)$ access vs $O(1)$ front-insertion.
- [[Stack]] — the classic application of a singly linked list (head = top).
- [[Asymptotic Analysis]] — the vocabulary ($O(1)$, $O(n)$) used in every table above.

