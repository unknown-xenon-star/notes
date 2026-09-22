---
title: "Application of Gauss Law, Maxwell's First Equation"
date: 2026-09-22
tags:
  - concept
  - emf
  - electrostatics
  - gauss-law
  - maxwell-equations
aliases:
  - "Gauss Law"
  - "Gauss's Law"
  - "Maxwell's First Equation"
  - "Electric Flux Density"
status: completed
---

# 🧲 Application of Gauss Law & Maxwell's First Equation

> [!NOTE] 💡 The Big Picture Intuition
> Imagine the field as a **flow of invisible "fluid"** pouring out of every positive charge and draining into every negative one. Gauss's law is the bookkeeping statement for this flow: **the total outflow through any closed surface equals exactly the charge enclosed** — no more, no less. Surfaces that miss the charge balance their in-and-out flow; surfaces that enclose it count it all. The magic: choose a surface where the flow exits *uniformly and perpendicular* (a symmetry surface), and the integral collapses to simple multiplication — turning page-long integrals into one-line answers. This note covers the flux concept, the law, its point-form (Maxwell's first equation), and the classic symmetric applications.

---

## 1. Electric Flux & Flux Density

**Electric flux** $\Psi$ — the total "flow" piercing a surface, measured by counting field lines:
$$\Psi = \int_S \mathbf{D} \cdot d\mathbf{S} \qquad \text{units: coulombs (C)}$$

**Electric flux density** (displacement field):
$$\mathbf{D} = \varepsilon \mathbf{E} \qquad \text{units: C/m}^2$$

> [!TIP] 🧠 Why invent D when E exists?
> $\mathbf{E}$ depends on the medium ($\varepsilon$ changes it); $\mathbf{D}$ depends **only on the free charge** that created it. Gauss's law in $\mathbf{D}$ works identically in any dielectric — no medium bookkeeping inside the integral. The dot product $\mathbf{D}\cdot d\mathbf{S}$ counts only the component *perpendicular* to the surface — field lines skimming along a surface contribute nothing ([[Review of Vectors]], dot product = alignment).

---

## 2. Gauss's Law (Integral Form)

> [!IMPORTANT] 🎯 The Law
> $$\boxed{\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}} \qquad \text{or equivalently} \qquad \oint_S \mathbf{E} \cdot d\mathbf{S} = \frac{Q_{enc}}{\varepsilon}$$
> Total flux out of **any closed surface** = total **free charge enclosed**, regardless of where the charge sits inside or the surface's shape.

**Reading the law**:
- $Q_{enc} = 0$ → net outflow is zero (what flows in must flow out — or no field crosses at all).
- Enclose more charge → proportionally more flux. One coulomb enclosed → exactly one coulomb of flux.
- The surface ("Gaussian surface") is *imaginary* — you choose it for convenience.

> [!WARNING] ⚠️ What Gauss's law does NOT say
> It does **not** say $\mathbf{D} = 0$ outside, or that the field is zero where $Q_{enc}=0$. It only constrains the **net** flux. A dipole inside a sphere: net flux zero, but the field is strong everywhere — inflow through one hemisphere exactly cancels outflow through the other.

---

## 3. The Symmetry Method (How to Actually Use It)

> [!IMPORTANT] 🎯 The 4-Step Recipe
> 1. **Classify the symmetry** — spherical (point/sphere), cylindrical (line/coax), planar (sheet/plate).
> 2. **Choose the Gaussian surface** so that on it, $\mathbf{D}$ is (a) **constant in magnitude** and (b) **purely normal** (or zero on some faces). Constant-coordinate surfaces are the natural candidates ([[Introduction to 3D Coordinate Systems]]).
> 3. **Collapse the integral**: $\oint \mathbf{D}\cdot d\mathbf{S} = D \cdot S_{active}$ (products of constants).
> 4. **Solve** $D \cdot S_{active} = Q_{enc}$, then $\mathbf{E} = \mathbf{D}/\varepsilon$.

**The three canonical results** (derivations take 3 lines each with the recipe):

| Source | Gaussian surface | Result | Decay |
| :--- | :--- | :--- | :---: |
| Point charge / charged sphere (outside) | concentric sphere, area $4\pi r^2$ | $D = \dfrac{Q}{4\pi r^2}$, $E = \dfrac{Q}{4\pi\varepsilon r^2}$ | $1/r^2$ |
| Infinite line charge $\rho_L$ | coaxial cylinder, $S = 2\pi\rho L$ | $D = \dfrac{\rho_L}{2\pi \rho}$, $E = \dfrac{\rho_L}{2\pi\varepsilon \rho}$ | $1/\rho$ |
| Infinite sheet $\rho_S$ | pillbox crossing the sheet | $D = \dfrac{\rho_S}{2}$, $E = \dfrac{\rho_S}{2\varepsilon}$ | constant |

