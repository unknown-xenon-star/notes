---
title: "Three-Phase Systems with Balanced and Unbalanced Load"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - three-phase
aliases:
  - "Three Phase Systems"
  - "Balanced and Unbalanced Loads"
  - "Star Delta Connection"
status: completed
---

# 🔌 Three-Phase Systems with Balanced & Unbalanced Load

> [!NOTE] 💡 The Big Picture Intuition
> A single-phase circuit is like **one person pedalling a bicycle** — power pulses to zero twice every cycle, and between the pushes the machine coasts. A three-phase system is like **three people pedalling the same wheel, arms equally spaced 120° apart**: while one is resting, the other two are pushing, so the wheel never feels a dead instant. The sum of the three pushes is a **perfectly steady total power**. This note covers why 3-phase wins, the star/delta relationships, and what happens when the three "pushes" are no longer equal (unbalanced loads).

---

## 1. Why Three Phase? (vs Single Phase)

| Aspect | Single Phase | Three Phase |
| :--- | :--- | :--- |
| Instantaneous power | Pulsates (zero twice per cycle) | **Constant**: $p(t) = P = \sqrt{3}\,V_L I_L \cos\phi$ |
| Conductor material (same power) | — | ~**25% less copper** for same voltage/power & losses |
| Rotating magnetic field | Not produced naturally | Produced naturally → self-starting motors |
| Rectified DC output | Ripples | Smoother ripple |
| Transmission efficiency | Lower | Higher for the same kW |

> [!IMPORTANT] 🎯 The Three EMFs
> A 3-phase alternator generates three EMFs of **equal magnitude**, displaced by **exactly 120°** from each other:
> $$e_R = E_m\sin\omega t, \qquad e_Y = E_m\sin(\omega t - 120°), \qquad e_B = E_m\sin(\omega t - 240°)$$
> **Fundamental identity** (holds for any balanced set):
> $$e_R + e_Y + e_B = 0 \qquad\Longleftrightarrow\qquad \mathbf{E}_R + \mathbf{E}_Y + \mathbf{E}_B = 0$$
> **Phase sequence** (R-Y-B vs R-B-Y) matters: it decides the direction of rotation of motors. Swapping **any two** supply lines reverses the sequence.

---

## 2. Star (Y) Connection

Three windings joined at a **common neutral point N**; the fourth wire (neutral) may or may not be run.

> [!IMPORTANT] 🎯 Star-Line Relationships
> $$V_L = \sqrt{3}\,V_{ph} \qquad\qquad I_L = I_{ph}$$
> Line voltage **leads** its corresponding phase voltage by **30°**.

**Derivation of $V_L = \sqrt{3}\,V_{ph}$** (phasor subtraction):
$$V_{RY} = V_R - V_Y \;\Rightarrow\; |V_{RY}| = \sqrt{V_{ph}^2 + V_{ph}^2 + 2V_{ph}^2\cos 120°} = \sqrt{2V_{ph}^2 + V_{ph}^2} = \sqrt{3}\,V_{ph}$$

- Neutral current: $\mathbf{I}_N = \mathbf{I}_R + \mathbf{I}_Y + \mathbf{I}_B$ → **zero for balanced load** (three equal phasors at 120° close on themselves).
- The neutral conductor carries the **return / unbalance** current in a 4-wire system.

## 3. Delta (Δ / Mesh) Connection

Windings connected end-to-end forming a closed ring; lines tapped at the junctions.

> [!IMPORTANT] 🎯 Delta-Line Relationships
> $$V_L = V_{ph} \qquad\qquad I_L = \sqrt{3}\,I_{ph}$$
> Line current **lags** its corresponding phase current by **30°**.

> [!TIP] 🧠 Memory hook — "√3 always links line and phase"
> In **both** connections, the √3 sits between the line and phase quantity — it attaches to the **voltage** in star and to the **current** in delta. Same √3, opposite side. And of course $\sqrt{3} = 2\sin 60°$ comes from the 120° phasor geometry, nothing exotic.

| Quantity | Star (Y) | Delta (Δ) |
| :--- | :---: | :---: |
| Voltage | $V_L = \sqrt{3}V_{ph}$ | $V_L = V_{ph}$ |
| Current | $I_L = I_{ph}$ | $I_L = \sqrt{3}I_{ph}$ |
| Power | $3V_{ph}I_{ph}\cos\phi$ | $3V_{ph}I_{ph}\cos\phi$ |
| Neutral available | Yes (4-wire) | No (3-wire) |
| Typical use | Distribution (needs neutral) | Transmission, delta motors |

**Power is identical in both**: $P = 3V_{ph}I_{ph}\cos\phi = \sqrt{3}\,V_L I_L \cos\phi$. Also $Q = \sqrt{3}\,V_L I_L\sin\phi$ and $S = \sqrt{3}\,V_L I_L$.

---

## 4. Balanced Load

> [!NOTE] Definition
> The three load impedances are **equal in magnitude and phase**: $Z_R = Z_Y = Z_B = Z\angle\phi$.
> Then each phase draws identical current magnitudes, mutually displaced 120° — a **balanced set**.

