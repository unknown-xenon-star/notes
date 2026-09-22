---
title: "Concepts of Curl"
date: 2026-09-22
tags:
  - concept
  - emf
  - vector-analysis
  - curl
aliases:
  - "Curl"
  - "Circulation"
  - "Stokes Theorem"
  - "Rotor"
status: completed
---

# 🌀 Concepts of Curl

> [!NOTE] 💡 The Big Picture Intuition
> Drop a tiny **paddle wheel** into the field as if the field were a flowing river. If the current pushes one side of the wheel harder than the other, the wheel **spins** — the field has *circulation* there. The curl is the vector that measures this: its **component along any axis** is the maximum spin per unit area about that axis, its **direction** (by the right-hand rule) is the axis the wheel would spin around. Curl ≈ "how swirly is the field at this point?" In electrostatics the punchline is the *absence* of swirl: $\nabla\times\mathbf{E} = \mathbf{0}$ — charge fields never form whirlpools, which is exactly why voltage around any loop is zero and why potential energy is well-defined ([[Electric Potential]]).

---

## 1. Definition: Circulation Density

The curl is defined through the **circulation** $\oint \mathbf{A}\cdot d\mathbf{l}$ around a shrinking loop:
$$(\nabla\times\mathbf{A})\cdot\mathbf{a}_n = \lim_{\Delta S \to 0} \frac{\oint \mathbf{A}\cdot d\mathbf{l}}{\Delta S}$$
— the circulation per unit area in the plane normal to $\mathbf{a}_n$, maximized over loop orientation.

**Units**: [A] per metre (e.g. V/m² for $\mathbf{E}$).

## 2. Computing the Curl

> [!IMPORTANT] 🎯 Cartesian Determinant Form
> $$\nabla\times\mathbf{A} = \begin{vmatrix} \mathbf{a}_x & \mathbf{a}_y & \mathbf{a}_z \\[4pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[4pt] A_x & A_y & A_z \end{vmatrix}$$
> $$= \left(\frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}\right)\mathbf{a}_x + \left(\frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}\right)\mathbf{a}_y + \left(\frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}\right)\mathbf{a}_z$$

**Component meanings** (this is what the determinant hides):
- $(\nabla\times\mathbf{A})_z = \dfrac{\partial A_y}{\partial x} - \dfrac{\partial A_x}{\partial y}$ → spin about the $z$-axis: how much $A_y$ grows rightward minus how much $A_x$ grows upward (shear = swirl).
- The other two follow by cyclic permutation $x \to y \to z \to x$.

> [!IMPORTANT] 🎯 Cylindrical & Spherical Forms
> $$\nabla\times\mathbf{A}\Big|_{cyl} = \begin{vmatrix} \dfrac{\mathbf{a}_\rho}{\rho} & \mathbf{a}_\phi & \dfrac{\mathbf{a}_z}{\rho} \\[6pt] \dfrac{\partial}{\partial\rho} & \dfrac{\partial}{\partial\phi} & \dfrac{\partial}{\partial z} \\[6pt] A_\rho & \rho A_\phi & A_z \end{vmatrix}$$
> $$\nabla\times\mathbf{A}\Big|_{sph} = \begin{vmatrix} \dfrac{\mathbf{a}_r}{r^2\sin\theta} & \dfrac{\mathbf{a}_\theta}{r\sin\theta} & \dfrac{\mathbf{a}_\phi}{r} \\[6pt] \dfrac{\partial}{\partial r} & \dfrac{\partial}{\partial\theta} & \dfrac{\partial}{\partial\phi} \\[6pt] A_r & rA_\theta & r\sin\theta\, A_\phi \end{vmatrix}$$
> (Same trick as divergence: multiply each component by its $h$-factors before differentiating.)

## 3. Stokes' Theorem (curl's bridge between line and surface)

> [!IMPORTANT] 🎯 Stokes' Theorem
> $$\boxed{\oint_C \mathbf{A}\cdot d\mathbf{l} = \int_S (\nabla\times\mathbf{A})\cdot d\mathbf{S}}$$
> The **circulation around a closed loop** equals the **total curl flux through any surface** bounded by that loop.

**Intuition**: sum the micro-spins of all little patches making up the surface — interior neighbours cancel (shared edges traversed oppositely), leaving only the macroscopic swirl along the rim. Note the surface is *any* spanning surface: a flat disc and a domed cap on the same rim give the same answer — the circulation only "sees" the boundary.

**For electrostatics** it gives the zero-circulation law:
$$\nabla\times\mathbf{E} = \mathbf{0} \quad\Longleftrightarrow\quad \oint \mathbf{E}\cdot d\mathbf{l} = 0 \quad\Longleftrightarrow\quad \mathbf{E} = -\nabla V \text{ exists}$$
(Conservative field ⇔ zero curl ⇔ gradient of a potential — three definitions of the same property.)

