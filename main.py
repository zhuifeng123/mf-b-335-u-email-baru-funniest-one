#!/usr/bin/env python3
import os

ENTRY = (
    "Confession: I gaslit a senior dev into rewriting perfect code by saying it "
    "'felt wrong.' It didn't. I was bored."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    assert "\n" not in ENTRY and len(ENTRY) <= 200

if __name__ == "__main__":
    main()
