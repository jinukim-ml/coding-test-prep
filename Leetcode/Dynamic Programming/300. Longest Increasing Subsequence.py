from typing import List

class Solution: # O(n^2) soltion
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
class Solution: # inverse order O(n^2) solution
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

from bisect import bisect_left
class Solution: # O(n log n) solution
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for elem in nums:
            idx = bisect_left(dp, elem)
            if idx == len(dp):
                dp.append(elem)
            else:
                dp[idx] = elem
        
        return len(dp)
