from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        
        for _ in range(n-k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)