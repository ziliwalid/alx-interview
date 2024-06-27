#!/usr/bin/python3
"""
Returns the perimeter of an island given the grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    x = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                x += 4
                if i > 0 and grid[i-1][j] == 1:
                    x -= 2
                if j > 0 and grid[i][j-1] == 1:
                    x -= 2
    return x