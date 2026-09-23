---
title: "Measurement of Power and Power Factor in Three-Phase Circuits"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - three-phase
  - measurement
aliases:
  - "Two Wattmeter Method"
  - "Three Wattmeter Method"
  - "Power Factor Measurement"
  - "Blondel's Theorem"
status: completed
---

# ⚡ Measurement of Power & Power Factor in Three-Phase Circuits

> [!NOTE] 💡 The Big Picture Intuition
> A wattmeter reads the product of the voltage across **its** coil and current through **its** coil. In a 3-phase system there is no single "the voltage" and "the current" — the trick is to insert wattmeters so their coils *share* the job. **Blondel's theorem** tells us the minimum number needed: for an $n$-wire system, $n-1$ wattmeters suffice, because one conductor can serve as the common reference for all the pressure coils. Three wires → **two wattmeters** — and as a bonus, the difference of their readings *hands you the power factor for free*.

---

## 1. Blondel's Theorem

> [!IMPORTANT] 🎯 Statement
> In an $n$-wire system, the total power can be measured with **$n - 1$ wattmeters**, provided no current flows in the remaining (reference) wire — or if it does, the missing power is accounted for.

| System | Wires | Wattmeters needed |
| :--- | :---: | :---: |
| 3-phase, 3-wire (star/delta) | 3 | **2** |
| 3-phase, 4-wire | 4 | **3** (or 2½-element meter) |
| Single phase | 2 | 1 |

---

## 2. Three-Wattmeter Method

Each wattmeter's current coil in one line, pressure coil from that line to **neutral** (4-wire systems, or 3-wire with an artificial neutral):

$$P = W_1 + W_2 + W_3$$

- Works for **balanced and unbalanced** loads, any power factor, with or without neutral.
- With a balanced load all three read equal: $W_1 = W_2 = W_3 = V_{ph}I_{ph}\cos\phi$.
- Cost: three instruments and a neutral connection — used mainly for unbalanced 4-wire measurements.

---

## 3. Two-Wattmeter Method (the exam favourite)

**Connections**: current coils in lines **R** and **B**; both pressure coils from their line to the **third line Y** (the reference). No neutral needed → works on any 3-wire load.

**Instantaneous power derivation** (balanced or unbalanced, 3-wire):
$$p = v_R i_R + v_Y i_Y + v_B i_B, \qquad i_R + i_Y + i_B = 0 \Rightarrow i_Y = -(i_R + i_B)$$
$$p = i_R(v_R - v_Y) + i_B(v_B - v_Y) = i_R v_{RY} + i_B v_{BY}$$
Average: $W_1 + W_2 = P$ — each wattmeter measures one term of this split. ✅

### The two readings

> [!IMPORTANT] 🎯 The Working Formulae (balanced load)
> $$W_1 = V_L I_L \cos(30° + \phi) \qquad\qquad W_2 = V_L I_L \cos(30° - \phi)$$
> $$\boxed{P = W_1 + W_2 = \sqrt{3}\,V_L I_L \cos\phi} \qquad \boxed{Q = \sqrt{3}\,(W_2 - W_1)}$$
> $$\tan\phi = \sqrt{3}\,\frac{W_2 - W_1}{W_2 + W_1} \qquad\Longleftrightarrow\qquad \cos\phi = \cos\left[\tan^{-1}\!\left(\sqrt{3}\,\frac{W_2 - W_1}{W_2 + W_1}\right)\right]$$

The two wattmeters do **not** read equal (except at unity pf) because each pressure coil sees a line voltage shifted $30° \pm \phi$ from its current.

> [!TIP] 🧠 The "30° ± φ" picture
> Wattmeter 1: current-coil current $\mathbf{I}_R$, pressure-coil voltage $\mathbf{V}_{RY}$. The angle between them is $(30° + \phi)$. Wattmeter 2 sees $(30° - \phi)$ — its voltage $\mathbf{V}_{BY}$ lands on the *other* side of $\mathbf{I}_B$. As $\phi$ grows, $W_1$'s angle widens (reading shrinks) while $W_2$'s narrows (reading grows). So think: **lagging pf → $W_2 > W_1$**; leading pf → $W_1 > W_2$.

