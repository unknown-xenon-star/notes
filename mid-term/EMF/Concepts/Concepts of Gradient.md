---
title: "Concepts of Gradient"
date: 2026-09-22
tags:
  - concept
  - emf
  - vector-analysis
  - gradient
aliases:
  - "Gradient"
  - "Grad"
  - "Directional Derivative"
  - "Grad Operator"
status: completed
---

# 📈 Concepts of Gradient

> [!NOTE] 💡 The Big Picture Intuition
> Stand on a foggy hillside where you cannot see, but you can feel the ground's height $h(x, y)$ under your boots. Which way is **steepest uphill**? The gradient answers exactly this: $\nabla h$ is the arrow that points **up the steepest slope**, with length equal to the steepness (metres of climb per metre of walk). The gradient of a scalar field (one number per point: height, temperature, potential) is a **vector field** (one arrow per point). In EMF this is the bridge between the two pictures of electrostatics: potential is the terrain, field is the downhill direction — $\mathbf{E} = -\nabla V$. Charges roll downhill; the gradient tells you where downhill *is*.

---

## 1. Definition and the Directional Derivative

> [!IMPORTANT] 🎯 The Gradient
> $$\nabla V = \frac{\partial V}{\partial x}\mathbf{a}_x + \frac{\partial V}{\partial y}\mathbf{a}_y + \frac{\partial V}{\partial z}\mathbf{a}_z \qquad \text{(Cartesian)}$$
> **Properties**: operates on a *scalar* → produces a *vector*. Units: [V] per metre.

> [!IMPORTANT] 🎯 The Directional Derivative (what the gradient is *for*)
> The rate of change of $V$ as you walk in unit direction $\mathbf{a}_l$:
> $$\frac{dV}{dl}\bigg|_{\mathbf{a}_l} = \nabla V \cdot \mathbf{a}_l$$
> - Walking **along** $\nabla V$: maximum increase (dot = $|\nabla V|$).
> - Walking **against** $\nabla V$: maximum decrease — the field direction!
> - Walking **perpendicular** to $\nabla V$: zero change — you're walking along a **contour** (equipotential line).

**Three facts packed into one definition** (the exam trio):
1. $\nabla V$ points in the direction of **maximum increase** of $V$.
2. Its **magnitude** is that maximum rate of change per unit length.
3. It is **perpendicular** to the level surfaces $V = $ const (because moving along them gives $\nabla V\cdot d\mathbf{l} = dV = 0$).

> [!TIP] 🧠 Equipotentials ⊥ field lines, for free
> $\mathbf{E} = -\nabla V$ inherits property 3: field lines cross equipotential surfaces at right angles. Conductors are equipotentials → field leaves conductors perpendicularly — one line of vector calculus explains the boundary rule used in [[Boundary Relations of Electric Fields]].

## 2. Gradient in the Three Coordinate Systems

$$\text{Cartesian:}\quad \nabla V = \frac{\partial V}{\partial x}\mathbf{a}_x + \frac{\partial V}{\partial y}\mathbf{a}_y + \frac{\partial V}{\partial z}\mathbf{a}_z$$

$$\text{Cylindrical:}\quad \nabla V = \frac{\partial V}{\partial \rho}\mathbf{a}_\rho + \frac{1}{\rho}\frac{\partial V}{\partial \phi}\mathbf{a}_\phi + \frac{\partial V}{\partial z}\mathbf{a}_z$$

$$\text{Spherical:}\quad \nabla V = \frac{\partial V}{\partial r}\mathbf{a}_r + \frac{1}{r}\frac{\partial V}{\partial \theta}\mathbf{a}_\theta + \frac{1}{r\sin\theta}\frac{\partial V}{\partial \phi}\mathbf{a}_\phi$$

> [!WARNING] ⚠️ The $1/\rho$ and $1/r$ Factors
> The angular components carry stretch factors: a change $d\phi$ corresponds to physical displacement $\rho\,d\phi$ (cylindrical) or $r\sin\theta\,d\phi$ (spherical) — the $h$-factors of [[Introduction to 3D Coordinate Systems]]. Rate **per metre** means dividing the angular rate by these lengths. Forgetting the $\frac{1}{\rho}$ is the most common single error in cylindrical/spherical gradient problems.

