class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        directions = [0, 1, 0, -1, 0]
        ans = [[rStart, cStart]]
        idx = n = 0
        while len(ans) < rows * cols:
            for _ in range(n // 2 + 1):
                rStart += directions[idx]
                cStart += directions[idx+1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
            n += 1
            idx = (idx + 1) % 4
        return ans