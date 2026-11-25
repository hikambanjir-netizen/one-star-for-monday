"""One Star for Monday - a make.fun one-line entry.

Writes a single one-star review to /output/entry.txt, written as if
Monday were a restaurant and the reviewer a diner who was served it
against their will: the special arrived uninvited, the one small order
never came, and the bill was eight meetings.
"""

import os

def review_line() -> str:
    """The review, kept in a real diner's three complaints.

    Something was served that nobody ordered, something small that was
    ordered never arrived, and the bill was worse than the meal. Every
    detail could only be Monday: the 6am seating, the five more
    minutes, the eight meetings.
    """
    return (
        "One star. The Monday special arrived uninvited at 6am, "
        "my order of five more minutes never came, "
        "and the bill was eight meetings."
    )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(review_line())


if __name__ == "__main__":
    main()
