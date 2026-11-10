# Accessibility (applies to every system)

These rules override any DESIGN.md that says otherwise. When a system contradicts them, follow this page and record the decision in that system's `references/source-notes.md`.

- **Contrast:** normal text ≥ 4.5:1; large text (24px+, or 18.66px+ bold) and UI components ≥ 3:1. If one of the system's greys fails, use it only for placeholders, disabled states and decorative icons.
- **Visible focus:** every interactive element gets a clear `:focus-visible` style (for example `outline: 2px solid` in the text color, `outline-offset: 2px`), even if the DESIGN.md says there is no focus ring.
- **Touch targets:** ≥ 44×44px on mobile.
- **Semantics:** `<button>` for actions, `<a href>` for navigation, a `<label>` for every field, `aria-label` on icon-only buttons, `aria-hidden="true"` on decorative SVG.
- **Color is never the only cue:** states (error, success, selected) are also distinguished by text, icon or shape.
- **Motion:** respect `prefers-reduced-motion`.
- **Language:** correct `lang` on `<html>`.
