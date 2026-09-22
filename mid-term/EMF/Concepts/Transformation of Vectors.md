---
title: "Transformation of Vectors"
date: 2026-09-22
tags:
  - concept
  - emf
  - vector-analysis
  - coordinate-transformations
aliases:
  - "Vector Transformations"
  - "Coordinate Transformation of Vectors"
  - "Unit Vector Transformations"
  - "Rotation Matrix"
status: completed
---

# 🔄 Transformation of Vectors

> [!NOTE] 💡 The Big Picture Intuition
> A physical vector — a force, a velocity, an electric field — is a **real arrow in space**. It does not change when you change the map you draw it on; only its **components** (the shadow it casts on each axis) change. Think of describing the same wind using a north–east grid vs a compass rose: the wind is one thing, its "north speed" and "east speed" differ. Vector transformation is exactly this: **same arrow, new shadow measurements**. The subtle (and exam-favourite) part: in curvilinear systems the *unit vectors themselves* depend on position — $\mathbf{a}_\rho$ at $\phi = 45°$ is a different arrow from $\mathbf{a}_\rho$ at $\phi = 90°$ — so a transformation is only meaningful **at a specified point**.

---

## 1. The Golden Rule: Same Vector, New Components

$$\mathbf{A} = A_x\mathbf{a}_x + A_y\mathbf{a}_y + A_z\mathbf{a}_z = A_\rho\mathbf{a}_\rho + A_\phi\mathbf{a}_\phi + A_z\mathbf{a}_z = A_r\mathbf{a}_r + A_\theta\mathbf{a}_\theta + A_\phi\mathbf{a}_\phi$$

The magnitude is invariant — the best self-check of any transformation:
$$|\mathbf{A}| = \sqrt{A_x^2 + A_y^2 + A_z^2} = \sqrt{A_\rho^2 + A_\phi^2 + A_z^2} = \sqrt{A_r^2 + A_\theta^2 + A_\phi^2}$$

> [!IMPORTANT] 🎯 The Recipe (works for every case)
> 1. **Know the point** — curvilinear unit vectors depend on the angles there.
> 2. **Dot with the new unit vectors**: $A_{\text{new}} = \mathbf{A}\cdot\mathbf{a}_{\text{new}}$ (this is all the "matrices" below really do).
> 3. **Check** $|\mathbf{A}|$ is unchanged.

---

## 2. The Projection Picture (Why the Formulas Work)

> [!TIP] 🧠 Cylindrical unit vectors at angle $\phi$
> At the point with azimuth $\phi$, the unit vectors are projections of the fixed Cartesian axes:
> $$\mathbf{a}_\rho = \cos\phi\,\mathbf{a}_x + \sin\phi\,\mathbf{a}_y \qquad (\text{outward, in the } xy\text{-plane})$$
> $$\mathbf{a}_\phi = -\sin\phi\,\mathbf{a}_x + \cos\phi\,\mathbf{a}_y \qquad (\text{tangential, } 90° \text{ CCW from } \mathbf{a}_\rho)$$
> $$\mathbf{a}_z = \mathbf{a}_z \qquad (\text{shared})$$
>
> **Spherical**: $\mathbf{a}_r = \sin\theta\cos\phi\,\mathbf{a}_x + \sin\theta\sin\phi\,\mathbf{a}_y + \cos\theta\,\mathbf{a}_z$, with $\mathbf{a}_\theta$ pointing "downhill" along the meridian and $\mathbf{a}_\phi$ the same tangential direction as in cylindrical.

Each matrix is literally a table of **dot products between old and new unit vectors** — row $i$, column $j$ entry = $\mathbf{a}_{\text{new},i}\cdot\mathbf{a}_{\text{old},j}$. Fill the table from a sketch and you never need to memorize signs.

---

## 3. The Four Conversion Tables

### Cartesian → Cylindrical
$$\begin{bmatrix} A_\rho \\ A_\phi \\ A_z \end{bmatrix} = \begin{bmatrix} \cos\phi & \sin\phi & 0 \\ -\sin\phi & \cos\phi & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} A_x \\ A_y \\ A_z \end{bmatrix}$$

i.e. $A_\rho = A_x\cos\phi + A_y\sin\phi$, $\quad A_\phi = -A_x\sin\phi + A_y\cos\phi$, $\quad A_z = A_z$.

### Cylindrical → Cartesian
$$\begin{bmatrix} A_x \\ A_y \\ A_z \end{bmatrix} = \begin{bmatrix} \cos\phi & -\sin\phi & 0 \\ \sin\phi & \cos\phi & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} A_\rho \\ A_\phi \\ A_z \end{bmatrix}$$

i.e. $A_x = A_\rho\cos\phi - A_\phi\sin\phi$, $\quad A_y = A_\rho\sin\phi + A_\phi\cos\phi$.

