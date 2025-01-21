class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        upper = sum(grid[0]) - grid[0][0]
        down = 0
        r2 = upper

        for i in range(1, n):
            upper -= grid[0][i]
            down += grid[1][i-1]
            r1 = max(upper, down)
            r2 = min(r2, r1)
        return r2