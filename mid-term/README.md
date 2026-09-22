---
title: "README: Mid-Term Knowledge Vault"
date: 2026-09-19
tags:
  - welcome
  - hub
status: active
---

# 🚀 README: Mid-Term Preparation Vault

Welcome to your central Obsidian vault optimized for mid-term exam preparation across your academic subjects.

---

## 📚 Subject Modules

### 1. 📐 Applied Numerical Methods (ANM)
All notes, concept deep-dives, formula sheets, and PDF course materials for ANM are organized under the **`ANM/`** directory.

- 🏠 **[[00 - Numerical Methods Index|ANM Master Study Hub & MOC]]** — Full syllabus roadmap, concept graph, and module overview.
- ⚡ **[[Numerical Methods Formula Sheet|ANM High-Yield Formula Cheat Sheet]]** — Complete formula summary, convergence orders, and SDD criteria.
- 🧠 **ANM Concept Notes (`ANM/Concepts/`)** — 15 concept notes organized by category:

  #### 📌 Foundational Concepts
  - _[[Roots of Equations]]_ — Geometric roots, algebraic vs transcendental, IVT, multiplicity
  - _[[Errors and Convergence]]_ — Absolute/relative/approximate errors, Scarborough rule, convergence orders

  #### 📌 Bracketing (Closed) Methods
  - _[[Bisection Method]]_ — Interval halving, linear convergence ($p=1$), iteration bound
  - _[[Regula Falsi Method]]_ — False position, stagnant endpoint trap, Illinois algorithm

  #### 📌 Open Methods (Single Equation)
  - _[[Fixed-Point Iteration]]_ — $x = g(x)$, Lipschitz condition $|g'(x)| < 1$, Aitken $\Delta^2$
  - _[[Newton-Raphson Method]]_ — Tangent iteration, quadratic convergence ($p=2$), square roots
  - _[[Secant Method]]_ — Finite-difference slope, superlinear convergence ($p \approx 1.618$)

  #### 📌 Iterative Linear Systems ($A\mathbf{x} = \mathbf{b}$)
  - _[[Gauss-Jacobi Method]]_ — Simultaneous displacement, iteration matrix $T_J$, SDD condition
  - _[[Gauss-Seidel Method]]_ — Successive displacement, iteration matrix $T_{GS}$, $2\times$ acceleration

  #### 📌 Polynomial Solvers
  - _[[Graeffe's Root-Squaring Method]]_ — Polynomial root separation via squarings, Descartes' Rule
  - _[[Lin-Bairstow Method]]_ — Double synthetic division, quadratic factor extraction

  #### 📌 Interpolation Methods
  - _[[Lagrange Interpolation]]_ — Basis polynomials, uniqueness theorem, interpolation error
  - _[[Newton Divided Difference Interpolation]]_ — Divided differences, incremental construction
  - _[[Newton Forward and Backward Difference Interpolation]]_ — Equally spaced nodes, $\Delta$/$\nabla$ operators
  - _[[Stirling's Formula]]_ — Node-centred central differences, symmetric averaging, best mid-table accuracy
  - _[[Bessel's Formula]]_ — Midpoint-centred central differences for targets between two central nodes
  - _[[Cubic Spline Interpolation]]_ — Piecewise cubics, $C^2$ continuity, Natural/Clamped/Not-a-Knot

### 2. 🌲 Data Structures & Algorithms (DSA)
All DSA notes live under the **`DSA/`** directory.

- 🏠 **[[00 - Data Structures and Algorithms Index|DSA Master Study Hub & MOC]]** — Syllabus roadmap, concept graph, and module overview.
- 🧠 **DSA Concept Notes (`DSA/Concepts/`)** — 4 concept notes:

  #### 📌 Foundations
  - _[[Asymptotic Analysis]]_ — $O$/$\Omega$/$\Theta$ bounds, complexity ladder, loop analysis, space complexity

  #### 📌 Linear Data Structures
  - _[[Arrays]]_ — Contiguous memory, $O(1)$ address arithmetic, shifting tax, dynamic doubling
  - _[[Linked List]]_ — Singly, doubly, and circular flavours; 3-pointer reversal; array-vs-list trade-offs
  - _[[Stack]]_ — LIFO, array/linked implementations, postfix evaluation, balanced parentheses

---

### 3. ⚡ Electromagnetic Fields (EMF)
All EMF notes live under the **`EMF/`** directory.

- 🏠 **[[00 - Electromagnetic Fields Index|EMF Master Study Hub & MOC]]** — Syllabus roadmap, concept graph, and module overview.
- 🧠 **EMF Concept Notes (`EMF/Concepts/`)** — 11 concept notes:

  #### 📌 Vector Analysis Toolkit
  - _[[Introduction to 3D Coordinate Systems]]_ — Cartesian/cylindrical/spherical systems, $h$-factors, $d\mathbf{l}$ and $dv$ elements
  - _[[Review of Vectors]]_ — dot & cross products, projections, distance vectors
  - _[[Transformation of Vectors]]_ — same vector, new components; the four conversion tables
  - _[[Concepts of Gradient]]_ — steepest ascent, directional derivative, $\mathbf{E} = -\nabla V$
  - _[[Concepts of Divergence]]_ — sources/sinks, divergence theorem, $\nabla\cdot\mathbf{D} = \rho_v$
  - _[[Concepts of Curl]]_ — circulation, paddle wheel, Stokes' theorem, $\nabla\times\mathbf{E} = 0$

  #### 📌 Electrostatics
  - _[[Various Charge Distribution, Coulomb's Law]]_ — four charge distributions, Coulomb's law, superposition, the slicing recipe
  - _[[Determination of Static Electric Fields]]_ — field concept, three strategies, ring/disc/dipole fields
  - _[[Application of Gauss Law, Maxwell's First Equation]]_ — flux, $\mathbf{D} = \varepsilon\mathbf{E}$, symmetry recipe, point form
  - _[[Electric Potential]]_ — scalar terrain, path independence, $W = q\Delta V$
  - _[[Boundary Relations of Electric Fields]]_ — pillbox & loop conditions, field refraction, conductor rules

---

## 🔑 Vault Standards & Pedagogical Architecture
1. **Human-First Conceptual Language**: Plain-English analogies, Feynman-technique explanations, and intuitive mental models.
2. **Standardized $\LaTeX$ Mathematics**: High-clarity equations, derivations, matrices, and step-by-step formulas.
3. **Line-by-Line Worked Examples**: Fully calculated numerical walkthroughs that you can follow step-by-step with your scientific calculator.
4. **Active Recall & Exam Self-Tests**: Interactive question blocks with collapsible solution keys (`> [!QUESTION]` and `> [!SUCCESS]- Solution`).