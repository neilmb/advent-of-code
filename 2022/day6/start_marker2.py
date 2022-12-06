"""Detect where the start-of-packet marker should be.

The input is a sequence of characters. We are looking for the first
position where the four consecutive characters are all different.
"""

import sys

from collections import deque

def main(marker_length=4):
    line = sys.stdin.read()
    buffer = deque([], maxlen=marker_length)
    pos = 0
    for character in line:
        pos += 1
        buffer.append(character)
        if (len(set(buffer)) == marker_length):
            print(pos)
            break

if __name__ == "__main__":
    main(14)
