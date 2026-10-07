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
# The capture group must match the unchecked state (' ') AND both checked
# spellings ('x'/'X') — we count done vs total from the same matches.
TASK_RE = re.compile(r"^- \[( |[xX])\] \[Day \d+ —", re.MULTILINE)


def read_blocks():
    """Return [(block_dir_name, done, total, drift_or_broken)]."""
    rows = []
    for block in sorted(p for p in DOCS.iterdir() if p.is_dir()):
        readme = block / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        checks = TASK_RE.findall(text)
        done, total = sum(1 for c in checks if c.lower() == "x"), len(checks)
        has_marker = "**Progress:**" in text
        marker = PROGRESS_RE.search(text)
        if has_marker and marker is None:
            # A marker that exists but cannot be parsed must never pass the
            # guard silently — treat it as drift.
            rows.append((block.name, done, total, True))
        elif marker is not None:
            marker_done, marker_total = int(marker.group(1)), int(marker.group(2))
            rows.append((block.name, done, total, (done, total) != (marker_done, marker_total)))
        else:
            rows.append((block.name, done, total, False))
    return rows


def main():
    rows = read_blocks()
    if not rows:
        print("no block READMEs found under docs/")
        return 1

    for block, done, total, drifted in rows:
        flag = " (marker drift!)" if drifted else ""
        bar = "#" * done + "." * (total - done)
        print(f"{block:32s} [{bar}] {done:>2}/{total}{flag}")
    overall_done = sum(r[1] for r in rows)
    overall_total = sum(r[2] for r in rows)
    print("-" * 50)
    print(f"{'OVERALL':32s} {overall_done:>3}/{overall_total} days complete")

    drifted = [r for r in rows if r[3]]
    if drifted:
        print("\nFAIL: progress markers out of sync with checkboxes:")
        for block, done, total, _ in drifted:
            print(f"  {block}: checkboxes say {done}/{total}, marker disagrees or is unreadable")
        return 1
    if len(sys.argv) < 2 or sys.argv[1] != "--quiet":
        print("\nAll progress markers in sync. Keep it up! 🎯")
    return 0


if __name__ == "__main__":
    sys.exit(main())