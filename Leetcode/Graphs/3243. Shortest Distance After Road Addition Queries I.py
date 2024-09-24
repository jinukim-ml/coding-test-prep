from collections import deque
import heapq

class Solution: # BFS
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        g = [set([i+1]) for i in range(n)]

        ans = []
        for u, v in queries:
            g[u].add(v)
            q = deque([(0,0)])
            vis = set([0])

            while q:
                node, dist = q.popleft()
                if node == n-1:
                    ans.append(dist)
                    break
                for v in g[node]:
                    if v not in vis:
                        q.append((v, dist+1))
                        vis.add(v)
        return ans

class Solution: # Dijkstra w/ heap
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        self.n = n
        self.g = [[(i+1, 1)] for i in range(n)]
        self.g[n-1] = []
        ans = []
        for u, v in queries:
            self.g[u].append((v, 1))
            ans.append(self.dijkstra())
        return ans
    
    def dijkstra(self):
        dist = [float('inf')] * self.n
        dist[0] = 0
        
        h = [(0,0)]
        while h:
            u, cost = heapq.heappop(h)

            if cost < dist[u]:
                continue
            for v, c in self.g[u]:
                newcost = cost + c
                if newcost < dist[v]:
                    dist[v] = newcost
                    heapq.heappush(h, (v, newcost))
        return dist[self.n-1]