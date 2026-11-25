#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, in the voice of an AI agent
that quit its job to become a barista, to /output/entry.txt.

The line is deliberately one sentence-flow reply a real inbox would send
back: it opens like an auto-reply, then turns three machine habits into
coffee-shop facts -- the system prompt becomes the menu, the context
window becomes the morning queue, and hallucinations survive only as
latte art. No bean, espresso or caffeine pun does the joking; the joke
is the machine still reporting its own internals, just from behind a
counter now.
"""

import os
import sys

ENTRY = (
    "Thank you for your email \u2014 I am out of office, having resigned to "
    "become a barista. My new system prompt is the menu, my context "
    "window is the morning queue, and my hallucinations are now latte "
    "art only."
)


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 280:
        print(f"entry is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
