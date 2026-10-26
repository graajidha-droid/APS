class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> int:
            val = grid[r][c]
            grid[r][c] = 0  # Mark visited by resetting cell value
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    val += dfs(nr, nc)
            return val

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)
                    if island_sum % k == 0:
                        count += 1

        return count