from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        ans = 0
        vis = set()
        h = [(0, 0)]

        while len(vis) < N:
            cost, i = heapq.heappop(h)
            if i in vis:
                continue
            ans += cost
            vis.add(i)
            for neicost, nei in adj[i]:
                if nei not in vis:
                    heapq.heappush(h, (neicost, nei))
        return ans