> [!TIP] 🧠 Memory hooks
> - **Cartesian → Cylindrical**: multiply by $+\cos\phi, +\sin\phi$ (project onto $\mathbf{a}_\rho$ then $\mathbf{a}_\phi$).
> - **Cylindrical → Cartesian**: $\cos\phi$ keeps its sign on $A_x$, $\sin\phi$ keeps its sign on $A_y$ ("cos stays with $x$, sin stays with $y$").
> - The two matrices are **transposes of each other** (orthogonal rotation matrices) — inverse = flip the sign of the off-diagonal $\sin\phi$ terms.

### Spherical → Cartesian
$$\begin{aligned}
A_x &= A_r\sin\theta\cos\phi + A_\theta\cos\theta\cos\phi - A_\phi\sin\phi \\
A_y &= A_r\sin\theta\sin\phi + A_\theta\cos\theta\sin\phi + A_\phi\cos\phi \\
A_z &= A_r\cos\theta - A_\theta\sin\theta
\end{aligned}$$

### Cartesian → Spherical
$$\begin{bmatrix} A_r \\ A_\theta \\ A_\phi \end{bmatrix} = \begin{bmatrix} \sin\theta\cos\phi & \sin\theta\sin\phi & \cos\theta \\ \cos\theta\cos\phi & \cos\theta\sin\phi & -\sin\theta \\ -\sin\phi & \cos\phi & 0 \end{bmatrix} \begin{bmatrix} A_x \\ A_y \\ A_z \end{bmatrix}$$

**Route strategy**: spherical ↔ Cartesian directly is heavy. When both endpoints are known in cylindrical terms, go **Cartesian → cylindrical → spherical** in two light steps instead of one heavy one. (Also remember the dictionary $\rho = r\sin\theta$, $z = r\cos\theta$ for point conversion.)

> [!WARNING] ⚠️ The Two Classic Mistakes
> 1. **Transforming the point but not the vector** — or vice versa. Points convert by the *dictionary* of [[Introduction to 3D Coordinate Systems]]; vector *components* convert by the tables above. Different operations!
> 2. **Using one angle everywhere** — the components at $\phi = 45°$ need $\phi = 45°$ plugged into every trig factor. Taking $\sin\phi$ at the wrong point invalidates the whole answer.

---

## 4. Worked Examples

### Worked Example 1: Cartesian → Cylindrical (a vector that becomes purely radial)
> [!EXAMPLE] Problem
> Express $\mathbf{A} = 2\mathbf{a}_x + 2\mathbf{a}_y$ at point $P(1, 1, 0)$ in cylindrical components.

**Step 1: Find the point's angle** — $\phi = \tan^{-1}(y/x) = \tan^{-1}(1) = 45°$

**Step 2: Apply the formulas**
$$A_\rho = A_x\cos\phi + A_y\sin\phi = 2\cos 45° + 2\sin 45° = 2\cdot\tfrac{\sqrt{2}}{2} + 2\cdot\tfrac{\sqrt{2}}{2} = 2\sqrt{2} \approx 2.828$$
$$A_\phi = -A_x\sin\phi + A_y\cos\phi = -2\sin 45° + 2\cos 45° = 0$$

**Step 3: Result & check**
$$\mathbf{A} = 2\sqrt{2}\,\mathbf{a}_\rho \approx 2.828\,\mathbf{a}_\rho, \qquad |\mathbf{A}|: \sqrt{8} \to 2\sqrt{2} \ ✅$$

**Geometric sanity**: the point $P(1,1)$ lies exactly on the ray $\phi = 45°$, and the vector $(2,2)$ points *along* that ray — so it must have zero swirl component $A_\phi$. ✅

### Worked Example 2: Cylindrical → Cartesian (pure tangential direction)
> [!EXAMPLE] Problem
> Express $\mathbf{A} = 3\mathbf{a}_\rho + 4\mathbf{a}_\phi + 5\mathbf{a}_z$ at $\phi = 90°$ in Cartesian components.

**Step 1: Evaluate the trig factors** — $\sin 90° = 1$, $\cos 90° = 0$

**Step 2: Convert**
$$A_x = A_\rho\cos\phi - A_\phi\sin\phi = 3(0) - 4(1) = -4$$
$$A_y = A_\rho\sin\phi + A_\phi\cos\phi = 3(1) + 4(0) = 3$$
$$A_z = 5$$

**Step 3: Check** — $|\mathbf{A}| = \sqrt{9 + 16 + 25} = \sqrt{50} = 5\sqrt{2}$ on both sides ✅
$$\boxed{\mathbf{A} = -4\mathbf{a}_x + 3\mathbf{a}_y + 5\mathbf{a}_z}$$

**Geometric sanity**: at $\phi = 90°$ (the $+y$ axis), $\mathbf{a}_\rho = \mathbf{a}_y$ and $\mathbf{a}_\phi = -\mathbf{a}_x$. So $3\mathbf{a}_\rho = 3\mathbf{a}_y$, $4\mathbf{a}_\phi = -4\mathbf{a}_x$ → $(-4, 3, 5)$ ✅

