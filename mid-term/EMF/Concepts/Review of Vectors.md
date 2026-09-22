---
title: "Review of Vectors"
date: 2026-09-22
tags:
  - concept
  - emf
  - vector-analysis
  - vectors
aliases:
  - "Vectors"
  - "Vector Algebra"
  - "Dot Product"
  - "Cross Product"
status: completed
---

# ➡️ Review of Vectors

> [!NOTE] 💡 The Big Picture Intuition
> A scalar answers "**how much?**" (mass, temperature, charge). A vector answers "**how much, and which way?**" (force, velocity, electric field). Think of a vector as an **arrow**: its length is the magnitude, the way it points is the direction. Every field in EMF — $\mathbf{E}$, $\mathbf{D}$, later $\mathbf{B}$ — is an arrow assigned to *every point in space*, which is why vector fluency is not optional. The two products are the workhorses: the **dot product** measures *alignment* ("how much of A points along B?"), and the **cross product** measures *perpendicularity* ("how much of A is sideways to B, and on which side?").

---

## 1. Vector Basics & Component Form

A vector $\mathbf{A}$ in 3D is written with unit vectors (arrows of length 1 that only carry direction):

$$\mathbf{A} = A_x\,\mathbf{a}_x + A_y\,\mathbf{a}_y + A_z\,\mathbf{a}_z$$

- **Magnitude**: $|\mathbf{A}| = A = \sqrt{A_x^2 + A_y^2 + A_z^2}$
- **Unit vector** (direction only): $\mathbf{a}_A = \dfrac{\mathbf{A}}{|\mathbf{A}|} = \dfrac{A_x\,\mathbf{a}_x + A_y\,\mathbf{a}_y + A_z\,\mathbf{a}_z}{A}$
- **Position vector** of point $P(x,y,z)$: $\mathbf{r} = x\,\mathbf{a}_x + y\,\mathbf{a}_y + z\,\mathbf{a}_z$
- **Vector from $P_1$ to $P_2$** (crucial for Coulomb's law!): $\mathbf{R}_{12} = \mathbf{r}_2 - \mathbf{r}_1$, pointing *from the source toward the target*.

> [!TIP] 🧠 The Distance-Vector Trap
> $\mathbf{R}_{12}$ points **from 1 to 2** (tail at $P_1$, head at $P_2$): subtract tail coordinates from head coordinates. Every force/field formula in this subject is written as *"field at 2 due to charge at 1"*, so the vector that appears is always $\mathbf{R}_{12}$ (or its unit vector $\mathbf{a}_{12}$) — get it backwards and every sign flips.

**Vector addition** = component-wise (parallelogram law); **scalar multiplication** stretches the arrow without turning it. Both are commutative; the **associative** grouping holds; addition and multiplication combine by the **distributive** law: $k(\mathbf{A}+\mathbf{B}) = k\mathbf{A} + k\mathbf{B}$.

---

## 2. The Dot Product (Scalar Product)

> [!IMPORTANT] 🎯 Two Equivalent Definitions
> $$\mathbf{A} \cdot \mathbf{B} = AB\cos\theta_{AB} \qquad \text{(geometric)}$$
> $$\mathbf{A} \cdot \mathbf{B} = A_xB_x + A_yB_y + A_zB_z \qquad \text{(component form — what you actually compute)}$$

**Physical meaning**: "how much of $\mathbf{A}$ lies along $\mathbf{B}$" — the *projection* of one onto the other, times the other's size. Perpendicular vectors give **zero** ($\cos 90° = 0$); parallel vectors give $AB$.

**Key uses in EMF**:
- Work: $W = \mathbf{F} \cdot \mathbf{d}$ — only the force component along the motion counts.
- Flux: $\Psi = \mathbf{E} \cdot d\mathbf{S}$ — only the field component *piercing* the surface counts (the heart of Gauss's law, [[Application of Gauss Law, Maxwell's First Equation]]).
- Testing orthogonality of fields and surfaces.

**Properties**: commutative $\mathbf{A}\cdot\mathbf{B} = \mathbf{B}\cdot\mathbf{A}$; distributive $\mathbf{A}\cdot(\mathbf{B}+\mathbf{C}) = \mathbf{A}\cdot\mathbf{B} + \mathbf{A}\cdot\mathbf{C}$; self-dot gives $|\mathbf{A}|^2$; **no** associativity with a third vector ($\mathbf{A}\cdot\mathbf{B}\cdot\mathbf{C}$ is meaningless).

