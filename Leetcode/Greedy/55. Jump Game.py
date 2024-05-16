from typing import List

class Solution: # Greedy solution
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0

class Solution: # DP solution (recursion + memoization)
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        def backtrack(idx: int) -> bool:
            if idx >= len(nums)-1:
                return True
            
            if dp[idx] == False:
                return False

            for jump in range(nums[idx], 0, -1):
                if backtrack(idx+jump):
                    return True
            dp[idx] = False
            return False
        return backtrack(0)