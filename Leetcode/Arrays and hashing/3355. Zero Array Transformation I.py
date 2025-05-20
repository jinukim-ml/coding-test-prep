class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        diff = [0] * (len(nums)+1)
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1
        
        running_sum = 0
        for i in range(len(nums)):
            running_sum += diff[i]
            if running_sum < nums[i]:
                return False
        return True