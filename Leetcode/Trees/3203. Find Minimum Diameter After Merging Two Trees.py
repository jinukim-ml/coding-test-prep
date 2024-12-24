from collections import deque
from math import ceil

class Solution:
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        # 1. Find an endpoint of the diameter in the given tree
        # 2. From that endpoint, find the farthest node -> this distance becomes the diameter
        n, m = len(edges1)+1, len(edges2)+1
        g1 = [set() for _ in range(n)]
        for u, v in edges1:
            g1[u].add(v)
            g1[v].add(u)
        
        g2 = [set() for _ in range(m)]
        for u, v in edges2:
            g2[u].add(v)
            g2[v].add(u)
        
        def bfs(graph: list[set], start_node: int) -> tuple[int, int]:
            dq = deque([start_node])
            visited = [False] * len(graph)
            visited[start_node] = True
            distance = 0
            endpoint = start_node
            while dq:
                for _ in range(len(dq)):
                    node = dq.popleft()
                    endpoint = node
                    for v in graph[node]:
                        if not visited[v]:
                            dq.append(v)
                            visited[v] = True
                distance += 1
            return endpoint, distance-1
        
        e1, _ = bfs(g1, 0)
        _, dist1 = bfs(g1, e1)

        e2, _ = bfs(g2, 0)
        _, dist2 = bfs(g2, e2)

        combined = ceil(dist1 / 2) + ceil(dist2 / 2) + 1
        return max(dist1, dist2, combined)