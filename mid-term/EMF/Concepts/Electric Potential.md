---
title: "Electric Potential"
date: 2026-09-22
tags:
  - concept
  - emf
  - electrostatics
  - potential
aliases:
  - "Electric Potential"
  - "Potential Difference"
  - "Voltage"
  - "Scalar Electric Potential"
status: completed
---

# ⛰️ Electric Potential

> [!NOTE] 💡 The Big Picture Intuition
> The electric field is a vector map (arrows everywhere); the potential is the same physics compressed into a **scalar landscape** — a terrain of hills (positive charges) and valleys (negative charges). Instead of asking "which way and how hard would a charge be pushed here?", we ask "**how high is this point?**". The link is direct: **positive charges roll downhill** (from high $V$ to low $V$), and the local slope of the terrain *is* the field (see [[Concepts of Gradient]]). Scalar terrain beats vector arrows for computation: potentials just *add as numbers* (no components!), which is why the potential route is often the smart way to find fields — [[Determination of Static Electric Fields]], Strategy 3.

---

## 1. Definition: Potential as Work per Unit Charge

> [!IMPORTANT] 🎯 Potential Difference
> $$V_{AB} = V_A - V_B = -\int_B^A \mathbf{E}\cdot d\mathbf{l} = \frac{W}{q} \qquad \text{units: volts (J/C)}$$
> $V_{AB}$ = the work done **by an external agent** carrying $+1$ C from $B$ to $A$ (per unit charge), against the field.

- The minus sign: moving *against* $\mathbf{E}$ (uphill) accumulates positive potential.
- Absolute potential is defined up to a constant; by convention $V(\infty) = 0$, giving $V(r) = \frac{Q}{4\pi\varepsilon_0 r}$ for a point charge.
- **Potential is path-independent**: because $\nabla\times\mathbf{E} = 0$ ([[Concepts of Curl]]), any two paths from $B$ to $A$ give the same integral. This is the electrostatic guarantee that makes "voltage between two points" meaningful.

## 2. Potential of the Standard Sources

| Source | Potential $V$ | Field $\mathbf{E} = -\nabla V$ |
| :--- | :--- | :--- |
| Point charge $Q$ | $\dfrac{Q}{4\pi\varepsilon_0 r}$ | $\dfrac{Q}{4\pi\varepsilon_0 r^2}\mathbf{a}_r$ |
| Dipole (far field, $\mathbf{p} = Q\mathbf{d}$) | $\dfrac{p\cos\theta}{4\pi\varepsilon_0 r^2}$ | $1/r^3$ decay (see [[Determination of Static Electric Fields]]) |
| Line charge $\rho_L$ | $\dfrac{\rho_L}{2\pi\varepsilon_0}\ln\frac{\rho_{ref}}{\rho}$ | $\dfrac{\rho_L}{2\pi\varepsilon_0 \rho}\mathbf{a}_\rho$ |
| Uniform field region | $-E_0 x + \text{const}$ | $E_0\,\mathbf{a}_x$ |

> [!WARNING] ⚠️ The Line-Charge Logarithm
> An infinite line's potential **cannot use $V(\infty)=0$** — the integral $\int \frac{d\rho}{\rho}$ diverges at infinity (the field doesn't fall fast enough). Use any convenient **reference radius** $\rho_{ref}$ instead; only potential *differences* are physical.

## 3. The Two Golden Relationships

> [!IMPORTANT] 🎯 E from V (the derivative direction)
> $$\mathbf{E} = -\nabla V \qquad \text{(the gradient operation, [[Concepts of Gradient]])}$$
> Field points **down the steepest slope** of the potential terrain. Component view: $E_x = -\partial V/\partial x$, etc.

> [!IMPORTANT] 🎯 V from E (the integral direction)
> $$V_{AB} = -\int_B^A \mathbf{E}\cdot d\mathbf{l}$$
> Potential difference = (minus the) area under the $E$-along-path curve.

**Energy viewpoint**: the potential energy of charge $q$ at potential $V$ is $U = qV$. Pushing $q$ from $A$ to $B$ costs
$$W = q(V_B - V_A)$$
External agent does positive work going uphill; the field does positive work going downhill.

