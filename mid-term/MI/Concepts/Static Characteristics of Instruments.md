---
title: "Static Characteristics of Instruments"
date: 2026-09-25
tags:
  - concept
  - mi
  - measurement-and-instrumentation
  - static-characteristics
aliases:
  - "Static and Dynamic Characteristics"
  - "Accuracy and Precision"
  - "Linearity, Hysteresis and Drift"
status: completed
---

# 📊 Static Characteristics of Instruments

> [!NOTE] 💡 The Big Picture Intuition
> Before trusting a witness in court, a lawyer cross-examines them: *how close to truth are you? how consistent? how sharp is your vision? do you change your story over time?* Instruments face the same interrogation. **Static characteristics** describe an instrument measuring quantities that are **constant or changing very slowly** — how accurate, how repeatable, how linear, how drifting. (Fast-changing inputs bring in *dynamic* characteristics — speed of response, lag, dynamic error — a different exam unit.) Master these ten words; they are the subject's favourite short-answer zone.

---

## 1. The Ten Characteristics at a Glance

| Characteristic | One-line definition | Expressed as |
| :--- | :--- | :--- |
| **Accuracy** | Closeness to the *true* value | % error, or % of FSD |
| **Precision** | Agreement among repeated readings | max deviation from mean, as % of mean |
| **Sensitivity** | Output change per unit input change | deflection/unit input (slope of calibration) |
| **Resolution** | Smallest input increment that produces a detectable output change | smallest unit on scale / digits |
| **Linearity** | Closeness of calibration curve to a straight line | max deviation from line, % of FSD |
| **Repeatability** | Same input, same conditions → same output | dispersion of readings |
| **Reproducibility** | Same input, *different* conditions → same output | dispersion across conditions |
| **Hysteresis** | Different readings for rising vs falling input | dead band as % of FSD |
| **Threshold** | Smallest input from zero that gives a detectable output | input units |
| **Dead Zone** | Largest range of input for which output is unchanged | input units (hysteresis + friction + backlash) |
| **Drift** | Slow change of output over time with input fixed | % of FSD per hour / per °C |

---

## 2. Accuracy vs Precision (the eternal pair)

- **Accuracy** = conformity to truth. Measured by **absolute error** $=$ |true − measured|; commonly quoted as
$$\%\ \text{error} = \frac{\lvert A_{measured} - A_{true} \rvert}{A_{true}} \times 100\%$$
  but instrument makers quote accuracy as **% of full-scale deflection (FSD)** — see the trap below.
- **Precision** = a measure of *dispersion* (repeatability), not of truth. Numerically,
$$\text{Precision} = \frac{\text{max deviation from mean}}{\text{mean value}} \times 100\%$$

> [!IMPORTANT] 🎯 Four possible combinations
> | | Precise | Not precise |
> | :--- | :--- | :--- |
> | **Accurate** | the dream instrument | scattered but centred readings |
> | **Not accurate** | tightly clustered *wrong* readings (systematic error!) | chaos |
> A tightly clustered reading set with a *stable offset* screams **systematic/calibration error** — fixable, unlike random scatter. Link: [[Errors in Measurement]].

> [!WARNING] ⚠️ % of FSD vs % of reading
> An instrument "accurate to 1% FSD" produces a *larger relative error* on small readings. Reading near full scale keeps the relative error near 1%; at 10% of scale it balloons to 10%. Always check which base the percentage uses — a standard 2-mark trap (worked in [[Introduction to Measurement]]).

---

## 3. Sensitivity, Resolution, Threshold, Dead Zone

- **Sensitivity** $= \dfrac{\Delta q_o}{\Delta q_i}$ — the slope of the calibration curve. A 1 V change producing a 5 mm pointer shift → sensitivity $= 5$ mm/V. A *steeper* calibration curve = more sensitive. (For DMMs: sensitivity is set by internal loading — but the count of digits sets resolution.)
- **Resolution** = smallest increment of input that produces a *detectable* change in output. A 100-div scale over 0–50 V resolves $\frac{50}{100} = 0.5$ V. Digital: a $3\tfrac{1}{2}$-digit display on the 20 V range resolves $0.01$ V.
- **Threshold** = the smallest input, *starting from zero*, that produces a detectable output. (Below threshold the pointer just trembles.)
- **Dead zone** = the largest range of input values for which the instrument gives **no output change**. It is the *combined* consequence of **hysteresis + friction + backlash** — a "deaf zone" where the instrument ignores input changes entirely.

> [!TIP] 🧠 Keep the three apart
> **Threshold** — input from *zero* needed to get *any* response. **Dead zone** — range of input over which there is *no* response at all (can sit anywhere on the scale, caused by mechanical slack). **Hysteresis** — *two different* responses depending on direction of approach.

---

## 4. Linearity

The output should be a straight line in the input — linear response makes scales uniform, interpolation easy, and mathematics friendly. Real instruments sag or bow somewhere on the scale.

- **Linearity** is measured as the **maximum deviation of the calibration curve from the best-fit straight line, expressed as % of FSD**.
- No instrument is perfectly linear; the spec *"linearity ±0.2% FSD"* bounds the bow.

> [!NOTE] Why non-linearity matters
> An ammeter with poor linearity can still be *accurate* — if its calibration table is known. Linearity matters most when you *interpolate between calibrated points* assuming equal divisions.

---

## 5. Repeatability vs Reproducibility vs Hysteresis

