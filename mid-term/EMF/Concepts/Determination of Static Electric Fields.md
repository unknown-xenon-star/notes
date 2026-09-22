---
title: "Determination of Static Electric Fields"
date: 2026-09-22
tags:
  - concept
  - emf
  - electrostatics
  - electric-field
aliases:
  - "Static Electric Fields"
  - "Electric Field Intensity"
  - "Electric Field of Continuous Distributions"
status: completed
---

# 🎯 Determination of Static Electric Fields

> [!NOTE] 💡 The Big Picture Intuition
> The electric field is the **"force per unit probe charge"** at each point in space — $\mathbf{E} = \lim_{q_t \to 0} \frac{\mathbf{F}}{q_t}$ — a way of drawing the influence of charges into the space around them. Imagine every point of space holding a small arrow: the field is a complete **arrow map**. We determine this map three ways: **direct integration** (sum the $d\mathbf{E}$ from every charge element — honest but laborious), **Gauss's law** (when symmetry does the work — fast but needs the right shape), or the **potential route** (scalar integral first, differentiate after). This note is the field concept + the honest way; the shortcut lives in [[Application of Gauss Law, Maxwell's First Equation]].

---

## 1. The Field Concept — Why Bother?

Why introduce a field at all when Coulomb's law already gives forces directly? Because the field picture makes influence a **local, spatial** quantity: charge A sets up a field everywhere in space; charge B then responds only to the field **at its own location**. This action-by-proxy view is what later makes energy density, potential, boundary conditions — and eventually waves — possible.

> [!IMPORTANT] 🎯 Definition of the Electric Field Intensity
> $$\mathbf{E} = \lim_{q_t \to 0} \frac{\mathbf{F}}{q_t} \qquad \text{units: V/m} = \text{N/C}$$
> The probe charge $q_t$ must be infinitesimal so it does not disturb the source charges.

**E of a point charge** (Coulomb + the definition, the atom of all field formulas):
$$\mathbf{E} = \frac{Q}{4\pi\varepsilon_0 R^2}\,\mathbf{a}_R$$

