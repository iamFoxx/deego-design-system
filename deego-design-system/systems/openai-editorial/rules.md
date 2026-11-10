# OpenAI Editorial — system rules

Visual reference: the OpenAI website. The mood is "research lab notebook at noon": white surfaces, near-black type, almost no color. Restraint is the identity. Typography does the heavy lifting, components are lightweight and whitespace structures the page.

The original source is `DESIGN.md`. This file resolves its contradictions and gaps (see `references/source-notes.md`); when they conflict, follow this file.

## Files in this system

| File | When to read |
|---|---|
| `references/tokens.md` | Always, before writing code or designing (includes a Tailwind v4 block) |
| `references/components.md` | Always, for specs and reference HTML |
| `references/layout-and-imagery.md` | Full pages: landing pages, sites, whole screens |
| `references/source-notes.md` | When DESIGN.md and these rules seem to disagree |
| `assets/tokens.css`, `assets/components.css` | Inline into the `<style>` of HTML/CSS output |
| `assets/starter-landing.html` | Starting point or composition reference for landing pages (links the two CSS files; inline them when delivering a single file) |

## The rules that define the style

These rules are what make the result recognizable. Break one and the style disappears.

- **Monochrome.** Text #000000, secondary #666666, tertiary #8f8f8f, background #ffffff, subtle surface #f1f1f1. No accent colors, no UI gradients, no brand hues. Color only enters through photography.
- **One filled button per screen.** The black button (bg #000, white text) is the page's "full stop", the primary action. Every other action is an outlined or ghost button.
- **Pills for everything interactive.** Buttons, chips/tags and inputs use `border-radius: 9999px`. Never 8px or 12px on buttons.
- **6px on cards and images.** A near-zero, architectural radius. Never 12px or 16px.
- **Hairline borders.** Every border and divider is `1px solid rgba(0,0,0,0.12)`.
- **No shadows on content.** The only shadow (`--shadow-sm`) appears on the outlined button's hover.
- **Whitespace instead of dividers.** Sections are separated by 32-64px (up to 120px between large blocks), with no horizontal rules or background color changes.
- **Restrained weights.** 400 for body; 500 for nav, labels, buttons and headings (including the 48px display); 600 only at the 28px heading tier. Never 700+.
- **Negative tracking on large headings.** Display 48px at -0.03em; heading 28px at +0.011em.
- **Editorial body text.** 17px, line-height 1.65, -0.01em. Never body text below 16px.
- **Text first.** No icons inside buttons or links. Thin-stroke icons only in the search input and the nav utility area.
- **Editorial composition.** Max width 1200px, asymmetric 2-column grids (about 65/35 or 35/65) instead of 3+ card grids.

## Brand and content

- This is a style, not the OpenAI brand. Never use the OpenAI logo, wordmark or the names "OpenAI" or "ChatGPT" in the interfaces you create. Use the user's project name; without one, invent a neutral name with a typographic wordmark (16px, weight 500).
- Font: OpenAI Sans is proprietary. Use Inter (400/500/600) with `font-feature-settings: 'calt' 1, 'liga' 1`.
- Images: large-format editorial photography. Without real images, prefer a purely typographic composition; use the soft-gradient placeholders (`.ph-*`) only when the layout genuinely needs an image.

## Context adaptations

- **Landing pages:** the full system; centered hero; a single black CTA.
- **App screens and dashboards:** same language, higher density (12-24px, tables, 3+ columns when the data justifies it). State colors in `references/tokens.md`.
- **Mobile:** responsive scale in `references/tokens.md`; touch targets ≥ 44px.
- **Dark mode:** only when the environment requires it; derived tokens in `assets/tokens.css` (the filled button inverts to white).
- **HTML email:** `../../shared/email-html.md` with these values: button #000000 / text #ffffff, radius 9999px, title 32px weight 500 tracking -0.96px, opaque border #e0e0e0.

## System-specific checklist

- [ ] At most one filled (black) button per screen.
- [ ] No color outside the palette in the UI.
- [ ] Buttons, chips and inputs at 9999px; cards and images at 6px.
- [ ] Borders at rgba(0,0,0,0.12); no box-shadow on cards.
- [ ] No weight above 600; 600 only at the 28px heading.
- [ ] Body at 17px / 1.65; display tracking -0.03em.
- [ ] No icons inside buttons.
- [ ] No OpenAI/ChatGPT logo or names.