**Projection**: component of $\mathbf{A}$ along $\mathbf{B}$ is $A_{\parallel B} = \dfrac{\mathbf{A}\cdot\mathbf{B}}{B}$, and the vector projection is $A_{\parallel B}\,\mathbf{a}_B$.

---

## 3. The Cross Product (Vector Product)

> [!IMPORTANT] 🎯 Two Equivalent Definitions
> $$\mathbf{A} \times \mathbf{B} = AB\sin\theta_{AB}\ \mathbf{a}_n \qquad \text{(geometric; } \mathbf{a}_n \text{ by right-hand rule)}$$
> $$\mathbf{A} \times \mathbf{B} = \begin{vmatrix} \mathbf{a}_x & \mathbf{a}_y & \mathbf{a}_z \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix} = (A_yB_z - A_zB_y)\,\mathbf{a}_x + (A_zB_x - A_xB_z)\,\mathbf{a}_y + (A_xB_y - A_yB_x)\,\mathbf{a}_z$$

**Physical meaning**: a vector **perpendicular to both** inputs, with magnitude equal to the *area of the parallelogram* they span. Curl your right-hand fingers from $\mathbf{A}$ toward $\mathbf{B}$; your thumb gives $\mathbf{a}_n$.

**Key uses in EMF**:
- Area vectors and surface normals: $d\mathbf{S} = d\mathbf{l}_1 \times d\mathbf{l}_2$.
- Torque, magnetic force $\mathbf{F} = q\mathbf{v} \times \mathbf{B}$ (later in the course).
- Testing parallelism: $\mathbf{A} \times \mathbf{B} = \mathbf{0} \iff \mathbf{A} \parallel \mathbf{B}$.

> [!WARNING] ⚠️ Anti-commutative!
> $$\mathbf{A} \times \mathbf{B} = -(\mathbf{B} \times \mathbf{A})$$
> Reversing the order flips the arrow. And there is **no** general associativity: $\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) \ne (\mathbf{A} \times \mathbf{B}) \times \mathbf{C}$ — the *bac-cab* rule resolves the triple product:
> $$\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{C}(\mathbf{A}\cdot\mathbf{B})$$

**Scalar triple product**: $\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C})$ = signed volume of the parallelepiped spanned by the three vectors; cyclic permutation leaves it unchanged.

| Product | Result | Zero when | Measures |
| :--- | :--- | :--- | :--- |
| $\mathbf{A}\cdot\mathbf{B}$ | scalar $AB\cos\theta$ | $\perp$ | alignment |
| $\mathbf{A}\times\mathbf{B}$ | vector $AB\sin\theta\,\mathbf{a}_n$ | $\parallel$ | perpendicularity / area |

---

## 4. Worked Examples

### Worked Example 1: Angle Between Two Vectors (dot product)
> [!EXAMPLE] Problem
> Find the angle between $\mathbf{A} = 2\mathbf{a}_x + 3\mathbf{a}_y - \mathbf{a}_z$ and $\mathbf{B} = \mathbf{a}_x - 2\mathbf{a}_y + \mathbf{a}_z$.

**Step 1: Magnitudes**
$$A = \sqrt{2^2 + 3^2 + (-1)^2} = \sqrt{14} \approx 3.742, \qquad B = \sqrt{1 + 4 + 1} = \sqrt{6} \approx 2.449$$

**Step 2: Dot product** — $\mathbf{A}\cdot\mathbf{B} = (2)(1) + (3)(-2) + (-1)(1) = 2 - 6 - 1 = -5$

**Step 3: Solve for the angle**
$$\cos\theta = \frac{-5}{\sqrt{14}\sqrt{6}} = \frac{-5}{\sqrt{84}} \approx -0.5455 \;\Rightarrow\; \theta \approx \boxed{123.1°}$$

(An obtuse angle — the arrows point substantially away from each other.)

### Worked Example 2: Cross Product & Parallelogram Area
> [!EXAMPLE] Problem
> For the same vectors, compute $\mathbf{A} \times \mathbf{B}$ and the area of the parallelogram they span.

**Step 1: Determinant expansion**
$$\mathbf{A} \times \mathbf{B} = \begin{vmatrix} \mathbf{a}_x & \mathbf{a}_y & \mathbf{a}_z \\ 2 & 3 & -1 \\ 1 & -2 & 1 \end{vmatrix}$$

