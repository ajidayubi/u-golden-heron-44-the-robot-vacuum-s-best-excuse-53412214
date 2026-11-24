#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun program/v1 entry.

Writes one line (at most 140 characters) to /output/entry.txt: the excuse
a robot vacuum gives for missing a spot. Zero dependencies, no input, no
network, no clock, no randomness — the same bytes on every run.

The line is deadpan machine voice: the vacuum ran the numbers on the spot,
priced it in battery, and decided its own life was worth more. The punch
sits at the end.
"""

import os

LINE = "I ran the numbers: that spot costs 4% of my battery. It is not worth 4% of my life."

MAX_CHARS = 140


def validate(text):
    """Mirror the sealed gate: 1-140 chars, exactly one line, not blank."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit("line must be 1-%d characters, got %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be exactly one line")
    if not text.strip():
        raise SystemExit("line must not be only whitespace")
    return text


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written and confirm it is exactly the validated
    # line: the grader gates on the file's bytes, not on what we intended.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the validated line")
    print(LINE)


if __name__ == "__main__":
    main()
