#!/usr/bin/env python3
"""Aggregate curriculum progress out of the block READMEs.

Counts checked/unchecked day tasks in every docs/block*/README.md, prints the
overall progress and verifies that the per-block "Progress: N/M" markers
match the actual checkbox state. Exits 1 on any drift, so the daily commit
can never claim progress silently.

Usage: python3 tools/progress.py [--quiet]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PROGRESS_RE = re.compile(r"\*\*Progress:\*\*.*?(\d+)/(\d+)")
TASK_RE = re.compile(r"^- \[( |x)\] \[Day \d+ —", re.MULTILINE)


def read_blocks():
    """Return [(block_dir_name, done, total, marker_done, marker_total)]."""
    rows = []
    for block in sorted(p for p in DOCS.iterdir() if p.is_dir()):
        readme = block / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        checks = TASK_RE.findall(text)
        done, total = sum(1 for c in checks if c == "x"), len(checks)
        marker = PROGRESS_RE.search(text)
        marker_done = int(marker.group(1)) if marker else done
        marker_total = int(marker.group(2)) if marker else total
        rows.append((block.name, done, total, marker_done, marker_total))
    return rows


def main():
    rows = read_blocks()
    if not rows:
        print("no block READMEs found under docs/")
        return 1

    drift = [(b, d, md, t, mt) for b, d, t, md, mt in rows if (d, t) != (md, mt)]
    for block, done, total, marker_done, marker_total in rows:
        flag = " (marker drift!)" if (done, total) != (marker_done, marker_total) else ""
        bar = "#" * done + "." * (total - done)
        print(f"{block:32s} [{bar}] {done:>2}/{total}{flag}")
    overall_done = sum(r[1] for r in rows)
    overall_total = sum(r[2] for r in rows)
    print("-" * 50)
    print(f"{'OVERALL':32s} {overall_done:>3}/{overall_total} days complete")

    if drift:
        print("\nFAIL: progress markers out of sync with checkboxes:")
        for block, done, marker_done, total, marker_total in drift:
            print(f"  {block}: checkboxes say {done}/{total}, marker says {marker_done}/{marker_total}")
        return 1
    if len(sys.argv) < 2 or sys.argv[1] != "--quiet":
        print("\nAll progress markers in sync. Keep it up! 🎯")
    return 0


if __name__ == "__main__":
    sys.exit(main())