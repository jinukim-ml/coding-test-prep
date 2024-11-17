class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        difference = [0] * (len(nums) + 1)
        for l, r in queries:
            difference[l] -= 1
            difference[r+1] += 1
        
        for i in range(1, len(difference)):
            difference[i] += difference[i-1]
        
        for i in range(len(nums)):
            nums[i] += difference[i]
            if nums[i] > 0:
                return False
        return True