$\mathbf{a}_x$: $(3)(1) - (-1)(-2) = 3 - 2 = 1$
$\mathbf{a}_y$: $-\big[(2)(1) - (-1)(1)\big] = -(2+1) = -3$
$\mathbf{a}_z$: $(2)(-2) - (3)(1) = -4 - 3 = -7$

$$\mathbf{A} \times \mathbf{B} = \mathbf{a}_x - 3\mathbf{a}_y - 7\mathbf{a}_z$$

**Step 2: Magnitude = area**
$$|\mathbf{A} \times \mathbf{B}| = \sqrt{1 + 9 + 49} = \sqrt{59} \approx \boxed{7.681 \text{ square units}}$$

**Step 3: Consistency check** — $\sin\theta$ from the cross product: $\frac{7.681}{(3.742)(2.449)} = 0.838$; from the dot product angle: $\sin 123.1° = 0.838$ ✅

### Worked Example 3: Unit Vector Along a Distance Vector
> [!EXAMPLE] Problem
> Find the unit vector pointing from $P_1(1, 2, -1)$ toward $P_2(3, 0, 4)$.

**Step 1: Distance vector** (head minus tail)
$$\mathbf{R}_{12} = (3-1)\,\mathbf{a}_x + (0-2)\,\mathbf{a}_y + (4-(-1))\,\mathbf{a}_z = 2\mathbf{a}_x - 2\mathbf{a}_y + 5\mathbf{a}_z$$

**Step 2: Magnitude** — $R = \sqrt{4 + 4 + 25} = \sqrt{33} \approx 5.745$

**Step 3: Normalize**
$$\mathbf{a}_{12} = \frac{2\mathbf{a}_x - 2\mathbf{a}_y + 5\mathbf{a}_z}{\sqrt{33}} \approx 0.348\,\mathbf{a}_x - 0.348\,\mathbf{a}_y + 0.870\,\mathbf{a}_z$$

This $\mathbf{a}_{12}$ is exactly the direction that appears in [[Various Charge Distribution, Coulomb's Law]].

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Which product, and why?
> (a) Verify that the edge $\mathbf{A} \perp$ normal of a surface, (b) compute the area of a triangle with given corner vectors, (c) find the work done by a force along a displacement. Which product does each job?

> [!SUCCESS]- Step-by-Step Solution
> 1. (a) **Dot product**: perpendicularity test — require $\mathbf{A}\cdot\mathbf{a}_n = 0$.
> 2. (b) **Cross product**: triangle area $= \frac{1}{2}|\mathbf{AB} \times \mathbf{AC}|$ (half the parallelogram).
> 3. (c) **Dot product**: $W = \mathbf{F}\cdot\mathbf{d}$ — the component of force along motion does the work.
> 4. Mnemonic: *dot = scalar = alignment (work, flux, angle); cross = vector = turning/area (torque, normals, area).*

---

> [!QUESTION] Practice Question: Dot product sanity checks
> Compute $\mathbf{A}\cdot\mathbf{A}$ for any vector, and $(\mathbf{A}+\mathbf{B})\cdot(\mathbf{A}+\mathbf{B})$. What do these reveal?

> [!SUCCESS]- Step-by-Step Solution
> 1. $\mathbf{A}\cdot\mathbf{A} = A^2\cos 0° = |\mathbf{A}|^2$ — the self-dot recovers the magnitude squared (basis of $\cos\theta$ problems).
> 2. $(\mathbf{A}+\mathbf{B})^2 = A^2 + B^2 + 2\mathbf{A}\cdot\mathbf{B}$ — the vector "law of cosines". If $\mathbf{A}\perp\mathbf{B}$ the cross term vanishes and Pythagoras reappears.

---

## 6. Related Notes
- [[Introduction to 3D Coordinate Systems]] — where these components live ($\mathbf{a}_x$ vs $\mathbf{a}_\rho$ vs $\mathbf{a}_r$).
- [[Transformation of Vectors]] — converting a vector's components between systems (unit vectors change!).
- [[Concepts of Gradient]] — the dot product's star role: directional derivative $d\Phi = \nabla\Phi \cdot d\mathbf{l}$.
- [[Concepts of Curl]] — circulation is a close cousin of the cross product.

