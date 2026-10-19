class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Stop if outside grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Stop if water or already visited
            if grid[r][c] == "0":
                return

            # Mark as visited
            grid[r][c] = "0"

            # Explore all four directions
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands