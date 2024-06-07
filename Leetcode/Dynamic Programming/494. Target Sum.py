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

# Solution().findTargetSumWays([35,37,9,29,36,0,44,32,44,13,2,37,14,21,41,36,9,23,41,17], 42)

Solution().findTargetSumWays([i for i in range(1, 21)], 9000)