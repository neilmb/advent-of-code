"""Detect where the start-of-packet marker should be.

The input is a sequence of characters. We are looking for the first
position where the four consecutive characters are all different.
"""

import sys

from collections import deque

def main():
    line = sys.stdin.read()
    four_buffer = deque([], maxlen=4)
    pos = 0
    for character in line:
        pos += 1
        four_buffer.append(character)
        if (len(set(four_buffer)) == 4):
            print(pos)
            break

if __name__ == "__main__":
    main()
