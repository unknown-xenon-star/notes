# Rules for Obsidian Mid-Term Notes: LaTeX, Human-First Pedagogy & Examples

## 1. LaTeX Notation Everywhere
- Format every single mathematical symbol, variable, coefficient, index, equation, bounds, error, and formula using LaTeX.
- Inline math: `$x_k$`, `$f'(x)$`, `$\alpha \in [a, b]$`, `$\epsilon = 10^{-4}$`.
- Block equations: Use `$$ ... $$` with aligned blocks (`\begin{aligned} ... \end{aligned}`) or matrices (`\begin{bmatrix} ... \end{bmatrix}`).
- Avoid unformatted plain-text math like `x_k+1 = x_k - f(x_k)/f'(x_k)`. Always write `$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$`.
- In Markdown tables, avoid pipe collision with absolute values by using properly enclosed `$|g'(x)|$` or `$\vert g'(x) \vert$`.

## 2. Human-First Conceptual Language (Feynman Technique)
- **Big Picture First**: Start every note with an intuitive, non-jargon explanation of what the method does and the problem it solves.
- **Visual Analogies**: Use intuitive analogies (e.g., ski slopes, binary search, recipe cooking, amplifying acoustic signals) to build lasting mental models.
- **Explain the "Why"**: Don't just present equations; explain what each term physically or geometrically represents.
- **Clarity over Complexity**: Use conversational, engaging, yet academically rigorous prose.

## 3. Mandatory Worked Examples & Calculator Steps
- Every concept note must include at least one fully worked, step-by-step numerical example.
- Break down each calculation line-by-line so students can follow along step-by-step with their scientific calculator:
  - Step 1: Verification of prerequisites / initial conditions
  - Step 2: Substitution into the iteration formula
  - Step 3: Explicit intermediate arithmetic
  - Step 4: Error calculation and convergence check
  - Step 5: Iteration summary table
- Provide active recall self-test practice problems with collapsible `> [!SUCCESS]- Solution` callouts.
