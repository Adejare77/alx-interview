#!/usr/bin/python3
""" Island Permieter """


def island_perimeter(grid):
    """ finds the perimeter of an island """
    island = 0
    repated_edges = 0
    for row_idx, rows in enumerate(grid):
        for col_idx, cols in enumerate(rows):
            if cols:
                island += 1
                if (col_idx - 1 >= 0 and rows[col_idx - 1]):
                    repated_edges += 2
                if (row_idx - 1 >= 0 and grid[row_idx - 1][col_idx]):
                    repated_edges += 2

    permieter_of_all_island = 4 * island - repated_edges
    return permieter_of_all_island
