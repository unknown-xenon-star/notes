---
title: "Introduction to 3D Coordinate Systems"
date: 2026-09-22
tags:
  - concept
  - emf
  - vector-analysis
  - coordinate-systems
aliases:
  - "3D Coordinate Systems"
  - "Cartesian Coordinate System"
  - "Cylindrical Coordinate System"
  - "Spherical Coordinate System"
status: completed
---

# 🌐 Introduction to 3D Coordinate Systems

> [!NOTE] 💡 The Big Picture Intuition
> A coordinate system is just a **naming scheme for locations in space**. Instead of one rigid "street grid" (Cartesian), nature gives us situations that scream for different maps: a wire's field is the same at every angle → **cylindrical**; a point charge's field depends only on distance → **spherical**. Choosing the right coordinate system is like choosing the right tool: a rectangular peg fits a rectangular hole. The entire subject of Electromagnetic Fields is built on the skill of **describing a point, a length, an area, and a volume in all three systems** — and switching between them fluently.

---

## 1. Why Three Systems? The GPS Analogy

- **Cartesian** $(x, y, z)$ — the city grid: "3 blocks east, 4 blocks north, 2 floors up." Best for **rectangular** objects (plates, slabs, boxes).
- **Cylindrical** $(\rho, \phi, z)$ — the tornado map: "how far from the axis $\rho$, at what compass angle $\phi$, at what height $z$." Best for **wires, tubes, coaxial cables**.
- **Spherical** $(r, \theta, \phi)$ — the radar/planet map: "how far from the centre $r$, at what polar tilt $\theta$ (down from the north pole), at what compass angle $\phi$." Best for **point charges, spheres, antennas**.

> [!IMPORTANT] 🎯 The Golden Rule of EMF
> Pick the coordinate system in which the **surfaces of your problem are constant-coordinate surfaces**. A point charge creates spherical equipotentials → spherical. An infinite line charge creates cylindrical field tubes → cylindrical. A parallel-plate capacitor creates flat sheets → Cartesian. The right choice turns ugly integrals into one-line answers.

---

## 2. The Three Systems at a Glance

| Feature | Cartesian | Cylindrical | Spherical |
| :--- | :---: | :---: | :---: |
| Coordinates | $(x, y, z)$ | $(\rho, \phi, z)$ | $(r, \theta, \phi)$ |
| Unit vectors | $\mathbf{a}_x, \mathbf{a}_y, \mathbf{a}_z$ | $\mathbf{a}_\rho, \mathbf{a}_\phi, \mathbf{a}_z$ | $\mathbf{a}_r, \mathbf{a}_\theta, \mathbf{a}_\phi$ |
| Range | $-\infty$ to $\infty$ each | $\rho \ge 0,\ 0 \le \phi < 2\pi$ | $r \ge 0,\ 0 \le \theta \le \pi,\ 0 \le \phi < 2\pi$ |
| Constant-coord surfaces | 3 pairs of planes | cylinder + half-plane + plane | sphere + cone + half-plane |
| Differential length $d\mathbf{l}$ | $dx\,\mathbf{a}_x + dy\,\mathbf{a}_y + dz\,\mathbf{a}_z$ | $d\rho\,\mathbf{a}_\rho + \rho\, d\phi\,\mathbf{a}_\phi + dz\,\mathbf{a}_z$ | $dr\,\mathbf{a}_r + r\, d\theta\,\mathbf{a}_\theta + r \sin\theta\, d\phi\,\mathbf{a}_\phi$ |
| Differential volume $dv$ | $dx\, dy\, dz$ | $\rho\, d\rho\, d\phi\, dz$ | $r^2 \sin\theta\, dr\, d\theta\, d\phi$ |

> [!WARNING] ⚠️ The $h$-Factors (Metric Coefficients)
> Notice the "stretch factors" $h_\phi = \rho$ (cylindrical) and $h_\theta = r$, $h_\phi = r\sin\theta$ (spherical). A small step $d\phi$ in angle covers an **arc length** $= (\text{radius to the axis of rotation}) \times d\phi$ — that radius is $\rho$ for the cylinder and $r\sin\theta$ for the sphere. Forgetting these factors is the **#1 exam mistake** in volume and surface integrals.

```
Cartesian dV:  cube                 Cylindrical dV:  wedge-brick            Spherical dV:  pyramid-brick
   dz |____                        side walls: dρ and ρdφ                  sides: r dθ and r sinθ dφ
      /   /|                       height: dz                              radial shell: dr
     /___/ |  dx                   all edges ≈ small                       all edges ≈ small
     |__| /                        volume = ρ dρ dφ dz                     volume = r² sinθ dr dθ dφ
        dy
```

---

## 3. Point Transformations (The Dictionary)

> [!IMPORTANT] 🎯 Cartesian ↔ Cylindrical
> $$\rho = \sqrt{x^2 + y^2}, \qquad \phi = \tan^{-1}\!\frac{y}{x}, \qquad z = z$$
> $$x = \rho \cos\phi, \qquad y = \rho \sin\phi, \qquad z = z$$

> [!IMPORTANT] 🎯 Cartesian ↔ Spherical
> $$r = \sqrt{x^2 + y^2 + z^2}, \qquad \theta = \cos^{-1}\!\frac{z}{r}, \qquad \phi = \tan^{-1}\!\frac{y}{x}$$
> $$x = r\sin\theta\cos\phi, \qquad y = r\sin\theta\sin\phi, \qquad z = r\cos\theta$$

**Memory hook**: $\rho = r\sin\theta$ is the "shadow" of $r$ on the $xy$-plane, and $z = r\cos\theta$ is its height. Then reuse the cylindrical dictionary for the $(\rho, y, x)$ part.

