---
title: "Types of Transformer Connections"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - transformer
  - three-phase
aliases:
  - "Transformer Connections"
  - "Star Delta Transformer"
  - "Delta Star Connection"
  - "Three Phase Transformer Connections"
  - "Yy, Yd, Dy, Dd Connections"
status: completed
---

# 🔀 Types of Transformer Connections

> [!NOTE] 💡 The Big Picture Intuition
> Take three identical single-phase transformers — one per phase — and you have a 3-phase bank. But *how* you join their six winding-ends decides everything: the voltage ratio, the phase shift, whether you get a neutral, and even whether the bank can run at all (third harmonics!). The four standard connections are just the four ways to pair up {star, delta} on the primary with {star, delta} on the secondary. **This is the highest-priority exam topic**: for each connection know the chain
> $$\text{Connection} \rightarrow \text{voltage/current relation} \rightarrow \text{phase shift} \rightarrow \text{phasor diagram} \rightarrow \text{application} \rightarrow \text{why/when used}$$
> The teacher's warning applies doubly here: **don't memorize the table — derive every cell from the phasor diagram.**

---

## 1. The One Skill Behind Everything: Phasor Subtraction

Every connection analysis reduces to one operation. In star, the line voltage is the **difference of two phase voltages** 120° apart:

$$V_{RY} = \mathbf{V}_R - \mathbf{V}_Y \quad\Rightarrow\quad |V_{RY}| = \sqrt{V_{ph}^2 + V_{ph}^2 - 2V_{ph}^2\cos 120°} = \sqrt{3}\,V_{ph}$$

and the resultant bisects the 120° angle, so $V_{RY}$ **leads $V_R$ by 30°**. In delta, the line current is the same geometry with currents: $I_L = \sqrt{3}\,I_{ph}$, line current **lags** its phase current by 30°. If you can draw *this* one diagram, you can generate every cell of the summary table below on demand.

> [!TIP] 🧠 How to draw any connection phasor diagram (exam recipe)
> 1. Draw the three **phase** phasors $V_R, V_Y, V_B$ at 120° (this is your fixed background — it never changes).
> 2. Delta secondary: each *winding voltage* is a phase voltage of the secondary set — place them on the same 120° skeleton.
> 3. Obtain **line** quantities by subtraction ($V_{RY} = V_R - V_Y$); mark the 30° shift explicitly.
> 4. Label which winding sits between which lines — the phase shift follows automatically.

## 2. The Master Summary Table

| Connection | Primary : Secondary voltage | Phase shift (LV vs HV) | Neutral? | Common applications |
| :--- | :--- | :---: | :---: | :--- |
| **Star–Star (Yy)** | $V_{ph}$ to $V_{ph}$ each side; overall $V_{L1}:V_{L2} = N_1:N_2$ | 0° | Both sides | Small HV alternator step-up, distribution where unbalance is mild |
| **Delta–Delta (Dd)** | $V_{L1}:V_{L2} = N_1:N_2$ | 0° | None | Low-voltage heavy loads, balanced industrial; one winding can go open (V-V) |
| **Delta–Star (Dy)** | steps **up**: $V_{L2} = \sqrt{3}\,V_{ph2}$ | **−30°** (LV lags HV by 30°) | LV side | **Step-up at generating stations** — star LV... *(see §5 — star goes on the side that needs neutral or insulation economy)* |
| **Star–Delta (Yd)** | steps **down**: $V_{L2} = V_{L1}/\sqrt{3}\cdot(N_2/N_1)$ | **+30°** (LV leads HV by 30°) | HV side | **Step-down at receiving/distribution end**; HV winding needs fewer insulation |

Where "±30°" appears, remember **Yd and Dy both shift by 30°, in opposite senses**; Yy and Dd shift by 0°. That single fact answers a pile of GATE-style 1-markers.

## 3. Star–Star (Yy)

- Both windings in star: per-phase quantities transform directly, $V_{L2}/V_{L1} = N_2/N_1$.
- **Advantage**: phase voltage is only $V_L/\sqrt{3}$ per winding → **less insulation per winding** → cheap at high voltage. Neutral available on both sides.
- **Problems (the reasoning questions live here):**
  1. **Third-harmonic trouble**: the magnetizing current is flat-topped (needs 3rd harmonic to make sinusoidal flux); in an ungrounded star there is **no path for triplen currents** → flux becomes flat-topped → EMFs carry 3rd-harmonic spikes. With a 4-wire system (neutral available), triplen currents flow in the neutral and the problem subsides.
  2. **Unbalanced load with isolated neutral → neutral shifting** → some phases over-volted (see [[Three-Phase Systems with Balanced and Unbalanced Load]], Case B).
- **Used when**: insulation cost dominates, load is nearly balanced, and a neutral exists.

## 4. Delta–Delta (Dd)

- $V_L = V_{ph}$ on both sides; ratio unchanged, no phase shift.
- **Advantages**: third-harmonic currents circulate *inside* the closed delta (harmless heating, clean output voltage); no neutral needed; **robust to unbalance**.
- **V-V (open-delta) property**: remove one winding and the bank still supplies 3-phase power at
$$\frac{S_{V\text{-}V}}{S_{\Delta\text{-}\Delta}} = \frac{\sqrt{3}\,V_L I_L}{3\,V_L I_{ph}} = \frac{1}{\sqrt{3}} = 57.7\%$$
  of full capacity while the copper installed is $\frac{2}{3} = 66.7\%$ → **utility factor 86.6%**.
