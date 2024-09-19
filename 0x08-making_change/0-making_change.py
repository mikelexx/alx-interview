#!/usr/bin/python3
"""
The objective is to find the minimum number
of coins required to make up a given total amount,
given a list of coin denominations. This project challenges
you to apply your understanding of algorithms to devise a
solution that is not only correct but also efficient.
"""


def helper(sorted_coins, max_idx, total, count):
    """ finds the minimum number of coins
    needed to get to total else -1 if not possible
    """
    temp_total = total
    temp_count = count
    temp_max_idx = max_idx
    if (max_idx < 0):
        return -1
    while (max_idx >= 0):
        biggest = sorted_coins[max_idx]
        if total < biggest:
            max_idx -= 1
            continue
        rem = total - biggest
        count += 1
        if rem == 0:
            return count
        total = rem
    res = helper(sorted_coins, temp_max_idx - 1, temp_total, temp_count)
    return res


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
    if total == 0:
        return 0
    sorted_coins = sorted(coins)
    return helper(sorted_coins, len(coins) - 1, total, 0)