> [!TIP] 🧠 Calculator Quadrant Warning
> Always compute $\phi$ with $\tan^{-1}(y/x)$ **respecting the signs of $x$ and $y$** (use `atan2` or sketch the point). $\tan^{-1}(1)$ is $45°$ *or* $225°$ — the point's quadrant decides. Also: $\theta$ is measured **from the $+z$-axis** (0° at the north pole, 90° on the equator plane, 180° at the south pole), *not* from the $xy$-plane.

---

## 4. Worked Examples

### Worked Example 1: Cartesian → Cylindrical
> [!EXAMPLE] Problem
> Express the point $P(2, 2, 3)$ in cylindrical coordinates.

**Step 1: Radial distance** — $\rho = \sqrt{x^2 + y^2} = \sqrt{2^2 + 2^2} = \sqrt{8} = 2\sqrt{2} \approx 2.828$

**Step 2: Azimuth angle** — $\phi = \tan^{-1}\!\left(\frac{y}{x}\right) = \tan^{-1}\!\left(\frac{2}{2}\right) = \tan^{-1}(1) = 45°$ (first quadrant, so no adjustment needed)

**Step 3: Height is unchanged** — $z = 3$

$$\boxed{P\big(2\sqrt{2},\ 45°,\ 3\big) \approx (2.828,\ 45°,\ 3)}$$

**Check**: $x = 2.828\cos 45° = 2$ ✅, $y = 2.828\sin 45° = 2$ ✅.

### Worked Example 2: Cartesian → Spherical
> [!EXAMPLE] Problem
> Express the point $P(1, 1, \sqrt{6})$ in spherical coordinates.

**Step 1: Radius** — $r = \sqrt{x^2 + y^2 + z^2} = \sqrt{1 + 1 + 6} = \sqrt{8} = 2\sqrt{2} \approx 2.828$

**Step 2: Polar angle** — $\cos\theta = \dfrac{z}{r} = \dfrac{\sqrt{6}}{2\sqrt{2}} = \dfrac{\sqrt{3}}{2} \Rightarrow \theta = 30°$

**Step 3: Azimuth** — $\phi = \tan^{-1}\!\left(\frac{1}{1}\right) = 45°$

$$\boxed{P\big(2\sqrt{2},\ 30°,\ 45°\big)}$$

**Check**: $z = 2\sqrt{2}\cos 30° = 2\sqrt{2} \cdot \frac{\sqrt{3}}{2} = \sqrt{6}$ ✅.

### Worked Example 3: Volume Element in Spherical Coordinates
> [!EXAMPLE] Problem
> Find the volume of a sphere of radius $a$ using the spherical differential volume.

**Step 1: Write the element** — $dv = r^2 \sin\theta\, dr\, d\theta\, d\phi$

**Step 2: Set the limits for a full sphere** — $r: 0 \to a$, $\theta: 0 \to \pi$, $\phi: 0 \to 2\pi$

**Step 3: Integrate**

$$V = \int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^a r^2 \sin\theta\, dr\, d\theta\, d\phi = \left(\frac{a^3}{3}\right)\big(2\big)\big(2\pi\big) = \boxed{\frac{4}{3}\pi a^3}$$

**Why the factors matter**: drop the $\sin\theta$ and you would get $\frac{2\pi a^3}{3}$ — wrong by $2\times$ (you computed a double-cone, not a sphere).

---

## 5. Active Recall & Exam Self-Test

> [!QUESTION] Practice Question: Why does $d\phi$ alone have no length meaning?
> In cylindrical coordinates, why must the $\phi$-component of differential length be $\rho\, d\phi$ and not just $d\phi$?

> [!SUCCESS]- Step-by-Step Solution
> 1. $d\phi$ is an **angle** (dimensionless in radians), not a distance.
> 2. Arc length formula: $s = (\text{radius}) \times (\text{angle})$. A point at distance $\rho$ from the $z$-axis sweeps an arc $\rho\, d\phi$ when it rotates by $d\phi$.
> 3. The same angular step $d\phi = 0.01$ rad corresponds to a *bigger* physical step at larger $\rho$ — the stretch factor $h_\phi = \rho$ captures exactly this.
> 4. Same logic in spherical: the two angular stretch factors are $h_\theta = r$ and $h_\phi = r\sin\theta$ (the $\sin\theta$ shrinks the circle of latitude as you approach the poles).

---

> [!QUESTION] Practice Question: Which system for which object?
> You must integrate the field of (a) a coaxial cable, (b) a point charge, (c) a rectangular PCB trace. Which coordinate system for each, and why?

> [!SUCCESS]- Step-by-Step Solution
> 1. **Coaxial cable** → cylindrical: the conductors are surfaces of constant $\rho$; the field depends only on $\rho$.
> 2. **Point charge** → spherical: field magnitude depends only on $r$; equipotentials are constant-$r$ spheres.
> 3. **PCB trace (rectangular)** → Cartesian: boundaries are planes $x = \text{const}$, $y = \text{const}$.
> 4. Rule: make the *boundaries* constant-coordinate surfaces so limits become single numbers instead of functions.

---

## 6. Related Notes
- [[Review of Vectors]] — the algebra (dot, cross, components) used inside any system.
- [[Transformation of Vectors]] — how *directions* (unit vectors), not just points, change between systems.
- [[Various Charge Distribution, Coulomb's Law]] — first place where the spherical/cylindrical choice pays off.
- [[Concepts of Divergence]] — the $\nabla$ operator looks different in each system.

