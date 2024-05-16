from typing import List

class Solution: # DP solution
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')] * (len(nums) + 1)

        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(nums[i], nums[i] + dp[i+1])
        
        return max(dp)
    
class Solution: # greedy(?) solution
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]

        total = 0
        for n in nums:
            total += n
            ans = max(ans, total)
            if total < 0:
                total =0
        return ans