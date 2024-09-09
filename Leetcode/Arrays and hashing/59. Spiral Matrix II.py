class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        item = 1
        while item <= n**2:
            for c in range(left, right+1):
                ans[top][c] = item
                item += 1
            top += 1

            for r in range(top, bottom+1):
                ans[r][right] = item
                item += 1
            right -= 1

            for c in range(right, left-1, -1):
                ans[bottom][c] = item
                item += 1
            bottom -= 1

            for r in range(bottom, top-1, -1):
                ans[r][left] = item
                item += 1
            left += 1
        return ans