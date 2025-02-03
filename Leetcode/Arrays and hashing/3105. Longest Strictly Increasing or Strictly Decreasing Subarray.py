class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing = []
        decreasing = []
        res = 0
        for n in nums:
            if not increasing or increasing[-1] < n:
                increasing.append(n)
            else:
                increasing = [n]
            if not decreasing or decreasing[-1] > n:
                decreasing.append(n)
            else:
                decreasing = [n]
            res = max(res, len(increasing), len(decreasing))
        return res