> [!TIP] 🧠 Why scalars beat vectors
> Superposing potentials is **arithmetic**: $V = \sum \frac{Q_i}{4\pi\varepsilon_0 R_i}$ — no angles, no components, no cancellation bookkeeping. Compute the scalar terrain first, then differentiate to get the full vector field in one stroke. (Compare: superposing $\mathbf{E}$ directly needs a separate cosine projection per charge — see [[Various Charge Distribution, Coulomb's Law]].)

---

## 4. Worked Examples

### Worked Example 1: Potential & Work Between Two Points
> [!EXAMPLE] Problem
> $Q = 5$ nC at the origin. Find $V_A$ at $r_A = 10$ cm, $V_B$ at $r_B = 40$ cm, and the work to move $q = 2$ nC from $A$ to $B$.

**Step 1: The two potentials** (with $V(\infty) = 0$)
$$V_A = \frac{(8.988\times10^9)(5\times10^{-9})}{0.1} = \frac{44.94}{0.1} = 449.4 \text{ V}$$
$$V_B = \frac{44.94}{0.4} = 112.4 \text{ V}$$

**Step 2: Work** — moving a *positive* test charge away from a *positive* source is downhill:
$$W_{A\to B} = q(V_B - V_A) = (2\times10^{-9})(112.4 - 449.4) = \boxed{-674 \text{ nJ}}$$

**Step 3: Interpret the minus sign** — the *field* does $+674$ nJ of work; the external agent actually *receives* energy (like lowering a mass on a rope). Moving the charge back $B \to A$ would cost $+674$ nJ.

### Worked Example 2: Path Independence
> [!EXAMPLE] Problem
> In the uniform field $\mathbf{E} = 2\mathbf{a}_x + 3\mathbf{a}_y$ V/m, compute $\Delta V$ from the origin to $(1, 1, 0)$ along (a) the straight diagonal, (b) the staircase path along $x$ then $y$.

**Step 1: Diagonal path** — $d\mathbf{l} = (dx, dy, 0)$, on the diagonal $dy = dx$:
$$V_{origin} - V_{(1,1)} = \int_0^1 (2 + 3)\,dt = \boxed{5 \text{ V}}$$

**Step 2: Staircase path** — segment 1 ($y=0$, $x: 0\to1$): $\int 2\,dx = 2$; segment 2 ($x=1$, $y: 0\to1$): $\int 3\,dy = 3$
$$\text{Total} = 2 + 3 = \boxed{5 \text{ V}} ✅$$

**Step 3: The lesson** — identical answers; only the *endpoints* matter because $\nabla \times \mathbf{E} = 0$ in electrostatics. (If a claimed "electrostatic" field gave different answers on different paths, it could not exist — its curl would be nonzero.)

### Worked Example 3: Finding E from a Given V (line and sphere cases)
> [!EXAMPLE] Problem
> (a) $V = 10/r$ volts (spherical). Find $\mathbf{E}$ at $r = 2$ m. (b) $V = \frac{\rho_L}{2\pi\varepsilon_0}\ln(\rho_{ref}/\rho)$: confirm $\mathbf{E}$.

**Step 1 (a): differentiate**
$$E_r = -\frac{dV}{dr} = -\frac{d}{dr}\left(\frac{10}{r}\right) = \frac{10}{r^2} \;\Rightarrow\; \mathbf{E}(2) = \frac{10}{4}\,\mathbf{a}_r = \boxed{2.5\,\mathbf{a}_r \text{ V/m}}$$
(This is the field of a $Q = 4\pi\varepsilon_0 \times 10 \approx 1.11$ nC point charge.)

**Step 2 (b): cylindrical derivative**
$$E_\rho = -\frac{\partial V}{\partial \rho} = -\frac{\rho_L}{2\pi\varepsilon_0}\cdot\frac{d}{d\rho}\ln\frac{\rho_{ref}}{\rho} = -\frac{\rho_L}{2\pi\varepsilon_0}\left(-\frac{1}{\rho}\right) = \frac{\rho_L}{2\pi\varepsilon_0\rho}$$

✅ exactly the standard line-charge field — the potential route reproduces the direct result with one scalar derivative instead of a vector integral.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Equipotentials ⊥ field lines
> Explain why equipotential surfaces and field lines always meet at right angles.

> [!SUCCESS]- Step-by-Step Solution
> 1. On an equipotential surface $V = \text{const}$, moving along it changes nothing: $dV = \nabla V \cdot d\mathbf{l} = 0$ for every tangent $d\mathbf{l}$.
> 2. A vector whose dot product with *every* tangent direction is zero must be **normal** to the surface.
> 3. $\mathbf{E} = -\nabla V$ → $\mathbf{E}$ is normal to every equipotential.
> 4. Consequences: conductors are equipotentials, so $\mathbf{E}$ must leave conductor surfaces perpendicularly — the seed of [[Boundary Relations of Electric Fields]].

---

> [!QUESTION] Practice Question: Dipole potential and its slope
> A dipole $\mathbf{p} = 2$ pC·m points along $+z$. Find $V$ at $r = 10$ cm, $\theta = 0°$, then verify the axial field formula of [[Determination of Static Electric Fields]] from it.

> [!SUCCESS]- Step-by-Step Solution
> 1. Far-field dipole potential: $V = \frac{p\cos\theta}{4\pi\varepsilon_0 r^2}$.
> 2. Numbers: $V = \frac{(2\times10^{-12})(8.988\times10^9)(1)}{(0.1)^2} = \frac{0.01798}{0.01} = 1.80$ V.
> 3. Axial field: $E_r = -\frac{\partial V}{\partial r} = \frac{2p\cos\theta}{4\pi\varepsilon_0 r^3}$ → at $\theta = 0$: $E = \frac{2(2\times10^{-12})(8.988\times10^9)}{10^{-3}} = 35.95$ V/m ✅ matches the direct dipole result.
> 4. Bonus: differentiating w.r.t. $\theta$ gives $E_\theta = \frac{p\sin\theta}{4\pi\varepsilon_0 r^3}$ — both dipole field components from one scalar expression.

---

## 6. Related Notes
- [[Concepts of Gradient]] — the machinery of $\mathbf{E} = -\nabla V$.
- [[Determination of Static Electric Fields]] — when the potential route is the winning strategy.
- [[Application of Gauss Law, Maxwell's First Equation]] — the other half of electrostatics; Laplace's equation $\nabla^2 V = -\rho_v/\varepsilon$ follows by combining the two.
- [[Boundary Relations of Electric Fields]] — potential continuity at material interfaces.

