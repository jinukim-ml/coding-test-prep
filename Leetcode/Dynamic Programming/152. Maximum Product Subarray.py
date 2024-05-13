from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        
        curMax, curMin = 1, 1
        for x in nums:
            preMax = curMax
            curMax = max(x * curMax, x * curMin, x)
            curMin = min(x * preMax, x* curMin, x)
            ans = max(ans, curMax)
        return ans

class Solution: # two pointer-esque solution
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ans = float('-inf')
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums)-i-1]
            ans = max(ans, prefix, suffix)

            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return ans