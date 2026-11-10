#!/usr/bin/env bash
# Builds dist/deego-design-system.zip (and .skill) for upload to claude.ai.
# The zip contains the deego-design-system/ folder at its root, as claude.ai expects.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/check.py
mkdir -p dist
rm -f dist/deego-design-system.zip dist/deego-design-system.skill
zip -rq dist/deego-design-system.zip deego-design-system -x "*.DS_Store" "*/__pycache__/*"
cp dist/deego-design-system.zip dist/deego-design-system.skill
echo "Built: dist/deego-design-system.zip (and .skill)"
