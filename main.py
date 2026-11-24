#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (1-200 chars) to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
Standard library only.
"""

import os

LINE = (
    "I threw my back out reaching for the snooze button. "
    "My own spine is now on strike."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
