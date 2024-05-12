from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0
        for i in range(len(nums)-1):
            tmp = prev1
            prev1 = max(prev1, nums[i] + prev2)
            prev2 = tmp
        ans = prev1

        prev1, prev2 = 0, 0
        for i in range(1, len(nums)):
            tmp = prev1
            prev1 = max(prev1, nums[i] + prev2)
            prev2 = tmp
        return max(ans, prev1)