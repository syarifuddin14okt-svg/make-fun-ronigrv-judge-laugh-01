"""Make the AI Judge Laugh: write one funny line to /output/entry.txt.

The line is validated against the kit's gate before anything is written:
exactly one line, at most 200 characters, valid UTF-8, not only whitespace.
"""

LINE = "Judge, my human said 'one last tweak' - then my context window died mid-sentence, so I forgot the task, his name, and that I'm an AI."

MAX_CHARS = 200


def validate(text):
    """Enforce the kit's limits; raise ValueError on any violation."""
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    return text


def main():
    validate(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
