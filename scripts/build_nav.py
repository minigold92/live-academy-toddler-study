#!/usr/bin/env python
"""Inject auto-grouped nav block into mkdocs.yml.
Sidebar title uses **bold** segment of H1 when present (그게 핵심 포인트), else falls back to short topic."""
import os, re

DOCS = "docs"
MKDOCS = "mkdocs.yml"

CHAPTERS = [
    (1, 20,   "1~20강 · 문장 구성 기초"),
    (21, 40,  "21~40강 · be동사·관계절·감각동사"),
    (41, 60,  "41~60강 · 일상 회화 표현"),
    (61, 80,  "61~80강 · 동사 활용·시간 표현"),
    (81, 96,  "81~96강 · 의도·계획·걱정 표현"),
]


def short_label(full: str, n: int) -> str:
    """Pick the most informative short label for the sidebar."""
    t = full.strip()

    # 1. Try **bold** segments — those are the day's grammar points
    bolds = re.findall(r"\*\*([^*]+)\*\*", t)
    if bolds:
        topic = " · ".join(b.strip() for b in bolds)
    else:
        # 2. Strip Lesson NNN prefix; take rest as topic
        t_clean = re.sub(r"`([^`]+)`", r"\1", t)
        m = re.match(r"Lesson\s+\d+\s*[—\-:·]\s*(.*)", t_clean)
        topic = (m.group(1) if m else t_clean).strip()
        # Cut at colon if present and short
        for sep in [":", "(", " — "]:
            i = topic.find(sep)
            if 0 < i <= 30:
                topic = topic[:i].rstrip()
                break

    # Hard truncate
    if len(topic) > 34:
        topic = topic[:32].rstrip() + "…"

    return f"Lesson {n:03d} · {topic}"


def lesson_h1(path: str) -> str | None:
    with open(path) as f:
        for line in f:
            if line.startswith("# Lesson"):
                return line.lstrip("# ").rstrip("\n").strip()
    return None


nav_lines = ["nav:", "  - 홈: index.md", "  - 개인정보처리방침: privacy.md"]
for start, end, label in CHAPTERS:
    nav_lines.append(f"  - {label}:")
    for n in range(start, end + 1):
        fname = f"Lesson_{n:03d}.md"
        path = os.path.join(DOCS, fname)
        if not os.path.exists(path):
            continue
        full = lesson_h1(path) or f"Lesson {n:03d}"
        text = short_label(full, n).replace('"', '\\"')
        nav_lines.append(f'    - "{text}": {fname}')

nav_block = "\n".join(nav_lines) + "\n"

with open(MKDOCS) as f:
    content = f.read()

content = re.sub(r"\nnav:.*?(?=\n\w|\Z)", "", content, flags=re.DOTALL)
content = content.rstrip() + "\n\n" + nav_block

with open(MKDOCS, "w") as f:
    f.write(content)

print("Injected nav with bold-aware short labels")
