class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        res = []
        r, c = 0, 0
        while len(res) < m*n:
            res.append(mat[r][c])
            if (r+c)%2:
                if r == m-1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
            else:
                if c == n-1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
        return res