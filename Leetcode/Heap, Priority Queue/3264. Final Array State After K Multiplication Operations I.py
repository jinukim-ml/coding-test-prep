import heapq

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        h = []
        for i, n in enumerate(nums):
            heapq.heappush(h, (n, i))
        
        for _ in range(k):
            n, i = heapq.heappop(h)
            n *= multiplier
            heapq.heappush(h, (n, i))
        
        while h:
            n, i = heapq.heappop(h)
            nums[i] = n
        return nums