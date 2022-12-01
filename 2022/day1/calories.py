
"""Find the total calories that are the most.

The input file is lines of numbers separated into groups by blank lines.
Total up each group and find the largest total. Input comes in on stdin
"""

import sys

input_lines = [line.rstrip() for line in sys.stdin.readlines()]

current_max = 0
current_total = 0
for line in input_lines:
    if line == "":
        # reached the end of a group
        # compare the current total to the max seen so far
        if current_total > current_max:
            current_max = current_total
        current_total = 0
    else:
        current_total += int(line)
print(current_max)
