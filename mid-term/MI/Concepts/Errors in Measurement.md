---
title: "Errors in Measurement"
date: 2026-09-25
tags:
  - concept
  - mi
  - measurement-and-instrumentation
  - errors
aliases:
  - "Types of Errors in Measurement"
  - "Propagation of Errors"
  - "Limiting Error"
status: completed
---

# 🚨 Errors in Measurement

> [!NOTE] 💡 The Big Picture Intuition
> No measurement is ever perfect — the true value is a horizon you approach but never touch. The professional move is not to pretend errors away but to **name them, classify them, and compute how they spread** through your calculations. Why bother classifying? Because each error *family* has a different cure: gross errors are cured by **care**, systematic errors by **calibration and compensation**, and random errors by **averaging**. Diagnose the family, and the fix is obvious.

---

## 1. The Error Family Tree

```
                    Errors in Measurement
                   /         |          \
          GROSS ERRORS   SYSTEMATIC    RANDOM ERRORS
          (human blunders)  ERRORS      (unpredictable scatter)
                           /     |      \
                   INSTRUMENTAL ENVIRON- OBSERVATIONAL
                      ERRORS   MENTAL      ERRORS
                               ERRORS
```

### 1.1 Gross Errors
**Human blunders**: misreading the scale (parallax), transposing digits while recording, using a wrong scale factor, connecting the instrument wrongly, computing carelessly.

- **Cure**: care, double-checking, repeating readings by different observers, automated recording. You cannot *calculate* gross errors away — only discipline them out.

### 1.2 Systematic Errors
Errors that follow a **definite law** — repeatable, and therefore correctable once identified. Three sub-families:

| Sub-type | Source | Example | Remedy |
| :--- | :--- | :--- | :--- |
| **Instrumental** | Imperfect design/adjustment, ageing, loading effect of the instrument itself | Zero off-set on a voltmeter, friction in bearings, a stretched spring, DMM loading a high-resistance circuit | Calibration, correction factors, proper design, high-impedance instruments |
| **Environmental** | External conditions: temperature, pressure, humidity, magnetic/electrostatic fields, supply-voltage variation | Resistance change with temperature; stray-field pickup; expansion of scale | Temperature compensation, shielding, control of conditions, corrections computed from known laws |
| **Observational** | How the *observer* reads the instrument | **Parallax error** on analog scales; stroboscopic/synchronization errors | Mirror-backed scales, digital displays, careful eye position |

> [!TIP] 🧠 Which systematic error is it? Ask *who/what* is misbehaving
> The **instrument** misbehaves → instrumental. The **environment** disturbs it → environmental. The **observer** reads it wrongly → observational.

### 1.3 Random Errors
Unpredictable variations — tiny fluctuations in friction, supply, or human reaction time — occurring **without a fixed law**, equally likely to be $+$ or $-$. They make repeated readings scatter about the mean.

- **Cure**: statistics. Take **many readings and average** — random errors partially cancel:
$$\bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n} \quad \text{with dispersion quantified by} \quad \sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$$

> [!IMPORTANT] 🎯 The one-para exam answer: "How will you minimize errors?"
> **Gross** → careful reading/recording, repeat measurements. **Systematic** → select good instruments, **calibrate** against standards, apply correction factors, compensate/shield against environment, use mirror scales & correct technique. **Random** → increase the number of readings and take the **arithmetic mean**; use statistical analysis (standard deviation) to state the confidence in the result.

---

## 2. Absolute, Relative, and Percentage Error

- **Absolute error**: $E_{abs} = \lvert A_{measured} - A_{true} \rvert$ — always positive, always in the unit of the quantity.
- **Relative error**: $\varepsilon_r = \dfrac{E_{abs}}{A_{true}}$ — a pure number; the *natural* error measure for a quantity.
- **Percentage error**: $\%\ \text{error} = \varepsilon_r \times 100\%$.

### Limiting Error (% FSD) — the instrument-maker's convention
Instruments are sold with a **guaranteed accuracy quoted as % of full-scale deflection**. This fixed absolute band $E_{FSD}$ becomes a **larger relative error on small readings**:

$$\text{limiting error}\ (\%\ \text{of FSD}) = \frac{E_{abs}}{A_{FSD}}\times 100\%
\;\Longrightarrow\;
\%\ \text{error of reading} = \frac{E_{abs}}{A_{reading}}\times 100\% = \frac{\%\ \text{FSD} \times A_{FSD}}{A_{reading}}$$

> [!WARNING] ⚠️ Exam trap
> The relative error at reading $A$ is $\%\ \text{FSD} \times \dfrac{A_{FSD}}{A}$ — it *blows up* as $A$ shrinks. Never quote a "% of FSD" figure as "% of reading" without converting.

---

## 3. Propagation of Errors

When the wanted quantity is computed from measured ones (the **indirect method**), each measurement error propagates into the result. Let quantities $X = f(A, B, \dots)$ with small independent errors $\delta A, \delta B, \dots$

