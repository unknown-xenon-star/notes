---
title: "Classification of Instruments"
date: 2026-09-25
tags:
  - concept
  - mi
  - measurement-and-instrumentation
  - instruments
aliases:
  - "Absolute and Secondary Instruments"
  - "Deflection and Null Type Instruments"
  - "Analog and Digital Instruments"
status: completed
---

# 🧰 Classification of Instruments

> [!NOTE] 💡 The Big Picture Intuition
> "Instrument" is an umbrella over a huge family — ammeters, energy meters, X-Y recorders, digital multimeters. To study them you must first **sort** them, and there are two independent sorting games. **Game 1: where does the calibration come from?** (absolute vs secondary). **Game 2: what does the instrument *do* with the reading, and how does it reach it?** (indicating/recording/integrating; analog/digital; deflection/null). One physical device can sit in several boxes at once — your lab's multimeter is *secondary + indicating + digital + deflection-type* all at once.

---

## 1. By Calibration Source

### 1.1 Absolute Instruments
Give the measured quantity **in terms of the instrument's own constants** (dimensions, deflection angle, physical laws) — **no external calibration** against a standard is needed.

**Classic examples**: **Rayleigh current balance**, **tangent galvanometer** ($I = K\tan\theta$, where $K$ is computed from coil geometry and Earth's horizontal field), **electrostatic voltmeter** based on plate attraction force $F = \frac{1}{2}V^2\frac{dC}{dx}$.

- Used mainly in **standard laboratories** to *create* calibrations, not on shop floors — they are slow and need skilled handling.

### 1.2 Secondary Instruments
Determine the quantity only **after calibration against an absolute instrument** (or a standard). The dial was taught what the numbers mean by someone else.

**Examples**: every everyday instrument — ammeters, voltmeters, wattmeters, energy meters, your lab multimeter.

> [!IMPORTANT] 🎯 The one-line exam answer
> *"Absolute instruments give the value from the instrument's own constants; secondary instruments must be calibrated against an absolute instrument or a standard before use."*

---

## 2. By Function

| Type | What it does | Example |
| :--- | :--- | :--- |
| **Indicating** | Shows the instantaneous value on a scale/pointer/display | PMMC ammeter, voltmeter, CRO |
| **Recording** | **Draws a continuous trace** of the value vs time on paper (or stores it) | X-Y recorder, ECG machine, chart recorder |
| **Integrating** | **Adds up** the total quantity over time (product of quantity × time) | Energy (kWh) meter, water meter, petrol pump |

> [!TIP] 🧠 Memory hook
> **Indicate = instant, Record = writes the history, Integrate = adds the total.** The domestic electricity meter is the classic integrating instrument — it never shows "power now", it accumulates energy all month.

---

## 3. Analog vs Digital

| Aspect | Analog | Digital |
| :--- | :--- | :--- |
| Output | Continuous pointer deflection on a scale | Discrete numeric display |
| Reading errors | Parallax, interpolation between marks | Essentially none in *reading* |
| Resolution | Limited by scale and human eye | Set by number of digits (e.g. $3\tfrac{1}{2}$-digit DMM) |
| Power take-off | Draws energy from the measurand (loading error) | Very high input impedance → minimal loading |
| Speed, storage | Slower; hard to store/interface | Fast; easy to store, transmit, and compute |
| Noise tolerance | Degradation visible on signal | Quantization noise only; robust |

**Example**: mercury thermometer vs digital thermometer; moving-coil voltmeter vs DMM.

---

## 4. Deflection Type vs Null Type

This classification matters most for **bridges** — the exam heart of this subject.

### 4.1 Deflection Type
The measurand produces a **physical deflection** of a pointer against a calibrated restoring spring/counter-torque; the value is read from the deflection. The instrument **draws energy from the measured circuit** to move the pointer.

**Examples**: PMMC ammeter, moving-iron voltmeter, **deflection-type Wheatstone bridge** (detector shows an out-of-balance current, calibrated in terms of $R_x$).

### 4.2 Null Type
The measurand's effect is **cancelled (balanced) by an opposing known effect** until a **detector shows zero**. The value is then taken from the *settings of the opposing standard*.

**Examples**: **DC potentiometer**, **Wheatstone bridge at balance** (galvanometer reads zero; $R_x$ read from ratio arms), two-pan chemical balance, **AC bridges** throughout [[AC Bridges — Principle and Balance Conditions]].

| Property | Deflection type | Null type |
| :--- | :--- | :--- |
| Accuracy | Lower (spring calibration drifts) | **Higher** (depends on standards, not on detector) |
| Speed of measurement | Fast — direct reading | Slower — manual/automatic balancing needed |
| Energy from circuit | Continuous draw | Zero at balance — **no loading error** |
| Detector role | Scales the reading | Only flags **zero** (never calibrated itself) |

> [!WARNING] ⚠️ Exam traps
> 1. In a null-type instrument, the **detector need not be calibrated at all** — it only has to indicate *zero* faithfully. Accuracy lives entirely in the standard arms. This is *the* reasoning answer for "why are bridges more accurate than direct-reading instruments?"
> 2. At balance, the bridge **draws no current from the measurand** — the measurement does not disturb the circuit (no loading error).
> 3. Don't confuse *analog* with *deflection*: a deflection bridge can be analog, but the categories are independent.

---

## 5. Worked Example

> [!EXAMPLE] Problem — classify these instruments
> (a) Tangent galvanometer, (b) domestic kWh meter, (c) DMM used to check a battery, (d) Wheatstone bridge with galvanometer, (e) ECG chart recorder.

**Classification:**

| Instrument | Absolute/Secondary | Function | Analog/Digital | Deflection/Null |
| :--- | :--- | :--- | :--- | :--- |
| (a) Tangent galvanometer | **Absolute** | Indicating | Analog | Deflection |
| (b) kWh meter | Secondary | **Integrating** | Analog (disc) | Deflection (torque-driven disc) |
| (c) DMM | Secondary | Indicating | **Digital** | Deflection (internal ADC) |
| (d) Wheatstone bridge | Secondary (uses standard arms) | Indicating/compare | — | **Null** |
| (e) ECG recorder | Secondary | **Recording** | Analog (pen) | Deflection |

## 6. Self-Test (Active Recall)

1. Why can a tangent galvanometer be called absolute? *(Its constant K is computed from coil radius, turns, and $B_H$ — no calibration against another instrument.)*
2. Your lab ammeter is which class, and why? *(Secondary — its scale was set by calibration against a standard.)*
3. Why does a null measurement not load the measured circuit? *(At balance the detector current is zero → no power drawn.)*
4. State two reasons digital instruments are preferred for precision work. *(No parallax/interpolation errors; very high input impedance reduces loading.)*
5. Name the three functional classes with one example each. *(Indicating–ammeter, Recording–chart recorder, Integrating–kWh meter.)*

## 7. Related Concepts

- **Parent module**: [[00 - Measurement and Instrumentation Index]]
- The null idea in its full power: [[DC Bridges — Measurement of Resistance]] · [[AC Bridges — Principle and Balance Conditions]]
- Vocabulary introduced here, deepened there: [[Static Characteristics of Instruments]]
- Where instrument misbehaviour gets counted: [[Errors in Measurement]]
