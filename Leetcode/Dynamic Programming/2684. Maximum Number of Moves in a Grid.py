class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(r: int, c: int, prev_val: int) -> int:
            if not 0 <= r < m or not 0 <= c < n or prev_val >= grid[r][c]:
                return -1
            if dp[r][c] != -1:
                return dp[r][c]
            
            upper_right = dfs(r-1, c+1, grid[r][c])
            right = dfs(r, c+1, grid[r][c])
            down_right = dfs(r+1, c+1, grid[r][c])
            dp[r][c] = max(upper_right, right, down_right) + 1
            return dp[r][c]
        
        ans = 0
        for r in range(m):
            ans = max(ans, dfs(r, 0, -1))
        
        return ans