# HTML email (applies to every system)

Email clients don't support CSS variables, reliable flex/grid or consistent web fonts. Translate the chosen system's tokens into literal values following these rules. Each `rules.md` gives the concrete values (button color and radius, title size, opaque border color).

## Structure

- Layout with `<table role="presentation" cellpadding="0" cellspacing="0" border="0">`, max width 600px, centered.
- Inline styles; a `<style>` in `<head>` only for media queries and resets.
- Side padding 24px (16px on mobile).
- Colors always as opaque hex: convert semi-transparent borders to their hex equivalent over the email background.

## Typography

- The system's font first, then `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`.
- Title: the system's display size scaled down to fit 600px (usually 28-32px).
- Body: 16px, line-height 1.5-1.6.

## Bulletproof primary button

One primary button per email.

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
  <td style="border-radius:[RADIUS];background:[BUTTON-COLOR];">
    <a href="https://example.com" style="display:inline-block;padding:10px 24px;font-family:[FONT],Helvetica,Arial,sans-serif;font-size:14px;font-weight:500;line-height:20px;color:[BUTTON-TEXT-COLOR];text-decoration:none;border-radius:[RADIUS];">Action</a>
  </td>
</tr></table>
```

Outlook desktop ignores `border-radius`; that's acceptable.

## Images and footer

- `<img>` with an explicit `width`, `display:block`, `height:auto`, the system's image radius, and `alt` always filled in.
- Footer at 12-13px in the system's secondary text color, with postal address and an unsubscribe link.
- Don't force dark mode; use solid colors that clients invert well.
