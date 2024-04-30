from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid]: # left half is sorted & right half has pivot
                if nums[l] <= target <= nums[mid]: # target is in sorted half -> normal binary search
                    r = mid - 1
                else: # target is not in sorted half -> find it in the other half
                    l = mid + 1
            elif nums[l] >= nums[mid]: # left half has pivot & right half is sorted
                if nums[mid] <= target <= nums[r]: # target is in sorted half -> normal binary search
                    l = mid + 1
                else: # target is not in sorted half -> find it in the other half
                    r = mid - 1

            if nums[mid] == target:
                return mid
        return -1