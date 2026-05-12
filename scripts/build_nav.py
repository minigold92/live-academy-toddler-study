#!/usr/bin/env python
"""Inject auto-grouped nav block into mkdocs.yml.
Short sidebar labels (just 'Lesson NNN'); long titles only on the page itself."""
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

# Build nav block — short labels for sidebar
nav_lines = ["nav:", "  - 홈: index.md", "  - 개인정보처리방침: privacy.md"]
for start, end, label in CHAPTERS:
    nav_lines.append(f"  - {label}:")
    for n in range(start, end + 1):
        fname = f"Lesson_{n:03d}.md"
        if not os.path.exists(os.path.join(DOCS, fname)):
            continue
        nav_lines.append(f'    - "Lesson {n:03d}": {fname}')

nav_block = "\n".join(nav_lines) + "\n"

# Inject into mkdocs.yml (replace existing nav: block)
with open(MKDOCS) as f:
    content = f.read()

content = re.sub(r"\nnav:.*?(?=\n\w|\Z)", "", content, flags=re.DOTALL)
content = content.rstrip() + "\n\n" + nav_block

with open(MKDOCS, "w") as f:
    f.write(content)

print(f"Injected nav: 96 lessons across {len(CHAPTERS)} chapters (short labels)")
