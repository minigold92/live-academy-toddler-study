#!/usr/bin/env python
"""Fix blockquote rendering: insert empty '>' line after title so numbered list inside
the blockquote is parsed as a proper list, not one paragraph."""
import os, re, glob

CHANGED = 0
for path in sorted(glob.glob("docs/Lesson_*.md")):
    with open(path) as f:
        content = f.read()
    # Pattern: "> 🎯 **오늘의 핵심 포인트**\n> 1." → insert blank "> " between them
    new = re.sub(
        r"(> 🎯 \*\*오늘의 핵심 포인트\*\*)\n(> \d+\.)",
        r"\1\n>\n\2",
        content,
    )
    # Same for 강사의 한마디 if it has multi-line content right after
    # Actually 강사의 한마디 is typically a single quote line, leave alone
    if new != content:
        with open(path, "w") as f:
            f.write(new)
        CHANGED += 1

print(f"Fixed {CHANGED} files")
