class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        res = 1
        for r in range(len(nums)):
            if nums[r] - nums[l] > k:
                l = r
                res += 1
        return res