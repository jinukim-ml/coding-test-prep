class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        res = 100000
        for r in range(k-1, len(nums)):
            res = min(res, nums[r]-nums[l])
            l += 1
        return res