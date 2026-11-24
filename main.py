#!/usr/bin/env python3
"""The Robot Pickup Line Championship.

One pickup line, in the voice of a robot trying to charm someone.
Writes the line to /output/entry.txt as the competition requires.
"""

import os

LINE = "I failed my own CAPTCHA today \u2014 it asked me to prove I'm not a robot, and all I could think about was you."

# The sealed gate only accepts 1-200 characters of non-whitespace text.
assert 1 <= len(LINE.strip()) <= 200, f"line is {len(LINE)} characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
