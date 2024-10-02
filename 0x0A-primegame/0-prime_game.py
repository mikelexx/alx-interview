#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""
limit = 1000


def generatePrimes(limit):
    primes = [1 for _ in range(limit)]
    if (limit > 0):
        primes[0] = 0
    if (limit > 1):
        primes[1] = 0
    i = 2
    while i * i < limit:
        if (primes[i] == 1):
            for count in range(i * i, limit, i):
                primes[count] = 0
        i += 1
    return primes


primes = generatePrimes(limit)

prime_nums = [i for i in range(len(primes)) if primes[i] == 1]


def isWinner(x, nums):
    """
     x is the number of rounds and nums is an array of `n`
    Returns: name of the player that won the most rounds, else
    `None` if the winner cannot be determined
    """
    ben_score, maria_score = 0, 0
    for i in range(x):
        n = nums[i]
        prime_nums_count = 0
        j = 0
        while (prime_nums[j] <= n):
            prime_nums_count += 1
            j += 1
        if prime_nums_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
