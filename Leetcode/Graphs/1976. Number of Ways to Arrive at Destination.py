import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))
        
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        h = [(0, 0)]
        while h:
            t, node = heapq.heappop(h)
            if dist[node] < t:
                continue
            for v, cost in g[node]:
                if t + cost < dist[v]:
                    dist[v] = t + cost
                    ways[v] = ways[node]
                    heapq.heappush(h, (dist[v], v))
                elif t + cost == dist[v]:
                    ways[v] += ways[node]
        return ways[-1] % (10**9 + 7)