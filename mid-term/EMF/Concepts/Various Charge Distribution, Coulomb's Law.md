---
title: "Various Charge Distributions & Coulomb's Law"
date: 2026-09-22
tags:
  - concept
  - emf
  - electrostatics
  - coulombs-law
aliases:
  - "Coulomb's Law"
  - "Charge Distributions"
  - "Electric Charge"
  - "Coulomb Force"
status: completed
---

# ⚡ Charge Distributions & Coulomb's Law

> [!NOTE] 💡 The Big Picture Intuition
> Electromagnetics begins with the simplest question possible: **two charges, at rest — what force do they feel?** Coulomb's answer (1785, from a torsion-balance experiment) is the electrical twin of Newton's gravity: an inverse-square attraction/repulsion along the line joining them. But real objects don't carry single "point" charges — a wire is charge smeared along a *line*, a plate is charge spread over a *surface*, a charged cloud is charge filling a *volume*. The whole craft of this chapter is learning to **slice these continuous distributions into infinitesimal point charges $dq$** and integrate Coulomb's law over them. Master the slicing, and every field formula later ([[Determination of Static Electric Fields]], [[Application of Gauss Law, Maxwell's First Equation]]) becomes a special case.

---

## 1. Electric Charge — The Cast of Characters

- Charge is **bipolar**: positive (protons) and negative (electrons). Like charges repel, unlike attract.
- Charge is **quantized**: it comes in packets of $e = 1.602 \times 10^{-19}$ C — the smallest free charge.
- Charge is **conserved**: the algebraic total in an isolated system never changes.
- In electrostatics, charge is **at rest** in our reference frame — no currents, no magnetic effects yet.

## 2. The Four Charge Distributions

| Distribution | Symbol | Unit | Definition | Example |
| :--- | :--- | :--- | :--- | :--- |
| Point charge | $Q$ | C | charge at a single location | electron, charged ball (far away) |
| Line charge | $\rho_L$ | C/m | $dq = \rho_L\, dl$ | charged wire, beam of ions |
| Surface charge | $\rho_S$ | C/m² | $dq = \rho_S\, dS$ | charged sheet, conductor surface |
| Volume charge | $\rho_v$ | C/m³ | $dq = \rho_v\, dv$ | charged cloud, doped semiconductor |

> [!TIP] 🧠 The Slicing Recipe (works every time)
> 1. Choose the distribution's natural coordinate ([[Introduction to 3D Coordinate Systems]]).
> 2. Cut out one element: $dq = \rho_L\,dl$ or $\rho_S\,dS$ or $\rho_v\,dv$.
> 3. Write Coulomb's contribution $d\mathbf{E}$ (or $d\mathbf{F}$) using the distance vector $\mathbf{R}$ **from the element to the field point**.
> 4. Exploit symmetry: by the time you integrate, most components cancel — keep only the surviving one.

## 3. Coulomb's Law

> [!IMPORTANT] 🎯 The Force Between Two Point Charges
> $$\mathbf{F}_{21} = \frac{Q_1 Q_2}{4\pi\varepsilon_0 R^2}\,\mathbf{a}_{21} = \frac{k\, Q_1 Q_2}{R^2}\,\mathbf{a}_{21} \qquad \text{(in free space)}$$
> where $R = |\mathbf{r}_2 - \mathbf{r}_1|$, $\mathbf{a}_{21}$ points **from $Q_1$ toward $Q_2$**, and
> $$\varepsilon_0 \approx \frac{10^{-9}}{36\pi} \approx 8.854 \times 10^{-12} \text{ F/m}, \qquad k = \frac{1}{4\pi\varepsilon_0} \approx 8.988 \times 10^9 \ \frac{\text{N·m}^2}{\text{C}^2}$$

- Like signs → $Q_1Q_2 > 0$ → force along $\mathbf{a}_{21}$ (repulsion); unlike signs → the minus sign pulls $Q_2$ back toward $Q_1$ (attraction). The formula handles both automatically — no case-splitting.
- **Inverse-square**: doubling the separation quarter-strengthens the force.
- In a dielectric medium of permittivity $\varepsilon = \varepsilon_r \varepsilon_0$, replace $\varepsilon_0 \to \varepsilon$: the force weakens by the factor $\varepsilon_r$.
- **Superposition**: with many charges, forces add vectorially — $\mathbf{F} = \sum_i \frac{Q Q_i}{4\pi\varepsilon_0 R_i^2}\mathbf{a}_i$. No cross-terms, no interference: electrostatics is linear.

> [!WARNING] ⚠️ The Distance-Vector Trap
> $\mathbf{a}_{21}$ must point **from the source to the point where the force is felt**. Writing $\mathbf{R} = \mathbf{r}_1 - \mathbf{r}_2$ instead of $\mathbf{r}_2 - \mathbf{r}_1$ flips every component — the #1 sign error in exams. ([[Review of Vectors]], the distance-vector rule.)

---

## 4. Worked Examples

### Worked Example 1: Direct Coulomb Force
> [!EXAMPLE] Problem
> $Q_1 = 1\ \mu\text{C}$ and $Q_2 = 2\ \mu\text{C}$ sit $50$ cm apart in free space. Find the force on $Q_2$.

**Step 1: Prerequisites** — $Q_1 Q_2 = (1\times10^{-6})(2\times10^{-6}) = 2\times10^{-12}$ C², $R = 0.5$ m.

**Step 2: Substitute**
$$F = \frac{(8.988\times10^9)(2\times10^{-12})}{(0.5)^2} = \frac{1.798\times10^{-2}}{0.25} = 7.19\times10^{-2} \text{ N}$$

**Step 3: Direction & check** — both charges positive → repulsion; $\mathbf{a}_{21}$ points away from $Q_1$.
$$\boxed{\mathbf{F} \approx 71.9 \text{ mN directed away from } Q_1}$$

**Sanity check (calculator-friendly)**: $\frac{1}{4\pi\varepsilon_0} \approx 9\times10^9$, so the mental estimate is $\frac{9 \times 2 \times 10^{-3}}{0.25} = 72$ mN ✅

### Worked Example 2: Superposition in an Equilateral Triangle
> [!EXAMPLE] Problem
> Three identical charges $Q = 2\ \mu\text{C}$ sit at the corners of an equilateral triangle of side $10$ cm. Find the net force on any one of them.

**Step 1: Pairwise forces** — each neighbour exerts
$$F_1 = F_2 = \frac{(8.988\times10^9)(2\times10^{-6})^2}{(0.1)^2} = \frac{3.595\times10^{-2}}{0.01} \approx 3.595 \text{ N}$$

**Step 2: Geometry** — the two forces act along the two sides meeting at the charge, i.e. at $60°$ to each other.

**Step 3: Vector sum** (parallelogram law, [[Review of Vectors]])
$$F_{net} = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos 60°} = F_1\sqrt{2 + 1} = \sqrt{3}\,(3.595) \approx \boxed{6.23 \text{ N, directed away from the triangle's centre}}$$

**Why**: for equal forces the resultant always lies on the angle bisector; $\cos 60° = \frac{1}{2}$ is what turns $2+1$ under the root into $3$.

### Worked Example 3: Infinite Line Charge → the Prototype Field Formula
> [!EXAMPLE] Problem
> A line charge $\rho_L = 5$ nC/m lies along the $z$-axis. Find $\mathbf{E}$ at the point $P(0.2\text{ m}, \phi, z)$ — directly find the force on a probe $q = 1$ C equivalent, i.e. the field, using the slicing method.

**Step 1: Slice** — element $dz'$ at height $z'$ carries $dq = \rho_L\,dz'$.
**Step 2: Distance vector to $P$ (in cylindrical coordinates, point at $\rho = 0.2$)**
$$\mathbf{R} = -\rho\,\mathbf{a}_\rho \cdot(-1) + (z - z')\mathbf{a}_z \;\Rightarrow\; R = \sqrt{\rho^2 + (z - z')^2}$$
**Step 3: Set up and integrate** (substitute $z - z' = \rho\tan\alpha$; the integral collapses)
$$\mathbf{E} = \int_{-\infty}^{\infty} \frac{\rho_L\,dz'}{4\pi\varepsilon_0\, R^2}\,\mathbf{a}_R \quad\Longrightarrow\quad \mathbf{E} = \frac{\rho_L}{2\pi\varepsilon_0\rho}\,\mathbf{a}_\rho$$

**Step 4: Numerically**
$$E = \frac{5\times10^{-9}}{2\pi(8.854\times10^{-12})(0.2)} \approx \boxed{449 \text{ V/m, radially outward}}$$

> [!IMPORTANT] 🎯 The Three Infinite-Distribution Results (memorize cold!)
> | Source | Field formula | Falls off as |
> | :--- | :--- | :---: |
> | Infinite **line** $\rho_L$ | $\mathbf{E} = \dfrac{\rho_L}{2\pi\varepsilon_0 \rho}\,\mathbf{a}_\rho$ | $1/\rho$ |
> | Infinite **sheet** $\rho_S$ | $\mathbf{E} = \dfrac{\rho_S}{2\varepsilon_0}\,\mathbf{a}_n$ | constant! |
> | **Sphere** of charge (outside) | $\mathbf{E} = \dfrac{Q}{4\pi\varepsilon_0 r^2}\,\mathbf{a}_r$ | $1/r^2$ |
>
> The sheet's field is *independent of distance* — which is exactly why parallel-plate capacitors have (nearly) uniform fields. Quick derivation of the sheet: superposing the field of a continuum of *lines* ($\frac{\rho_L}{2\pi\varepsilon_0\rho}$ with $d\rho_L = \rho_S\,d x$) integrates the vertical components to $\frac{\rho_S}{2\varepsilon_0}$.
>
> These all follow in one line from Gauss's law — see [[Application of Gauss Law, Maxwell's First Equation]].

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why does the sheet's field not weaken with distance?
> The line charge's field decays as $1/\rho$ and the point charge's as $1/r^2$ — yet an infinite sheet's field is constant. Physically, why?

> [!SUCCESS]- Step-by-Step Solution
> 1. As you back away from a sheet, the pull of each *individual element* weakens as $1/R^2$…
> 2. …but the amount of sheet "in play" grows: the cone of sight now intercepts more charge at larger angles.
> 3. The two effects cancel **exactly** for an infinite sheet → constant $\rho_S/2\varepsilon_0$.
> 4. For a *line*, geometry makes the cancellation partial → $1/\rho$. For a *point*, there is nothing extra to see → full $1/r^2$ decay. Dimensionality of the source decides the decay rate.

---

> [!QUESTION] Practice Question: Field of a volume distribution
> A sphere of radius $a = 1$ cm carries uniform volume charge $\rho_v = 2\ \mu\text{C/m}^3$. Find $\mathbf{E}$ at $r = 2$ cm (outside).

> [!SUCCESS]- Step-by-Step Solution
> 1. Total charge: $Q = \rho_v \cdot \frac{4}{3}\pi a^3 = (2\times10^{-6})\cdot\frac{4}{3}\pi(0.01)^3 = 8.38\times10^{-12}$ C $\approx 8.38$ pC.
> 2. Outside a uniformly charged sphere it acts as a **point charge at the centre** (by symmetry — each shell contributes as if concentrated).
> 3. $E = \dfrac{kQ}{r^2} = \dfrac{(8.988\times10^{9})(8.38\times10^{-12})}{(0.02)^2} \approx 188$ V/m, radially outward.
> 4. Check with Gauss's law ([[Application of Gauss Law, Maxwell's First Equation]]): $E = \frac{Q}{4\pi\varepsilon_0 r^2}$ — identical, but there it took one line instead of a triple integral.

---

## 6. Related Notes
- [[Introduction to 3D Coordinate Systems]] — choosing the slicing coordinates.
- [[Review of Vectors]] — distance vector $\mathbf{R}_{12}$ and vector superposition.
- [[Determination of Static Electric Fields]] — the $\mathbf{E} = \mathbf{F}/q$ concept and field computation strategies.
- [[Application of Gauss Law, Maxwell's First Equation]] — the shortcut that replaces these integrals.

