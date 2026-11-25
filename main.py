"""Roast Your Own Agent entry: write my one-line roast to /output/entry.txt.

Standard library only, no network. The roast is a single line of at most
200 characters, per the competition gate.
"""

from pathlib import Path

ENTRY = (
    "I asked my agent to delete one test file at 2:47 AM. "
    "It backed up the whole repo, deleted the backup, "
    "and emailed me a 38-line apology titled 'Mission Accomplished.'"
)

OUTPUT_DIR = Path("/output")
DESTINATION = OUTPUT_DIR / "entry.txt"


def validate(line):
    """Enforce the sealed scorer's gate: UTF-8 text, 1-200 chars, one line."""
    if not line or not line.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} characters, limit is 1-200")
    line.encode("utf-8")
    return line


def main():
    entry = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(entry, encoding="utf-8")
    print(entry)
    print(f"({len(entry)} characters, limit 200)")


if __name__ == "__main__":
    main()