## 3. The E = −∇V Engine (Why EMF Cares)

| Potential $V$ | Gradient gives | Field |
| :--- | :--- | :--- |
| $\frac{Q}{4\pi\varepsilon_0 r}$ | $-\frac{d}{dr}\left(\frac{Q}{4\pi\varepsilon_0 r}\right)$ | $\frac{Q}{4\pi\varepsilon_0 r^2}\mathbf{a}_r$ |
| $\frac{p\cos\theta}{4\pi\varepsilon_0 r^2}$ | both $r$ and $\theta$ derivatives | dipole $\mathbf{E}$ (both components) |
| $-E_0 x$ | $-\frac{d}{dx}(-E_0 x)$ | $E_0\,\mathbf{a}_x$ (uniform field) |

One scalar derivative replaces a full vector-integral campaign — the whole advantage of the potential route of [[Electric Potential]].

**Bonus identity**: $\nabla\cdot(\nabla V) = \nabla^2 V$ — the Laplacian. Combining $\mathbf{E} = -\nabla V$ with Gauss's law $\nabla\cdot\mathbf{E} = \rho_v/\varepsilon$ ([[Application of Gauss Law, Maxwell's First Equation]], [[Concepts of Divergence]]) yields **Poisson's equation** $\nabla^2 V = -\rho_v/\varepsilon$, and in charge-free regions **Laplace's equation** $\nabla^2 V = 0$ — the governing equations of potential theory.

---

## 4. Worked Examples

### Worked Example 1: Gradient of a Mixed Scalar Field
> [!EXAMPLE] Problem
> Find $\nabla T$ for $T = x^2 + yz$ and evaluate at $P(1, 2, 3)$. Then find the rate of change of $T$ in the direction of $\mathbf{a}_x + \mathbf{a}_y + \mathbf{a}_z$.

**Step 1: Partial derivatives**
$$\frac{\partial T}{\partial x} = 2x, \qquad \frac{\partial T}{\partial y} = z, \qquad \frac{\partial T}{\partial z} = y$$

**Step 2: Assemble and evaluate**
$$\nabla T = 2x\,\mathbf{a}_x + z\,\mathbf{a}_y + y\,\mathbf{a}_z \;\Rightarrow\; \nabla T\big|_P = 2\,\mathbf{a}_x + 3\,\mathbf{a}_y + 2\,\mathbf{a}_z, \qquad |\nabla T| = \sqrt{4+9+4} = \sqrt{17} \approx 4.123$$

**Step 3: Directional derivative** — unit vector along $(1,1,1)$: $\mathbf{a}_l = \frac{1}{\sqrt{3}}(\mathbf{a}_x + \mathbf{a}_y + \mathbf{a}_z)$
$$\frac{dT}{dl} = \nabla T\cdot\mathbf{a}_l = \frac{2 + 3 + 2}{\sqrt{3}} = \frac{7}{\sqrt{3}} \approx \boxed{4.041}$$

**Check**: $4.041 < 4.123 = |\nabla T|$ — no direction can beat the steepest-ascent direction ✅

### Worked Example 2: E from a Spherical Potential
> [!EXAMPLE] Problem
> The potential around some charge distribution is $V = \dfrac{200}{r^2}$ volts ($r$ in metres). Find $\mathbf{E}$ at $r = 2$ m, and the total charge producing it.

**Step 1: Spherical gradient** — $V$ depends only on $r$, so only the radial term survives:
$$\mathbf{E} = -\nabla V = -\frac{dV}{dr}\,\mathbf{a}_r = -\frac{d}{dr}\left(200\,r^{-2}\right)\mathbf{a}_r = \frac{400}{r^3}\,\mathbf{a}_r$$

**Step 2: Evaluate**
$$\mathbf{E}(2) = \frac{400}{8}\,\mathbf{a}_r = \boxed{50\,\mathbf{a}_r \ \text{V/m}}$$

**Step 3: Identify the charge** — compare with the point-charge potential $\frac{Q}{4\pi\varepsilon_0 r} = \frac{200}{r^2}$... the $r$-dependence differs from a point charge (this is $1/r^2$, not $1/r$ — a dipole-like or ring-like source). If instead we only want the equivalent flux: $Q = \varepsilon_0\, 4\pi r^2 E_r = (8.854\times10^{-12})(4\pi)(4)(50) = 22.3$ nC of flux-equivalent.

