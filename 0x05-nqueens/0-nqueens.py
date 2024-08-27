#!/usr/bin/python3
"""
Solving the N queens problem using Backtracking
"""
import sys


def is_safe(curr_row, col, chess):
    """
    assert that queen placed at certain position is not attackable
    """
    queen = chess[curr_row][col]
    # ishorizontally safe
    for j in range(n):
        val = chess[curr_row][j]
        if val != 0 and val != queen:
            return False
    # isvertically safe
    for i in range(n):
        val = chess[i][col]
        if val != 0 and val != queen:
            return False
    # isdiagonally safe
    i = 0
    ur_flag, ul_flag, dr_flag, dl_flag = True, True, True, True
    while ur_flag or ul_flag or dr_flag or dl_flag:
        up_right, down_right, up_left, down_left = 0, 0, 0, 0
        if col + i < n and curr_row - i >= 0:
            up_right = chess[curr_row - i][col + i]
        else:
            ur_flag = False
        if col + i < n and curr_row + i < n:
            down_right = chess[curr_row + i][col + i]
        else:
            dr_flag = False
        if col - i >= 0 and curr_row - i >= 0:
            up_left = chess[curr_row - i][col - i]
        else:
            ul_flag = False
        if col - i >= 0 and curr_row + i < n:
            down_left = chess[curr_row + i][col - i]
        else:
            dl_flag = False
        if (0, 0, 0, 0) != (up_right, up_left, down_right, down_left):
            return False
        i += 1
    # all conditions passed
    return True


def place_queen(curr_row, chess, queen, res):
    """
    The N queens puzzle is the challenge of placing
    N non-attacking queens on an N×N chessboard.
    """
    row_len = len(chess)
    if curr_row >= row_len:
        queens_positions = [[i, j] for i in range(len(chess))
                            for j in range(len(chess[i])) if chess[i][j] != 0]
        res.append(queens_positions)
        return res
    for j in range(row_len):
        if is_safe(curr_row, j, chess):
            chess[curr_row][j] = queen
            place_queen(curr_row + 1, chess, queen + 1, res)
            chess[curr_row][j] = 0
    return res


"""
==================
DRIVER CODE FOR TESTING
====================
"""
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)
n = sys.argv[1]
try:
    n = int(n)
    if n < 4:
        print('N must be at least 4')
        exit(1)
except Exception as e:
    print("N must be a number")
    exit(1)

queen = 1
chess = [[0 for _ in range(n)] for _ in range(n)]
res = place_queen(0, chess, 1, [])
for board in res:
    print(board)
