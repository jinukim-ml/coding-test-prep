from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        if l >= len(nums):
            return [-1, -1]
        elif target != nums[l]:
            return [-1, -1]
        else:
            r = bisect_right(nums, target)
            return [l, r-1]