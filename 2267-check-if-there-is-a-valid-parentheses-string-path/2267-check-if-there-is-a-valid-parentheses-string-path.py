class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, balance):
            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            if balance > m - i + n - j:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            if i + 1 < m and dfs(i + 1, j, balance):
                return True

            if j + 1 < n and dfs(i, j + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)