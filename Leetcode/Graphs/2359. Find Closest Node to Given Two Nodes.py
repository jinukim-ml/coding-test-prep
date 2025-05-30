from collections import deque

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)
        distances = [[-1 for _ in range(n)] for _ in range(2)]
        mapping = {0: node1, 1: node2}
        for i in range(2):
            node = mapping[i]
            visited = set([node])
            q = deque([node])
            d = 0
            while q:
                u = q.popleft()
                distances[i][u] = d
                if edges[u] != -1 and edges[u] not in visited:
                    visited.add(edges[u])
                    q.append(edges[u])
                d += 1
        
        threshold = float('inf')
        res = -1
        for i in range(n-1, -1, -1):
            d1, d2 = distances[0][i], distances[1][i]
            if d1 > -1 and d2 > -1:
                d = max(d1, d2)
                if d <= threshold:
                    threshold = d
                    res = i
        return res