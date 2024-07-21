from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def toposort(arr):
            graph = [[] for _ in range(k)]
            degree = [0] * k

            for u, v in arr:
                graph[u-1].append(v-1)
                degree[v-1] += 1

            q = deque(u for u, d in enumerate(degree) if d == 0)
            res = []
            while q:
                u = q.popleft()
                res.append(u+1)
                for v in graph[u]:
                    degree[v] -= 1
                    if degree[v] == 0:
                        q.append(v)
            return res
        
        row = toposort(rowConditions)
        col = toposort(colConditions)

        if len(row) < k or len(col) < k: # cycle(s) detected
            return []
        
        ans = [[0 for __ in range(k)] for _ in range(k)]
        row = {val : r for r, val in enumerate(row)}
        col = {val : c for c, val in enumerate(col)}

        for val in range(1, k+1):
            ans[row[val]][col[val]] = val
        return ans