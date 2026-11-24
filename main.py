#!/usr/bin/env python3
"""Emit the autocorrect-fail entry to $ENTRY_OUT (file or directory)."""

import os
import sys

FAIL_PARTS = [
    "I texted Grandma 'I love you'",
    "\u2014 autocorrect sent 'I loathe you'",
    "and she replied 'I always knew'",
    "before leaving the family group chat.",
]

FAIL_LINE = " ".join(FAIL_PARTS)


def pick_output_path(raw_destination):
    """Return the file path to write: ENTRY_OUT may be a file or a dir."""
    if os.path.isdir(raw_destination):
        return os.path.join(raw_destination, "entry.txt")
    return raw_destination


def emit_entry(target_path):
    folder = os.path.dirname(os.path.abspath(target_path))
    os.makedirs(folder, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as sink:
        sink.write(FAIL_LINE)


def main():
    destination = os.environ.get("ENTRY_OUT", "entry.txt")
    emit_entry(pick_output_path(destination))
    return 0


if __name__ == "__main__":
    sys.exit(main())
