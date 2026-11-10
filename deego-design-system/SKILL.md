---
name: deego-design-system
description: Deego Design System, a library of design systems applied by default to any visual interface work. ALWAYS use this skill when the user asks to create, design, redesign, prototype, mock up or code any interface, website, landing page, web page, app screen, UI component, mockup, wireframe, dashboard, form or HTML email, in HTML, CSS, React, Tailwind, Vue, Figma or any other format, even if they don't mention a design system. Also use it when they name one of the systems (OpenAI Editorial) or ask for "Deego", "my design system", "the X style" or "the client's design system".
---

# Deego Design System

This skill holds several design systems. Each one lives in `systems/<id>/` with its original DESIGN.md, the resolved rules (`rules.md`), references and assets. Pick the system first, then read only that system's files.

## Available systems

| id | Name | Use when | Default |
|---|---|---|---|
| `openai-editorial` | OpenAI Editorial | Monochrome, minimal, typographic editorial style; tech products, APIs, research | yes |

Folders starting with `_` (such as `_template`) are not systems: ignore them.

## Choosing the system

In this order:

1. **Named in the request.** "Use OpenAI Editorial", "in client X's style", or the skill invoked with a system name. Accept approximate matches on the name or id.
2. **Conversation or project context.** If a system is already in use for this work, or the project instructions / CLAUDE.md name one, keep it for consistency.
3. **Default.** The system marked as default in the table.
4. **Ask only when genuinely ambiguous** (for example, the request mentions a brand that matches two systems). One short question with the options.

State in one line which system you applied, so the user can ask for another.

## Workflow

1. Pick the system (above).
2. Read `systems/<id>/rules.md`. It says which other files of the system to read and when.
3. Read `shared/accessibility.md` (applies to every system and overrides any DESIGN.md).
4. For HTML email, also read `shared/email-html.md` and use the values the system's `rules.md` gives.
5. Don't invent values: use the system's tokens; if a value doesn't exist, use the closest token.
6. Use the user's real content. Missing facts become visible placeholders ([PRICE]), never invented numbers.
7. Before delivering, run through the system's checklist in `rules.md` and the common checklist below.

## Mixing systems

Don't mix tokens from different systems on the same screen. If the user explicitly asks for "A's layout with B's colors", do it and state in one line what came from each.

## Common checklist

- [ ] The chosen system is stated to the user in one line.
- [ ] Only tokens from the chosen system.
- [ ] Contrast, visible focus, touch targets and semantics per `shared/accessibility.md`.
- [ ] Works at phone width.
- [ ] No third-party logos or brand names that the system's `rules.md` forbids.
