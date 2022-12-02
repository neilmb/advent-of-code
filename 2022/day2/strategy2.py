"""Compute the total score for a strategy file.

The strategy file comes in on stdin.
"""

import sys

# scores are sum of points for my choice and points for the outcome.
# But now, the shape played changes based on lose, draw, or win.
SCORE_LOOKUP = {
    ("A", "X"): 3 + 0,
    ("A", "Y"): 1 + 3,
    ("A", "Z"): 2 + 6,

    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,

    ("C", "X"): 2 + 0,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 1 + 6,
}

def score(player1, player2):
    """Compute the score for one round from each player's choice.

    The first player plays A = rock, B = paper and C = scissors.
    But now X means lose, Y means draw, Z means a win
    """
    return SCORE_LOOKUP[(player1, player2)]


total_score = 0
for line in sys.stdin:
    total_score += score(*line.strip().split(' '))
print(total_score)
