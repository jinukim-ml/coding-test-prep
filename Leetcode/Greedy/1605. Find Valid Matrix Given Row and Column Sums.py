class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        ans = [[0 for __ in range(len(colSum))] for _ in range(len(rowSum))]
        r, c = 0, 0
        while r < len(rowSum) and c < len(colSum):
            val = min(rowSum[r], colSum[c])
            ans[r][c] = val
            rowSum[r] -= val
            colSum[c] -= val

            if rowSum[r] == 0:
                r += 1
            if colSum[c] == 0:
                c += 1
        return ans