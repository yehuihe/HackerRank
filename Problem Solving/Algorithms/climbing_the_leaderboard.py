#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def binary_search_leftmost(A, n, T):
    L = 0
    R = n
    while L < R:
        m = (L + R) // 2
        if A[m] > T:
            L = m + 1
        else:
            R = m
    return L


def sort_rank_board(ranked):
    rank_board = []
    for v in ranked:
        if v not in rank_board:
            rank_board.append(v)
    return rank_board


def climbingLeaderboard(ranked, player):
    """Climbing the leaderboard solution

    Parameters
    ----------
    ranked : array-like
        The leaderboard scores.

    player : array-like
        The player's scores.

    Returns
    -------
    rank : array-like
        The player's rank after each new score.
    """
    rank_board = sort_rank_board(ranked)

    rank = []
    for score in player:
        rank.append(
            binary_search_leftmost(rank_board, len(rank_board), score) + 1
        )
        rank_board.append(score)
        rank_board = sort_rank_board(sorted(rank_board, reverse=True))
    return rank


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('result: %s' % result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
