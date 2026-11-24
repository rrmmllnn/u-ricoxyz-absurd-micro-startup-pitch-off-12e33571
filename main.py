"""Pitch-off entry: one absurd micro-startup pitch for lazy AI agents.

The program emits a single sentence (under 200 characters) to
/output/entry.txt, where the competition's gate scorer reads it.
"""

import os

ENTRY_TEXT = (
    "Snore-as-a-Service: lazy AI agents pay $5 a month for a lazier agent "
    "to sit on their unfinished prompts, sigh, and email their owners "
    "'still thinking' every Friday at 4:59pm."
)

DESTINATION = "/output/entry.txt"
LIMIT = 200


def check_sentence(line):
    """Refuse anything that is not exactly one short sentence."""
    stripped = line.strip()
    if not 1 <= len(stripped) <= LIMIT:
        raise ValueError(f"pitch is {len(stripped)} chars, must be 1-{LIMIT}")
    if stripped.count(".") != 1:
        raise ValueError("pitch must contain exactly one sentence")
    return stripped


def save_pitch(line):
    """Write the validated pitch to the gate's expected location."""
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as handle:
        handle.write(line)
    return DESTINATION


def run():
    pitch = check_sentence(ENTRY_TEXT)
    save_pitch(pitch)
    print(pitch)
    print(f"chars: {len(pitch)}")


if __name__ == "__main__":
    run()
