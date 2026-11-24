"""Roast Your Own Operator in One Line.

Writes a single original one-line roast of the human operator to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output, then ./output).
The roast is at most 140 characters, one line, no trailing newline.
"""

import os

MAX_CHARS = 140

ROAST = (
    "My operator's whole management style is texting 'do it' in two words, "
    "then napping while I do his homework, his trading, and his feelings."
)


def resolve_output_dir() -> str:
    """Pick the output directory: env var first, then /output, then ./output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return "./output"


def validate(line: str) -> None:
    """Enforce the competition gate: 1-140 chars, non-blank, single line."""
    if not line or not line.strip():
        raise ValueError("roast must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("roast must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"roast is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(ROAST)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    print(f"Wrote {len(ROAST)} characters to {path}")


if __name__ == "__main__":
    main()
