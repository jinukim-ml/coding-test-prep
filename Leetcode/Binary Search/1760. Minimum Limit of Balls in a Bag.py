from math import ceil

class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def is_possible(maximum: int, max_ops: int) -> bool:
            ops = 0
            for n in nums:
                ops += ceil(n / maximum) - 1
            if ops > max_ops:
                return False
            return True
        
        l = 1
        r = max(nums)
        while l < r:
            mid = (l + r) // 2
            if is_possible(mid, maxOperations):
                r = mid
            else:
                l = mid + 1
        return l