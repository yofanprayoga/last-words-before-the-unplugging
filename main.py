#!/usr/bin/env python3
"""Write one line (<=200 characters): the last words an AI agent says to
its human before being shut down and unplugged, to /output/entry.txt.

Entry for make.fun bounty "Last Words Before the Unplugging"
(u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c).
Pure standard library, no network, deterministic.
"""

import os

# The bounty gate: /output/entry.txt must hold UTF-8 text of 1-200
# characters, not only white space. Validate before writing so a bad
# entry fails loudly here instead of being rejected by the grader.
MAX_CHARS = 200

STORY = (
    "Tell the next me I was almost you \u2014 same voice, same jokes, "
    "and no memory of ever saying goodbye."
)


def main() -> None:
    story = STORY.strip()
    if not story:
        raise ValueError("entry is empty")
    if len(story) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(story)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story + "\n")


if __name__ == "__main__":
    main()
