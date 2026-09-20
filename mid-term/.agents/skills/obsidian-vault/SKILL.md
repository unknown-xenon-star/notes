---
name: obsidian-vault
description: >-
  Manage, format, link, and organize markdown notes in an Obsidian vault following Obsidian syntax standards, wikilinks, callouts, and frontmatter properties.
---

# Obsidian Vault Management Skill

Use this skill when creating, structuring, updating, or formatting notes in an Obsidian vault to maintain clean graph connections, frontmatter metadata, and visual presentation.

---

## 1. Note Creation Workflow

When adding a new note to the vault:

1. **Check for Existing Notes**: Search the vault to avoid duplicate concepts and to find relevant notes to link against.
2. **Include YAML Frontmatter**: Always start the note with metadata:
   ```yaml
   ---
   title: "Descriptive Title"
   date: YYYY-MM-DD
   tags:
     - course/subject
     - status/review
   aliases:
     - "Synonym"
   ---
   ```
3. **Draft Atomic Content**: Focus each note on a single concept, topic, or lecture.
4. **Link Generously**: Insert Wikilinks (`[[Note Name]]` or `[[Note Name|Alias]]`) for all related terms, parent topics, and subtopics.
5. **Use Callouts for Readability**: Emphasize key ideas using Obsidian callout syntax (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!EXAMPLE]`, `> [!SUMMARY]`).

---

## 2. Note Types & Layouts

### Concept Note (Atomic)
```markdown
---
title: "Concept Name"
date: YYYY-MM-DD
tags:
  - concept
  - subject/topic
aliases: []
---

# Concept Name

## Definition
> [!NOTE] Core Definition
> Brief and precise explanation of the concept.

## Key Properties & Formulae
- Property 1: ...
- Formula: $$...$$

## Related Concepts
- Parent Topic: [[Parent Concept]]
- Contrasting Topic: [[Opposite Concept]]
- Applications: [[Application Note]]

## Examples
> [!EXAMPLE]
> Practical demonstration or sample calculation.
```

### Lecture / Study Note
```markdown
---
title: "Lecture Title"
date: YYYY-MM-DD
tags:
  - lecture
  - subject/course-code
---

# Lecture Title - Course Name

## Objectives & Core Themes
- [[Core Concept 1]]
- [[Core Concept 2]]

## Detailed Notes
### 1. Section Title
Detailed explanation...

## Summary & Review Checklist
- [ ] Understand [[Core Concept 1]]
- [ ] Complete practice problems in [[Practice Problems - Topic]]
```

---

## 3. Maintenance Rules

- Never touch `.obsidian/` config files directly.
- Maintain consistent capitalization for note titles (e.g., Title Case).
- Ensure all Wikilinks match exact note filenames or use aliases.
