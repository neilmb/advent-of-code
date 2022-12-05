"""Sum the priorities for badges in groups of 3 rucksacks.

Rucksack contents are on each line. In each group of 3 lines, one
item will occur on all three lines. Find it and sum up the priorities.

Input is expected on stdin.
"""

import sys

from more_itertools import chunked

def find_badge(lines):
    """Find the id badge on 3 lines

    Input is an iterable of 3 strings. One character occurs on all three of
    those lines.
    """
    so_far = set(lines[0])
    for line in lines[1:]:
        so_far = so_far.intersection(line)
    assert(len(so_far) == 1)
    return so_far.pop()


def priority(character):
    """Each character has a priority, 1-26 for a-z and 27-52 for A-Z."""
    this_ord = ord(character)
    if this_ord < 97:
        # ord("a") is 97, uppercase comes before
        return this_ord - 65 + 27
    else:
        # lowercase
        return this_ord - 97 + 1


def main():
    total = 0

    for lines in chunked((line.strip() for line in sys.stdin.readlines()), 3):
        common_letter = find_badge(lines)
        total += priority(common_letter)
    print(total)

if __name__ == "__main__":
    main()
