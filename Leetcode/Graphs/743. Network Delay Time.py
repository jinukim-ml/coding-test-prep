from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) < n-1:
            return -1

        adj = defaultdict(list)
        vis = set()
        h = [(0, k)]
        for u, v, w in times:
            adj[u].append((w, v))

        
        ans = 0
        while h:
            w1, u = heapq.heappop(h)
            if u in vis:
                continue
            
            vis.add(u)
            ans = w1
            for w2, v in adj[u]:
                if v not in vis:
                    heapq.heappush(h, (w1+w2, v))
        
        if len(vis) == n:
            return ans
        else:
            return -1