#!/usr/bin/python3
""" Module 0-island_perimeter """


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid """
    perimeter = 0

    # Cache the length of rows and columns for efficiency
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                # Check above neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
