class Solution: # two pointers solution. O(n)
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums)-1
        for i in range(len(nums)):
            j = len(nums)-i-1
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1
            if nums[j] > pivot:
                res[r] = nums[j]
                r -= 1
        while l <= r:
            res[l] = pivot
            l += 1
        return res

class Solution: # simle brute force solution. O(n)
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less, equal, greater = [], [], []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                equal.append(n)
        return less + equal + greater

import heapq
class Solution: # heapq solution. O(log n)
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        greater = []
        num_pivots = 0
        for i, n in enumerate(nums):
            if n < pivot:
                heapq.heappush(less, (i, n))
            elif n > pivot:
                heapq.heappush(greater, (i, n))
            else:
                num_pivots += 1
        
        i = 0
        while less:
            _, n = heapq.heappop(less)
            nums[i] = n
            i += 1
        while num_pivots > 0:
            nums[i] = pivot
            i += 1
            num_pivots -= 1
        while greater:
            _, n = heapq.heappop(greater)
            nums[i] = n
            i += 1
        return nums