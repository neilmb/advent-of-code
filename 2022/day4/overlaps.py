"""Count complete overlaps in ranges.

Each line is a range of numbers separated by a comma. Count how many lines
have ranges where one completely contains the other.

Input comes in on stdin.
"""

import sys

def completely_contains(range1, range2):
    """Do two ranges contain each other completely?

    range1 and range2 are 2-tuples of start and end values.
    """
    set1 = set(range(int(range1[0]), int(range1[1]) + 1))
    set2 = set(range(int(range2[0]), int(range2[1]) + 1))
    return len(set1.intersection(set2)) == min(len(set1), len(set2))


def main():
    count = 0
    for line in sys.stdin.readlines():
        range1, range2 = (each.split("-") for each in line.strip().split(","))
        assert(len(range1) == 2)
        assert(len(range2) == 2)
        if completely_contains(range1, range2):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
