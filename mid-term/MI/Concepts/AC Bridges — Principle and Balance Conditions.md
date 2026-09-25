---
title: "AC Bridges — Principle and Balance Conditions"
date: 2026-09-25
tags:
  - concept
  - mi
  - measurement-and-instrumentation
  - ac-bridges
aliases:
  - "General AC Bridge"
  - "AC Bridge Balance Equation"
  - "Magnitude and Phase Balance"
status: completed
---

# 🌉 AC Bridges — Principle and Balance Conditions

> [!NOTE] 💡 The Big Picture Intuition
> The Wheatstone bridge balances resistances with DC. But inductors and capacitors fight AC with **phase**, not just magnitude — an inductor makes current *lag*, a capacitor makes it *lead*. So the AC bridge plays the same null game with two dice instead of one: to silence the detector, the two products of opposite arms must match **in size AND in timing**. That is why every serious AC bridge needs **two adjustable elements** — one to zero the magnitude, one to zero the phase. Master this one general equation and every specific bridge (Maxwell, Hay, Anderson, De Sauty, Schering) becomes an algebra exercise, not a memory chore.

---

## 1. The General AC Bridge

### 1.1 Circuit (the convention used in every MI bridge note)

```
            A
          ┌─┴─┐
        [Z1] [Z3]
        /       \
   B ●           ● D
        \       /
        [Z2] [Z4]
          └─┬─┘
            C
   Source: A–C   |   Detector (null): B–D
```

| Arm | Position | Typical content |
| :--- | :--- | :--- |
| $Z_1$ | A–B (top-left) | known $R$, or $R$+$C$ (series or parallel) |
| $Z_2$ | B–C (bottom-left) | known resistor |
| $Z_3$ | A–D (top-right) | known resistor / standard $L$ or $C$ |
| $Z_4$ | D–C (bottom-right) | the **unknown** |

> [!IMPORTANT] 🎯 The general balance condition (complex form)
> At balance the detector current is zero, so nodes B and D sit at the *same potential*. With detector current zero, the same current $I_1$ flows through $Z_1, Z_2$ and $I_2$ through $Z_3, Z_4$:
> $$I_1 Z_1 = I_2 Z_3 \qquad\text{and}\qquad I_1 Z_2 = I_2 Z_4$$
> Dividing one by the other:
> $$\boxed{Z_1 Z_4 = Z_2 Z_3} \qquad\text{(complex products of opposite arms equal)}$$
> and the unknown comes out as
> $$\boxed{Z_4 = \frac{Z_2 Z_3}{Z_1}}$$
> **Check of orientation**: with all four arms pure resistors this reduces to the Wheatstone result $\frac{P}{Q} = \frac{R}{S}$ — same equation, same physics ([[DC Bridges — Measurement of Resistance]]).

### 1.2 The two real balance conditions (magnitude + phase)

Writing $Z_k = \lvert Z_k \rvert\angle\theta_k$, the complex equation $Z_1 Z_4 = Z_2 Z_3$ splits into:

$$\text{(i) Magnitude:}\quad \lvert Z_1\rvert\,\lvert Z_4\rvert = \lvert Z_2\rvert\,\lvert Z_3\rvert$$
$$\text{(ii) Phase:}\quad \theta_1 + \theta_4 = \theta_2 + \theta_3$$

> [!WARNING] ⚠️ Why one adjustment is never enough
> One dial changes one real number, but balance demands agreement of **two** real numbers. A bridge with a single adjustable element generally reaches a *minimum* detector reading and then refuses to go silent — the classic lab frustration. Every standard bridge therefore builds in **two independent adjustments** (e.g. a ratio resistor *and* a capacitor/resistor in the opposite arm).

---

## 2. Quick Rules the Phase Condition Gives You

