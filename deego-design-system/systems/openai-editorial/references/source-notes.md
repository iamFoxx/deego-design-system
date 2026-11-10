# Notes on the source

Decisions made where `DESIGN.md` is contradictory or silent.

| Topic | In the source | Decision | Why |
|---|---|---|---|
| Weight 600 | "Only for the largest headings" vs "only at the 28px tier"; display examples at 500 | Display 48px at 500; heading 28px at 600 | Matches the component examples |
| Body text | Do's say 17px/1.65; the scale has no body token | New token `--text-body: 17px` | Fills the gap in the scale |
| Input padding | "10px vertical / 24px right / 52px left" vs example "10px/52px/10px/24px" | 10px 24px 10px 52px (icon on the left) | The description says the left padding reserves space for an icon |
| Input border | rgb(229,231,235) vs rgba(0,0,0,0.12) in the guide | rgba(0,0,0,0.12) | Global rule: every border is hairline |
| Focus | "No visible focus ring" | Visible focus required | Accessibility (WCAG 2.4.7) |
| Whisper | Described both as a "decorative accent" and as a hover tint | Hover/selection tint only | Consistent with the monochrome system |
| `--section-gap: 32-64px` | Invalid CSS value | Three tokens: 32 / 64 / 120px | Valid CSS |
| Extra radii (`--radius-3xl` 24px, 40px, 6.08px) | Listed without a role | Omitted (except 20px on textarea) | No defined use; keep the system simple |
| Dark mode | None (light theme) | Derived tokens, used only when the environment requires them | Many environments require both themes |
| Mobile, forms, tables, states, email | None | Derived, marked [derived] | Cover the requests the skill must support |
| OpenAI Sans | Proprietary font | Inter as substitute | Available on Google Fonts and close in metrics |
| Brand | OpenAI wordmark, "Try ChatGPT" | Never reproduce; use the project's name | It's a reference style, not the brand |
| "Similar Brands" | List of similar brands | Ignored | Not applicable design information |
