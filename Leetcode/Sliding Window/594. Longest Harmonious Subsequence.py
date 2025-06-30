class Solution: # sorting + sliding window
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        l = 0
        res = 0
        for r in range(1, len(nums)):
            while nums[r] - nums[l] > 1 and l < r:
                l += 1
            if nums[r]-nums[l] == 1:
                res = max(res, r-l+1)
        return res

from collections import Counter

class Solution: # counting
    def findLHS(self, nums: list[int]) -> int:
        counter = Counter(nums)
        res = 0
        for k, v in counter.items():
            if k+1 in counter:
                res = max(res, counter[k] + counter[k+1])
        return res