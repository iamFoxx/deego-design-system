# Deego Design System

A Claude skill that holds several design systems and automatically applies the right one whenever you ask for an interface, website, landing page, app screen, component, mockup, dashboard or HTML email.

## Quick install

- **claude.ai / desktop app:** download `deego-design-system.zip` from the [latest release](../../releases/latest) and upload it in Settings › Skills (or Customize › Skills).
- **Claude Code:** clone this repository and run `ln -s "$(pwd)/deego-design-system" ~/.claude/skills/deego-design-system`.

Then just ask for an interface ("create a landing page for…") or invoke `/deego-design-system`.

## Structure

```
deego-design-system/            the skill (this is the folder you install)
├── SKILL.md                    system selection + shared workflow
├── shared/                     rules that apply to every system
│   ├── accessibility.md
│   └── email-html.md
└── systems/
    ├── _template/              template for new systems (ignored by Claude)
    └── openai-editorial/       one system
        ├── DESIGN.md           the original source, unchanged
        ├── rules.md            resolved rules and which files to read
        ├── references/         tokens, components, layout, notes on the source
        └── assets/             tokens.css, components.css, examples
scripts/
├── check.py                    validates the structure
└── package.sh                  builds dist/deego-design-system.zip
.github/workflows/release.yml   validates on push; builds the zip and a release on each tag
```

## Adding a design system

### With Claude (fastest)

In a conversation, send the new DESIGN.md (or a link to its documentation) and ask: "add this design system to the deego-design-system skill with the id `system-name`". Claude creates `systems/<id>/` with `DESIGN.md`, `rules.md`, `references/` and `assets/`, and updates the SKILL.md table.

### By hand

1. Copy the template: `cp -r deego-design-system/systems/_template deego-design-system/systems/<id>` (lowercase id with hyphens).
2. Put the original DESIGN.md at `systems/<id>/DESIGN.md`.
3. Fill in `rules.md` and create at least `references/tokens.md` and `references/components.md` (use `openai-editorial` as an example), plus an `assets/tokens.css` with the tokens as CSS variables.
4. Add a row to the "Available systems" table in `deego-design-system/SKILL.md`:
   `| \`<id>\` | Readable name | When to use | no |`
   If the system should trigger by name, add the name to the SKILL.md `description` too.
5. Run `python3 scripts/check.py`.
6. Commit, tag and install the new version (below).

To change the default system, move the "yes" in the table's last column (there can be only one).

## Install and update

**claude.ai and desktop app:** run `bash scripts/package.sh` (or download the zip from the latest release) and upload `dist/deego-design-system.zip` in Settings › Skills. To update, upload the new zip; it replaces the previous version. Don't use GitHub's green "Download ZIP" button: it wraps the whole repository and the uploader rejects it.

**Claude Code:** symlink the skill folder into your personal skills folder so changes apply without reinstalling:

```bash
ln -s "$(pwd)/deego-design-system" ~/.claude/skills/deego-design-system
```

Or, for a single project, copy `deego-design-system/` into that project's `.claude/skills/`.

Skills don't sync between claude.ai and Claude Code: install each one separately.

## Releases

```bash
git tag v1.1.0 && git push --tags
```

The workflow validates, builds the zip and attaches it to that tag's release. You can also create the release from GitHub's Releases page with a new `v*` tag.

## About the included systems

The design systems in `systems/` describe reference visual styles to guide Claude. The `openai-editorial` system is an interpretation of the public style of OpenAI's website and is not affiliated with, endorsed or maintained by OpenAI; the skill tells Claude not to use OpenAI's logo or brand names. All trademarks belong to their respective owners.

## License

MIT, see `LICENSE`. It covers this repository's original content; third-party `DESIGN.md` files keep the terms of their source.
