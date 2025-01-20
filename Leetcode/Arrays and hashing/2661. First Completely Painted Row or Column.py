class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        coords = {}
        for r in range(m):
            for c in range(n):
                coords[mat[r][c]] = (r, c)
        
        rows = [0] * m
        cols = [0] * n

        for i, num in enumerate(arr):
            r, c = coords[num]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i