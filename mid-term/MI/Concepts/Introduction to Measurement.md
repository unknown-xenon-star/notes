---
title: "Introduction to Measurement"
date: 2026-09-25
tags:
  - concept
  - mi
  - measurement-and-instrumentation
  - measurement-basics
aliases:
  - "Significance of Measurement"
  - "Methods of Measurement"
  - "Measurement Standards"
status: completed
---

# 📏 Introduction to Measurement

> [!NOTE] 💡 The Big Picture Intuition
> You cannot control what you cannot **measure**. A temperature dial, a weighing scale, a multimeter — all answer one question: *"how much?"* A measurement system is a **messenger**: it picks up a physical quantity (heat, force, current), carries it through processing stages, and delivers a number you can trust. The whole subject of Measurement & Instrumentation is about making that messenger **accurate, reliable, and trustworthy** — because every engineering decision, every payment of an electricity bill, every lab result ultimately rests on a measured number.

---

## 1. Significance of Measurement

Measurement is the bridge between the physical world and the world of numbers. Without it:

- **No experiment**: a hypothesis stays untested unless a quantity can be measured and compared with theory.
- **No commerce**: electricity bills, fuel pumps, and weighing bridges all depend on standardized measurement — a kWh of energy must mean the same in every city.
- **No control**: feedback control (a thermostat, a governor) is blind without a sensor feeding back the measured value.
- **No quality**: industrial tolerances (a shaft $25.000 \pm 0.01$ mm) are meaningless without instruments that can verify them.

> [!IMPORTANT] 🎯 The three pillars every measured value leans on
> 1. A **standard** — the agreed definition of the unit (what exactly is 1 kg? 1 volt?).
> 2. A **calibrated instrument** — one that has been compared against that standard.
> 3. A stated **accuracy** — no measurement is complete without knowing *how wrong it might be*.

---

## 2. Methods of Measurement

### 2.1 Direct Method
The unknown quantity is determined **directly against the unit**, with the measured value readable on the instrument itself — no intermediate calculation with other quantities.

**Examples**: measuring length with a ruler, current with an ammeter, temperature with a mercury thermometer, pressure with a Bourdon gauge.

