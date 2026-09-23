---
title: "LVDT (Linear Variable Differential Transformer)"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - instrumentation
  - lvdt
aliases:
  - "Linear Variable Differential Transformer"
  - "LVDT Sensor"
status: completed
---

# 📏 LVDT (Linear Variable Differential Transformer)

> [!NOTE] 💡 The Big Picture Intuition
> An LVDT is a transformer that measures **position**. Picture one primary coil with two secondary coils wound on either side of it, and a movable iron slug inside. AC in the primary → flux out → EMFs in both secondaries. Now slide the core: the closer the slug is to a secondary, the more flux it funnels into *that* one. Wire the two secondaries in **series opposition** and their outputs subtract — so the net output is proportional to **how far off-centre the core is**, with the phase telling you **which side**. Position becomes voltage; direction becomes phase. No sliding contacts, no wear, essentially infinite resolution.

---

## 1. Construction

```
        ┌──────┬────────┬──────┐
        │ Sec1 │ Primary│ Sec2 │
   ═════╪══════╪════════╪══════╪═════  ← movable ferromagnetic core
        │  A   │   P    │  B   │
        └──────┴────────┴──────┘
        S1a ●─── series opposition ───● S2b  →  output e_o = e_A − e_B
```

- **One primary (P)** excited with AC (typically 50 Hz–20 kHz, 1–10 V).
- **Two identical secondaries (A, B)** placed symmetrically, connected in **series opposition**.
- **Movable soft-iron core** slides in the bore; attached to the measured object via a non-magnetic pushrod.

## 2. Working — the Three Positions

| Core position | $e_A$ vs $e_B$ | Output $e_o = e_A - e_B$ |
| :--- | :---: | :---: |
| **Centre (null)** | equal magnitude | **0 V** |
| **Right (towards B)** | $e_B > e_A$ | finite output, phase = reference (say 0°) |
| **Left (towards A)** | $e_A > e_B$ | same magnitude, **phase flipped 180°** |

> [!IMPORTANT] 🎯 The two informations in the output
> 1. **Magnitude** of $e_o$ ∝ displacement (within the linear range) → *how far*.
> 2. **Phase** relative to the primary reference → *which direction*.
> $$e_o = K \cdot x \quad \text{(linear range)}, \qquad \text{sensitivity } K \text{ in mV/mm per volt of excitation}$$

Because the secondaries oppose, the *differential* trick gives: cancellation at centre (null), linear growth on either side, and a built-in direction sign (via phase). The characteristic is V-shaped if you plot magnitude only — the two arms have opposite phase.

## 3. Advantages & Limitations

**Advantages:**
- **Frictionless & wear-free** (core doesn't touch the coils) → essentially infinite life and resolution.
- **High sensitivity and repeatability**; excellent linearity over the rated stroke.
- Low output impedance, robust, insensitive to temperature drift of the core's permeability.

**Limitations:**
- Needs **AC excitation + demodulator/phase-sensitive detector** to recover sign.
- Dynamic response limited by excitation frequency (not for very fast vibration).
- Sensitive to stray magnetic fields (needs shielding).

## 4. Applications

- Displacement / thickness gauging in machining and rolling mills.
- Load cells and pressure transducers (convert force → deflection → displacement).
- Aircraft, hydraulics and civil-engineering structural monitoring (creep/deflection).
- Servo feedback sensors for position loops.

> [!WARNING] ⚠️ Exam pointers (LVDT was flagged "importance unclear")
> The teacher said check the class/lab material — treat these as the safe core questions:
> 1. **Why series opposition?** *(To make output zero at centre and proportional to displacement, with phase giving direction.)*
> 2. **What happens at null?** *(Ideally 0 V; in practice a small residual "null voltage" from winding asymmetry.)*
> 3. **Why is resolution called "infinite"?** *(Output is continuous analogue — no contacts, no steps.)*
> 4. **How do you know direction from a magnitude meter?** *(You don't — you need a phase-sensitive detector.)*

## 5. Worked Example

> [!EXAMPLE] Problem
> An LVDT has sensitivity 2.4 mV/mm per volt of excitation and is driven with 5 V AC. The output (after demodulation) reads 60 mV. Find the displacement, and state how direction is known.

**Step 1 — Effective sensitivity:** $K = 2.4 \times 5 = 12$ mV/mm.

**Step 2 — Displacement:**
$$x = \frac{e_o}{K} = \frac{60\ \text{mV}}{12\ \text{mV/mm}} = \boxed{5\ \text{mm}}$$

**Step 3 — Direction:** the demodulated output's **phase** vs the excitation reference (in-phase → towards B, 180°-out → towards A). The magnitude alone can't tell you. ✅

## 6. Self-Test (Active Recall)

1. Sketch the coil arrangement and mark series opposition.
2. Why is the output-vs-position curve V-shaped in magnitude but linear with phase? *(Two linear arms of opposite phase meeting at null.)*
3. What limits the LVDT's usable speed? *(Excitation frequency / carrier bandwidth.)*
4. Two reasons an LVDT beats a potentiometer for displacement sensing. *(No contact/wear, higher resolution & life.)*

## 7. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- The transformer principle it exploits: [[Review of Single-Phase Transformer]]
- Differential-measurement cousins in 3-phase: [[Measurement of Power and Power Factor in Three-Phase Circuits]]
