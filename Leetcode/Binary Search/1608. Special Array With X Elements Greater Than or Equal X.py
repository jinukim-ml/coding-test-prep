from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l, r = 1, len(nums)

        while l <= r:
            x = (l + r) // 2
            cnt = 0
            for n in nums:
                if n >= x:
                    cnt += 1
            
            if cnt == x:
                return x
            
            if cnt > x:
                l = x + 1
            else:
                r = x - 1
        
        return -1