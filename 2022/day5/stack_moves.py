"""Decipher which crates are on top of which stacks at the end.

Input has a description of stacks in a vertically-oriented format, then
a sequence of moves.

At the end of the moves, which crates are on top of the stacks?

Input comes in on stdin.
"""

import sys, re

from collections import namedtuple

from more_itertools import split_at, chunked


def _num_stacks(last_line):
    """From the last line determine how many stacks we need."""
    line = last_line.replace(" ", "")
    return max(map(int, line))


def split_stacks(line):
    """Split a line of stack contents into a list of items.

    Stacks without items on this line will have empty strings.
    """

    def _clean(string):
        """Get rid of brackets and spaces."""
        return "".join(filter(lambda c: c not in "[] ", string))

    # columns are 3 characters long, separated with spaces get a list of those
    # strings
    columns = list(map(lambda l: "".join(l), chunked(line, 4)))
    # get rid of spaces and brackets, what's left are the correct values
    return [_clean(item) for item in columns]


def parse_stacks(stack_description):
    """Parse a list of lines into a description of stacks."""
    # last line tells us how many stacks we need
    # only works if there is at most 9 stacks
    num_stacks = _num_stacks(stack_description[-1])
    stacks = [[] for _ in range(num_stacks)]
    for line in stack_description[:-1]:
        for pos, value in enumerate(split_stacks(line)):
            if value:
                stacks[pos].append(value)
    return stacks


Move = namedtuple("Move", ["how_many", "source", "dest"])


def parse_move(line):
    """Parse a line into a Move object."""
    match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    if not match:
        raise ValueError("No match on line %s", line)
    return Move(*[int(i) for i in match.groups()])


def parse_moves(move_description):
    """Parse a list of lines into a list of move descriptions."""
    return [parse_move(line) for line in move_description]


def parse_input():
    """Parse input file into stacks and moves.

    The two sections are separated by a blank line.
    """
    stack_description, move_description = split_at(
        (line.rstrip("\n") for line in sys.stdin.readlines()),
        lambda line: len(line) == 0,
        maxsplit=1,
    )
    return parse_stacks(stack_description), parse_moves(move_description)


def apply_moves(stacks, moves):
    """Apply the moves to the given stacks."""
    for move in moves:
        # source and dest indexes are 1-based, so subtract 1
        source = stacks[move.source - 1]
        dest = stacks[move.dest - 1]
        for _ in range(move.how_many):
            item = source.pop(0)
            dest.insert(0, item)


def main():
    stacks, moves = parse_input()
    apply_moves(stacks, moves)
    print("".join(stack[0] for stack in stacks))


if __name__ == "__main__":
    main()
