class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        diff = 0
        res = 0
        high = 0
        for n in nums:
            res = max(res, diff * n)
            diff = max(diff, high - n)
            high = max(high, n)
        return res