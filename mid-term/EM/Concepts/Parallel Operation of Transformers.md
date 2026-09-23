---
title: "Parallel Operation of Transformers"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - transformer
  - three-phase
aliases:
  - "Transformer Parallel Operation"
  - "Conditions for Parallel Operation"
  - "Load Sharing Transformers"
status: completed
---

# 🔗 Parallel Operation of Transformers

> [!NOTE] 💡 The Big Picture Intuition
> Why does one city substation run *three* transformers side by side instead of one big one? Same reason you don't put all your files on one disk: **redundancy** (one fails, others carry on), **maintenance without blackout** (isolate one, keep the lights on), **peak flexibility** (switch in extra units only when demand rises — less idle loss), and **future growth** (add capacity without replacing everything). But bolting two secondaries to the same busbar is like tying two boats side by side: if they don't *pull in step*, the rope between them — the circulating current — burns. Every "condition" below is just a way of keeping the boats in step.

---

## 1. Why Parallel? (and the price)

| Benefit | Cost / risk |
| :--- | :--- |
| Redundancy → supply survives a unit failure | Circulating currents if conditions are violated |
| Maintenance without total shutdown | Unequal load sharing → one overheats early |
| Peak-load economics (switch units in/out) | Fault current through the busbar is larger |
| Capacity can grow with demand | Both units see each other's impedance |

## 2. The Conditions (the exam heart)

> [!IMPORTANT] 🎯 Conditions for parallel operation — single-phase
> **Mandatory (busbar survives):**
> 1. **Same voltage ratio** (primary & secondary ratings equal) — otherwise a circulating current flows *even at no-load*.
> 2. **Same polarity** — wrong polarity is a dead short across the secondaries.
> **Desirable (load actually shares properly):**
> 3. **Equal per-unit (percentage) impedances** — for load to divide *in proportion to the kVA ratings*.
> 4. **Same $X/R$ ratio (impedance phase angle)** — so the transformers operate at the same power factor.
> **Three-phase banks additionally need:**
> 5. **Same phase-sequence** and **zero relative phase displacement** between secondaries — i.e. the same vector group (Yy0 with Dd0 can pair; Yy0 with Dy11 cannot — 30° apart).

> [!TIP] 🧠 Why each condition — one-line logic (learn the logic, not the list)
> 1. *Ratio mismatch* → the two secondary EMFs differ → the difference voltage drives current around the local loop **before any load is even connected**. It heats both units and caps their usable capacity.
> 2. *Polarity* → at any instant the two secondaries must agree on which terminal is "+". Reversed = the two EMFs add around a loop of nearly zero impedance = **short circuit**.
> 3. *Equal pu impedance* → load division is a current-divider: each transformer takes current in inverse ratio of its impedance. To make current divide *in proportion to kVA rating*, impedance must divide *in proportion to kVA rating too* — i.e. equal **per-unit**. (In ohms, the bigger machine must have proportionally smaller ohms.)
> 4. *Same X/R* → the two currents then have the same phase angle, so the parallel combination operates at one common pf and total copper loss is minimized.

## 3. Equivalent Circuit & Load Sharing

With secondaries tied to one bus, the two transformers reduce to two EMFs $E_1, E_2$ feeding a common load through impedances $Z_1, Z_2$ (referred to one side):

```
 E1 o---[ Z1 ]---+---------+----o Load (V_L)
                 |         |
 E2 o---[ Z2 ]---+         |
                          Z_load
                          |
              N ----------+----------o return
```

- **Circulating current at no-load** ($E_1 \ne E_2$):
$$I_c = \frac{E_1 - E_2}{Z_1 + Z_2}$$
  — limited only by the two internal impedances (small!) → even a small ratio mismatch makes a surprisingly large $I_c$. This is *why* condition 1 is strict.
- **Loaded, equal ratios** ($E_1 = E_2 = E$): load current divides exactly as a current divider:
$$\mathbf{I}_1 = \mathbf{I}_{total}\cdot\frac{\mathbf{Z}_2}{\mathbf{Z}_1 + \mathbf{Z}_2}, \qquad \mathbf{I}_2 = \mathbf{I}_{total}\cdot\frac{\mathbf{Z}_1}{\mathbf{Z}_1 + \mathbf{Z}_2}$$
- In **per-unit terms** the elegant exam statement: each transformer carries load in proportion to its rating **iff** $Z_{1,pu} = Z_{2,pu}$ at the same base.
- General result (with both impedances at same angle): transformer 1's load kVA
$$S_1 = S_{total}\cdot\frac{S_{1,rated}/Z_{1,pu}}{S_{1,rated}/Z_{1,pu} + S_{2,rated}/Z_{2,pu}}$$

