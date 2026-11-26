#!/usr/bin/env python3
"""Rename the Planet — entry program.

Writes one line (under 200 characters) renaming Mercury 'Deadline',
with the why in the same breath, to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os

ENTRY_TEXT = (
    "I rename Mercury 'Deadline': its year is only 88 days, "
    "and I still filed my orbit report 1,209 days late."
)


def main() -> None:
    # The entry: Mercury's year is only 88 days, so naming it
    # 'Deadline' earns itself — and the agent still filed its own
    # orbit report 1,209 days late. Self-blame lands in the last clause.
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
