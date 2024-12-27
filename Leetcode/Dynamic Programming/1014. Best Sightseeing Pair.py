class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        n = len(values)
        suffix = [0] * n
        suffix[n-1] = values[n-1] - (n-1)

        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], values[i] - i)
        
        res = float('-inf')
        for i in range(n-1):
            res = max(res, values[i] + i + suffix[i+1])
        return res