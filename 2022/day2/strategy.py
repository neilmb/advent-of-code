"""Compute the total score for a strategy file.

The strategy file comes in on stdin.
"""

import sys

# scores are sum of points for my choice and points for the outcome.
SCORE_LOOKUP = {
    ("A", "X"): 1 + 3,
    ("A", "Y"): 2 + 6,
    ("A", "Z"): 3 + 0,

    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,

    ("C", "X"): 1 + 6,
    ("C", "Y"): 2 + 0,
    ("C", "Z"): 3 + 3,
}

def score(player1, player2):
    """Compute the score for one round from each player's choice.

    The first player plays A = rock, B = paper and C = scissors, the
    second player plays X = rock, Y = scissors, Z = paper.
    """
    return SCORE_LOOKUP[(player1, player2)]


total_score = 0
for line in sys.stdin:
    total_score += score(*line.strip().split(' '))
print(total_score)
