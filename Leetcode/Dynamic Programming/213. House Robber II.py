class Solution:
    def rob(self, nums: list[int]) -> int:
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

class Solution: # 
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        res = dp[-2]
        
        dp = [0 for _ in range(n)]
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        res = max(res, dp[-1])
        return res