> [!TIP] 🧠 Curl/Gradient identity
> $\nabla\times(\nabla V) \equiv \mathbf{0}$ for any scalar $V$ — mixed partials commute, and the determinant's rows annihilate each other. Physically: a pure downhill-slope field can never swirl. Its dual: $\nabla\cdot(\nabla\times\mathbf{A}) \equiv 0$ — swirl fields have no sources.

## 4. The Paddle-Wheel Zoo (build physical intuition)

| Field | Curl | Paddle wheel says |
| :--- | :--- | :--- |
| $\mathbf{A} = C\,\mathbf{a}_x$ (uniform) | $\mathbf{0}$ | whole wheel pushed equally — no spin |
| $\mathbf{A} = x\,\mathbf{a}_y$ (shear flow) | $\mathbf{a}_z$ | right side pushed harder → spins CCW |
| $\mathbf{A} = \dfrac{k}{\rho}\mathbf{a}_\phi$ (drain vortex, $\rho\ne0$) | $\mathbf{0}$ | surprising! inner speed-up exactly cancels curvature |
| $\mathbf{A} = \omega\rho\,\mathbf{a}_\phi$ (solid rotation) | $2\omega\,\mathbf{a}_z$ | spins with the flow like a rigid rotor |

The vortex row is the famous subtlety: a *draining* bathtub vortex has huge speed but **zero curl everywhere except the centre** — while water rotating *rigidly* (all points same angular speed $\omega$) has curl $2\omega$ everywhere. Curl measures *differential* spin (velocity difference across the wheel), not curvature of streamlines.

---

## 5. Worked Examples

### Worked Example 1: Cartesian Curl of a Shear Field
> [!EXAMPLE] Problem
> Compute $\nabla\times\mathbf{A}$ for $\mathbf{A} = y\,\mathbf{a}_x - x\,\mathbf{a}_y$, and verify Stokes' theorem on the unit square in the $xy$-plane.

**Step 1: The z-component** (x,y components vanish — no z-dependence anywhere):
$$(\nabla\times\mathbf{A})_z = \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} = \frac{\partial(-x)}{\partial x} - \frac{\partial(y)}{\partial y} = -1 - 1 = -2$$
$$\nabla\times\mathbf{A} = -2\,\mathbf{a}_z \qquad \text{(uniform swirl about } -z\text{)}$$

**Step 2: Surface integral** — over the unit square with $d\mathbf{S} = d\mathbf{a}_z$ (CCW boundary):
$$\int_S (\nabla\times\mathbf{A})\cdot d\mathbf{S} = -2 \times 1 = -2$$

**Step 3: Line integral, side by side** (CCW: $+x$ along bottom, $+y$ along right, $-x$ along top, $-y$ along left)
- Bottom ($y=0$): $\mathbf{A} = 0\cdot\mathbf{a}_x$ → contributes $0$
- Right ($x=1$): $\mathbf{A} = y\mathbf{a}_x - \mathbf{a}_y$, $d\mathbf{l} = dy\,\mathbf{a}_y$ → $\int_0^1 (-1)\,dy = -1$
- Top ($y=1$): $\mathbf{A} = \mathbf{a}_x - x\mathbf{a}_y$, $d\mathbf{l} = dx\,\mathbf{a}_x$ but traversed $x: 1\to0$ → $\int_1^0 (1)\,dx = -1$
- Left ($x=0$): $\mathbf{A} = y\mathbf{a}_x$, $d\mathbf{l} = -dy\,\mathbf{a}_y$ → $\mathbf{A}\cdot d\mathbf{l} = 0$

$$\oint \mathbf{A}\cdot d\mathbf{l} = 0 - 1 - 1 + 0 = \boxed{-2} ✅ \text{ matches the surface integral}$$

### Worked Example 2: The Point-Charge Field Has Zero Curl
> [!EXAMPLE] Problem
> Show that $\mathbf{E} = \dfrac{Q}{4\pi\varepsilon_0 r^2}\mathbf{a}_r$ has zero curl (for $r \ne 0$).

**Step 1: Spherical curl, radial field** — only the $\mathbf{a}_\theta$ and $\mathbf{a}_\phi$ rows can survive; with $A_\theta = A_\phi = 0$ and no $\theta,\phi$ dependence:
$$(\nabla\times\mathbf{E})_\phi = \frac{1}{r}\left[\frac{\partial(r E_\theta)}{\partial r} - \frac{\partial E_r}{\partial\theta}\right] = \frac{1}{r}\left[0 - 0\right] = 0$$