### Reading behaviour vs power factor (balanced load, $V_L I_L$ normalised)

| $\cos\phi$ | $\phi$ | $W_1 = \cos(30°+\phi)$ | $W_2 = \cos(30°-\phi)$ | Comment |
| :---: | :---: | :---: | :---: | :--- |
| 1 | 0° | 0.866 | 0.866 | Equal readings |
| 0.866 | 30° | 0.5 | 1 | $W_1 = \tfrac12 W_2$ |
| 0.5 | 60° | 0 | 0.866 | $W_1$ reads **zero** |
| 0 → (lag) | > 60° | negative | > 0.866 | $W_1$ reads **backwards** — reverse its pressure coil and subtract |
| 0 | 90° | −0.5 | 0.5 | $W_1 + W_2 = 0$: pure reactance draws no average power |

> [!WARNING] ⚠️ Exam traps
> 1. $W_2 - W_1$ (or $W_1 - W_2$) is **always positive for lagging** load when labelled as above — fix the convention in the question and state it.
> 2. A **negative** reading is not an error: reverse the pressure-coil connection and **subtract** that reading.
> 3. $\tan\phi$ formula gives $|\phi|$; decide lag/lead from which meter reads larger.
> 4. Total reactive power carries the $\sqrt{3}$: $Q = \sqrt{3}(W_2 - W_1)$ — a favourite slip is forgetting it.
> 5. The method **fails (reads wrongly) on unbalanced 4-wire loads** — the $i_Y = -(i_R + i_B)$ step dies when the neutral carries current.

---

## 4. Worked Examples

### Worked Example 1: Find P, Q and pf from two readings
> [!EXAMPLE] Problem
> Two wattmeters read $W_1 = 5$ kW and $W_2 = 2.5$ kW on a balanced 3-phase load. Find total power, power factor, and the line current if $V_L = 400$ V.

**Step 1 — Total power:**
$$P = W_1 + W_2 = 7.5 \text{ kW}$$

**Step 2 — Power factor:**
$$\tan\phi = \sqrt{3}\,\frac{5 - 2.5}{5 + 2.5} = \sqrt{3}\,\frac{2.5}{7.5} = 0.577 \Rightarrow \phi = 30° \Rightarrow \boxed{\cos\phi = 0.866\ (\text{lag})}$$

**Step 3 — Line current:**
$$I_L = \frac{P}{\sqrt{3}\,V_L\cos\phi} = \frac{7500}{\sqrt{3}(400)(0.866)} \approx \boxed{12.5\ \text{A}}$$

### Worked Example 2: Reading goes negative
> [!EXAMPLE] Problem
> The same load runs at $\cos\phi = 0.4$ lagging, $W_2 = 8$ kW. Predict $W_1$'s behaviour.

$\phi = \cos^{-1}(0.4) = 66.4° > 60°$ → $W_1$ must read **negative**.

$$W_1 = V_L I_L\cos(30° + 66.4°), \qquad W_2 = V_L I_L \cos(30° - 66.4°) = 8000 \Rightarrow V_L I_L = \frac{8000}{\cos(-36.4°)} = 9934 \text{ W}$$
$$W_1 = 9934\cos(96.4°) \approx \boxed{-1.13\ \text{kW}}$$

Operationally: reverse $W_1$'s pressure coil, note the positive deflection, and use $P = W_2 - |W_1|$.

---

## 5. Self-Test (Active Recall)

1. State Blondel's theorem and use it to justify 2 wattmeters on a 3-wire system.
2. Two wattmeters read 12 kW and −4 kW. Find P, Q, and pf. *(P = 8 kW, Q = 27.7 kVAR, pf = 0.28 lag)*
3. Prove that at $\cos\phi = 0.5$ one wattmeter reads zero.
4. Why does the two-wattmeter method need modification on a 4-wire unbalanced load?

---

## 6. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- The load being measured: [[Three-Phase Systems with Balanced and Unbalanced Load]]
- pf correction uses the same $Q$: [[Harmonic Reduction in Phase Voltages]]
- Power transfer stage upstream: [[Review of Single-Phase Transformer]]
