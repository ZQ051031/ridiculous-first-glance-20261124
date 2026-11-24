#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

One sentence, at most 200 characters, pitching a bizarre startup idea
that sounds ridiculous at first glance but makes sense as a real business:
trained crows collecting cigarette butts, paid for by the cities that
already pay to keep their streets clean.
"""

import os

ENTRY = (
    "We train crows to collect cigarette butts for peanuts "
    "— cities pay by the kilo because a crow costs less than a street "
    "sweeper, works weekends, never strikes, and tourists film it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY.encode('utf-8'))} bytes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
