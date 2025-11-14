class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        diff = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] += 1
        
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                up = 0 if i == 0 else res[i-1][j]
                left = 0 if j == 0 else res[i][j-1]
                diag = 0 if i == 0 or j == 0 else res[i-1][j-1]
                res[i][j] = diff[i][j] + up + left - diag
        return res