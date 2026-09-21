# Changes Ongoing - Mid-Term Knowledge Vault

## Overview
This file tracks all changes made to the Mid-Term Knowledge Vault (ANM). It serves as a persistent changelog so that if the work is transferred to another AI, the history can be resumed seamlessly.

## Version History

### v1.0 - Initial Setup (2026-09-19)
- Created main vault structure with ANM subfolders
- Added core README.md with project overview
- Organized ANM concept notes (15 files covering roots, interpolation, iterative methods, splines)
- Configured Obsidian vault settings (.obsidian/config)
- Added skill definitions (midterm-prep, obsidian-vault)
- Created index.md mapping all concepts
- Added PDF course material (Errors and Convergence.pdf)
- Set up maintenance scripts (fix_index.py, fix_index.ps1)

### v1.1 - Interpolation Methods Completion (2026-09-19)
- Completed all 15 ANM concept notes:
  - Roots of Equations (including multiplicity, Descartes' Rule)
  - Errors and Convergence (absolute/relative error, convergence orders)
  - Bisection Method (interval bisection, guarantees)
  - Regula Falsi Method (linear interpolation, stagnation handling)
  - Fixed-Point Iteration (general theory, convergence conditions)
  - Newton-Raphson Method (derivatives, quadratic convergence)
  - Secant Method (finite difference, no derivative needed)
  - Gauss-Jacobi Method (simultaneous displacement)
  - Gauss-Seidel Method (successive displacement)
  - Graeffe's Root-Squaring Method (polynomial root isolation)
  - Lin-Bairstow Method (quadratic factorization)
  - Cubic Spline Interpolation (piecewise cubic, local control)
  - Newton Divided Difference (forward/backward differences)
  - Newton Forward/Backward Difference (equal-spacing optimizations)
- Created high-yield formula sheet (Summaries/Numerical Methods Formula Sheet.md)
- Added practice question templates and active recall structures

### v1.2 - Skills & Configuration (2026-09-19)
- Defined midterm-prep skill (study material generation, mock exams, Cornell notes)
- Defined obsidian-vault skill (wiki standards, linking, frontmatter)
- Configured Obsidian vault settings (PDF export, appearance, plugins, graph)
- Verified all files are properly linked and indexed

### v1.3 - Interpolation Cleanup & Index Update (2026-09-20)
- Repaired structural duplication in the interpolation notes:
  - Lagrange Interpolation: restored the misplaced "Special Cases (Linear & Quadratic)" section as Section 4, removed the empty duplicate "## 2" heading and the duplicated basis-polynomial block at the end of the file, fixed section numbering (1-7).
  - Newton Divided Difference: moved "The Divided Difference Table" (Section 3) back between Sections 2 and 4, removed the duplicate block after Related Notes.
  - Newton Forward/Backward: restored the two missing rows of the "When to Use Which?" table that had been split off to the end of the file.
- Added Module 6 "Interpolation & Curve Fitting" to the ANM Mermaid knowledge graph and syllabus in `ANM/00 - Numerical Methods Index.md` (now links all 4 interpolation notes).
- Removed stale one-off scripts `fix_index.py` / `fix_index.ps1` (hardcoded `E:/` Windows paths; their intended index fix is now applied directly).
- Fixed "How to Resume" to reference the actual index file location.

### v1.4 - Integration (Quadrature) Module (2026-09-20)
- Added 6 new concept notes in `ANM/Concepts/`:
  - Lagrange Inverse Interpolation (swapped-variable formula, three-point root estimate, secant connection)
  - Trapezoidal Rule (composite scheme, geometric bias, worked example on 1/(1+x²), n=6)
  - Simpson's 1/3 Rule (parabolic panels, 1-4-2 weight pattern, exact-for-cubics proof, n=6 example)
  - Simpson's 3/8 Rule (cubic panels, 1-3-3-1 weights, single + composite examples, hybrid strategies)
  - Weddle's Rule (6th-difference rule, 41/140 → 3/10 swap, 1-5-1-6-1-5-1 pattern, examples vs Simpson)
  - Error in Quadrature Formulas – Trapezoidal, Simpson's (single-panel + composite error terms, strip-doubling law, tolerance-driven n, Richardson/Romberg)
- All worked-example numbers verified computationally (quadrature results vs π/4, ln 4, ln 7; root estimates vs bisection).
- Updated `ANM/00 - Numerical Methods Index.md`: added Module 7 "Numerical Integration (Quadrature)" to Mermaid graph + syllabus, linked Lagrange Inverse Interpolation under Module 6.
- Updated `ANM/Summaries/Numerical Methods Formula Sheet.md`: added Section 5 "Numerical Integration (Quadrature)" comparison table, renumbered error section, extended quick links.

### v1.5 - DSA Subject Module (2026-09-21)
- Created new subject folder `DSA/` with `Concepts/` subfolder, mirroring the ANM structure.
- Added 4 concept notes in `DSA/Concepts/`:
  - Asymptotic Analysis (Big-O/Ω/Θ, complexity ladder, loop analysis, space complexity)
  - Arrays (address arithmetic base+i×w, row-major 2D, shifting tax, dynamic doubling)
  - Linked List (singly, doubly, circular; reversal; array-vs-list trade-offs)
  - Stack (LIFO, array/linked implementations, postfix evaluation, balanced parentheses)
- Created master index `DSA/00 - Data Structures and Algorithms Index.md` with Mermaid knowledge graph + syllabus modules.
- Updated `README.md` to register DSA as subject module 2.

### v1.7 - DSA Notes Converted to C++ (2026-09-21)
- Standing rule added to `.agents/rules/pedagogy_and_latex.md`: **all code in DSA notes must be C/C++ only**.
- Converted all 8 Python code blocks across the 4 DSA notes to C++ (`#include <bits/stdc++.h>`):
  - Asymptotic Analysis: loop-analysis snippets (`` ```cpp `` callouts) + complexity-table program.
  - Arrays: vector capacity-doubling watcher, manual shift-insert, two-pointer reverse.
  - Linked List: full SinglyLinkedList class (insertHead/insertTail/remove/search/reverse) + circular Josephus round-robin; section-4 pseudocode rewritten as real C++.
  - Stack: template ArrayStack class, postfix evaluator, balanced-parentheses checker.
- Every program compiled with `g++ -std=c++17 -Wall` and executed; documented outputs corrected to actual results (Josephus order is C A E B with survivor D — the old Python comment was wrong).

### v1.8 - DSA Syllabus Expansion: 7 New Concept Notes (2026-09-21)
- Created 7 new notes in `DSA/Concepts/` (all C++, all compiled & run):
  - **Introduction to Data Structures** (definitions, D-A-F triplet, classification tree, ADT vs implementation, operation-cost table)
  - **Algorithm Evaluation** (algorithm properties, criteria, apriori vs apostiori, design techniques, O(1)-vs-O(n) timing demo)
  - **Multi-dimensional Arrays** (row/column-major, 2D/3D address formulas, lower-bound variants, cache benchmark)
  - **Sparse Matrices** (sparsity threshold 3(t+1) < mn, triplet representation, merge-add, verified against hand example)
  - **Structure** (heterogeneous records, padding, struct-vs-array, offsetof verification)
  - **Pointers** (&/*, pointer arithmetic = array formula, new/delete, dangling pointers, trace examples)
  - **Infix, Postfix and Prefix Notations** (precedence table, shunting-yard traces, infix→prefix via reverse, postfix/prefix evaluation)
- Skipped as already-present: Arrays, Stack (representation + operations + applications), per user's "skip if present" instruction.
- Updated `DSA/00 - Data Structures and Algorithms Index.md`: Mermaid graph now shows all 11 notes with construction/trade-off edges; Foundations module expanded to 5 notes, Linear module to 6 notes.
- Added cross-links: Arrays ↔ Multi-dimensional Arrays/Sparse Matrices/Structure, Stack → Notations, Linked List → Pointers/Structure, Asymptotic Analysis → Algorithm Evaluation/Intro.

### v1.6 - Simpson Filename & Wikilink Repair (2026-09-21)
- Renamed two notes whose filenames contained `/` (an illegal path character, which made every wikilink pointing at them dead):
  - `Simpson's 1-3 Rule.md` → `Simpson's One-Third Rule.md`
  - `Simpson's 3-8 Rule.md` → `Simpson's Three-Eighths Rule.md`
- Converted all 33 `[[Simpson's 1/3 Rule]]` / `[[Simpson's 3/8 Rule]]` wikilink instances across 8 files (including Mermaid graph links) to the new legal filenames; titles and frontmatter untouched.
- Added `"Simpson's 1/3 Rule"` / `"Simpson's 3/8 Rule"` frontmatter aliases so legacy spellings still resolve in Obsidian's quick switcher.
- Verified integrity: all other tracked markdown files byte-identical to git; zero residual old-style links.

## Change Log

| Version | Date | Author | Changes | Status |
|---------|------|--------|---------|--------|
| v1.0 | 2026-09-19 | User | Initial setup - created vault structure, README, ANM notes, Obsidian config | Completed |
| v1.1 | 2026-09-19 | User | Completed all 15 ANM concept notes, formula sheet, practice templates | Completed |
| v1.2 | 2026-09-19 | User | Added midterm-prep and obsidian-vault skills, configured Obsidian settings | Completed |
| v1.3 | 2026-09-20 | User | Fixed interpolation note structure, added Interpolation module (6) to ANM index, removed stale fix_index scripts | Completed |
| v1.4 | 2026-09-20 | AI (Codebuff) | Added 6 integration/quadrature notes (Lagrange inverse interpolation, Trapezoidal, Simpson 1/3 & 3/8, Weddle, quadrature errors), updated index + formula sheet | Completed |
| v1.5 | 2026-09-21 | AI (Codebuff) | Created DSA subject folder with 4 concept notes (Asymptotic Analysis, Arrays, Linked List, Stack) + master index MOC; registered subject in README | Completed |
| v1.6 | 2026-09-21 | AI (Codebuff) | Renamed Simpson notes to legal filenames (no `/`), fixed all 34 dead wikilinks, added alias coverage | Completed |
| v1.7 | 2026-09-21 | AI (Codebuff) | Converted all DSA Python code to C++, added C/C++-only rule, compile-verified every snippet | Completed |
| v1.8 | 2026-09-21 | AI (Codebuff) | Added 7 DSA concept notes (Intro DS, Algorithm Evaluation, Multi-dim Arrays, Sparse Matrices, Structure, Pointers, Notations), updated index + cross-links | Completed |

## Recent Activity

### 2026-09-19
- Created `changes_ongoing.md` (this file)
- Organized ANM concept notes in `/ANM/Concepts/`
- Built master index in `index.md` with Mermaid flowchart
- Added PDF course material (`Errors and Convergence.pdf`)
- Configured Obsidian vault settings
- Defined skill profiles for midterm prep and Obsidian management

### 2026-09-19
- Wrote all 15 ANM concept notes (Roots, Interpolation, Iterative Methods, Splines)
- Created high-yield formula cheat sheet
- Established active recall question formats

### 2026-09-20
- Repaired duplicated/misplaced sections in the three interpolation notes
- Added Interpolation & Curve Fitting (Module 6) to the ANM index and Mermaid graph
- Removed obsolete `fix_index.py` / `fix_index.ps1` scripts
- Added Lagrange Inverse Interpolation note and 5 numerical-integration notes (Module 7)
- Verified all worked examples numerically; updated formula sheet with quadrature tables

## File Status

| File | Status | Last Modified |
|------|--------|---------------|
| README.md | ✅ Active | 2026-09-19 |
| ANM/00 - Numerical Methods Index.md | ✅ Active | 2026-09-19 |
| ANM/Concepts/*.md | ✅ Active | 2026-09-20 |
| .obsidian/*.json | ✅ Active | 2026-09-19 |
| .obsidian/workspace.json | ✅ Active | 2026-09-19 |
| .obsidian/app.json | ✅ Active | 2026-09-19 |
| .obsidian/core-plugins.json | ✅ Active | 2026-09-19 |
| .obsidian/graph.json | ✅ Active | 2026-09-19 |
| ANM/Errors and Convergence.pdf | ✅ Active | 2026-09-19 |

## How to Resume

If this vault is moved to another AI or shared with others:

1. Load `changes_ongoing.md` to see the complete history
2. Navigate to `ANM/` folder for all concept notes
3. Use `README.md` for overall project overview
4. Refer to `ANM/00 - Numerical Methods Index.md` for the knowledge map
5. All files are properly linked and ready to use

## Future Improvements

- Add more advanced topics (optimization, differential equations)
- Create more practice exam questions
- Implement automated quiz generation
- Add video resource links
- Expand to other courses in the vault

---
*Generated on 2026-09-19*
*Last updated: 2026-09-21*
*Version: v1.8*
