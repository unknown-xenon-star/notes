---
title: "Review of Single-Phase Transformer"
date: 2026-09-23
tags:
  - concept
  - em
  - electrical-machines
  - transformer
aliases:
  - "Single Phase Transformer"
  - "Transformer Basics"
status: completed
---

# ⚡ Review of Single-Phase Transformer

> [!NOTE] 💡 The Big Picture Intuition
> Two coils staring at each other across a laminated iron limb. Nothing touches, nothing moves — yet power flows. A changing current in coil 1 creates a **changing flux**, and a changing flux threads coil 2, inducing a voltage in it. That is the entire transformer: **conduction replaced by flux as the messenger**. Since the flux is common to both coils, whatever turns-ratio the coils have is the ratio by which voltage is transformed — and current is transformed *inversely*, so that power in ≈ power out. Before studying 3-phase connections, everything here must be automatic.

---

## 1. Construction & Principle

- **Core-type**: windings wrapped around the limbs, flux surrounds them. **Shell-type**: winding hugged on both sides by the core (better magnetic circuit, harder to repair).
- **Laminated silicon-steel core**: thin sheets insulated from each other → cuts the loop available for **eddy currents** (the exam says *don't memorize loss derivations* — just know laminations kill eddy loss, and that core loss is present whenever fluxed, load or no load).
- **Principle of operation**: apply $V_1$ → a small no-load current draws → mutual flux $\Phi$ established in the core → Faraday's law in each winding:
$$v_1 = N_1 \frac{d\Phi}{dt} \qquad v_2 = N_2 \frac{d\Phi}{dt}$$

> [!IMPORTANT] 🎯 The Instant Ratios
> $$\frac{E_2}{E_1} = \frac{N_2}{N_1} = K \qquad \text{and} \qquad \frac{I_2}{I_1} \approx \frac{N_1}{N_2} = \frac{1}{K}$$
> So a step-up transformer raises voltage $K$ times and **reduces** current $K$ times. Power in ≈ power out (minus small losses). An **ideal transformer** drops all losses and zero leakage; a **practical** one keeps the picture but adds small series and shunt imperfections.

## 2. EMF Equation (one-line derivation)

Flux $\Phi = \Phi_m \sin\omega t$; average rate of change of a sine over a quarter cycle is $4f\Phi_m$; rms is $\frac{\pi}{2\sqrt{2}} = 1.11$ times average:

$$\boxed{E = 4.44\, f\, N\, \Phi_m \ \text{volts}}$$

**Why 4.44?** Faraday gives rms EMF $= 4.44 f N \Phi_m$ because $1.11 \times 4 = 4.44$. That's it. In a transformer both windings share the *same* core flux, so the ratio $E_2/E_1 = N_2/N_1$ falls out immediately.

## 3. The Simplified Equivalent Circuit

Referred to primary — with $K = N_2/N_1$ fixed, secondary quantities get **divided by $K^2$** when brought to the primary side ($I_2' = K I_2$ is bigger, so $R_2' = R_2/K^2$ is bigger):

$$R_{eq} = R_1 + \frac{R_2}{K^2}, \qquad X_{eq} = X_1 + \frac{X_2}{K^2}$$

Then the transformer reduces to a simple series impedance $Z_{eq} = R_{eq} + jX_{eq}$ behind an ideal ratio box — and the **voltage regulation** follows:

$$\% \text{VR} = \frac{V_{no\text{-}load} - V_{full\text{-}load}}{V_{full\text{-}load}} \times 100 \approx \frac{I_2(R_{eq}\cos\phi \pm X_{eq}\sin\phi)}{V_2} \times 100 \quad (+ \text{ lag,} - \text{ lead})$$

> [!TIP] 🧠 Regulation in one sentence
> Regulation answers: *"If I hang a load on this transformer, how much does the terminal voltage sag?"* Lagging pf sags it more (the $\pm$ in the formula); leading pf can even make it **negative** (voltage *rises*). This single idea is behind half the reasoning questions.

## 4. Losses — Just the Logic (per exam scope)

> [!WARNING] ⚠️ Exam scope note
> The teacher said **detailed losses / eddy-current derivations are NOT required**. Know only:
> - **Core (iron) loss** = hysteresis + eddy; present **whenever the core is fluxed**, i.e. at *all* loads including no-load; nearly constant if $V$ and $f$ are constant.
> - **Copper loss** $= I^2R$; varies with the **square of load**.
> - **Efficiency**: $\eta = \frac{\text{output}}{\text{output} + P_{core} + P_{cu}}$; maximum when **variable copper loss = constant core loss**, and that's *all* you need to reason with.

## 5. Worked Example

> [!EXAMPLE] Problem
> A 1-phase, 50 Hz transformer has 500 turns on the primary and 100 on the secondary. Primary voltage is 2000 V. Find (a) the secondary voltage, (b) the flux in the core, (c) secondary current when the transformer supplies a 20 kW resistive load (ignore losses).

**Step 1 — Turns ratio:** $K = N_2/N_1 = 100/500 = 0.2$

**Step 2 — Secondary voltage:**
$$E_2 = K E_1 = 0.2 \times 2000 = \boxed{400\ \text{V}}$$

**Step 3 — Flux:** from $E_1 = 4.44 f N_1 \Phi_m$:
$$\Phi_m = \frac{2000}{4.44 \times 50 \times 500} = \frac{2000}{111000} = \boxed{0.018\ \text{mWb}} \ (18\ \text{mWb})$$

**Step 4 — Secondary current:** load current $I_2 = P/V_2 = 20000/400 = \boxed{50\ \text{A}}$; primary current $I_1 = I_2/K = 50/0.2 = 250$ A. Check: $2000 \times 250 \times 10^{-3} = 50$ kW? No — check properly: $V_1 I_1 = 2000 \times 50 / 0.2 = 500{,}000$ VA vs $V_2 I_2 = 400 \times 50 = 20{,}000$ W. **Trap avoided**: $I_1 = I_2/K$ is wrong when $K$ was defined as $N_2/N_1$ for a *step-down* unit; with the definition used here, $I_1 = K I_2 = 0.2 \times 50 = 10$ A. Then $V_1 I_1 = 2000 \times 10 = 20$ kVA ✓ equals $V_2 I_2 = 400 \times 50 = 20$ kVA ✓.

> [!WARNING] ⚠️ The classic slip
> Define $K$ **once** ($K = N_2/N_1 = E_2/E_1$) and stick to it: $E_2 = K E_1$, $I_2 = I_1/K$. Swapping the ratio mid-numerical is the single most common transformer mistake.

## 6. Self-Test (Active Recall)

1. A 50 Hz transformer core carries $\Phi_m = 0.02$ Wb and the primary has 300 turns. Find the primary voltage, and the secondary turns for a 440 V secondary. *(E₁ = 4.44 × 50 × 300 × 0.02 = 1332 V; N₂ = 300 × 440/1332 ≈ 99 turns.)*
2. Why is the core laminated, in one sentence? *(To break the circulating path of eddy currents induced by the changing flux.)*
3. A transformer is rated in kVA, not kW. Why? *(Losses set heating limits: core loss depends on voltage, copper loss on current — neither cares about the load's power factor, hence VA rating.)*
4. At what load does a transformer hit maximum efficiency, and why? *(When variable $I^2R$ loss equals the constant core loss — minimize the total loss fraction.)*

## 7. Related Concepts

- **Parent module**: [[00 - Electrical Machines Index]]
- These ideas, three phases wide: [[Three-Phase Systems with Balanced and Unbalanced Load]]
- The mains event: [[Types of Transformer Connections]] · [[Parallel Operation of Transformers]] · [[Autotransformer]]
- Power measured downstream: [[Measurement of Power and Power Factor in Three-Phase Circuits]]
