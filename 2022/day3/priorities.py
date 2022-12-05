"""Sum the priorities for mis-filed items in rucksacks.

Rucksack contents are on each line, half in one compartment,
half in the other. One item is in both compartments. For each
line, find the item that is in both, compute its "priority"
and sum those up.

Input is expected on stdin.
"""

import sys

def split_compartments(line):
    """Split a list of items into two even strings.

    The input has an even number of characters, return the first and second
    halves as a 2-tuple.
    """
    length = len(line)
    # Use integer division
    return (line[:length//2], line[length//2:])

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

    for line in sys.stdin.readlines():
        first, second = split_compartments(line.strip())
        common_letter = set(first).intersection(second).pop()
        total += priority(common_letter)
    print(total)

if __name__ == "__main__":
    main()
