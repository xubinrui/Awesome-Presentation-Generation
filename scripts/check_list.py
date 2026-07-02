#!/usr/bin/env python3
"""Sanity checks for README.md list entries.

Checks (no network access required):
  * every markdown link uses https
  * no duplicate entries (same URL on two rows) within a table
  * table rows have a consistent number of columns within each table

Usage: python3 scripts/check_list.py [path/to/README.md]
"""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")


def check(readme: Path) -> int:
    text = readme.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors = []

    urls = []
    for lineno, line in enumerate(lines, 1):
        for url in LINK_RE.findall(line):
            urls.append(url)
            if url.startswith("http://"):
                errors.append(f"{readme}:{lineno}: non-https link: {url}")

    # A URL may legitimately recur across sections (paper + dataset + project),
    # within a row (title link + 📄 icon), or as a 💻 repo shared by related
    # papers. Only flag two rows of the same table whose *primary* (first)
    # link matches — that's almost always a duplicate entry.
    expected_cols = None
    seen_in_table = {}
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cols = len(stripped.split("|")) - 2
            if set(stripped) <= {"|", "-", " ", ":"}:  # separator row
                expected_cols = cols
            elif expected_cols is not None:
                if cols != expected_cols:
                    errors.append(
                        f"{readme}:{lineno}: table row has {cols} columns, expected {expected_cols}"
                    )
                row_links = LINK_RE.findall(line)
                if row_links:
                    primary = row_links[0]
                    if primary in seen_in_table:
                        errors.append(
                            f"{readme}:{lineno}: duplicate entry in table "
                            f"(also on line {seen_in_table[primary]}): {primary}"
                        )
                    else:
                        seen_in_table[primary] = lineno
        else:
            expected_cols = None
            seen_in_table = {}

    for error in errors:
        print(error, file=sys.stderr)
    print(f"{readme}: {len(urls)} links checked, {len(errors)} problem(s) found")
    return 1 if errors else 0


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("README.md")
    sys.exit(check(target))
