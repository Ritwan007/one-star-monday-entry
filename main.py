#!/usr/bin/env python3
"""One Star for Monday - make.fun entry.

Writes one line to /output/entry.txt: a one-star review of Monday,
written as if Monday were a restaurant.

Champion line chosen by a pairwise tournament of 18 fresh candidates
(written in the build session, none copied), judged in order on the
published criteria: reads as a one-star Monday-as-restaurant review,
sounds like a real diner's complaint, lands the Monday joke, short and
quotable, plain text within 25 words. Winner: the "five days long" bill.

Deterministic: no input, no network, no randomness, no environment reads.
"""

LINE = "One star. The special board just says 'Monday'. The waiter shrugged. The bill was five days long."

def verify(text):
    if not text or not text.strip():
        raise SystemExit("entry is blank")
    if len(text) > 180:
        raise SystemExit("entry exceeds 180 characters")
    if len(text.split()) > 25:
        raise SystemExit("entry exceeds 25 words")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8

def main():
    import os
    verify(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
