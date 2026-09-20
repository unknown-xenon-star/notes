---
name: midterm-prep
description: >-
  Generate high-yield study guides, practice exam questions, Cornell note summaries, formula cheat sheets, and flashcards for mid-term exam preparation.
---

# Mid-Term Exam Preparation Skill

Use this skill when the user asks to prepare study materials, generate mock exam questions, create formula cheat sheets, summarize course topics, or build active recall review notes for upcoming mid-term exams.

---

## 1. Study Material Workflows

### A. High-Yield Revision Sheet
When asked to create a review or summary note for a topic or exam unit:
1. **Topic Hierarchy**: Outline the primary themes and syllabus requirements.
2. **Key Concepts & Definitions**: Summarize each core definition concisely.
3. **Crucial Formulas & Theorems**: Group formulas into clean LaTeX blocks with variable definitions.
4. **Common Mistakes & Pitfalls**: Highlight typical exam trap areas using `> [!WARNING]`.
5. **Exam Tips**: Provide mnemonics and memory aids in `> [!TIP]`.

### B. Practice Test / Mock Exam Generation
When generating practice problems:
1. **Diverse Question Formats**: Include Multiple Choice, Short Answer, Concept Comparison, and Multi-Step Analytical/Numerical Problems.
2. **Difficulty Tiers**: Tag problems with difficulty levels (Easy, Medium, Challenging).
3. **Collapsible Solution / Answer Key**: Provide step-by-step solutions formatted clearly:
   ```markdown
   ### Problem 1: [Topic] (Difficulty: Medium)
   State the problem clearly...

   > [!QUESTION] Problem Prompt
   > What is the result when...

   > [!SUCCESS]- Solution & Explanation
   > **Step 1:** ...
   > **Step 2:** ...
   > **Final Answer:** ...
   ```

### C. Cornell Notes & Flashcard Format
For active recall:
- Left Column / Cues: Key terms, question prompts, and trigger concepts.
- Right Column / Notes: Explanations, bullet points, and diagrams.
- Bottom: 2-3 sentence summary of the entire note.

---

## 2. Note Structure Example: Midterm Review Sheet

```markdown
---
title: "Midterm Review - Course Name"
date: YYYY-MM-DD
tags:
  - exam-prep
  - midterm
  - subject/course-code
status: active-review
---

# Midterm Exam Review: [Subject Name]

## 📌 Exam Details & Topics Covered
- Date / Duration: ...
- Chapters Covered: [[Chapter 1]], [[Chapter 2]], [[Chapter 3]]
- Weightage / Format: ...

---

## 🔑 High-Yield Concept Breakdown

### 1. [[Core Topic 1]]
> [!IMPORTANT] Core Takeaway
> Key theorem or principle that is guaranteed to appear.

### 2. [[Core Topic 2]]
- Formula: $$...$$
- Key Condition: ...

---

## ⚠️ Common Traps & Pitfalls
> [!WARNING] Avoid These Errors
> - Don't forget units / boundary conditions.
> - Confusing concept A with concept B.

---

## 📝 Practice Questions & Mock Problems
Link to practice notes: [[Practice Exam - Course Name]]
```