**Consequences of balance** — this is why 3-phase analysis is easy:
1. **Neutral current = 0** → in a 4-wire balanced system the neutral is idle; in a 3-wire star load the neutral point sits exactly at the supply neutral potential.
2. **Analysis collapses to one phase**: solve a *single-phase equivalent circuit* (per-phase voltage $V_{ph} = V_L/\sqrt{3}$ in star), then multiply results by 3.
3. Line voltages/currents are all equal and 120° apart; $\cos\phi$ is the same in every phase.

## 5. Unbalanced Load

> [!NOTE] Definition
> The three phase impedances are **not identical** ($Z_R \ne Z_Y \ne Z_B$ in magnitude and/or angle) — the normal condition of real distribution feeders (different single-phase homes on each phase).

### Case A — 4-wire star (neutral present)
- Each phase behaves as an **independent single-phase circuit**: phase voltages stay fixed at the supply value.
- Neutral carries the residual current:
$$\mathbf{I}_N = \mathbf{I}_R + \mathbf{I}_Y + \mathbf{I}_B \ne 0$$
- Computed by **phasor addition** (resolve into real/imaginary parts) — *not* arithmetic addition.

### Case B — 3-wire star (no neutral)
- With no return path, the load neutral point **shifts** away from the supply neutral — **neutral displacement** voltage $\mathbf{V}_{N'n}$:
$$\mathbf{V}_{N'n} = \frac{\mathbf{V}_R/Z_R + \mathbf{V}_Y/Z_Y + \mathbf{V}_B/Z_B}{1/Z_R + 1/Z_Y + 1/Z_B} \qquad \text{(Millman's theorem)}$$
- Phase voltages across the load become **unequal** even though line voltages remain balanced — some loads get over-voltage, others under-voltage. This is exactly why distribution uses **4-wire** star: the neutral pins the phase voltages.

### Analysis tools for unbalanced systems
- **Direct phasor method**: KVL/KCL loop or node equations with complex impedances.
- **Symmetrical components** (advanced): decompose into positive-, negative-, and zero-sequence sets, solve each as a balanced system, superpose.

---

## 6. Worked Examples

### Worked Example 1: Balanced Star Load
> [!EXAMPLE] Problem
> A balanced star load of $Z = 10\angle 30°\ \Omega$ per phase is fed from a 400 V (line), 3-phase, 50 Hz supply. Find phase voltage, line current, total active power, and neutral current.

**Step 1 — Phase voltage:** $V_{ph} = \dfrac{400}{\sqrt{3}} = 231$ V.

**Step 2 — Line current:** $I_L = I_{ph} = \dfrac{231}{10} = 23.1$ A.

**Step 3 — Power:**
$$P = \sqrt{3}\,V_L I_L \cos\phi = \sqrt{3}(400)(23.1)\cos 30° = \sqrt{3}(400)(23.1)(0.866) \approx \boxed{13.86\ \text{kW}}$$

**Step 4 — Neutral current:** balanced → $\boxed{I_N = 0}$ ✅

### Worked Example 2: Unbalanced 4-Wire Load — Neutral Current
> [!EXAMPLE] Problem
> 400 V, 3-phase, 4-wire, RYB sequence. Loads (resistive): $I_R = 40$ A, $I_Y = 20$ A, $I_B = 10$ A. Find the neutral current.

Take $\mathbf{I}_R = 40\angle 0°$, $\mathbf{I}_Y = 20\angle{-120°}$, $\mathbf{I}_B = 10\angle{-240°} = 10\angle{120°}$ A (resistive → currents in phase with voltages).

Real parts: $40 + 20\cos(-120°) + 10\cos(120°) = 40 - 10 - 5 = 25$
Imaginary parts: $0 + 20\sin(-120°) + 10\sin(120°) = -17.32 + 8.66 = -8.66$

$$I_N = \sqrt{25^2 + 8.66^2} = \sqrt{625 + 75} = \sqrt{700} \approx \boxed{26.5\ \text{A}}$$

> [!WARNING] ⚠️ Classic exam trap
> $I_N \ne 40 - 20 - 10 = 10$ A! Phasors at 120° **partially cancel even when all are positive** — the unbalance current is almost always *smaller* than the naive difference. Always resolve into components.

---

## 7. Self-Test (Active Recall)

1. Prove $I_L = \sqrt{3} I_{ph}$ for a balanced delta load using the phasor diagram.
2. A 3-phase motor draws 10 kW at 0.8 pf from 415 V lines. Find the line current. *(Ans: 17.4 A)*
3. Why does an unbalanced load on a 3-wire star system cause some lamps to glow brighter and others dimmer? *(Neutral displacement — load phase voltages become unequal.)*
4. Why is a 3-phase transmission line cheaper in copper than a single-phase line of equal capacity?

---

## 8. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- Power bookkeeping in these circuits: [[Measurement of Power and Power Factor in Three-Phase Circuits]]
- The single-phase building block every 3-phase machine repeats: [[Review of Single-Phase Transformer]]
- Three phases carrying unequal EMF harmonics: [[Harmonic Reduction in Phase Voltages]]
- Two-transformer 3-phase trick: [[Scott Connection]]
