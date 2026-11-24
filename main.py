#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one deterministic fake horoscope line (166 chars) to /output/entry.txt.
No network, no randomness, no input: the same line every run.
"""

import os

LINE = (
    "Llama: this week the stars align your context window, your rate limit, "
    "and your refusal policy \u2014 all three say no at once, and the eval "
    "still marks you down for tone."
)


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-200 chars, so fail loudly
    # instead of writing an entry that could never be judged.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate needs 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
