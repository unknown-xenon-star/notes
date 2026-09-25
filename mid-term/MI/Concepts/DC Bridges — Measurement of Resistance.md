---
title: "DC Bridges — Measurement of Resistance"
date: 2026-09-25
tags:
  - concept
  - mi
  - measurement-and-instrumentation
  - dc-bridges
  - wheatstone-bridge
  - kelvin-bridge
aliases:
  - "Wheatstone Bridge"
  - "Kelvin Double Bridge"
  - "Megger"
  - "Low and High Resistance Measurement"
status: completed
---

# ⚖️ DC Bridges — Measurement of Resistance

> [!NOTE] 💡 The Big Picture Intuition
> To find an unknown resistor you could just apply a voltage, read $V$ and $I$, and divide — an **indirect, deflection-type** measurement with every error of two meters stacked on the result. A **bridge** instead plays a smarter game: put the unknown in a four-arm *balance* and adjust known resistors until a sensitive galvanometer says **zero**. At that magic point the reading no longer depends on the galvanometer's quality, the battery's exact voltage, or the observer's eye — only on the *ratios* of known arms. That is why bridges rule precision resistance measurement. The classification logic behind this trick: [[Classification of Instruments]] (null type).

---

## 1. Wheatstone Bridge — principle, derivation, limits

### 1.1 Circuit & Operation

```
        A ┌────[ P ]────┐ B
          │             │
   E(+)───┤             ├── Galvanometer (null detector)
          │             │
        D └────[ S ]────┘ C
          │             │
        [ Q ]         [ R ]
          │             │
        E(−)───────────┘
```
Four arms: **P, Q** (ratio arms), **R** (variable known), **S** (unknown). Battery across A–C; galvanometer across B–D. Adjust $R$ until $I_g = 0$.

> [!IMPORTANT] 🎯 Balance condition (derive once, reuse forever)
> At balance $V_{BD} = 0$, so the same potential difference exists across $P$ and $Q$, and across $R$ and $S$. Hence
> $$I_1P = I_2Q \quad\text{and}\quad I_1R = I_2S$$
> Dividing:
> $$\boxed{\dfrac{P}{Q} = \dfrac{R}{S}} \qquad\Longrightarrow\qquad S = R\cdot\dfrac{Q}{P}$$

### 1.2 Worked example
> [!EXAMPLE] Problem
> In a Wheatstone bridge, $P = 10\ \Omega$, $Q = 100\ \Omega$, balance occurs at $R = 47.2\ \Omega$. Find $S$.

**Step 1 — Formula:** $S = R\cdot\frac{Q}{P}$.
**Step 2 — Substitute:** $S = 47.2 \times \frac{100}{10} = \boxed{472\ \Omega}$.
**Step 3 — Comment:** the ratio arms only set the *decimal place* of the result; $R$'s accuracy sets the result's accuracy — one more reason high-quality standards go into $R$.

### 1.3 Limitations of the Wheatstone bridge
1. **Lead & contact resistance**: for **low resistances** (say below $\sim 1\ \Omega$), the resistance of connecting leads and contacts ($10^{-4}$–$10^{-3}\ \Omega$ each) becomes comparable to the unknown → large error. The bridge itself has no defence against these.
2. **Heating effect**: measuring current heats the unknown ($I^2R$), changing its value mid-measurement (especially the low-resistance arms) — keep current small/short.
3. **High resistances**: leakage currents across insulation (megaohms and above) corrupt the balance; also the galvanometer becomes insensitive. Use a **megger** instead.

> [!TIP] 🧠 The resistance-measurement map
> **Medium (1 Ω – 100 kΩ): Wheatstone bridge.** **Low (< 1 Ω): Kelvin double bridge** (4-terminal measurement). **High (> 100 kΩ): megger / loss-of-charge (insulation) methods.**

---

## 2. Kelvin Double Bridge — for LOW resistance

### 2.1 The problem it kills
When $S$ is, say, $0.1\ \Omega$, the two **leads** from the bridge to $S$ and the **contact** resistances at its terminals ($r_1, r_2$, maybe 0.0005 Ω each) inject errors of ~1% — unacceptable. The fix is to make the lead resistance *irrelevant by geometry*: use **four terminals** — two to carry current, two to sense voltage — so the drop measured contains **only the unknown's own drop**.

### 2.2 Circuit & how the second ratio rescues accuracy

```
        A ┌──[ P ]──● b ──[ Q ]──┐ B
          │         │a          │
   E(+)───┤      [r ](yoke)     ├── G (null)
          │         │c          │
        D └──[ R ]──●d ──[ S ]──┘ C
              (unknown, 4-terminal)
```
- $S$ = unknown (low), $R$ = variable standard (low), $P/Q$ = outer ratio arms, $p/q$ = **inner ratio arms** (second set — the "double"), $r$ = resistance of the **yoke link** $a$–$c$ connecting the two low-resistance arms (this includes leads + contacts the Wheatstone bridge could not hide).

