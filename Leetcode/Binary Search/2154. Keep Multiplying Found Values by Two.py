from bisect import bisect_left

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums.sort()
        while True:
            i = bisect_left(nums, original)
            if i == len(nums) or nums[i] != original:
                break
            original *= 2
        return original