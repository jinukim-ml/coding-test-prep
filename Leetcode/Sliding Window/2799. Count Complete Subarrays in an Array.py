from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        s = set(nums)
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while len(freq.keys()) == len(s):
                res += len(nums) - r
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    freq.pop(nums[l])
                l += 1
        return res