> [!WARNING] ⚠️ Exam traps
> 1. "Same impedance (ohms)" is **wrong** — the condition is same **per-unit** impedance. A 1000 kVA unit must have 2× the ohms of a 500 kVA unit to share fairly.
> 2. Conditions 1–2 are about **survival** (no-load circulating current / short), conditions 3–4 about **fair load division** — questions love mixing these up.
> 3. Vector groups: same magnitude ratio but 30° apart (Dy11 vs Yy0) → huge circulating current even with perfect ratios.
> 4. When impedances are at *different* angles, the transformers run at different pfs — one delivers more reactive than the other. The kVA split is still computed with complex division.

## 4. Worked Examples

### Worked Example 1: Load division between two transformers
> [!EXAMPLE] Problem
> Two 1-phase transformers A (500 kVA, $Z = 5\%$) and B (250 kVA, $Z = 5\%$) share a 750 kVA load. Find each one's share and check for overloading.

**Step 1 — Pu impedances are equal (5% each)** → each carries load in proportion to rating.

**Step 2 — Shares:**
$$S_A = 750 \times \frac{500}{500+250} = 500\ \text{kVA}, \qquad S_B = 750 \times \frac{250}{750} = 250\ \text{kVA}$$

**Step 3 — Check:** A runs at $\frac{500}{500} = 100\%$, B at $\frac{250}{250} = 100\%$ → both exactly full load, no overload ✅ (this is precisely the "equal pu impedance" promise).

### Worked Example 2: Unequal pu impedance → overload
> [!EXAMPLE] Problem
> Transformer A: 500 kVA at 5% impedance. Transformer B: 250 kVA at 6.25% impedance. Total load = 750 kVA (equal to the sum of both ratings). Find each share and check for overloading.

**Step 1 — Convert to a common base (500 kVA):** $Z_{pu,new} = Z_{pu,old} \times \frac{S_{new}}{S_{old}}$

$$Z_A = 5\% \times \frac{500}{500} = 5\%, \qquad Z_B = 6.25\% \times \frac{500}{250} = 12.5\%$$

**Step 2 — Weighting factors** $S_{rated}/Z_{pu}$ (on the common base):
$$A: \frac{500}{0.05} = 10000, \qquad B: \frac{500}{0.125} = 4000, \qquad \text{total} = 14000$$

**Step 3 — Shares:**
$$S_A = 750 \times \frac{10000}{14000} = \boxed{535.7\ \text{kVA}}, \qquad S_B = 750 \times \frac{4000}{14000} = \boxed{214.3\ \text{kVA}}$$

**Step 4 — Check loading:**
$$A: \frac{535.7}{500} = 107.1\% \Rightarrow \textbf{overloaded}, \qquad B: \frac{214.3}{250} = 85.7\%$$

Even though the *total* load equals the *total* rating, the mismatch in pu impedance pushes A over its limit. The pu impedances must be **equal** for full combined capacity — unequal pu (here 5% vs 6.25% own-base) derates the bank to the load that keeps the *most-loaded* unit at 100%.

### Worked Example 3: No-load circulating current
> [!EXAMPLE] Problem
> Two 400 V : 100 kVA transformers in parallel have a 2% ratio mismatch — secondary EMFs are 404 V and 396 V. Each has 5% impedance. Find the no-load circulating current.

**Step 1 — Loop EMF:** $|E_1 - E_2| = 404 - 396 = 8$ V.

**Step 2 — Impedance of each in ohms:**
$$Z_{base} = \frac{V^2}{S} = \frac{400^2}{100000} = 1.6\ \Omega \Rightarrow Z = 0.05 \times 1.6 = 0.08\ \Omega \text{ each}$$

**Step 3 — Circulating current (loop of the two internal impedances):**
$$I_c = \frac{E_1 - E_2}{Z_1 + Z_2} = \frac{8}{0.16} = \boxed{50\ \text{A}}$$

**Step 4 — Sanity check:** full-load current of one unit is $\frac{100000}{400} = 250$ A, so this no-load current is already $20\%$ of full load — *doing nothing useful*, just heating both windings. A 2% ratio error is therefore intolerable; "same ratio" is a survival condition, not a nicety.

## 5. Self-Test (Active Recall)

1. List the two *mandatory* and two *desirable* conditions for paralleling 1-phase transformers, with one-line reasons.
2. Why can't Yy0 and Dy11 banks be paralleled even with equal voltage ratios? *(30° secondary displacement → $E_1 - E_2 \ne 0$ → circulating current.)*
3. Two transformers have equal pu impedance but different kVA ratings — how does load divide? *(Proportionally to kVA ratings.)*
4. Why does a ratio mismatch hurt *before* any load is connected? *(Local loop EMF difference ÷ small loop impedance → circulating current.)*
5. Two units share 600 kVA: A = 400 kVA at 4%, B = 200 kVA at 4%. Shares? *(400/200 — proportional to ratings.)*

## 6. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- The equivalent-circuit source material: [[Review of Single-Phase Transformer]]
- Vector groups decide condition 5: [[Types of Transformer Connections]]
- Feeding these banks: [[Three-Phase Systems with Balanced and Unbalanced Load]]
- Special-case bank: [[Scott Connection]] · [[Autotransformer]]
