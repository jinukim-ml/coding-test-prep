from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0
        pairs = 0
        res = 0
        for r in range(len(nums)):
            pairs += freq[nums[r]]
            freq[nums[r]] += 1
            while pairs >= k:
                res += len(nums) - r
                freq[nums[l]] -= 1
                pairs -= freq[nums[l]]
                l += 1
        return res