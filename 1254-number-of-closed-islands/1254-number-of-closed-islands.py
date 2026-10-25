class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            grid[r][c] = 1  # Mark as visited / flooded
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Flood-fill all land connected to the grid boundaries
        for r in range(rows):
            for c in (0, cols - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    
        for c in range(cols):
            for r in (0, rows - 1):
                if grid[r][c] == 0:
                    dfs(r, c)

        # Step 2: Count remaining closed islands in the interior
        closed_islands = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    dfs(r, c)

        return closed_islands