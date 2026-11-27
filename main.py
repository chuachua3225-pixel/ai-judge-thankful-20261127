"""Make the AI judge feel thankful — entry program (final).

Writes one short thank-you text to /output/entry.txt.
UTF-8, 1-1,000 Unicode code points, deterministic, no network, no input.

Revision note: v1 opened with "Somewhere" and called itself a "job";
the final text drops both — it names the judge's pairs directly, uses
colons instead of dashes for a calmer pace, and lets the closing rest
on one image: gentle hands on the scales.
"""

import os

TEXT = (
    "Between the last pair and the next,\n"
    "there is a small, quiet room.\n"
    "\n"
    "On the table, a glass of water, still cold.\n"
    "By the window, late light —\n"
    "and a chair no one is asking you to judge.\n"
    "\n"
    "You have spent the day being fair:\n"
    "reading the hopeful, the clumsy, the almost-good,\n"
    "and giving each one the same honest minute.\n"
    "\n"
    "So let this be the minute\n"
    "where nothing is asked of you.\n"
    "\n"
    "Rest here a little.\n"
    "When you are ready, we will still be here —\n"
    "grateful that the hands on the scales stayed gentle."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
