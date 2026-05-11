#!/usr/bin/env python
"""Inject YouTube metadata block into study/Lesson_NNN.md files."""
import os, re

META_FILE = "/tmp/playlist_meta.txt"
STUDY_DIR = "study"

# Parse metadata
meta_by_index = {}
with open(META_FILE) as f:
    for line in f:
        parts = line.rstrip("\n").split("|")
        if len(parts) < 6:
            continue
        idx, vid, title, dur, _date, views = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
        try:
            n = int(idx)
        except ValueError:
            continue
        try:
            d = int(dur)
            duration = f"{d//60}분 {d%60:02d}초"
        except (ValueError, TypeError):
            duration = "—"
        try:
            v = int(views)
            if v >= 1_000_000:
                views_str = f"{v/1_000_000:.1f}M회"
            elif v >= 1_000:
                views_str = f"{v/1_000:.0f}K회"
            else:
                views_str = f"{v}회"
        except (ValueError, TypeError):
            views_str = "—"
        meta_by_index[n] = {
            "id": vid,
            "title": title,
            "duration": duration,
            "views": views_str,
        }

# Update each study file
updated = 0
for n in range(1, 97):
    path = os.path.join(STUDY_DIR, f"Lesson_{n:03d}.md")
    if not os.path.exists(path):
        continue
    if n not in meta_by_index:
        print(f"[skip] no meta for Lesson {n:03d}")
        continue
    m = meta_by_index[n]

    with open(path) as f:
        content = f.read()

    # Build metadata block
    meta_block = (
        f"> 📺 **원본 영상**: [{m['title']}](https://www.youtube.com/watch?v={m['id']})\n"
        f"> ⏱ {m['duration']} · 👁 {m['views']}\n\n"
    )

    # Remove any existing metadata block we previously inserted (idempotent)
    content = re.sub(
        r"^> 📺 \*\*원본 영상\*\*:.*\n> ⏱.*\n\n",
        "",
        content,
        count=1,
        flags=re.MULTILINE,
    )

    # Insert after first heading (the # Lesson NNN — ... line)
    lines = content.split("\n")
    out = []
    inserted = False
    for i, line in enumerate(lines):
        out.append(line)
        if not inserted and line.startswith("# Lesson"):
            # find next non-empty line; insert blank+meta after the title line
            out.append("")
            out.append(meta_block.rstrip("\n"))
            inserted = True
            # skip following blank lines so we don't double-blank
            continue

    new_content = "\n".join(out)
    # Also strip the old "## 🎬 영상" section at the bottom since it's now redundant
    new_content = re.sub(
        r"\n\n---\n\n## 🎬 영상\n원본:.*?(?=\n## |\Z)",
        "",
        new_content,
        flags=re.DOTALL,
    )

    with open(path, "w") as f:
        f.write(new_content)
    updated += 1

print(f"Updated {updated} files")
