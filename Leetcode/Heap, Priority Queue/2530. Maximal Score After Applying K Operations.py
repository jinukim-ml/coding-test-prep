from math import ceil
import heapq

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -n)
        
        ans = 0
        for i in range(k):
            val = -1 * heapq.heappop(h)
            ans += val
            val = ceil(val/3)
            heapq.heappush(h, -val)
        return ans