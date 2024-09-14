class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        ans = 0
        streak = 0
        maxval = 0
        for n in nums:
            if maxval < n:
                maxval = n
                ans = streak = 0
            
            if maxval == n:
                streak += 1
            else:
                streak = 0
            ans = max(ans, streak)

        return ans