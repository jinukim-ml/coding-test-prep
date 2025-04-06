class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        max_idx, max_size = 0, 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_idx = i
        
        res = []
        n = nums[max_idx]
        for i in range(max_idx, -1, -1):
            if n % nums[i] == 0 and dp[i] == max_size:
                res.append(nums[i])
                n = nums[i]
                max_size -= 1
        return res