**Why each works**: the sphere makes $D$ uniform on the curved face ($D \cdot 4\pi r^2 = Q$); the cylinder kills the end-caps (field is radial, so $\mathbf{D}\cdot d\mathbf{S} = 0$ there) leaving only the curved wall; the pillbox has $\mathbf{D}$ normal on the two flat faces and zero through the sides, giving $2DA = \rho_S A$ — the pillbox area $A$ cancels entirely, the geometric root of the distance-independence.

**Inside a uniformly charged volume** — the enclosed charge grows with radius:
- Uniform sphere, $\rho_v$: inside ($r \le a$): $D = \dfrac{\rho_v r}{3}$ (grows linearly); outside: $D = \dfrac{\rho_v a^3}{3r^2} = \dfrac{Q}{4\pi r^2}$ (point-like).
- Infinite line within radius $\rho$ encloses $\rho_L \cdot$ length → same $1/\rho$ outside formula.

---

## 4. Maxwell's First Equation (Point / Differential Form)

Apply the **divergence theorem** ([[Concepts of Divergence]]) to the integral law:
$$\oint_S \mathbf{D}\cdot d\mathbf{S} = \int_{vol} (\nabla \cdot \mathbf{D})\, dv = \int_{vol} \rho_v\, dv$$
Since this holds for *every* volume, the integrands must match point-by-point:

> [!IMPORTANT] 🎯 Maxwell's First Equation (Gauss's law, point form)
> $$\boxed{\nabla \cdot \mathbf{D} = \rho_v} \qquad \text{or} \qquad \nabla \cdot \mathbf{E} = \frac{\rho_v}{\varepsilon}$$
> **Meaning**: charge density is the *source* of field lines — $\nabla\cdot\mathbf{D}$ measures the "outflow per unit volume" at each point; where it is positive, field lines are born; negative, they die (sinks).

**Verification by example** (line charge): $\mathbf{D} = \frac{\rho_L}{2\pi\rho}\mathbf{a}_\rho$. In cylindrical coordinates $\nabla\cdot\mathbf{D} = \frac{1}{\rho}\frac{\partial(\rho D_\rho)}{\partial \rho} = \frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\frac{\rho_L}{2\pi}\right) = 0$ for $\rho \ne 0$ ✅ — divergence-free everywhere *except* at the line itself, where all the flux is born.

---

## 5. Worked Examples

### Worked Example 1: Flux Through a Cube Face
> [!EXAMPLE] Problem
> A point charge $Q = 10$ nC sits at the centre of a cube. Find the flux through **one face**.

**Step 1: Total flux** — by Gauss's law, $\Psi_{total} = Q = 10$ nC (in $\mathbf{D}$-flux terms; equivalently $Q/\varepsilon_0$ in $\mathbf{E}$-flux terms).

**Step 2: Symmetry** — the cube has 6 identical faces and the charge sits dead centre: the flux splits equally.

**Step 3: One face**
$$\Psi_{face} = \frac{Q}{6} = \boxed{1.67 \text{ nC}}$$

