from typing import List
import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i, (x, y) in enumerate(points):
            h.append((math.sqrt(x**2 + y**2), i))

        heapq.heapify(h)

        cnt = 0
        ans = []
        while cnt < k:
            _, idx = heapq.heappop(h)
            ans.append(points[idx])
            cnt += 1
        
        return ans