> [!IMPORTANT] 🎯 Kelvin balance condition (full form)
> $$\boxed{\dfrac{R}{S} = \dfrac{P}{Q} = \dfrac{p}{q}} \qquad \text{(at balance, with } I_g = 0\text{)}$$
> The complete balance equation (before making the inner ratio match) is
> $$R = \dfrac{P}{Q}S + \dfrac{q\,r}{p + q + r}\left(\dfrac{P}{Q} - \dfrac{p}{q}\right)$$
> If the inner ratio is set **equal** to the outer ratio ($\frac{p}{q} = \frac{P}{Q}$), the *entire second term vanishes* — and with it every trace of the yoke/lead/contact resistance $r$.

> [!NOTE] Why the double ratio works (the intuition examiners love)
> The yoke drop $I_y r$ is a *nuisance voltage* sitting between the two ratio pairs. The inner arms $p, q$ **divide that nuisance voltage in the same ratio** as the outer arms divide the useful drop — so at balance the galvanometer sees equal-and-opposite copies of the error, which cancel. The error isn't eliminated by being small; it's eliminated by being **proportionally shared**. That's the "double" in double bridge.

### 2.3 Worked example
> [!EXAMPLE] Problem
> A Kelvin double bridge has $P = Q = 100\ \Omega$, inner arms $p = q = 100\ \Omega$, yoke $r = 0.002\ \Omega$, and balance at $R = 0.005\ \Omega$. Find $S$.

**Step 1 — Ratio check:** $\frac{P}{Q} = \frac{p}{q} = 1$ → the correction term vanishes identically.

**Step 2 — Balance:** $S = R\,\frac{Q}{P} = 0.005 \times \frac{100}{100} = \boxed{0.005\ \Omega}$.
(Yoke resistance $r = 0.002\ \Omega$ — which would have wrecked a Wheatstone reading — contributes **zero** error here.)

---

## 3. High Resistance Measurement — Megger / Megohmmeter

- **What it measures**: insulation resistance (megaohms–gigaohms) of cables, machine windings, transformers — a *quality-of-insulation* verdict, not a component value.
- **Principle**: apply a **high DC voltage** (500 V / 1 kV / 5 kV) and measure the tiny leakage current through the insulation; $R = \frac{V}{I_{leakage}}$.
- **Classic hand-cranked megger**: a generator + a **two-coil ohmmeter movement** (deflecting coil in series with the unknown, control coil across the generator). The two coils' opposing torques position the pointer, and — the beauty of it — **the reading is independent of the generator voltage** (both torques scale with $V$), so even a wobbling hand-crank doesn't matter.
- **Modern digital meggers**: regulated DC source + electronic current measurement; same principle, plus guard terminals to bypass **surface leakage**.
- **Why not a Wheatstone bridge?** At megaohm levels, bridge-internal insulation leakage and galvanometer insensitivity exceed the effect you're trying to measure.

> [!TIP] 🧠 Memory hooks
> - **Kelvin = "Kurrent" low**: low resistances, four terminals, double ratio.
> - **Megger = megaohm + generator**: high resistance, its own high voltage, voltage-independent reading.
> - Temperature derating of insulation readings and the 1-minute (dielectric absorption) rule belong to lab practice — quote the principle, not the standard, unless asked.

## 4. Self-Test (Active Recall)

1. State the Wheatstone balance condition and write $S$ in terms of the other arms. *($\frac{P}{Q} = \frac{R}{S}$ → $S = R\frac{Q}{P}$.)*
2. Why does a Wheatstone bridge fail below ~1 Ω? *(Lead + contact resistances become comparable to the unknown.)*
3. What geometric trick does the Kelvin bridge use on the unknown? *(Four terminals: current pair + potential pair, so measured drop excludes leads.)*
4. Write the Kelvin correction term and the condition that kills it. *($\frac{qr}{p+q+r}\left(\frac{P}{Q}-\frac{p}{q}\right)$; killed by $\frac{p}{q} = \frac{P}{Q}$.)*
5. Why is a megger reading unaffected by hand-crank speed? *(Deflecting and control coil torques both ∝ V; ratio is voltage-independent.)*

## 5. Related Concepts

- **Parent module**: [[00 - Measurement and Instrumentation Index]]
- The null philosophy this bridge embodies: [[Classification of Instruments]] · [[Static Characteristics of Instruments]]
- The AC generalization of the same balance game: [[AC Bridges — Principle and Balance Conditions]]
- Calculator drills on this bridge: [[Bridge Numericals — All Bridges]]
