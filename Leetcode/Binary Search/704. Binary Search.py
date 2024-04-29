from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            pivot = nums[mid]
            if pivot < target:
                l = mid + 1
            elif pivot > target:
                r = mid - 1
            else:
                return mid
        
        return -1