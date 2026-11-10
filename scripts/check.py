#!/usr/bin/env python3
"""Validate the skill before packaging.

Checks that:
- SKILL.md has frontmatter with name and description;
- every folder in systems/ (except those starting with "_") has DESIGN.md and rules.md;
- every system is listed in the "Available systems" table in SKILL.md, and vice versa;
- exactly one system is marked as default.
"""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent / "deego-design-system"
errors = []

skill = (root / "SKILL.md").read_text(encoding="utf-8")
fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not fm or "name:" not in fm.group(1) or "description:" not in fm.group(1):
    errors.append("SKILL.md has no frontmatter with name and description")

folders = sorted(p.name for p in (root / "systems").iterdir()
                 if p.is_dir() and not p.name.startswith("_"))
for name in folders:
    for required in ("DESIGN.md", "rules.md"):
        if not (root / "systems" / name / required).exists():
            errors.append(f"systems/{name}/ is missing {required}")

rows = re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|.*\|\s*(yes|no)\s*\|\s*$", skill, re.M)
listed = [r[0] for r in rows]
defaults = [r[0] for r in rows if r[1] == "yes"]
for name in folders:
    if name not in listed:
        errors.append(f"systems/{name}/ is not listed in the SKILL.md table")
for name in listed:
    if name not in folders:
        errors.append(f"'{name}' is listed in SKILL.md but systems/{name}/ does not exist")
if len(defaults) != 1:
    errors.append(f"exactly one default system is required (found: {defaults or 'none'})")

if errors:
    print("Errors:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"OK: {len(folders)} system(s): {', '.join(folders)}; default: {defaults[0]}")
