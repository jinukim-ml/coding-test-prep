from typing import List

class Solution: # Recursion + memoization
    def rob(self, nums: List[int]) -> int:
        self.houses = nums
        self.memo = [-1] * len(nums)
        return self.recur(len(nums)-1)

    def recur(self, i: int) -> int:
        if i < 0:
            return 0

        if self.memo[i] >= 0:
            return self.memo[i]
        
        res = max(self.houses[i] + self.recur(i-2), self.recur(i-1))
        self.memo[i] = res
        return res
    
class Solution: # Iteration + memoization
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [-1] * (len(nums)+1)
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            memo[i+1] = max(nums[i] + memo[i-1], memo[i])
        return memo[len(nums)]
    
class Solution: # Iteration w/ 2 variables
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1 = 0
        prev2 = 0
        for n in nums:
            tmp = prev1
            prev1 = max(prev1, n + prev2)
            prev2 = tmp
        return prev1