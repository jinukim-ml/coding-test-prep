from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = []
        for c, p in zip(capital, profits):
            heapq.heappush(pairs, (c,p))
        
        completed = 0
        h = []
        while completed < k:
            while pairs and pairs[0][0] <= w:
                cap, pro = heapq.heappop(pairs)
                heapq.heappush(h, -pro)
                
            if not h:
                return w
            
            w -= heapq.heappop(h)
            completed += 1
        return w