### Worked Example 3: Cartesian → Spherical via the Radial Shortcut
> [!EXAMPLE] Problem
> Express $\mathbf{A} = \mathbf{a}_x + \mathbf{a}_y + \sqrt{6}\,\mathbf{a}_z$ at $P(1, 1, \sqrt{6})$ in spherical components.

**Step 1: Point in spherical form** — $r = \sqrt{8} = 2\sqrt{2}$, $\theta = 30°$, $\phi = 45°$ (from [[Introduction to 3D Coordinate Systems]], Worked Example 2)

**Step 2: Spot the shortcut first** — the vector $(1, 1, \sqrt{6})$ points exactly *away from the origin through $P$* — it is a **radially outward** vector, so it must be pure $\mathbf{a}_r$.

**Step 3: Confirm by formula** — with $\theta = 30°$, $\phi = 45°$: $\sin\theta = \frac{1}{2}$, $\cos\theta = \frac{\sqrt{3}}{2}$, $\sin\phi = \cos\phi = \frac{\sqrt{2}}{2}$:

**Horizontal ($r$-component):**
$$A_r = (1)(\tfrac{1}{2}\cdot\tfrac{\sqrt{2}}{2}) + (1)(\tfrac{1}{2}\cdot\tfrac{\sqrt{2}}{2}) + \sqrt{6}\cdot\tfrac{\sqrt{3}}{2} = 0.3536 + 0.3536 + 2.1213 = 2.8284$$

**Meridian ($\theta$-component):**
$$A_\theta = (1)(\tfrac{\sqrt{3}}{2}\cdot\tfrac{\sqrt{2}}{2}) + (1)(\tfrac{\sqrt{3}}{2}\cdot\tfrac{\sqrt{2}}{2}) - \sqrt{6}\cdot\tfrac{1}{2} = 0.6124 + 0.6124 - 1.2247 = 0$$

**Azimuth ($\phi$-component):**
$$A_\phi = -(1)\tfrac{\sqrt{2}}{2} + (1)\tfrac{\sqrt{2}}{2} = 0$$$

$$\boxed{\mathbf{A} = 2\sqrt{2}\,\mathbf{a}_r \approx 2.828\,\mathbf{a}_r, \qquad A_\theta = A_\phi = 0}$$

**Check**: $|\mathbf{A}| = \sqrt{1 + 1 + 6} = 2\sqrt{2}$ preserved ✅. The shortcut ("if $\mathbf{A} \parallel \mathbf{r}$, expect pure $\mathbf{a}_r$") turned a page of algebra into one line.

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why is the transformation meaningless without a point?
> "Convert $\mathbf{A} = 2\mathbf{a}_x + 2\mathbf{a}_y$ to cylindrical." Why is this instruction incomplete?

> [!SUCCESS]- Step-by-Step Solution
> 1. Cylindrical unit vectors $\mathbf{a}_\rho, \mathbf{a}_\phi$ are functions of position: $\mathbf{a}_\rho(\phi) = \cos\phi\,\mathbf{a}_x + \sin\phi\,\mathbf{a}_y$.
> 2. Without the point, $\phi$ is unknown, so the projection coefficients $\cos\phi, \sin\phi$ are unknown.
> 3. Correct form: "Convert $\mathbf{A}$ **at the point** $P(1,1,0)$" → then $\phi = 45°$ and the procedure is well-defined.
> 4. Only $\mathbf{a}_z$ is position-independent. In spherical, *all three* unit vectors vary from point to point.

---

> [!QUESTION] Practice Question: Rotation matrix acting on a basis vector
> What does the Cartesian→cylindrical matrix do to the input $\mathbf{a}_x = (1, 0, 0)^T$ at a general $\phi$? Interpret the output.

> [!SUCCESS]- Step-by-Step Solution
> 1. Output components: $A_\rho = \cos\phi$, $A_\phi = -\sin\phi$, $A_z = 0$.
> 2. So $\mathbf{a}_x = \cos\phi\,\mathbf{a}_\rho - \sin\phi\,\mathbf{a}_\phi$ — the matrix applied to a *unit vector* returns its components in the new basis.
> 3. Sketch check at $\phi = 90°$: $\mathbf{a}_x$ should equal $-\mathbf{a}_\phi$ there (tangential direction at the $+y$-axis points in $-x$) → components $(0, -1, 0)$ ✅.
> 4. This is the same "dot-with-new-basis" recipe: rows of the matrix are the new unit vectors written in old components.

---

## 6. Related Notes
- [[Introduction to 3D Coordinate Systems]] — point transformations and the $h$-factors ($\rho\,d\phi$, $r\,d\theta$, $r\sin\theta\,d\phi$).
- [[Review of Vectors]] — the dot product *is* the transformation engine ($A_{\text{new}} = \mathbf{A}\cdot\mathbf{a}_{\text{new}}$).
- [[Various Charge Distribution, Coulomb's Law]] — why field expressions are written per-system (e.g. $E_\theta = 0$ for a point charge).
- [[Concepts of Curl]] — cross/dot structure of the curl operator in all three systems.

