"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "I asked IT why the printer only breaks before a deadline, and they said it's the only machine here that actually reads the calendar."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 132 characters, one sentence;
# setup (printer breaks before deadlines) turns on IT's answer, punchline last
# ("the only machine here that actually reads the calendar").
