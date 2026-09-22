---
title: "Boundary Relations of Electric Fields"
date: 2026-09-22
tags:
  - concept
  - emf
  - electrostatics
  - boundary-conditions
aliases:
  - "Boundary Conditions"
  - "Boundary Conditions of Electric Fields"
  - "Dielectric Boundary Conditions"
  - "Refraction of Electric Field"
status: completed
---

# 🪟 Boundary Relations of Electric Fields

> [!NOTE] 💡 The Big Picture Intuition
> When an electric field crosses from one material into another, it behaves like **light entering water — it bends**. The rules for *how* it bends are the boundary conditions, and every one of them is just a famous law applied to a tiny box or loop straddling the interface. Two questions drive everything: **what happens to the normal component** (probe it with a pillbox → Gauss's law) and **what happens to the tangential component** (probe it with a thin rectangle → conservatism of $\mathbf{E}$). The payoff: given the field on one side of a lens, cable, or insulator joint, these rules hand you the field on the other side *without solving Maxwell's equations from scratch*.

---

## 1. The Two-Media Setup

Medium 1 ($\varepsilon_1$) meets medium 2 ($\varepsilon_2$) across a surface with unit normal $\mathbf{a}_{n12}$ pointing **from 1 into 2**. Decompose each field at the interface:

$$\mathbf{E}_1 = E_{1t}\,\mathbf{a}_t + E_{1n}\,\mathbf{a}_{n12}, \qquad \mathbf{D}_1 = \varepsilon_1 \mathbf{E}_1, \qquad \mathbf{D}_2 = \varepsilon_2 \mathbf{E}_2$$

Four components cross the boundary — two obey continuity laws, two inherit jumps.

## 2. Condition 1: The Normal Component (Gauss's Law in a Pillbox)

Draw a tiny **pillbox** (coin) straddling the boundary with face area $A$ and vanishing height. Apply Gauss's law ([[Application of Gauss Law, Maxwell's First Equation]]):

$$D_{1n}A - D_{2n}A = \rho_s A \quad\Longrightarrow\quad \mathbf{a}_{n12}\cdot(\mathbf{D}_1 - \mathbf{D}_2) = \rho_s$$

> [!IMPORTANT] 🎯 Normal Component of D
> $$D_{1n} - D_{2n} = \rho_s \qquad \text{(the jump in } D_n \text{ equals the free surface charge density)}$$

**Special cases**:
- **No free surface charge** ($\rho_s = 0$, the default between two dielectrics): $D_{1n} = D_{2n}$ → the normal $D$ is **continuous**.
- **Conductor ↔ dielectric**: inside a conductor $\mathbf{E} = \mathbf{0}$ (else charges would keep moving), so just outside $D_n = \rho_s$ — all flux terminates on surface charge.

> [!TIP] 🧠 Why $E_n$ jumps even when $D_n$ doesn't
> With $\rho_s = 0$: $D_{1n} = D_{2n}$, but $\mathbf{E} = \mathbf{D}/\varepsilon$ and $\varepsilon$ changes across the boundary! So
> $$E_{2n} = \frac{\varepsilon_1}{\varepsilon_2}E_{1n}$$
> The field's normal component jumps **inversely with permittivity** — a high-$\varepsilon$ medium carries the same $D$ with a smaller $E$ (it "absorbs the strain").

## 3. Condition 2: The Tangential Component (Conservative E in a Loop)

Draw a tiny **rectangle** straddling the boundary, length $\Delta w$ along the surface, height → 0. Electrostatic $\mathbf{E}$ is conservative ($\oint \mathbf{E}\cdot d\mathbf{l} = 0$, [[Electric Potential]]):

$$E_{1t}\Delta w - E_{2t}\Delta w = 0 \quad\Longrightarrow\quad E_{1t} = E_{2t}$$

> [!IMPORTANT] 🎯 Tangential Component of E
> $$E_{1t} = E_{2t} \qquad \text{(tangential E is ALWAYS continuous)}$$

**Why always**: the vanishing loop encloses zero area and zero charge — nothing in electrostatics can make $\oint\mathbf{E}\cdot d\mathbf{l}$ nonzero across it. (In magnetics, the twin law $\oint\mathbf{H}\cdot d\mathbf{l}$ *does* pick up current, giving $H_t$ jumps — later in the course.)

**Conductor special case**: tangential $\mathbf{E}$ on a conductor surface must be $0$ (else surface charges would slide along it). So field lines meet **all conductor surfaces at 90°**.

## 4. Refraction of Field Lines: the $1/\varepsilon$ Law of Sines

Combine both conditions ($\rho_s = 0$):
$$\tan\theta_1 = \frac{E_{1t}}{E_{1n}} = \frac{E_{2t}}{D_n/\varepsilon_1}, \qquad \tan\theta_2 = \frac{E_{2t}}{E_{2n}} = \frac{E_{1t}}{D_n/\varepsilon_2}$$

Dividing one by the other:

> [!IMPORTANT] 🎯 Law of Refraction for Field Lines
> $$\frac{\tan\theta_2}{\tan\theta_1} = \frac{\varepsilon_2}{\varepsilon_1}$$
> where $\theta_i$ is measured **from the normal**. A field line entering a higher-$\varepsilon$ medium bends **away from the normal**; entering lower-$\varepsilon$ bends toward it — the **opposite** of light refraction, because $\varepsilon$ plays the role of $1/n$.

