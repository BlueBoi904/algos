def numIslands(grid):
    maxArea = 0
    if not grid:
        return maxArea

    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def dfs(row, col, curr):
        if not (row < rows and col < cols and col > -1) or not grid[row][col] == 1 or (row, col) in visited:
            return
        visited.add((row, col))
        curr += 1

        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

        return curr

    for row in range(rows):
        for col in range(cols):
            curr = dfs(row, col, 0)
            maxArea = max(maxArea, curr)
    print(maxArea)
    return maxArea


numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])  # Output  => 1

numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])  # Output  => 3
