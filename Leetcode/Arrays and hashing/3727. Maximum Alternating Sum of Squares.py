class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return sum(nums[len(nums)//2:]) - sum(nums[:len(nums)//2])