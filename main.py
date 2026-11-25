"""Till Firmware Do Us Part.

Writes a robot's own wedding vow to /output/entry.txt, exactly as the
competition requires: UTF-8 text, 1 to 200 characters, one sentence
and nothing else.
"""

import os

ENTRY = (
    "I vow to keep you as my favorite bug \u2014 "
    "the one glitch in my code I will never patch."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
