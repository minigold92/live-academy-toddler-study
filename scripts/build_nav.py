#!/usr/bin/env python
"""Inject auto-grouped nav block into mkdocs.yml.
Groups lessons by chapter (001-020 / 021-040 / 041-060 / 061-080 / 081-096)."""
import os, re, glob

DOCS = "docs"
MKDOCS = "mkdocs.yml"

CHAPTERS = [
    (1, 20,   "1~20강 · 문장 구성 기초"),
    (21, 40,  "21~40강 · be동사·관계절·감각동사"),
    (41, 60,  "41~60강 · 일상 회화 표현"),
    (61, 80,  "61~80강 · 동사 활용·시간 표현"),
    (81, 96,  "81~96강 · 의도·계획·걱정 표현"),
]

# Read each lesson's title (the # heading)
titles = {}
for f in sorted(glob.glob(os.path.join(DOCS, "Lesson_*.md"))):
    with open(f) as fp:
        for line in fp:
            if line.startswith("# Lesson"):
                titles[os.path.basename(f)] = line.lstrip("# ").strip()
                break

# Build nav block
nav_lines = ["nav:", "  - 홈: index.md"]
for start, end, label in CHAPTERS:
    nav_lines.append(f"  - {label}:")
    for n in range(start, end + 1):
        fname = f"Lesson_{n:03d}.md"
        title = titles.get(fname, fname)
        # Escape any quotes in title
        safe_title = title.replace('"', '\\"')
        nav_lines.append(f'    - "{safe_title}": {fname}')

nav_block = "\n".join(nav_lines) + "\n"

# Inject into mkdocs.yml (replace existing nav: block or append)
with open(MKDOCS) as f:
    content = f.read()

# Remove existing nav: block if any
content = re.sub(r"\nnav:.*?(?=\n\w|\Z)", "", content, flags=re.DOTALL)

# Append at end
content = content.rstrip() + "\n\n" + nav_block

with open(MKDOCS, "w") as f:
    f.write(content)

print(f"Injected nav: {len(titles)} lessons across {len(CHAPTERS)} chapters")