- ✅ Quick, simple, cheap.
- ❌ The human senses (or the instrument's mechanism) limit accuracy — rarely enough for high precision work.

### 2.2 Indirect Method
The wanted quantity is **not measured itself**; instead one or more *other* quantities (which it depends on, through a known physical law) are measured, and the result is **computed**.

**Examples**:
- Measuring **power** $P = VI$ by measuring $V$ and $I$ separately.
- Finding a **speed** from measured distance and time.
- Determining **dielectric loss** of a capacitor from bridge measurements.

- ✅ Can be far more accurate when the related quantities are easy to measure well.
- ❌ Extra steps: errors in each measured quantity **propagate** into the result (see [[Errors in Measurement]]).

### 2.3 Comparison Method
The unknown is measured by **comparing it directly against a known standard of the same kind** — the essence of all **bridge methods** (the core of this subject's exam zone!). The unknown and the standard are placed in the same circuit, and balance is found when their effects cancel.

**Examples**:
- **Wheatstone bridge** (unknown resistance vs known resistances) — [[DC Bridges — Measurement of Resistance]].
- **AC bridges** for $L$ and $C$ — [[AC Bridges — Principle and Balance Conditions]].
- Balancing a chemical weight on a two-pan balance against standard masses.

- ✅ Highest achievable accuracy — the result depends on ratio devices, and *at balance the detector reading is independent of the supply*.
- ❌ Needs a skilled observer and a balancing procedure; slower than direct reading.

> [!TIP] 🧠 One-line mnemonic
> **Direct = read it. Indirect = compute it. Comparison = balance it.**

---

## 3. Measurement Standards

A **standard** is the physical embodiment of the unit — the reference everything is traced back to. Because a laboratory in Tokyo and one in Berlin must report the same volt, standards are arranged in a **chain of hierarchy**, each level calibrated against the one above it.

| Level | Standard | What it is | Used by |
| :--- | :--- | :--- | :--- |
| 1 | **International** | Defined by international agreement (SI): metre, kilogram, second, ampere... | BIPM / national labs |
| 2 | **Primary** | Maintained by national laboratories (NPL, NIST) with highest possible accuracy | National labs only |
| 3 | **Secondary** | Calibrated **against the primary** at the national lab; kept by industrial labs | Industries, big labs |
| 4 | **Working** | Calibrated against the **secondary**; the everyday lab/shop-floor standard | Daily measurement work |

> [!NOTE] The traceability chain
> $$\text{International} \rightarrow \text{Primary} \rightarrow \text{Secondary} \rightarrow \text{Working}$$
> Every instrument in use should be *traceable* to the top of this chain — that is what makes a metre in one lab equal to a metre in another.

**Examples of working standards**:
- Standard **resistors** (e.g. $1\ \Omega$, $100\ \Omega$ manganin coils — manganin because its temperature coefficient is nearly zero),
- Standard **cells** (Weston cadmium cell, e.m.f. $\approx 1.0186$ V, extremely stable),
- Standard **masses**, **capacitors**, and **inductors** for bridge work.

---

## 4. The Performance Vocabulary (Accuracy, Precision, Sensitivity, Resolution)

These four words get used loosely in daily life but are *strictly distinct* in exams. Full detail lives in [[Static Characteristics of Instruments]]; here is the pocket version:

| Term | Question it answers | Defining idea |
| :--- | :--- | :--- |
| **Accuracy** | How close to the *true* value? | Conformity to truth; expressed as % of full-scale deflection |
| **Precision** | How *repeatable* are the readings? | Agreement among repeated measurements — says nothing about truth! |
| **Sensitivity** | How big a response per unit input? | $\text{sensitivity} = \dfrac{\text{output (deflection)}}{\text{input change}}$ |
| **Resolution** | What is the *smallest input increment* it can register? | Smallest discernible change of input |

> [!WARNING] ⚠️ The accuracy–precision trap (a guaranteed exam favourite)
> A watch that reads **10:10 exactly every day** when the true time is 10:00 is **precise but not accurate** — repeated readings agree, but all are wrong. High precision does **not** imply high accuracy; the reverse is also possible. The classic one-liner: *"Precision is a measure of dispersion, accuracy is a measure of conformity."*

---

## 5. Worked Example

> [!EXAMPLE] Problem
> A $0–200$ V electrostatic voltmeter has a scale of 100 divisions. The pointer can be read to 1 division, and the instrument's guaranteed accuracy is 1% of full-scale reading. (a) What is its resolution? (b) When reading 100 V, how large an error might the accuracy statement imply, and what is it as a percentage of the reading?

**Step 1 — Resolution:**
The smallest input change the instrument can register is 1 division out of 200 V over the full scale:
$$\text{Resolution} = \frac{200\ \text{V}}{100\ \text{div}} = \boxed{2\ \text{V per division}}$$

**Step 2 — Accuracy limit (guaranteed error):**
The error is specified as % of **full-scale**, not of the reading:
$$\text{error} = 1\% \times 200\ \text{V} = \pm 2\ \text{V}$$

**Step 3 — Convert to % of the actual reading:**
$$\%\ \text{error of reading} = \frac{2}{100} \times 100\% = \boxed{2\%}$$

**Step 4 — Interpret:** the *same* ±2 V band is only $\frac{2}{200} \times 100\% = 1\%$ when reading near full scale. So a % of FSD instrument looks **twice as bad in relative terms at half scale** — always read near the upper part of the scale, and always check *which base* a quoted percentage uses.

## 6. Self-Test (Active Recall)

1. Classify: measuring resistance by a Wheatstone bridge — direct, indirect, or comparison? *(Comparison — unknown vs standard in the same circuit.)*
2. Why is manganin chosen for standard resistors? *(Almost zero temperature coefficient → value stable.)*
3. A multimeter reads 9.99, 10.00, 9.98 V for a true 10.50 V source. Accurate, precise, both, or neither? *(Precise but not accurate — tight cluster, far from truth.)*
4. Name the hierarchy levels between an international standard and your lab bench instrument. *(Primary → Secondary → Working.)*
5. Why should a measurement be taken near full scale of an instrument? *(A % of FSD error is a larger % of a small reading — relative error grows as the reading shrinks.)*

## 7. Related Concepts

- **Parent module**: [[00 - Measurement and Instrumentation Index]]
- Where these four performance words are treated in full depth: [[Static Characteristics of Instruments]]
- When measured values go wrong and how to count the ways: [[Errors in Measurement]]
- The comparison method in its most exam-heavy form: [[DC Bridges — Measurement of Resistance]] · [[AC Bridges — Principle and Balance Conditions]]