**The power move**: no integration over the face was needed — only symmetry. Move the charge *off-centre* and the total stays 10 nC but the faces no longer share equally (then you'd need $\int \mathbf{E}\cdot d\mathbf{S}$ directly).

### Worked Example 2: Coaxial Cable Field
> [!EXAMPLE] Problem
> A coaxial cable's inner conductor carries line charge $\rho_L = 2\ \mu\text{C/m}$. Find $\mathbf{D}$ and $\mathbf{E}$ at $\rho = 1$ m (in the dielectric, $\varepsilon_r = 2$).

**Step 1: Gaussian surface** — coaxial cylinder of length $L$, radius $\rho = 1$ m. Enclosed charge: $Q_{enc} = \rho_L L$.

**Step 2: Collapse the integral** — field is radial; end-caps contribute nothing:
$$D \cdot (2\pi \rho L) = \rho_L L \;\Rightarrow\; D = \frac{\rho_L}{2\pi\rho}$$

**Step 3: Numbers**
$$D = \frac{2\times10^{-6}}{2\pi(1)} = 0.318\ \mu\text{C/m}^2, \qquad E = \frac{D}{\varepsilon_r\varepsilon_0} = \frac{0.318\times10^{-6}}{2(8.854\times10^{-12})} \approx \boxed{1.80\times10^4 \ \text{V/m, radial}}$$

**Check**: $\mathbf{E}$ at the same point in *free space* would be $3.595\times10^4$ V/m — the dielectric halves it ✅ (dielectrics weaken fields by $\varepsilon_r$).

### Worked Example 3: Sphere of Charge, Inside and Out
> [!EXAMPLE] Problem
> An insulating sphere ($a = 2$ cm) carries uniform $\rho_v = 1\ \mu\text{C/m}^3$. Find $\mathbf{D}$ at (a) $r = 1$ cm, (b) $r = 4$ cm.

**Step 1: Inside ($r = 1$ cm < $a$)** — enclosed charge is only the core within radius $r$:
$$Q_{enc} = \rho_v \cdot \frac{4}{3}\pi r^3 \;\Rightarrow\; D(4\pi r^2) = \rho_v \frac{4}{3}\pi r^3 \;\Rightarrow\; D = \frac{\rho_v r}{3} = \frac{(10^{-6})(0.01)}{3} = \boxed{3.33\ \text{nC/m}^2}$$

**Step 2: Outside ($r = 4$ cm > $a$)** — enclose the whole sphere:
$$Q = \rho_v \frac{4}{3}\pi a^3 = (10^{-6})\frac{4}{3}\pi(0.02)^3 = 33.5\ \text{nC}$$
$$D = \frac{Q}{4\pi r^2} = \frac{33.5\times10^{-9}}{4\pi(0.04)^2} = \boxed{1.67\ \text{nC/m}^2} \;\; (= \varepsilon_0 E \Rightarrow E \approx 188 \text{ V/m})$$

**Step 3: Behaviour check** — $D$ grows *linearly* inside ($\propto r$), decays as $1/r^2$ outside, peaks at the surface: $D(a) = \frac{\rho_v a}{3} = 6.67$ nC/m² ✅ continuity across the boundary.

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why does the pillbox area cancel?
> For the infinite sheet, show explicitly why the pillbox's area $A$ never appears in the final answer $D = \rho_S/2$.

> [!SUCCESS]- Step-by-Step Solution
> 1. Pillbox of face area $A$ straddling the sheet: flux exits **both** flat faces (symmetry sends field both ways), total $= 2DA$; sides contribute zero ($\mathbf{D} \perp d\mathbf{S}$ there).
> 2. Enclosed charge: $Q_{enc} = \rho_S A$ (the sheet patch inside the box).
> 3. Gauss: $2DA = \rho_S A \Rightarrow A$ cancels $\Rightarrow D = \rho_S/2$.
> 4. Deeper meaning: bigger box → proportionally more flux *and* more enclosed charge — the ratio is fixed by the source density alone. That scale-invariance *is* the distance-independence of the sheet's field.

---

> [!QUESTION] Practice Question: Divergence form, checked twice
> Verify $\nabla\cdot\mathbf{D} = \rho_v$ for a uniform sphere of charge, both inside ($r<a$) and outside ($r>a$).

> [!SUCCESS]- Step-by-Step Solution
> 1. Inside: $\mathbf{D} = \frac{\rho_v r}{3}\mathbf{a}_r$. In spherical coordinates $\nabla\cdot\mathbf{D} = \frac{1}{r^2}\frac{\partial(r^2 D_r)}{\partial r} = \frac{1}{r^2}\frac{\partial}{\partial r}\left(\frac{\rho_v r^3}{3}\right) = \frac{1}{r^2}\cdot\rho_v r^2 = \rho_v$ ✅
> 2. Outside: $\mathbf{D} = \frac{Q}{4\pi r^2}\mathbf{a}_r$ → $r^2 D_r = \frac{Q}{4\pi}$ = constant → $\nabla\cdot\mathbf{D} = 0$ ✅ (no charge outside).
> 3. Interpretation: divergence is nonzero *exactly where charge lives*; the outside field is divergence-free even though it's strong — pure through-flow, no sources.
> 4. The $1/r^2$ field is the unique divergence-free, curl-free radial field — which is why point-charge fields *must* have that shape.

---

## 7. Related Notes
- [[Various Charge Distribution, Coulomb's Law]] — the sources: $\rho_L$, $\rho_S$, $\rho_v$ and the prototype fields.
- [[Determination of Static Electric Fields]] — when symmetry is absent, integrate instead.
- [[Concepts of Divergence]] — the operator behind Maxwell's first equation and the divergence theorem.
- [[Electric Potential]] — the potential picture that Gauss's law complements.
- [[Boundary Relations of Electric Fields]] — what happens to $D_n$ and $E_t$ when crossing media.

