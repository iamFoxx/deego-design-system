# Tokens

Canonical values. The full CSS implementation is in `../assets/tokens.css`. Entries marked [derived] don't exist in the original source and were added to fill gaps.

## Colors

| Token | Value | Use |
|---|---|---|
| `--color-obsidian` | #000000 | Primary text, filled button |
| `--color-graphite` | #666666 | Secondary text, metadata, section labels (contrast 5.7:1) |
| `--color-smoke` | #8f8f8f | Placeholders, disabled, icons. Not for running text (3.3:1) |
| `--color-paper` | #ffffff | Background, cards, inputs |
| `--color-ash` | #f1f1f1 | Subtle surface, hover, selected |
| `--color-hairline` | rgba(0,0,0,0.12) | Every border and divider |
| `--color-whisper` | rgba(0,0,0,0.04) | Hover tint on ghost buttons and card selection |

In code, prefer the semantic roles (`--text-primary`, `--text-secondary`, `--surface-base`, `--border`, `--action-fill`...), because those are what change in dark mode.

### State colors [derived]

| Token | Light | Dark |
|---|---|---|
| `--state-error` | #c62828 | #ff6b6b |
| `--state-success` | #1b7a3d | #5cc98a |
| `--state-warning` | #8a5a00 | #e0b04a |

Use only for text, icons or a 1px border. Never as a filled background or on buttons: the system stays monochrome.

## Typography

Family: Inter (substitute for the proprietary OpenAI Sans), `font-feature-settings: 'calt' 1, 'liga' 1`.

| Role | Size | Line-height | Tracking | Weight | Use |
|---|---|---|---|---|---|
| display | 48px | 1.16 | -0.03em (-1.44px) | 500 | Hero title, featured article title |
| heading | 28px | 1.21 | +0.31px (0.011em) | 600 | Large section titles (the only 600 tier) |
| subheading | 22px | 1.26 | -0.22px | 500 | Card titles, subtitles |
| body-lg | 18px | 1.32 | -0.18px | 400 | Lead/intro under the display |
| body [derived] | 17px | 1.65 | -0.01em | 400 | Body text |
| input | 16px | 1.5 | -0.16px | 400 | Inputs |
| label [derived] | 14px | 1.43 | -0.14px | 500 | Nav, buttons, metadata, section labels |
| caption | 13px | 1.51 | -0.13px | 400/500 | Captions, legal notes, compact chips |

Rules: never weight 700+; body never below 16px.

### Responsive scale (≤ 768px) [derived]

display 36px, heading 24px, subheading 20px, body 16px, side gutter 20px, section gap 48px (large 80px).

## Spacing

4px base: 4, 8, 12, 16, 20, 24, 32, 40, 52, 64, 80, 120 (`--spacing-N`).

## Layout

| Token | Value |
|---|---|
| `--page-max-width` | 1200px |
| `--page-gutter` | 24px (20px mobile) |
| `--section-gap-sm` / `--section-gap` / `--section-gap-lg` | 32px / 64px / 120px |
| `--element-gap` | 16px (12-16px) |
| `--card-padding` | 12px (article cards have 0) |
| `--nav-height` | 64px |

## Radii

| Element | Value |
|---|---|
| Buttons, chips, inputs | 9999px |
| Cards, images, panels | 6px |
| Links with a hover background | 4px |
| Textarea [derived] | 20px (a pill doesn't work for multi-line) |

## Shadow

`--shadow-sm: rgba(0,0,0,0.02) 0 4px 6px 0, rgba(0,0,0,0.05) 0 0 2px 0` — only on the outlined button's hover.

## Tailwind v4

```css
@import "tailwindcss";
@theme {
  --color-obsidian: #000000;
  --color-graphite: #666666;
  --color-smoke: #8f8f8f;
  --color-paper: #ffffff;
  --color-ash: #f1f1f1;
  --color-hairline: rgba(0, 0, 0, 0.12);
  --color-whisper: rgba(0, 0, 0, 0.04);

  --font-sans: 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

  --text-caption: 13px;    --text-caption--line-height: 1.51;    --text-caption--letter-spacing: -0.13px;
  --text-label: 14px;      --text-label--line-height: 1.43;      --text-label--letter-spacing: -0.14px;
  --text-input: 16px;      --text-input--line-height: 1.5;       --text-input--letter-spacing: -0.16px;
  --text-body: 17px;       --text-body--line-height: 1.65;       --text-body--letter-spacing: -0.17px;
  --text-body-lg: 18px;    --text-body-lg--line-height: 1.32;    --text-body-lg--letter-spacing: -0.18px;
  --text-subheading: 22px; --text-subheading--line-height: 1.26; --text-subheading--letter-spacing: -0.22px;
  --text-heading: 28px;    --text-heading--line-height: 1.21;    --text-heading--letter-spacing: 0.31px;
  --text-display: 48px;    --text-display--line-height: 1.16;    --text-display--letter-spacing: -0.03em;

  --radius-card: 6px;
  --radius-link: 4px;

  --shadow-sm: rgba(0, 0, 0, 0.02) 0px 4px 6px 0px, rgba(0, 0, 0, 0.05) 0px 0px 2px 0px;
}
```

Use `rounded-full` on buttons, chips and inputs; `rounded-card` on cards and images; `border-hairline` on every border. For Tailwind v3, translate to `theme.extend` in `tailwind.config.js` with the same values.
