def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if (r < 0 or r >= rows or
            c < 0 or c >= cols):
            return

        if grid[r][c] == 0 or visited[r][c]:
            return

        visited[r][c] = True

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                dfs(r, c)

    return count


grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1]
]

print("Number of islands:", numIslands(grid))