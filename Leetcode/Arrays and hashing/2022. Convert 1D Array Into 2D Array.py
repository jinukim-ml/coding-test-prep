class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) / n != m:
            return []
        else:
            ans = []
            for row in range(m):
                ans.append(original[row * n:row * n + n])
            return ans