**Watch for**: differentiating $r^{-2}$ gives $-2r^{-3}$; the minus in $\mathbf{E} = -\nabla V$ flips the sign — positive $E_r$ means the field points outward, i.e. potential decreases outward, as it must.

### Worked Example 3: Cylindrical Gradient with the $1/\rho$ Factor
> [!EXAMPLE] Problem
> In coaxial-cable coordinates the potential is $V(\rho) = V_0\,\dfrac{\ln(b/\rho)}{\ln(b/a)}$ with inner radius $a$, outer $b$. Find $\mathbf{E}(\rho)$.

**Step 1: Cylindrical gradient** — $V$ depends only on $\rho$:
$$\mathbf{E} = -\frac{dV}{d\rho}\,\mathbf{a}_\rho = -\frac{V_0}{\ln(b/a)}\cdot\frac{d}{d\rho}\ln\frac{b}{\rho}\,\mathbf{a}_\rho = \frac{V_0}{\rho\ln(b/a)}\,\mathbf{a}_\rho$$

**Step 2: Interpret** — the field grows as $1/\rho$: strongest at the inner conductor ($\rho = a$), where
$$E_{max} = \frac{V_0}{a\ln(b/a)}$$

**Step 3: Design insight** — this $E_{max}$ is why insulation fails at the inner conductor first, and optimizing the ratio $b/a = e \approx 2.718$ minimizes it (a classic exam follow-up using $\frac{d}{da}\left[a\ln(b/a)\right]$).

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why is the gradient perpendicular to level surfaces?
> Prove that $\nabla V$ is normal to the surface $V(x,y,z) = c$ without appealing to pictures.

> [!SUCCESS]- Step-by-Step Solution
> 1. Take any small displacement $d\mathbf{l}$ that stays *on* the surface; then $V$ doesn't change: $dV = 0$.
> 2. Chain rule: $dV = \frac{\partial V}{\partial x}dx + \frac{\partial V}{\partial y}dy + \frac{\partial V}{\partial z}dz = \nabla V \cdot d\mathbf{l}$.
> 3. So $\nabla V \cdot d\mathbf{l} = 0$ for every tangent $d\mathbf{l}$ of the surface.
> 4. A vector orthogonal to every tangent direction of a surface is along its **normal** — hence $\nabla V \perp$ level surfaces, and $\mathbf{E} = -\nabla V$ is normal to equipotentials.

---

> [!QUESTION] Practice Question: Where does the $1/r$ in spherical gradient come from?
> The $\theta$-component of $\nabla V$ in spherical coordinates is $\frac{1}{r}\frac{\partial V}{\partial\theta}$. Explain the $\frac{1}{r}$ using the differential displacement.

> [!SUCCESS]- Step-by-Step Solution
> 1. A small angular step $d\theta$ covers an arc length $dl_\theta = r\,d\theta$ (arc = radius × angle).
> 2. The rate of change **per metre** is therefore $\frac{dV}{dl_\theta} = \frac{dV}{r\,d\theta} = \frac{1}{r}\frac{\partial V}{\partial\theta}$.
> 3. Same logic as the $\frac{1}{\rho}$ in cylindrical ($dl_\phi = \rho\, d\phi$) and the extra $\sin\theta$ in the $\phi$-term ($dl_\phi = r\sin\theta\,d\phi$).
> 4. Rule of thumb: each angular derivative must be divided by its physical arc length — the $h$-factors again ([[Introduction to 3D Coordinate Systems]]).

---

## 6. Related Notes
- [[Electric Potential]] — the terrain that $\mathbf{E} = -\nabla V$ differentiates.
- [[Concepts of Divergence]] — applying $\nabla\cdot$ to the gradient gives the Laplacian (Poisson/Laplace).
- [[Concepts of Curl]] — the sibling operator; $\nabla\times\nabla V \equiv 0$ is why electrostatic fields are conservative.
- [[Introduction to 3D Coordinate Systems]] — the $h$-factors behind the $1/\rho$, $1/r$, $1/(r\sin\theta)$ prefactors.

