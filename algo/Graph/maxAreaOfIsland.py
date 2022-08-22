"""

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)

You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

"""


def maxAreaOfIsland(grid):
    ans = 0
    R, C = len(grid), len(grid[0])

    def findArea(r, c):
        if 0 <= r <= R - 1 and 0 <= c <= C - 1:
            if grid[r][c] == 0:
                return 0
            else:
                grid[r][c] = 0
                return 1 + findArea(r + 1, c) + findArea(r - 1, c) + findArea(r, c + 1) + findArea(r, c - 1)
        return 0

    for r in range(R):
        for c in range(C):
            ans = max(ans, findArea(r, c))
    return ans


maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
                0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
# Output => 6