| Relation | Worst-case relative error | Notes |
| :--- | :--- | :--- |
| **Sum** $X = A + B$ | $\dfrac{\delta X}{X} = \dfrac{\delta A + \delta B}{A+B}$ | absolute errors **add**; result error is between the two relative errors |
| **Difference** $X = A - B$ | $\dfrac{\delta X}{X} = \dfrac{\delta A + \delta B}{A - B}$ | same numerator, **small denominator** → relative error explodes! |
| **Product** $X = A\cdot B$ | $\dfrac{\delta X}{X} = \dfrac{\delta A}{A} + \dfrac{\delta B}{B}$ | relative errors **add** |
| **Quotient** $X = A/B$ | $\dfrac{\delta X}{X} = \dfrac{\delta A}{A} + \dfrac{\delta B}{B}$ | relative errors still **add** |
| **Power** $X = A^n$ | $\dfrac{\delta X}{X} = n\,\dfrac{\delta A}{A}$ | exponent **multiplies** the relative error |
| **General** $X = f(A,B)$ | $\delta X = \dfrac{\partial f}{\partial A}\delta A + \dfrac{\partial f}{\partial B}\delta B$ | the master formula (first-order Taylor) |

> [!TIP] 🧠 Design wisdom from the propagation table
> 1. **Differences are dangerous**: compute $X = A - B$ from nearly equal $A, B$ and relative errors explode. (Classic physical example: two almost-equal resistors' difference, or loss tangent from nearly cancelling bridge arms.)
> 2. In **products/quotients**, the quantity with the *largest relative error dominates* — improve it first.
> 3. Exponents magnify: a 1% error in $r$ becomes 2% in $r^2$ and 3% in $r^3$. (Wheatstone-bridge sensitivity $\propto$ geometry factors, and the $n$-rule explains why in power-law formulas.)

---

## 4. Worked Examples

> [!EXAMPLE] Problem 1 — classify and compute
> A voltmeter (accuracy 2% of FSD, full scale 250 V) reads 100 V on a circuit whose true voltage is 98 V. (a) Classify the error between the reading and truth. (b) Find the absolute, relative and percentage errors. (c) Find the *limiting* relative error guaranteed by the meter.

**Step 1 — Classification:** the difference (100 vs 98 V) is a repeatable, law-abiding discrepancy → **systematic error** (instrumental component, e.g. calibration), unless proven random.

**Step 2 — Absolute error:**
$$E_{abs} = |100 - 98| = \boxed{2\ \text{V}}$$

**Step 3 — Relative and percentage error:**
$$\varepsilon_r = \frac{2}{98} = 0.0204 \quad\Rightarrow\quad \%\ \text{error} = \boxed{2.04\%}$$

**Step 4 — Limiting error from the meter's spec:**
$$E_{FSD} = 2\% \times 250 = 5\ \text{V} \quad\Rightarrow\quad \%\ \text{error of reading} = \frac{5}{100}\times 100\% = \boxed{5\%}$$
The *guaranteed* band (±5 V) is wider than the observed error (2 V) — the guarantee covers the worst case, and at half scale it looks twice as bad as the nameplate 2%.

> [!EXAMPLE] Problem 2 — propagation in a power computation
> The power in a resistor is computed from $P = V^2/R$. Measured: $V = 100 \pm 1$ V, $R = 10\ \Omega \pm 2\%$. Find the worst-case percentage error in $P$.

**Step 1 — Relative error in $V$:** $\dfrac{\delta V}{V} = \dfrac{1}{100} = 1\%$.

**Step 2 — Apply the propagation rules:** $P = V^2 R^{-1}$ →
$$\frac{\delta P}{P} = 2\,\frac{\delta V}{V} + 1\,\frac{\delta R}{R}$$

**Step 3 — Substitute:**
$$\frac{\delta P}{P} = 2(1\%) + 1(2\%) = \boxed{4\%}$$

**Step 4 — Sanity check:** $P = 100^2/10 = 1000$ W; error $= 4\% \times 1000 = \pm 40$ W. The exponent-2 on $V$ doubled the 1% voltage error — power-law variables dominate error budgets.

## 5. Self-Test (Active Recall)

1. Why can't you "average away" a systematic error? *(It follows a definite law and repeats identically — averaging only cancels random scatter; you need calibration/correction.)*
2. A 0–150 V meter guaranteed 1% FSD reads 30 V. Worst-case % error of the reading? *($1.5/30 \times 100 = 5\%$.)*
3. Which error class does parallax belong to, and what cures it? *(Observational systematic; mirror scale or digital readout.)*
4. Why is measuring a small difference of two large quantities error-prone? *(δA + δB lands on a tiny denominator $A - B$ → relative error explodes.)*
5. State the propagation rule for $X = A^3/B^2$. *(Relative error $= 3\,\delta A/A + 2\,\delta B/B$.)*
6. Twelve readings scatter tightly around 49.2 V while truth is 50.0 V. Error family? *(Systematic — precise but biased; recalibrate.)*

## 6. Related Concepts

- **Parent module**: [[00 - Measurement and Instrumentation Index]]
- The vocabulary this note quantifies: [[Static Characteristics of Instruments]] · [[Introduction to Measurement]]
- Bridges minimize reading errors by nulling — see how: [[DC Bridges — Measurement of Resistance]] · [[AC Bridges — Principle and Balance Conditions]]
- Worked bridge numbers where error discipline pays: [[Bridge Numericals — All Bridges]]
