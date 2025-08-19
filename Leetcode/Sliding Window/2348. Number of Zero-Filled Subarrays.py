class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        l, res = 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                res += r-l+1
            else:
                l = r+1
        return res
