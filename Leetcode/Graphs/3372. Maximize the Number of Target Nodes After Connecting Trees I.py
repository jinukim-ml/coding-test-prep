from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        n, m = len(edges1)+1, len(edges2)+1
        if k == 0:
            return [1] * n
        
        g1, g2 = defaultdict(list), defaultdict(list)
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)
        
        maxnodes_g1 = [0] * n
        for i in range(n):
            visited = set([i])
            q = deque([i])
            distance = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for v in g1[node]:
                        if v not in visited and distance < k:
                            q.append(v)
                            visited.add(v)
                distance += 1
            maxnodes_g1[i] = len(visited)
        
        maxnodes_g2 = 0
        for i in range(m):
            visited = set([i])
            q = deque([i])
            distance = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for v in g2[node]:
                        if v not in visited and distance < k-1:
                            q.append(v)
                            visited.add(v)
                distance += 1
            maxnodes_g2 = max(maxnodes_g2, len(visited))
        
        res = []
        for i in range(n):
            res.append(maxnodes_g1[i] + maxnodes_g2)
        return res