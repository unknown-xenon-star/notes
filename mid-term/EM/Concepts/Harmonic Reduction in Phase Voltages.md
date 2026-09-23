---
title: "Harmonic Reduction in Phase Voltages"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - transformer
  - harmonics
aliases:
  - "Third Harmonic Reduction"
  - "Triplen Harmonics Transformer"
  - "Harmonics in Three Phase Transformers"
status: completed
---

# 🌊 Harmonic Reduction in Phase Voltages

> [!NOTE] 💡 The Big Picture Intuition
> Iron loves to saturate. To force a *sinusoidal flux* through a saturating core, the magnetizing current cannot be a clean sine — it must be **flat-topped**, rich in **third harmonics**. Now the trap: in a *balanced three-phase set, all three third-harmonic currents are **in phase*** (three times the frequency means 3 × 120° = 360° = 0° shift). So the three phases *cannot cancel each other* and the third harmonic needs its own path home. Whether that path exists is decided entirely by **which connection you chose** — delta or star, grounded or not. This single idea explains the Yy noise problem, the delta's magic loop, and half the vector-group reasoning questions in the exam.

---

## 1. Where the Harmonics Come From

- $B$–$H$ curve is non-linear near saturation → for sinusoidal flux $\Phi$, the magnetizing current $i_m$ is **peaky / flat-topped**:
$$i_m(t) = I_{1}\sin\omega t + I_{3}\sin 3\omega t + I_{5}\sin 5\omega t + \dots$$
- Odd harmonics dominate; the **3rd is the biggest troublemaker**.
- Triplen set (3rd, 9th, 15th…): **zero-sequence** — all three phases *in phase* with each other (no 120° mutual cancellation).

> [!IMPORTANT] 🎯 The phase-math behind "triplen = in phase"
> Fundamental of phase Y lags R by 120°. But the 3rd harmonic of Y is at frequency $3\omega$, so its shift is $3 \times 120° = 360° \equiv 0°$. Same for B. **All three 3rd-harmonic waves are copies of each other** — that's why they behave like a single-phase signal riding on the 3-phase system and demand a *return path*.

## 2. Connection-by-Connection Consequences

| Connection | Triplen current path? | Result |
| :--- | :---: | :--- |
| **Delta (closed)** | Circulates **inside the delta loop** | Flux & EMF stay sinusoidal; extra heating only. The delta is a "harmonic cemetery". |
| **Star–Star, isolated neutral (3-wire)** | **None** | $i_m$ forced sinusoidal → flux **flat-topped** → phase EMFs carry large **3rd-harmonic spikes** ($e_3$ adds to each phase voltage). |
| **Star–Star, 4-wire (neutral grounded)** | Via neutral (zero-sequence flows line–neutral) | Harmonic currents return through the neutral → phase voltages clean; neutral carries triplen current. |
| **Star–Delta** | Delta side (if closed and circulating enabled) | Clean voltages; the delta absorbs the triplen demand regardless of which side is excited. |

**Line vs phase voltages in Yy (3-wire)**: the third-harmonic components of the three *line* voltages cancel in pairs (line voltage = difference of two in-phase triplens = zero!) — so **line voltages stay clean while phase voltages are distorted**. A beautiful exam question.

## 3. How the Harmonics Are Reduced (the fixes)

1. **Closed delta anywhere in the bank** — cheapest and most effective: gives triplen currents a local loop so flux remains sinusoidal.
2. **Grounded neutral (4-wire star)** — supplies a zero-sequence return path.
3. **Core construction**: **three-phase, three-limb cores** naturally *suppress* triplen flux — the triplen fluxes of the three limbs are in phase and must return through **air** (huge reluctance) → triplen flux is small to begin with. *(Three single-phase banks have independent iron paths → full-strength triplen trouble.)*
4. **Slightly over-rated design / derating** of Yy banks without delta tertiary.

> [!TIP] 🧠 One-line reasoning answers
> - *"Why does a delta connection reduce harmonics?"* → Triplen EMFs around the closed loop are **in phase and add arithmetically**, driving a circulating current that cancels the harmonic flux.
> - *"Why is Yy rarely used at high power?"* → No triplen path → distorted phase EMFs + neutral-shift on unbalance.
> - *"Why do line voltages show no 3rd harmonic even when phase voltages do?"* → $v_{RY,3} = v_{R,3} - v_{Y,3} = 0$ because the triplens are in phase.
> - *"Why do 3-limb cores reduce triplen flux?"* → In-phase triplen flux cannot use another limb as return; air path reluctance is enormous.

## 4. Worked Example

> [!EXAMPLE] Problem
> The phase voltage of a Yy (isolated neutral) transformer bank is measured as
> $$v_{ph}(t) = 230\sqrt2 \sin\omega t + 30\sqrt2 \sin 3\omega t \ \text{V}.$$
> Find (a) the rms phase voltage, (b) the rms line voltage, (c) the 3rd-harmonic content of the line voltage.

**Step 1 — Phase voltage rms** (harmonics add as root-sum-of-squares):
$$V_{ph} = \sqrt{230^2 + 30^2} = \sqrt{52900 + 900} = \sqrt{53800} = \boxed{231.9\ \text{V}}$$

**Step 2 — Line voltage:** fundamentals combine as $\sqrt3 \times 230 = 398.4$ V; the third-harmonic line component is **zero** (in-phase cancellation):
$$V_L = \sqrt{(\sqrt3 \times 230)^2 + 0^2} = \boxed{398.4\ \text{V}}$$

**Step 3 — 3rd-harmonic content of line voltage:** $\boxed{0}$ — all the distortion is trapped inside the phase quantities. (Rms meters on lines show a healthy system while insulation on phases still cops the spikes.)

## 5. Self-Test (Active Recall)

1. Why are triplen harmonics "zero-sequence"? *(3 × 120° = 360° → all three in phase.)*
2. Why does the delta loop heat up when it "absorbs" harmonics? *(Triplen EMFs add arithmetically around the loop; loop impedance is small → large circulating current, real $I^2R$ loss.)*
3. Why are three separate single-phase transformers worse than one 3-limb core for Yy? *(Independent iron triplen paths vs air-return suppression.)*
4. A star bank shows 5% third harmonic in phase voltage but clean line voltage. Explain in one line.

## 6. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- The connections that decide the harmonic story: [[Types of Transformer Connections]]
- Neutral behaviour with unbalance: [[Three-Phase Systems with Balanced and Unbalanced Load]]
- Magnetizing-current origin: [[Review of Single-Phase Transformer]]