**For a continuous distribution** (the slicing recipe of [[Various Charge Distribution, Coulomb's Law]]):
$$\mathbf{E} = \int \frac{dq}{4\pi\varepsilon_0 R^2}\,\mathbf{a}_R$$
with $\mathbf{R}$ running **from the source element $dq$ to the field point**.

---

## 2. The Three-Strategy Toolbox

| Strategy | When it works | Cost |
| :--- | :--- | :--- |
| 1. Direct integration of $d\mathbf{E}$ | any geometry | heavy — full vector integral |
| 2. Gauss's law | high symmetry (spheres, lines, planes) | one line |
| 3. Potential first, then $\mathbf{E} = -\nabla V$ | scalar integral easier than vector one | moderate |

Strategy 2 is [[Application of Gauss Law, Maxwell's First Equation]]; Strategy 3 is developed in [[Electric Potential]]. The rest of this note works Strategy 1 through its cleanest prototype — the ring.

---

## 3. Strategy 1: Direct Integration — the Ring Prototype

The **uniformly charged ring** is the classic first example: every element is equidistant from an axial point, so $R$ is constant and symmetry kills the radial components.

**Setup**: ring of radius $a$, total charge $Q$, in the $xy$-plane; field point on the axis at height $z$. Every $dq$ sits at $R = \sqrt{a^2 + z^2}$ from $P$.

- **Symmetry**: each element's $d\mathbf{E}$ has a radial part; the partner element diametrically opposite cancels it. Only the axial components $dE_z = dE\cos\alpha$ survive, with $\cos\alpha = \dfrac{z}{\sqrt{a^2+z^2}}$.
- **Constant $R$** lets it slide out of the integral:

$$E_z = \int \frac{dq}{4\pi\varepsilon_0 (a^2 + z^2)} \cdot \frac{z}{\sqrt{a^2+z^2}} = \frac{Q\,z}{4\pi\varepsilon_0 (a^2 + z^2)^{3/2}}$$

> [!IMPORTANT] 🎯 Axial Field of a Charged Ring
> $$\mathbf{E} = \frac{Q\,z}{4\pi\varepsilon_0 (a^2 + z^2)^{3/2}}\,\mathbf{a}_z, \qquad E = 0 \text{ at the centre } (z = 0)$$

**Building bigger objects from the ring**:
- **Disc** = stack of rings with $dQ = \rho_S\, 2\pi r\, dr$ → $E = \dfrac{\rho_S}{2\varepsilon_0}\left[1 - \dfrac{z}{\sqrt{z^2 + a^2}}\right]$.
- **Infinite sheet** = disc with $a \to \infty$ → $E = \dfrac{\rho_S}{2\varepsilon_0}$ (constant! — consistent with [[Various Charge Distribution, Coulomb's Law]]).

---

## 4. Worked Examples

### Worked Example 1: Point Charge Field
> [!EXAMPLE] Problem
> $Q = 8$ nC sits at the origin. Find $\mathbf{E}$ at $P(0, 0, 2)$ m.

**Step 1: Prerequisites** — $R = 2$ m, direction $\mathbf{a}_R = \mathbf{a}_z$ (point on the $+z$ axis).

**Step 2: Substitute**
$$\mathbf{E} = \frac{(8.988\times10^9)(8\times10^{-9})}{2^2}\,\mathbf{a}_z = \frac{71.9}{4}\,\mathbf{a}_z = \boxed{17.98\,\mathbf{a}_z \ \text{V/m}}$$

**Mental-math check**: $kQ = 9\times10^9 \times 8\times10^{-9} = 72$, then $72/4 = 18$ V/m ✅

### Worked Example 2: Ring Axial Field
> [!EXAMPLE] Problem
> A ring of radius $a = 5$ cm carries $Q = 2\ \mu\text{C}$ uniformly. Find $\mathbf{E}$ at $z = 12$ cm on its axis.

**Step 1: Prerequisites**
- $a^2 = 0.0025$ m², $z^2 = 0.0144$ m², $a^2 + z^2 = 0.0169$ m²
- $(a^2 + z^2)^{3/2} = (0.0169)^{1.5} = 0.0169 \times 0.13 = 0.002197$ m³

**Step 2: Substitute**
$$E = \frac{(8.988\times10^9)(2\times10^{-6})(0.12)}{0.002197} = \frac{2.157\times10^{3}}{2.197\times10^{-3}} \approx \boxed{9.82\times10^5 \ \text{V/m, along } \mathbf{a}_z}$$

**Step 3: Sanity checks**
- At $z = 0$: formula gives $E = 0$ — symmetry ✅
- At large $z$: $(a^2+z^2)^{3/2} \to z^3$, so $E \to \frac{Q}{4\pi\varepsilon_0 z^2}$ — the ring looks like a point charge ✅

### Worked Example 3: Dipole Field on the Axis
> [!EXAMPLE] Problem
> $+q$ at $z = +d/2$ and $-q$ at $z = -d/2$, with $q = 1$ nC, $d = 2$ mm. Find $\mathbf{E}$ at $r = 10$ cm on the dipole axis.

**Step 1: Dipole moment** — $p = qd = (1\times10^{-9})(2\times10^{-3}) = 2$ pC·m

**Step 2: Far-field dipole formulas** ($r \gg d$)
$$\mathbf{E}_{axis} = \frac{2p}{4\pi\varepsilon_0 r^3}\,\mathbf{a}_r \qquad \mathbf{E}_{equatorial} = -\frac{p}{4\pi\varepsilon_0 r^3}\,\mathbf{a}_r \ (\text{antiparallel to } \mathbf{p})$$

**Step 3: Numerically**
$$E = \frac{2(2\times10^{-12})(8.988\times10^9)}{(0.1)^3} = \boxed{35.95 \ \text{V/m along } \mathbf{p}}$$

> [!WARNING] ⚠️ The $1/r^3$ Decay
> A dipole's field falls as $1/r^3$ — one power faster than a single charge's $1/r^2$, because the $\pm$ charges nearly cancel at distance. Compare: a bare 1 nC at 10 cm gives 898.8 V/m, while the same charge paired with its cancel-partner gives only 35.95 V/m on the axis.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why integrate components, not magnitudes?
> For the ring's axial field we integrated the components $dE_z$, never the magnitudes $dE$. Why would integrating magnitudes be wrong?

> [!SUCCESS]- Step-by-Step Solution
> 1. $\mathbf{E}$ is a **vector**: contributions in different directions partially cancel; adding magnitudes ignores the cancellation and always overestimates.
> 2. The correct pattern: use symmetry to find which components cancel, integrate only the surviving component.
> 3. Adding magnitudes is valid only when all $d\mathbf{E}$ are parallel — e.g. axial points of a ring/disc, or a Gauss surface where $\mathbf{E}$ is everywhere normal.
> 4. Same pattern recurs in every superposition problem: see [[Various Charge Distribution, Coulomb's Law]].

---

> [!QUESTION] Practice Question: Why can't Gauss's law *always* determine E?
> Gauss's law $\oint \mathbf{D}\cdot d\mathbf{S} = Q_{enc}$ holds universally. Why can't we always solve it for $\mathbf{E}$?

> [!SUCCESS]- Step-by-Step Solution
> 1. The law constrains only the **flux integral** — i.e. the *normal* component averaged over the surface.
> 2. To pull $\mathbf{E}$ out of the integral we need it **constant in magnitude and purely normal** everywhere on the surface — a property of the geometry, not the law.
> 3. Only highly symmetric sources (sphere, infinite line, infinite plane, coaxial structures) provide such surfaces; for an arbitrary lump of charge no such surface exists.
> 4. Then Gauss gives *zero* useful information about the tangential component — that is where $\mathbf{E} = -\nabla V$ or direct integration takes over. See [[Application of Gauss Law, Maxwell's First Equation]].

---

## 6. Related Notes
- [[Various Charge Distribution, Coulomb's Law]] — slicing recipe, $dq$ elements, prototype infinite-source results.
- [[Application of Gauss Law, Maxwell's First Equation]] — the symmetry shortcut and divergence form.
- [[Electric Potential]] — the scalar-first route: compute $V$, then $\mathbf{E} = -\nabla V$.
- [[Concepts of Gradient]] — the operator that turns $V$ into $\mathbf{E}$.

