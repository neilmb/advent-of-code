"""Decipher which crates are on top of which stacks at the end.

Input has a description of stacks in a vertically-oriented format, then
a sequence of moves.

At the end of the moves, which crates are on top of the stacks?

Part 2 has a different rule for applying moves.

Input comes in on stdin.
"""

from stack_moves import parse_input

def apply_moves(stacks, moves):
    """Apply the moves to the given stacks."""
    for move in moves:
        # source and dest indexes are 1-based, so subtract 1
        source = stacks[move.source - 1]
        dest = stacks[move.dest - 1]
        to_move = source[:move.how_many]
        for _ in range(move.how_many):
            source.pop(0)
        dest[:0] = to_move  # terrible hack for extend at the beginning
                            # https://stackoverflow.com/a/19736074


def main():
    stacks, moves = parse_input()
    apply_moves(stacks, moves)
    print("".join(stack[0] for stack in stacks))


if __name__ == "__main__":
    main()
