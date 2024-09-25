#!/usr/bin/python3
"""
requirement: Create a function `def island_perimeter(grid)`:
that returns the perimeter of the island described in grid:
where:
    `grid` is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        `grid` is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water
    inside that isn’t connected to the water surrounding the island)
"""


def explore_island(grid, row_idx, col_idx, vis):
    vis.add((row_idx, col_idx))
    perimeter = 0
    # define left, right , up and down boundaries
    left = (row_idx, col_idx - 1)
    right = (row_idx, col_idx + 1)
    up = (row_idx - 1, col_idx)
    down = (row_idx + 1, col_idx)
    # check leftwards for wall
    if left not in vis:
        if (left[1] < 0 and 0 <= left[0] < len(grid)) \
                or grid[left[0]][left[1]] == 0:
            perimeter += 1
        else:
            vis.add(left)
            perimeter += explore_island(grid, left[0], left[1], vis)
    # check rightwars for wall
    if right not in vis:
        if(right[1] >= len(grid[0]) and 0 <= right[0] < len(grid)) \
                or grid[right[0]][right[1]] == 0:
            perimeter += 1
        else:
            vis.add(right)
            perimeter += explore_island(grid, right[0], right[1], vis)
    # check upwards for wall
    if up not in vis:
        if (up[0] < 0 and 0 <= up[1] < len(grid[0])) \
                or grid[up[0]][up[1]] == 0:
            perimeter += 1
        else:
            vis.add(up)
            perimeter += explore_island(grid, up[0], up[1], vis)
    # check downwards for wall
    if down not in vis:
        if (down[0] >= len(grid) and 0 <= down[1] < len(grid[0])) or \
                grid[down[0]][down[1]] == 0:
            perimeter += 1
        else:
            vis.add(down)
            perimeter += explore_island(grid, down[0], down[1], vis)
    return perimeter


def island_perimeter(grid):
    """
    returns: the perimeter of the island described in grid
    """
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                return explore_island(grid, i, j, set())
    return 0
