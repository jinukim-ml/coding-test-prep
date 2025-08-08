from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        l, res = 0, 0
        freq = defaultdict(int)
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res