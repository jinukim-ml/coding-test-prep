from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        # find the inflection point (the original nums[0]) -> find the smallest
        
        while l <= r:
            mid = (l + r) // 2
            if 0 < mid < len(nums) - 1 and nums[mid] == min(nums[mid], nums[mid-1], nums[mid+1]):
                return nums[mid]
            if nums[mid] < nums[l]: # the smallest is in the left half -> move the right pointer
                r = mid - 1
            elif nums[mid] > nums[r]: # the smallest is in the right half -> move the left pointer
                l = mid + 1
            else:
                return min(nums[l], nums[r], nums[mid])