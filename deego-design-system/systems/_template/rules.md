# [System name] — system rules

<!-- TEMPLATE: copy this folder to systems/<system-id>/, put the original DESIGN.md
     next to this file, create references/ and assets/, and fill in the sections.
     Remove these comments when done. Claude ignores folders starting with "_". -->

Visual reference: [where the style comes from]. Mood: [one sentence describing it].

The original source is `DESIGN.md`. This file resolves that source's contradictions and gaps (see `references/source-notes.md`); when they conflict, follow this file.

## Files in this system

| File | When to read |
|---|---|
| `references/tokens.md` | Always (colors, typography, spacing, radii, shadows, Tailwind) |
| `references/components.md` | Always (specs and reference HTML) |
| `references/layout-and-imagery.md` | Full pages |
| `references/source-notes.md` | When DESIGN.md and these rules seem to disagree |
| `assets/tokens.css`, `assets/components.css` | Inline into HTML/CSS output |

## The rules that define the style

<!-- 8 to 12 short rules, each with its reason. They are what makes the result recognizable. -->

- **[Rule].** [Exact value]. [Why.]

## Brand and content

<!-- Font and substitute, logo (allowed or not), brand names, image style. -->

## Context adaptations

- **Landing pages:**
- **App screens and dashboards:**
- **Mobile:**
- **Dark mode:**
- **HTML email:** `../../shared/email-html.md` with these values: button [color] / text [color], radius [value], title [size/weight], opaque border [hex].

## System-specific checklist

- [ ] [Check]
