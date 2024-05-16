class Solution: # Pascal's triangle
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n] * m

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    continue
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        return grid[m-1][n-1]

class Solution: # Pascal's triangle using combination
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(target: int) -> int:
            res = 1
            for i in range(2, target+1):
                res *= i
            return res
        return factorial(m-1 + n-1) // (factorial(m-1) * factorial(n-1))
    
class Solution: # DP solution
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for r in range(m-1):
            newrow = [1] * n
            for c in range(n-2, -1, -1):
                newrow[c] = newrow[c+1] + row[c]
            row = newrow

        return row[0]