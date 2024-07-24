#!/usr/bin/python3
"""
creating pascal triangle
"""


def pascal_triangle(n):
    """
    returns building lists for pascal's triangle
    """
    if n <= 0:
        return []
    res = []
    prev = [1]
    res.append(prev)
    for i in range(n - 1):
        prev = [1] + [prev[i] + prev[i + 1]
                      for i in range(len(prev) - 1)] + [1]
        res.append(prev)
    return res
