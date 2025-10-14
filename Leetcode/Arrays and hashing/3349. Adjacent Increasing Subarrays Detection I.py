class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        flags = [False for _ in range(n)]
        for i in range(n-k+1):
            for j in range(i+1, i+k):
                if nums[j] <= nums[j-1]:
                    break
            else:
                flags[i] = True
        
        for i in range(k, n):
            if flags[i] and flags[i-k]:
                return True
        return False