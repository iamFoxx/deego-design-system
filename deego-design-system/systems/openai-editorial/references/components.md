# Components

Ready-made classes in `../assets/components.css`. Each component below gives its spec and reference HTML.

## Buttons

All: pill (9999px), 14px weight 500, padding 8px 20px, no icons.

**Filled (`.btn-filled`)** — black background, white text. The primary action. At most one per screen.

**Outlined (`.btn-outline`)** — transparent, black text, hairline border. Secondary actions, filters, chips. Hover: whisper tint + `--shadow-sm`.

**Ghost (`.btn-ghost`)** — no background or border. Navigation, "Log in", "View more". Hover: whisper background.

```html
<a class="btn btn-filled" href="#">Get started</a>
<a class="btn btn-outline" href="#">Read the docs</a>
<a class="btn btn-ghost" href="#">Log in</a>
```

Typical hierarchy on a screen: 1 filled + N outlined/ghost. If two actions carry equal weight, use two outlined.

## Chip row

Outlined pills at 13-14px, 8px apart, centered under the hero input. Quick-action shortcuts or filters.

```html
<div class="chip-row">
  <button class="btn btn-outline">Plan a trip</button>
  <button class="btn btn-outline">Summarize a document</button>
</div>
```

## Search / prompt input

Pill, transparent, hairline border, 16px weight 400, padding 10px 24px 10px 52px (icon space on the left), placeholder #666, min height 48px. Visible focus required.

```html
<label class="search">
  <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
  <input type="text" placeholder="Ask anything" aria-label="Search">
</label>
```

## Form fields [derived]

Same language as the search input: pill, hairline border, 16px. Label at 14px weight 500 above; hint at 13px #666; error at 13px in `--state-error` with the field border in the same color. Textarea with a 20px radius.

```html
<div class="field">
  <label for="email">Email</label>
  <input id="email" type="email" placeholder="name@company.com">
  <span class="hint">We never share your email.</span>
</div>
```

## Top navigation

64px, white background, sticky, no bottom border (separation is whitespace only). Typographic wordmark on the left (16px, 500), links at 14px weight 500 with 16px rhythm, on the right: optional search icon, "Log in" ghost button, filled button for the primary action. On mobile the links hide (a "Menu" ghost button).

```html
<header class="nav"><div class="container nav-inner">
  <a class="nav-brand" href="#">Product name</a>
  <nav class="nav-links"><a href="#">Product</a><a href="#">Research</a><a href="#">Company</a></nav>
  <div class="nav-actions">
    <a class="btn btn-ghost" href="#">Log in</a>
    <a class="btn btn-filled" href="#">Try it</a>
  </div>
</div></header>
```

Note: if the nav already has the filled button, the hero must not have another. The hero can use an outlined button or the input itself as its action.

## Section header

Label at 14px weight 500 in #666, generous top margin (32-64px), with a "View more" ghost link aligned right. No bars or rules.

```html
<div class="section-header"><h2>Latest news</h2><a href="#">View more</a></div>
```

## Article card

No background, no shadow, no padding. Defined by the image (6px radius, 16:9) and the text below: title 22px weight 500, metadata 14px weight 500 in #666 ("Category · 5 min read").

```html
<article class="card">
  <div class="card-media ph-violet"></div>
  <h3 class="card-title">Article title</h3>
  <span class="card-meta">Research · 8 min read</span>
</article>
```

## Featured card (editorial hero)

One per section, in the wide column (~65%) or full width. Large image (4:3 or taller), display title 48px weight 500 at -0.03em, metadata 14px #666. The image does the visual work; the type adds editorial weight. Class: `.card.card-featured`.

## Panel [derived]

For content that needs an outline (pricing plans, feature cards, app panels): hairline border, 6px radius, 24px padding, no shadow, white background. A highlighted plan stands out through its filled button, not a background color.

## Table [derived]

14px, headers at 500 in #666, rows separated by hairlines, whisper on hover. No zebra striping, no header backgrounds.

## Footer

White background, several columns of links at 13-14px weight 500 in #666 (hover: black), top padding 64px+, legal line at 13px. No social icons or newsletter.
