class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        change_r , change_c = 0, 0
        # row count
        for r in range(m):
            for c in range(n//2):
                if grid[r][c] != grid[r][n-1-c]:
                    change_r += 1
        # column count
        for c in range(n):
            for r in range(m//2):
                if grid[r][c] != grid[m-1-r][c]:
                    change_c += 1
        
        return min(change_r, change_c)