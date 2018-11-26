import functools


def grid_helpers(grid):
    @functools.lru_cache(maxsize=None)
    def highest_in_row_of_building(num):
        return max(grid[num])

    @functools.lru_cache(maxsize=None)
    def highest_in_column_of_building(num):
        return max(grid[i][num] for i in range(len(grid)))

    return (highest_in_row_of_building, highest_in_column_of_building)


class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # grid is a squre
        n = len(grid)
        highest_in_row_of_building, highest_in_column_of_building = grid_helpers(grid)
        rt = 0
        for i in range(n):
            for j in range(n):
                amount = min((highest_in_row_of_building(i),
                              highest_in_column_of_building(j)))

                rt += (amount - grid[i][j])
        return rt

