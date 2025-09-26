from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                target = nums[i] + nums[j] # nums[i] + nums[j] > target
                index = bisect_left(nums, target, j+1, n) # if there's no valid number in nums[j+1:n], j+1 will be returned
                res += index-j-1
        return res