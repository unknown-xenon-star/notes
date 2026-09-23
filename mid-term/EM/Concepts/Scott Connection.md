---
title: "Scott Connection"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - transformer
  - three-phase
aliases:
  - "Scott T Connection"
  - "Three Phase to Two Phase Conversion"
status: completed
---

# 🔱 Scott Connection

> [!NOTE] 💡 The Big Picture Intuition
> You have a **3-phase** supply but a customer needs **2-phase** (some old furnaces, some control systems, feeding two circuits exactly 90° apart). You could build a rotary converter — or just wire up **two ordinary single-phase transformers** cleverly. One (the **main**) connects straight across two lines. The other (the **teaser**) hangs off the *centre tap* of the main's primary and reaches up to the third line. Geometry does the rest: the teaser voltage ends up exactly **90°** out of phase with the main's. Two transformers, zero moving parts, 3φ ↔ 2φ conversion in both directions.

---

## 1. The Two Transformers

```
  Line R ──┬──────────────┬
           │              │
      MAIN transformer    │
      primary (full)      │
           │              │
  Line Y ──┴── CT ─────────┤
                          │ teaser primary (86.6% turns)
  Line B ─────────────────┘
```

- **Main transformer**: full primary winding across lines **R–Y**, with a **centre tap (CT)** at 50%. Its secondary supplies one 2-phase output ($\alpha$).
- **Teaser transformer**: primary from the main's centre tap to line **B**, with turns = **$\frac{\sqrt3}{2} = 86.6\%$** of the main's primary turns. Its secondary supplies the other 2-phase output ($\beta$).

**Why 86.6%?** The teaser sits between the centre tap and line B. The voltage from CT to B is the phase-voltage phasor $\frac{1}{2}V_{RY}$ plus... geometrically, $V_{CT\text{-}B} = \frac{\sqrt3}{2} V_{RY}$ — the *altitude* of the equilateral voltage triangle. That altitude is exactly 90° from the base $V_{RY}$. The teaser must see this voltage with full-rated volts/turn, so its turns are scaled by $\frac{\sqrt3}{2}$.

> [!IMPORTANT] 🎯 What you get
> - Two single-phase outputs of **equal voltage**, displaced exactly **90°** — a genuine 2-phase system.
> - Conversion works **both ways** (3φ → 2φ and 2φ → 3φ).
> - The three lines see a balanced load (one half of main's primary + teaser combine per line).

## 2. Voltage Relations (point form)

With line voltage $V_L$:

| Quantity | Value |
| :--- | :--- |
| Main primary voltage (R–Y) | $V_L$ |
| Teaser primary voltage (CT–B) | $\frac{\sqrt3}{2}V_L = 0.866\,V_L$ |
| Main secondary (2φ output 1) | $\frac{N_2}{N_1}V_L$ |
| Teaser secondary (2φ output 2) | $\frac{N_2}{N_1}\cdot\frac{\sqrt3}{2}V_L$ — with teaser secondary turns scaled to match, = same as main secondary |
| Phase angle between outputs | **90°** |

The teaser's *smaller* primary turns ÷ *smaller* voltage keeps volts/turn (and flux) rated — a favourite 1-marker: *"Why does the teaser have 86.6% turns?"*

## 3. Applications

- **Electric furnaces** wanting 2-phase supply.
- Interconnecting a 2-phase system with a 3-phase grid (legacy systems).
- Feeding **two single-phase loads exactly in quadrature** from a 3-phase main (e.g. some traction and control schemes).
- Conceptual role in exams: tests whether you understand phasor geometry, not memory.

> [!WARNING] ⚠️ Exam traps
> 1. The teaser winding is **86.6%**, the centre tap is **50%** — don't swap them.
> 2. The 90° shift is *inherent* (from the triangle altitude), independent of the turns ratio.
> 3. Neutrals for 4-wire 2-phase output come from **mid-taps at 25% and 75%**... i.e. the teaser secondary's centre tap and the main's centre tap provide the neutral points — mention only if asked.
> 4. This is *not* the same as open-delta (V-V): V-V gives 3φ from two transformers of a Δ bank; Scott gives 3φ↔2φ with a tapped main + teaser.

## 4. Worked Example

> [!EXAMPLE] Problem
> A Scott connection runs from an 11 kV (line), 3-phase supply. The main secondary is rated 400 V. Find (a) the voltage across the teaser primary, (b) the turns ratio of main primary : main secondary, (c) the teaser primary turns if the main primary has 2000 turns.

**Step 1 — Teaser primary voltage:**
$$V_{teaser} = \frac{\sqrt3}{2} \times 11000 = 0.866 \times 11000 = \boxed{9526\ \text{V}}$$

**Step 2 — Main volts/turn basis:** main primary sees 11 kV over $N_1 = 2000$ turns → 5.5 V/turn.

**Step 3 — Main secondary turns:** $N_2 = \dfrac{400}{5.5} = \boxed{72.7 \approx 73\ \text{turns}}$.

**Step 4 — Teaser primary turns:** teaser must see 9526 V at the same 5.5 V/turn:
$$N_{teaser} = \frac{9526}{5.5} = 1732 \text{ turns} = \frac{\sqrt3}{2} \times 2000 \;✅$$

## 5. Self-Test (Active Recall)

1. Derive the 86.6% figure from the geometry of the voltage triangle. *(Altitude of the equilateral triangle on base $V_L$: $\frac{\sqrt3}{2}V_L$.)*
2. Why must the teaser have fewer turns than the main? *(Its primary voltage is only 86.6% of $V_L$; volts/turn must stay rated → turns scale down.)*
3. Where is the centre tap of the main connected? *(To the teaser primary's lower end and it sets the 90° geometry.)*
4. State one application where 2-phase supply is genuinely needed.

## 6. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- The four standard connections it complements: [[Types of Transformer Connections]]
- Phasor skeleton used throughout: [[Three-Phase Systems with Balanced and Unbalanced Load]]
- Ratio-saving cousin: [[Autotransformer]]
