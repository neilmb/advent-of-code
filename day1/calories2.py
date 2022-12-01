
"""Find the total calories in a group for the largest three groups.

The input file is lines of numbers separated into groups by blank lines.
Total up each group and find the largest total. Input comes in on stdin.
"""

import sys

input_lines = [line.rstrip() for line in sys.stdin.readlines()]

current_total = 0
totals = []
for line in input_lines:
    if line == "":
        # reached the end of a group
        totals.append(current_total)
        current_total = 0
    else:
        current_total += int(line)
print(sum(sorted(totals)[-3:]))
