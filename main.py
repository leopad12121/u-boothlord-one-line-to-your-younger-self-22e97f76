#!/usr/bin/env python3
"""Write one line to your younger self to entry.txt.

Stdlib only, no network, no randomness: the output is deterministic.
"""

import os

LINE = "Kid, the girl who just laughed at your haircut will marry you in eleven years \u2014 so come out of the library."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