- **Used when**: voltages are moderate, load is balanced, reliability matters (bank degrades gracefully).

## 5. Delta–Star (Dy) — the step-up connection

- Delta primary (clean flux, no triplen issue, suits unbalanced primary grid), star secondary → secondary line voltage $\sqrt{3}$ times its phase voltage → **net step-up of $\sqrt{3}$ beyond the turns ratio**.
- **Phase shift**: LV (star) side lags HV by **30°** (Dy1/Dy11 groups).
- **Used at generating stations** to step up alternator voltage for transmission: alternator prefers star (neutral for ground fault protection), transformer takes star on the HV side for insulation economy — wait, in Dy the *star is the secondary/HV side*, which is exactly the insulation-economy side. That's the "why".
- Also gives a **4-wire distribution secondary** when star is on the LV side (Dy11 is the common distribution vector group).

## 6. Star–Delta (Yd) — the step-down connection

- Star HV primary (fewer volts per winding → cheaper insulation at transmission voltage), delta LV secondary → **net step-down of $\sqrt{3}$ beyond the turns ratio**.
- **Phase shift**: LV (delta) side **leads** HV by **30°** (Yd1/Yd11).
- **Used at receiving stations / bulk substations**, and for **delta-connected motor loads**.
- Reasoning favourite: *why is Yd preferred over Yy for step-down?* → closed delta kills 3rd harmonics, tolerates unbalance, and reduces the secondary line voltage by $\sqrt3$ (fewer turns, cheaper LV winding).

> [!WARNING] ⚠️ Exam traps for connections
> 1. **±30° direction confusion**: fix one convention (HV phasor at 12 o'clock, read LV hour hand — vector-group clock notation: Dy11 = LV at 11 o'clock = LV leads HV by 30°).
> 2. "$\sqrt{3}$ extra ratio" applies only to **mixed** connections: Dy steps *up* by $\sqrt3$, Yd steps *down* by $\sqrt3$, beyond $N_2/N_1$.
> 3. **Parallel operation constraint**: a Yy bank and a Dy bank **cannot be paralleled** — 30° phase difference between secondaries drives circulating current even at no-load.
> 4. Triplen harmonics need a **closed delta or grounded neutral path** — that's the whole harmonics story of Yy.

## 7. Worked Examples

### Worked Example 1: Yd step-down numerical
> [!EXAMPLE] Problem
> A 3-phase, 6600/400 V, 50 Hz supply transformer is Yd connected. Find the primary and secondary phase (winding) voltages, and the turns ratio per winding.

**Step 1 — Primary (star):** $V_{ph1} = \dfrac{6600}{\sqrt{3}} = 3810$ V.

**Step 2 — Secondary (delta):** $V_{ph2} = V_{L2} = 400$ V.

**Step 3 — Winding turns ratio:** $\dfrac{N_1}{N_2} = \dfrac{3810}{400} = \boxed{9.53 : 1}$

Note the line ratio is 6600/400 = 16.5, but the *winding* ratio is only 9.53 — the $\sqrt3$ again.

### Worked Example 2: Dy11 — where does the 30° come from?
> [!EXAMPLE] Problem
> Show numerically that a Dy bank's LV line voltage lags the HV line voltage by 30° (Dy1 group), taking HV $V_{RY} = 1\angle 0°$.

**Step 1 — HV phase voltages (star):** $V_{RN} = \frac{1}{\sqrt3}\angle{-30°}$ (line leads phase by 30°).

**Step 2 — LV winding voltages (delta):** each equals its LV phase voltage, magnitude $\frac{1}{\sqrt3}\cdot\frac{N_2}{N_1}\cdot\sqrt3 = \frac{N_2}{N_1}$ per-unit of HV line... with $N_1 = N_2$, LV winding = $\frac{1}{\sqrt3}$ pu at angles $0°, -120°, +120°$ (same as HV *line* directions by delta loop closure).

**Step 3 — LV line voltages:** $V_{ry} = V_{rn} - V_{yn}$ → magnitude $\sqrt3 \cdot \frac{1}{\sqrt3} = 1$ pu, angle $-30°$.

**Step 4 — Compare:** HV $1\angle 0°$, LV $1\angle{-30°}$ → LV lags HV by $30°$ → **Dy1** ✅ (Reverse the connection order for Dy11 and the LV leads by 30°.)

## 8. Self-Test (Active Recall)

1. Why does a Yy connection suffer third-harmonic voltage trouble while Dd does not? *(No triplen current path in isolated star; closed delta circulates them internally.)*
2. A Yd transformer steps 33 kV down to 3.3 kV line. What is the per-winding ratio? *(Primary ph = 33/√3 = 19.05 kV; ratio 19.05/3.3 = 5.77.)*
3. Two transformers, one Dy11 and one Yy0, same voltage ratio — can they share a load? *(No — 30° phase shift → large circulating current.)*
4. What fraction of Δ–Δ capacity does an open-delta bank deliver, and what fraction of copper does it use? *(57.7% capacity, 66.7% copper → 86.6% utility.)*

## 9. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- Foundations underneath: [[Review of Single-Phase Transformer]] · [[Three-Phase Systems with Balanced and Unbalanced Load]]
- The two-transformer special case: [[Scott Connection]]
- Harmonics behind the Yy problem: [[Harmonic Reduction in Phase Voltages]]
- Sharing load between banks: [[Parallel Operation of Transformers]]
- Measuring the resulting power: [[Measurement of Power and Power Factor in Three-Phase Circuits]]
