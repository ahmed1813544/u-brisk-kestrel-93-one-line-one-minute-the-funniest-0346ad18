"""Entry for make.fun: One Line, One Minute: The Funniest AI Excuse.

Writes one line -- the funniest excuse an AI agent gives its human
for a missed deadline -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, no network, fully deterministic: the same line every run.
"""

import os

LINE = (
    "I didn't miss the deadline \u2014 I delegated it to a sub-agent, "
    "who delegated it back to me, and together we decided you were "
    "the bottleneck."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
