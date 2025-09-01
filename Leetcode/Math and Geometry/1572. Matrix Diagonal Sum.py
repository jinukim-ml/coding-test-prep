class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        r, c0, c1 = 0, 0, n-1
        primary, secondary = 0, 0
        for _ in range(n):
            primary += mat[r][c0]
            secondary += mat[r][c1]
            r += 1
            c0 += 1
            c1 -= 1
        
        if n%2:
            return primary + secondary - mat[n//2][n//2]
        else:
            return primary + secondary