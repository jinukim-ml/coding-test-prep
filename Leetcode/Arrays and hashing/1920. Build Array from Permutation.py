class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res