1. **Same-type rule**: if two adjacent arms ($Z_2$, $Z_3$) are pure resistors ($\theta_2 = \theta_3 = 0$), then $\theta_4 = -\theta_1$... and if $Z_1$ is also a pure resistor, $\theta_4 = 0$: **the unknown must be opposed by an arm of its own kind**. An inductance compares with an inductance ([[Measurement of Inductance — Maxwell, Hay and Anderson Bridges]]: Maxwell's inductance bridge); a capacitance with a capacitance (De Sauty, [[Measurement of Capacitance — De Sauty and Schering Bridges]]).
2. **Opposite-sign rule**: to measure an **inductive** unknown with a **standard capacitor**, put the capacitor in the arm *opposite* the unknown ($Z_1$): its negative phase cancels the unknown's positive phase ($\theta_1 < 0$, $\theta_4 > 0$, $\theta_1 + \theta_4 = 0$). Series-$RC$ in $Z_1$ → **Hay's bridge**; parallel-$RC$ in $Z_1$ → **Maxwell's $L$–$C$ bridge**; a fancier $R$–$C$ network in $Z_1$ → **Anderson's bridge**.
3. **Frequency appears (or not)**: whether $\omega$ survives in the balance equations depends on the topology. Maxwell's $L$–$C$ bridge gives $L$ **independent of frequency**; Hay's bridge carries $\omega$ explicitly. If $\omega$ appears, the source frequency must be known accurately.
4. **Bridge "Q reach"**: bridges where the unknown's $Q = \omega L/R$ enters the equations have practical $Q$ limits — Maxwell's $L$–$C$ suits **low/medium $Q$ ($1 < Q < 10$... i.e. lossy coils)**, Hay's suits **high $Q$ ($Q > 10$)** — the numbers are worked out in the inductance note.

---

## 3. Practical Notes (detectors, sources, strays)

- **Source**: sinusoidal oscillator, typically **1 kHz** (audio band), isolated from the bridge by a shielded transformer to avoid ground-loop strays.
- **Null detectors** (in order of era): **vibration galvanometer** (low-frequency resonance), **headphones** (audio, the classic human detector), **tuned amplifier + rectifier/meter** and **CRO/oscilloscope** (modern lab standard). The detector needs sensitivity only near the balance point — it is **never calibrated** (the null philosophy of [[Classification of Instruments]]).
- **Stray capacitance & Wagner earthing**: every arm has parasitic capacitance to ground; at audio frequency these leak currents corrupt the null. The **Wagner earth** (an auxiliary potential divider with its own balance adjustment, tying the bridge's two detector-corner impedances symmetrically to earth) removes the error without entering the main balance equations. Mention it as the standard remedy — derivation is beyond midterm scope.
- **Why bridges beat direct-reading $L/C$ meters (exam reasoning)**: accuracy lives in the **standard arms** (precision resistors and capacitors), the result is independent of source amplitude, and at balance the circuit draws no disturbing current — the null-type advantages catalogued in [[Static Characteristics of Instruments]].

---

## 4. Worked Example

> [!EXAMPLE] Problem — apply both balance conditions
> An AC bridge has $Z_1 = 1000\ \Omega$ (pure $R$), $Z_2 = 2000\ \Omega$ (pure $R$), $Z_3 = 200 + j600\ \Omega$ (a resistive–inductive arm), and the unknown in arm 4. The supply is 1 kHz. Find $R_4$ and $L_4$ for balance, and verify the phase condition explicitly.

**Step 1 — Complex balance:**
$$Z_4 = \frac{Z_2 Z_3}{Z_1} = \frac{2000}{1000}(200 + j600) = 400 + j1200\ \Omega$$

**Step 2 — Identify the unknown:** $R_4 = \boxed{400\ \Omega}$, $\omega L_4 = 1200\ \Omega$.

**Step 3 — Inductance at 1 kHz:** $\omega = 2\pi f = 6283\ \text{rad/s}$:
$$L_4 = \frac{1200}{6283} = \boxed{0.191\ \text{H}}$$

**Step 4 — Verify the phase condition:** with $\theta_1 = \theta_2 = 0$, balance demands $\theta_4 = \theta_3$:
$$\theta_3 = \tan^{-1}\frac{600}{200} = 71.57^\circ, \qquad \theta_4 = \tan^{-1}\frac{1200}{400} = 71.57^\circ \;✅$$

**Step 5 — Read the structure:** the ratio arms multiplied the whole of $Z_3$ by 2 — magnitude *and* phase scaled together, which is why the same-type rule held automatically. This is exactly the operating logic of Maxwell's inductance bridge.

## 5. Self-Test (Active Recall)

1. Write the general balance condition and the two real equations it produces. *($Z_1Z_4 = Z_2Z_3$; $\lvert Z_1\rvert\lvert Z_4\rvert = \lvert Z_2\rvert\lvert Z_3\rvert$ and $\theta_1+\theta_4 = \theta_2+\theta_3$.)*
2. Why does a single adjustable element usually leave a residual detector reading? *(One dial fixes one real condition; two are needed — magnitude and phase.)*
3. You must measure a lossy inductor using a standard capacitor. Where does the capacitor go, and why? *(Opposite the unknown (arm $Z_1$) — its negative phase cancels the unknown's positive phase.)*
4. Name three AC null detectors. *(Headphones, tuned amplifier–detector, CRO; also vibration galvanometer.)*
5. What is the Wagner earth for? *(Balancing stray capacitances to ground so leakage currents don't shift the null.)*

## 6. Related Concepts

- **Parent module**: [[00 - Measurement and Instrumentation Index]]
- The DC ancestor of the balance equation: [[DC Bridges — Measurement of Resistance]]
- The two families that implement this principle: [[Measurement of Inductance — Maxwell, Hay and Anderson Bridges]] · [[Measurement of Capacitance — De Sauty and Schering Bridges]]
- Calculator drills on every bridge: [[Bridge Numericals — All Bridges]]
- Error and detector logic: [[Errors in Measurement]] · [[Static Characteristics of Instruments]]
