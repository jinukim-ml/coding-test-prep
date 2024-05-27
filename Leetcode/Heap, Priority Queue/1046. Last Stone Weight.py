from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x == y:
                continue
            else:
                y -= x
                heapq.heappush(stones, y)
        
        if stones:
            return -1 * stones[0]
        else:
            return 0