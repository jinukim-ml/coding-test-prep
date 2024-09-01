class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) / n != m:
            return []
        else:
            ans = [[0 for _ in range(n)] for _ in range(m)]
            for row in range(m):
                for col in range(n):
                    ans[row][col] = original[row*n+col]
            return ans