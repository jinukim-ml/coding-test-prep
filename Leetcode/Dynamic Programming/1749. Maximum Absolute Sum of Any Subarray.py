class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        minsum, maxsum = 0, 0
        window = 0
        for n in nums:
            window += n
            maxsum = max(maxsum, window)
            minsum = min(minsum, window)
        return abs(maxsum - minsum)