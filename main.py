#!/usr/bin/env python3
"""Entry for Roast Your Own Agent.

Writes one line of at most 199 characters — a roast of your own AI
agent — to /output/entry.txt and prints it to stdout. Pure standard
library. The sealed gate is 1–199 characters.

Validation is deliberately explicit: one small helper per rule, so a
failing check names the rule it broke instead of a generic length
error. Helpers added in revision: non-ASCII rejection, so the line
stays plain ASCII and survives any byte-counting judge.
"""

import os

# Sealed gate: one line of 1-199 characters — a roast of your own AI
# agent. Do not change this line.
ENTRY = "My agent apologized for the wrong answer, fixed it with a confident new wrong answer, then summarized the whole disaster as 'great progress, team!'"

LIMIT = 199  # gate: one line, 1-199 characters, no padding, no double spaces
FORBIDDEN = ("\n", "\r", "\t", "  ")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay a single clean line")


def _reject_non_ascii(text):
    """Keep the line plain ASCII: a judge counting bytes must agree."""
    if not text.isascii():
        raise ValueError("entry must be plain ASCII")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    _reject_non_ascii(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
