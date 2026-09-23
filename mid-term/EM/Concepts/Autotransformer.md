---
title: "Autotransformer"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - transformer
aliases:
  - "Auto Transformer"
  - "Single Winding Transformer"
status: completed
---

# 🔧 Autotransformer

> [!NOTE] 💡 The Big Picture Intuition
> A normal transformer moves power from one coil to another *magnetically*. An autotransformer cheats beautifully: it uses **one single continuous winding**, where the input and output **share** part of it. Part of the power crosses magnetically (like a normal transformer), but the bigger part just **flows through the shared copper by conduction**, untouched by any induction. That's why an autotransformer is smaller, cheaper, and more efficient than a two-winding unit of the same rating — and also why the two sides are *electrically connected*, which is both its charm (saving) and its danger (no isolation).

---

## 1. Construction & Working

One winding $N_1$ tapped at point $C$, with $N_2 = N_{CB}$ forming the secondary:

```
   V1  o──── A ──[ N1 turns ]── B
                │
                C ── tap ──[ N2 = turns between C and B ]──o  V2 (load)
```

- Full winding $AB$ = $N_1$ turns sees $V_1$ → volts per turn $= V_1/N_1$.
- Secondary takes the *section* $CB$ ($N_2$ turns) →
$$\boxed{\frac{V_2}{V_1} = \frac{N_2}{N_1} = K}$$
  — the *same ratio law* as a two-winding transformer, because both share the same core flux.
- **Currents**: load current $I_2$; input current $I_1$. The shared (common) section $CB$ carries only the **difference**:
$$I_{CB} = I_2 - I_1 \quad (\text{step-down; } I_2 > I_1)$$
  because $I_2$ arriving from the load partially cancels $I_1$ entering the tap.

> [!IMPORTANT] 🎯 Power split — the whole point
> Input (or output) kVA $= V_1 I_1 = V_2 I_2 = S_{in}$, but it travels in two streams:
> $$\underbrace{V_2 I_1}_{\text{conducted}} + \underbrace{V_2(I_2 - I_1)}_{\text{transformed (inductive)}} = V_2 I_2$$
> The **transformed part is only $V_2 I_1 = S_{in}(1 - K)$**... for step-down with $K = N_2/N_1 < 1$, the conducted fraction is $K$ and the transformed fraction is $(1-K)$. The winding copper only needs to be sized for the **transformed** part → the saving.

## 2. Copper Saving — the exam's favourite derivation

Winding copper $\propto$ (turns × current × length). For a two-winding transformer of the same rating you'd need $N_1 I_1 + N_2 I_2$ worth of copper. The autotransformer needs only:

- Series section $AC$: $(N_1 - N_2)$ turns carrying $I_1$
- Common section $CB$: $N_2$ turns carrying $(I_2 - I_1)$

Ratio of copper used:
$$\frac{Cu_{auto}}{Cu_{2w}} = 1 - K \qquad (K = N_2/N_1)$$

> [!TIP] 🧠 The three headline consequences (memorize the logic, not just the numbers)
> 1. **Copper saving = $(1 - K)$** — the closer $V_2$ is to $V_1$ (K → 1), the more you save. At $K = 0.9$ you use 10% of the copper; the saving shrinks to nothing for very different voltages. **Autotransformers shine only for ratios near 1** (e.g. 220 V ↔ 200 V, or interconnecting 132 kV and 220 kV grids... ratios near 1 like 400/220 kV).
> 2. Therefore **lower losses → higher efficiency** and **better regulation** than a two-winding unit of the same output.
> 3. **Smaller size and cheaper** — but **no electrical isolation**, and a break in the common section can put full $V_1$ on the load side.

## 3. kVA Boosting (why a "small" winding handles a "big" load)

A two-winding transformer of rating $S_T$ can be reconnected as a step-up autotransformer, and its new rating jumps:

$$S_{auto} = \frac{S_{2w}}{1 - K} \qquad \text{(with } K = \text{boost fraction } N_2/N_1\text{)}$$

Example: a 5 kVA, 220/110 V two-winding unit reconnected as a 220 → 330 V autotransformer: $K = 110/220 = 0.5$, so $S_{auto} = 5/(1-0.5) = \mathbf{10}$ **kVA**. Same core, same copper — double the throughput, because half the kVA now arrives by conduction.

## 4. Applications

- **Motor starting** (induction/synchronous): reduced voltage start with cheap variable taps.
- **Variable-voltage supplies**: variac (continuously adjustable tap) for lab benches.
- **Interconnecting nearby transmission voltages** (e.g. 400 kV ↔ 220 kV) — the ratio is close to 1, so the copper saving is enormous.
- **Boosting/bucking** a supply voltage by a few percent (furnace/feeder regulation).

> [!WARNING] ⚠️ Exam traps
> 1. **No isolation** — the classic reasoning answer: autotransformers are unsafe for low-voltage instrument supplies because a winding fault applies primary voltage directly to the output.
> 2. The saving formula uses $K = N_2/N_1$ for **step-down**; if you define K as boost, flip the fraction — always state your definition first.
> 3. Impedance of an autotransformer is **lower** (roughly $(1-K)^2$ of the two-winding value referred the same way) → better regulation but **bigger fault currents**.
> 4. In the common section, current is the **difference** $I_2 - I_1$, not the load current — that's where the copper saving physically comes from.

## 5. Worked Example

> [!EXAMPLE] Problem
> A 1-phase autotransformer supplies a 10 kW, 200 V load from a 250 V supply. Assume ideal (lossless). Find (a) the currents $I_1, I_2$ and the common-section current, (b) the transformed and conducted kVA, (c) the copper saving vs a two-winding transformer.

**Step 1 — Load current:** $I_2 = \dfrac{10000}{200} = 50$ A.

**Step 2 — Input current:** $I_1 = \dfrac{10000}{250} = 40$ A.

**Step 3 — Common-section current:** $I_{CB} = I_2 - I_1 = 50 - 40 = \boxed{10\ \text{A}}$.

**Step 4 — Power split:**
$$S_{conducted} = V_2 I_1 = 200 \times 40 = 8\ \text{kVA}, \qquad S_{transformed} = V_2 (I_2 - I_1) = 200 \times 10 = 2\ \text{kVA}$$
Check: $8 + 2 = 10$ kVA ✅

**Step 5 — Copper saving:** here $K = V_2/V_1 = 200/250 = 0.8$:
$$Cu_{saving} = 1 - K = \boxed{20\%}$$
Only the 2 kVA transformed stream sizes the magnetic part — that's why the machine is small for its 10 kVA output.

## 6. Self-Test (Active Recall)

1. Why does the common section of an autotransformer carry $I_2 - I_1$ rather than $I_2$? *(KCL at the tap: the load current is partly fed by conduction from the line.)*
2. An autotransformer is ideal for 11 kV → 10 kV but poor for 11 kV → 440 V. Why, in copper terms? *(Saving = 1 − K; with K near 1 the copper needed is tiny, with K small it approaches a full two-winding design.)*
3. A 10 kVA two-winding transformer is reconnected as an autotransformer to boost 200 V to 300 V. New rating? *(K = 100/200 = 0.5 → 10/(1−0.5) = 20 kVA.)*
4. Give two applications where the missing isolation is acceptable, and one where it is not.

## 7. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- The two-winding baseline it saves against: [[Review of Single-Phase Transformer]]
- Another ratio trick, three-phase style: [[Types of Transformer Connections]] · [[Scott Connection]]
- Sharing the bus: [[Parallel Operation of Transformers]]
