#!/usr/bin/python3
"""
The objective is to find the minimum number
of coins required to make up a given total amount,
given a list of coin denominations. This project challenges
you to apply your understanding of algorithms to devise a
solution that is not only correct but also efficient.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    it  determines the fewest number of coins needed to meet
    a given amount total.
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have,
          it returns -1
        coins is a list of the values of the coins in your possession
        The value of a coin will always be an integer greater than 0
    Constraint: assumes you have an infinite number of
    each denomination of coin in the list
    """
    dp = [float("infinity")] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[total] != float('inf'):
        return dp[total]
    return -1
