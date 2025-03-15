class Solution: # O(n log n)
    def minCapability(self, nums: list[int], k: int) -> int:
        def is_possible(val: int) -> bool:
            houses = 0
            last_index = -2
            for i, n in enumerate(nums):
                if i - last_index >= 2 and n <= val:
                    last_index = i
                    houses += 1
                    if houses == k:
                        return True
            return False
        
        l, r = float('inf'), float('-inf')
        for n in nums:
            l = min(l, n)
            r = max(r, n)
        
        while l <= r:
            mid = (l + r) // 2
            if is_possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l