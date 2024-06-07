from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, val):
            if i == len(nums):
                if val == target:
                    return 1
                else:
                    return 0

            if (i, val) in dp:
                return dp[(i, val)]

            dp[(i, val)] = backtrack(i+1, val+nums[i]) + backtrack(i+1, val-nums[i])
            return dp[(i, val)]
        
        return backtrack(0, 0)