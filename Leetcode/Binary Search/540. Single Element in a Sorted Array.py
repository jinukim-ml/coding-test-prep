from bisect import bisect_left, bisect_right

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        def binsearch(l: int, r: int) -> int:
            if l > r:
                return -1
            mid = (l+r)//2
            val = nums[mid]
            
            lindex = bisect_left(nums, val)
            rindex = bisect_right(nums, val)
            if rindex - lindex == 1:
                return val
            else:
                l_res = binsearch(l, lindex-1)
                if l_res != -1:
                    return l_res
                else:
                    return binsearch(rindex, r)
        return binsearch(0, len(nums)-1)