**Step 2: Confirm via potential** — $V = \frac{Q}{4\pi\varepsilon_0 r}$, so $\mathbf{E} = -\nabla V$ is a pure gradient; and $\nabla\times(\nabla V) \equiv \mathbf{0}$ identically.

**Step 3: The meaning** — zero circulation is *the* license to define voltage: walk a test charge around any closed loop and the field gives back exactly what it took. Net work over a cycle = 0 → potential energy $qV$ is a well-defined bookkeeping number ([[Electric Potential]]). Magnetostatics will *break* this property ($\nabla\times\mathbf{B} = \mu_0\mathbf{J}$) — that's why no scalar "magnetic potential" of the same simple kind exists.

### Worked Example 3: Solid-Rotation Flow
> [!EXAMPLE] Problem
> Water rotates rigidly about the $z$-axis with angular speed $\omega$: velocity $\mathbf{v} = \omega\rho\,\mathbf{a}_\phi$. Find $\nabla\times\mathbf{v}$ and check Stokes for a circular loop of radius $R$.

**Step 1: Cylindrical curl** — only the $z$-row survives:
$$(\nabla\times\mathbf{v})_z = \frac{1}{\rho}\frac{\partial(\rho\, v_\phi)}{\partial\rho} = \frac{1}{\rho}\frac{\partial(\omega\rho^2)}{\partial\rho} = \frac{2\omega\rho}{\rho} = 2\omega$$
$$\nabla\times\mathbf{v} = 2\omega\,\mathbf{a}_z \qquad \text{(twice the angular velocity — a rigid rotor's signature)}$$

**Step 2: Stokes check** — surface side: $2\omega \cdot \pi R^2$. Line side: on the circle $\rho = R$, $\mathbf{v}$ is tangential with constant magnitude $\omega R$:
$$\oint \mathbf{v}\cdot d\mathbf{l} = (\omega R)(2\pi R) = 2\pi\omega R^2 ✅ \text{ equal}$$

**Physical note**: the paddle wheel rides along at $\omega$ while the local flow differential adds $+\omega$ (outer edge) and $-\omega$ (inner edge)... net spin rate $2\omega$ — curl of rigid rotation is *twice* the angular velocity, the classic factor-of-2.

---

## 6. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Curved but curl-free?
> The field $\mathbf{A} = \frac{k}{\rho}\mathbf{a}_\phi$ has perfectly circular streamlines, yet $\nabla\times\mathbf{A} = \mathbf{0}$ for $\rho \neq 0$. Reconcile.

> [!SUCCESS]- Step-by-Step Solution
> 1. Curl measures circulation **per unit area of a small loop**, not streamline curvature.
> 2. For a small rectangular loop: the inner edge (shorter path, stronger field... exactly $\frac{k}{\rho_{in}}$ vs $\frac{k}{\rho_{out}}$) and the outer edge contribute circulation whose difference cancels the radial-edge contributions — every effect pairs off to zero.
> 3. Computation: $(\nabla\times\mathbf{A})_z = \frac{1}{\rho}\frac{\partial(\rho A_\phi)}{\partial\rho} = \frac{1}{\rho}\frac{\partial(k)}{\partial\rho} = 0$.
> 4. But Stokes on a disc *containing the centre*: circulation $= k\cdot 2\pi \ne 0$ → all the curl is concentrated as a singularity at $\rho = 0$ (a vortex filament). Curved ≠ curl-full; the balance of $1/\rho$ decay does it.

---

> [!QUESTION] Practice Question: Why electrostatics needs curl = 0
> State the three equivalent statements of electrostatic conservatism and explain in one line why each implies the next.

> [!SUCCESS]- Step-by-Step Solution
> 1. $\nabla\times\mathbf{E} = \mathbf{0}$ (point form) ⇔ $\oint\mathbf{E}\cdot d\mathbf{l} = 0$ on every loop (Stokes: zero curl flux through any spanning surface) ⇔ $\mathbf{E} = -\nabla V$ (a zero-curl field can be written as a gradient — Helmholtz decomposition).
> 2. Consequence: work done moving $q$ between two points is path-independent → the potential difference $V_{AB}$ is a function of endpoints only ([[Electric Potential]], path-independence example).
> 3. In time-varying fields Faraday's law $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ destroys this — hence "voltage" around loops becomes path-dependent and the simple scalar potential picture needs repair.

---

## 7. Related Notes
- [[Electric Potential]] — zero curl is what makes the potential terrain well-defined.
- [[Concepts of Gradient]] — $\nabla\times\nabla V = \mathbf{0}$ links the two operators.
- [[Concepts of Divergence]] — the other half of the vector-calculus toolkit; $\nabla\cdot(\nabla\times\mathbf{A}) = 0$.
- [[Review of Vectors]] — the determinant mechanics reused from the cross product.

