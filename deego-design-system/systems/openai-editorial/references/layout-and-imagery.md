# Layout and imagery

## Page model

- Container with a 1200px max width and generous side margins (24px, 20px on mobile).
- **Hero:** an interaction vertically centered on an empty white canvas. For a product with an input (search, prompt, short form), the input is the whole first screen: display title above (e.g. "What can I help with?"), pill input, chip row below. A "command line" feeling. For a hero without an input: display title, body-lg lead in #666 at ~640px max width, one action (outlined, if the nav already has the filled button).
- **Below the hero:** an asymmetric 2-column editorial grid — featured article/block on the left (~65%) with full-bleed photography, a stacked column of smaller cards on the right with 32px between them. Collapses to one column on mobile.
- **Vertical rhythm:** 32-64px between sections, up to 120px between large blocks. Never change the background color between sections; never use horizontal rules.
- **Density:** spacious and editorial. One idea per visual unit, large type, lots of air. Avoid 3+ card grids on marketing pages; for a long list of items, prefer 2 columns or a vertical list of title + description.
- **Navigation:** minimal top bar. No mega menu, no sidebar (except on app screens).

## Typical landing page sections (usual order)

1. Nav
2. Hero (display + lead + action, or input + chips)
3. Large image/demo (6px card, full bleed within the container)
4. 2-column editorial grid (featured + cards)
5. Features as an editorial list: section label, 28px heading, 2 columns of 22px title + 17px text pairs
6. Social proof as text (quote at body-lg, author as a #666 label) — no colored logos; customer logos, if any, in monochrome at 40-50% opacity
7. Final CTA: heading + one action
8. Footer

## Imagery

- Large-format, cinematic editorial photography: cosmic/space (planets, solar surfaces, nebulae) for features, product screenshots for business sections, abstract gradient washes (sunrise oranges, soft purples) for story cards.
- Images full bleed inside the card, 6px radius, no inset, no shadow.
- No illustrations, no 3D, no lifestyle or generic stock photography.
- Without real images: prefer a purely typographic layout; the `.ph-sunrise`, `.ph-violet`, `.ph-deep` placeholders from `components.css` only when an image slot is essential. They are the only place gradients are allowed.
- Product screenshots: inside a panel with a hairline border and 6px radius, on a #f1f1f1 background if it needs to stand out from white.

## Icons

Thin stroke (1.5px), monochrome (black or #8f8f8f), outlined, never filled or multicolor. Only in the search input (magnifier, send arrow) and the nav utility area. On app screens they can appear in lists and toolbars in the same style. Never inside text buttons.