## 5. Worked Example: Dielectric Interface Field Refraction

> [!EXAMPLE] Problem
> Medium 1 ($\varepsilon_{r1} = 2$) has $\mathbf{E}_1 = 3\mathbf{a}_x + 4\mathbf{a}_y + 5\mathbf{a}_z$ V/m at a boundary whose normal is $\mathbf{a}_z$ (pointing from medium 1 into medium 2, $\varepsilon_{r2} = 5$). No free surface charge. Find $\mathbf{E}_2$ and the refraction angles.

**Step 1: Split E₁ into normal/tangential** — normal direction is $\mathbf{a}_z$:
$$E_{1n} = 5, \qquad \mathbf{E}_{1t} = 3\mathbf{a}_x + 4\mathbf{a}_y \quad (|\mathbf{E}_{1t}| = 5)$$

**Step 2: Tangential continuity** — $\mathbf{E}_{2t} = \mathbf{E}_{1t} = 3\mathbf{a}_x + 4\mathbf{a}_y$

**Step 3: Normal continuity of D** — $D_{1n} = \varepsilon_0(2)(5) = 10\varepsilon_0$; continuity: $\varepsilon_0(5)\,E_{2n} = 10\varepsilon_0 \Rightarrow E_{2n} = 2$ V/m

**Step 4: Reassemble**
$$\boxed{\mathbf{E}_2 = 3\mathbf{a}_x + 4\mathbf{a}_y + 2\mathbf{a}_z \ \text{V/m}}$$

**Step 5: Refraction check** — $\tan\theta_1 = \frac{E_{1t}}{E_{1n}} = \frac{5}{5} = 1 \Rightarrow \theta_1 = 45°$; $\tan\theta_2 = \frac{5}{2} = 2.5 \Rightarrow \theta_2 = 68.2°$
$$\frac{\tan\theta_2}{\tan\theta_1} = \frac{2.5}{1} = \frac{\varepsilon_{r2}}{\varepsilon_{r1}} = \frac{5}{2} ✅$$

**Step 6: Magnitudes** — $|\mathbf{E}_1| = \sqrt{9+16+25} = \sqrt{50} = 7.071$ V/m; $|\mathbf{E}_2| = \sqrt{9+16+4} = \sqrt{29} = 5.385$ V/m. The field weakens inside the higher-$\varepsilon$ medium (same $D_n$, bigger $\varepsilon$).

**Step 7: D continuity check** — $D_{1n} = (8.854\times10^{-12})(2)(5) = 88.5$ pC/m²; $D_{2n} = (8.854\times10^{-12})(5)(2) = 88.5$ pC/m² ✅

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Which components jump, and why?
> At a charge-free dielectric interface: $E_t$ continuous, $D_n$ continuous — but $E_n$ and $D_t$ generally *jump*. Why this asymmetric pair?

> [!SUCCESS]- Step-by-Step Solution
> 1. $E_t$: from $\oint\mathbf{E}\cdot d\mathbf{l} = 0$ around a vanishing loop — no electrostatic mechanism can support a tangential-E jump.
> 2. $D_n$: from $\oint\mathbf{D}\cdot d\mathbf{S} = Q_{enc}$ on a vanishing pillbox — no free charge → no $D_n$ jump.
> 3. The other two have no protecting law: $E_n = D_n/\varepsilon$ jumps because $\varepsilon$ changes step-wise; $D_t = \varepsilon E_t$ jumps because $\varepsilon$ multiplies the continuous $E_t$.
> 4. Memory hook: **"E-tangent, D-normal"** are the protected components; their partners inherit the permittivity jump.

---

> [!QUESTION] Practice Question: Conductor boundary values
> A conductor surface in air carries free surface charge $\rho_s = 20$ nC/m². What is $\mathbf{E}$ just outside, and why must it be perpendicular?

> [!SUCCESS]- Step-by-Step Solution
> 1. Pillbox on the conductor surface: inside $\mathbf{E} = \mathbf{0}$ → only the outer face carries flux → $D_{n} = \rho_s$ → $E = \rho_s/\varepsilon_0 = \frac{20\times10^{-9}}{8.854\times10^{-12}} \approx 2259$ V/m.
> 2. Perpendicularity: if $E_t \ne 0$, surface charges would experience a tangential force and move — contradicting statics. So $\mathbf{E}$ is normal, magnitude $\rho_s/\varepsilon_0$.
> 3. The field just outside depends only on the **local** $\rho_s$ — a strikingly local result, and the basis of capacitor-plate field calculations.
> 4. Note: treat conductors through their own condition ($\mathbf{E}_{inside} = \mathbf{0}$), not as "infinite permittivity" dielectrics.

---

## 7. Related Notes
- [[Application of Gauss Law, Maxwell's First Equation]] — source of the pillbox (normal-D) condition.
- [[Electric Potential]] — source of the loop (tangential-E) condition; $V$ continuous across all boundaries.
- [[Concepts of Gradient]] — why conductor surfaces (equipotentials) must have perpendicular field lines.
- [[Various Charge Distribution, Coulomb's Law]] — surface charge $\rho_s$ in the pillbox.