- **Repeatability**: same observer, same instrument, same conditions, **short time interval** → closeness of repeated readings.
- **Reproducibility**: same input but with **changed conditions** — different observer, different instrument of the same type, different lab, different day → closeness of results. Reproducibility failures usually reveal **environmental or observational errors**.
- **Hysteresis**: input raised from 0 → X reads one value; input brought down from max → X reads *another*. Causes: mechanical slack (dead band) and magnetic/elastic memory (dead space). Quantified as **dead band** $=$ upscale reading $-$ downscale reading, as % of FSD.

> [!EXAMPLE] Hysteresis in numbers
> Approaching 50 units **from below** the instrument reads 49.9; approaching **from above** it reads 50.3.
> Dead band $= 50.3 - 49.9 = 0.4$ units; on a 0–100 unit scale that is $\frac{0.4}{100}\times 100 = \mathbf{0.4\%\ FSD}$.

---

## 6. Drift

Drift = slow, unwanted change of output with the input held constant — the instrument's answer slowly *walks away*. Causes: **temperature variations, component ageing, supply instability, humidity**.

| Drift type | What shifts | Signature on calibration curve |
| :--- | :--- | :--- |
| **Zero drift** | The whole calibration shifts **parallel** by a constant | Same slope, offset zero; spec'd e.g. "0.02% FSD/°C" |
| **Span (sensitivity) drift** | The **slope** changes | Zero fixed, reading error grows with input |
| **Zonal drift** | Shift confined to a **portion** of the range | Bows in one zone only |

> [!TIP] 🧠 Diagnosis logic
> A reading wrong by the *same amount everywhere* → **zero drift** (recalibrate the zero). Error *proportional to reading* → **span drift** (sensitivity changed — often temperature on resistive elements). Error *only in part of the scale* → **zonal drift**.

---

## 7. Worked Example

> [!EXAMPLE] Problem — accuracy vs precision on a true 100 V source
> Two voltmeters A and B each read a true $100.0$ V source four times:
> $$A: \ 98.0,\ 102.0,\ 99.0,\ 101.0 \qquad B: \ 101.8,\ 102.0,\ 102.2,\ 101.9$$
> For each meter find (a) the mean, (b) the accuracy as % error of the mean, (c) the precision as % of max deviation from the mean, and (d) conclude which systematic error each shows.

**Step 1 — Meter A mean:**
$$\bar{A} = \frac{98.0 + 102.0 + 99.0 + 101.0}{4} = \frac{400.0}{4} = 100.0\ \text{V}$$

**Step 2 — Meter A accuracy:**
$$\%\ \text{error} = \frac{|100.0 - 100.0|}{100.0}\times 100\% = \boxed{0\%} \;(\text{perfectly accurate})$$

**Step 3 — Meter A precision:** deviations from mean: $-2,\ +2,\ -1,\ +1$; max $|dev| = 2.0$ V:
$$\text{Precision} = \frac{2.0}{100.0}\times 100\% = \boxed{2\%} \;(\text{poor — random scatter})$$

**Step 4 — Meter B mean:**
$$\bar{B} = \frac{101.8 + 102.0 + 102.2 + 101.9}{4} = \frac{407.9}{4} = 101.975\ \text{V} \approx 102.0\ \text{V}$$

**Step 5 — Meter B accuracy:**
$$\%\ \text{error} = \frac{|101.975 - 100.0|}{100.0}\times 100\% \approx \boxed{2\%} \;(\text{inaccurate})$$

**Step 6 — Meter B precision:** deviations: $-0.175,\ +0.025,\ +0.225,\ -0.075$; max $|dev| = 0.225$:
$$\text{Precision} = \frac{0.225}{101.975}\times 100\% \approx \boxed{0.22\%} \;(\text{excellent})$$

**Step 7 — Conclude:** Meter A is **accurate but not precise** (random errors, scatter centred on truth). Meter B is **precise but not accurate** — its tight cluster sits *systematically* 2 V high: a **calibration (systematic) error**. The fix for B is one recalibration; A needs better measurement technique. Full error taxonomy: [[Errors in Measurement]].

## 8. Self-Test (Active Recall)

1. State the numerical definitions of accuracy and precision used above. *(Accuracy = |mean − true|/true ×100; precision = max deviation from mean / mean ×100.)*
2. Why is a % of FSD accuracy quote pessimistic at low readings? *(Same absolute band, smaller reading → bigger relative error.)*
3. Differentiate dead zone, dead band, and threshold in one line each. *(Dead zone: input range with no output change; dead band: upscale − downscale reading difference; threshold: smallest input from zero giving detectable output.)*
4. An instrument's error grows in proportion to the reading as the lab warms up. Which drift? *(Span/sensitivity drift — the slope changed.)*
5. Why can reproducibility fail while repeatability stays excellent? *(Conditions changed — temperature, observer, different instrument → environmental/observational errors enter.)*
6. Where does a bridge's accuracy live — in the galvanometer or elsewhere? *(In the standard/ratio arms; the detector only signals null — see [[Classification of Instruments]].)*

## 9. Related Concepts

- **Parent module**: [[00 - Measurement and Instrumentation Index]]
- Pocket versions of these terms: [[Introduction to Measurement]]
- What corrupts readings and how to classify it: [[Errors in Measurement]]
- Instruments whose specs these words describe: [[Classification of Instruments]]
- The most accurate applications of the null principle: [[DC Bridges — Measurement of Resistance]] · [[AC Bridges — Principle and Balance Conditions]]
