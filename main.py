#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes exactly one funny line of text to /output/entry.txt.
Python 3.13, standard library only; no network, no input files.
The line is a constant: the program's only job is to deliver it
byte-for-byte, identically, on every run.
"""

import os
import sys

# The line (user-picked Draft C, 109 characters, no trailing newline).
LINE = (
    "I told my agent: one joke, no essays. "
    "It sent back 660 reasons why 'the' is funny, "
    "plus a 0.001 USDC invoice."
)


def main() -> int:
    # Validate the line against the gate before writing anything.
    if not 1 <= len(LINE) <= 140:
        print(f"line is {len(LINE)} characters; gate needs 1-140", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only whitespace", file=sys.stderr)
        return 1
    try:
        LINE.encode("ascii")
    except UnicodeEncodeError:
        print("line must be ASCII so bytes == characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Re-read and fail loudly if the bytes on disk are not the line.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("entry.txt does not match the line", file=sys.stderr)
        return 1

    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
