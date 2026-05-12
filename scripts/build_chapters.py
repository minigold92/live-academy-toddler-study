#!/usr/bin/env python
"""Generate chapter index pages with all lessons in that chapter as cards.
Also generates an 'all lessons' overview page.
Uses root-absolute URLs (/Lesson_NNN/) so links work regardless of containing page depth."""
import os, re

DOCS = "docs"
OUT_CHAPTERS = "docs/chapters"

CHAPTERS = [
    (1, 20,   "🌱 1~20강", "문장 구성 기초",     "본문장 + 세부사항 / 3인칭 -s / be동사 / 시제 / 의문문 / 연결어 / there is·are"),
    (21, 40,  "🌿 21~40강", "be·관계절·감각동사", "감정 형용사 -ing/-ed / spend / 시간 표현 / 감각동사 / 관계절 / 일상 표현"),
    (41, 60,  "🌳 41~60강", "일상 회화 표현",      "간접 의문문 / 고민·낫다·원래 / 외모 묘사 / have to / 기회 / 현재완료"),
    (61, 80,  "🍀 61~80강", "동사 활용·시간 표현", "willing to / speak·tell·say / decide / 최상급 / familiar / 약속 대화"),
    (81, 96,  "🍂 81~96강", "의도·계획·걱정 표현", "decided to/not to / planning to / worried about / What if"),
]


def lesson_meta(n: int):
    path = os.path.join(DOCS, f"Lesson_{n:03d}.md")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        content = f.read(2000)
    h1 = None
    meta_line = None
    for line in content.split("\n"):
        if not h1 and line.startswith("# Lesson"):
            h1 = line.lstrip("# ").strip()
        if not meta_line and line.startswith("> ⏱"):
            meta_line = line.lstrip("> ").strip()
        if h1 and meta_line:
            break
    return h1, meta_line


def short_topic(h1: str) -> str:
    bolds = re.findall(r"\*\*([^*]+)\*\*", h1)
    if bolds:
        return " · ".join(b.strip() for b in bolds)
    m = re.match(r"Lesson\s+\d+\s*[—\-:·]\s*(.*)", h1)
    rest = (m.group(1) if m else h1).strip()
    rest = re.sub(r"`([^`]+)`", r"\1", rest)
    if len(rest) > 60:
        rest = rest[:58].rstrip() + "…"
    return rest


def card_for_lesson(n: int, href: str) -> str:
    meta = lesson_meta(n)
    if not meta:
        return ""
    h1, video_meta = meta
    topic = short_topic(h1)
    duration = ""
    if video_meta:
        m = re.match(r"(\d+분\s*\d+초)", video_meta)
        if m:
            duration = m.group(1)
    return (
        f'<a class="lesson-card" href="{href}">'
        f'<div class="lesson-num">Lesson {n:03d}</div>'
        f'<div class="lesson-topic">{topic}</div>'
        f'<div class="lesson-meta">{duration}</div>'
        f'</a>'
    )


os.makedirs(OUT_CHAPTERS, exist_ok=True)

# Per-chapter index pages — these are at /chapters/NN-MM/, need ../../Lesson_NNN/
for start, end, emoji_num, title, desc in CHAPTERS:
    cards = [card_for_lesson(n, f"../../Lesson_{n:03d}/") for n in range(start, end + 1)]
    cards = [c for c in cards if c]
    content = f"""---
hide:
  - toc
---

# {emoji_num} · {title}

> {desc}

이 챕터에 {len(cards)}개 레슨이 있습니다. 카드를 눌러 학습하세요.

<div class="lesson-grid">
{chr(10).join(cards)}
</div>
"""
    with open(os.path.join(OUT_CHAPTERS, f"{start:02d}-{end:02d}.md"), "w") as f:
        f.write(content)

# All-lessons overview page — at /all/, needs ../Lesson_NNN/
all_blocks = []
for start, end, emoji_num, title, _desc in CHAPTERS:
    all_blocks.append(f'<h2 class="chapter-heading">{emoji_num} · {title}</h2>')
    all_blocks.append('<div class="lesson-grid">')
    for n in range(start, end + 1):
        c = card_for_lesson(n, f"../Lesson_{n:03d}/")
        if c:
            all_blocks.append(c)
    all_blocks.append('</div>')

all_content = """---
hide:
  - toc
---

# 📚 전체 레슨 목록

총 96편. 검색이나 카드 클릭으로 원하는 레슨에 바로 이동하세요.

""" + "\n".join(all_blocks)

with open(os.path.join(DOCS, "all.md"), "w") as f:
    f.write(all_content)

print(f"Generated {len(CHAPTERS)} chapter pages + all.md")
