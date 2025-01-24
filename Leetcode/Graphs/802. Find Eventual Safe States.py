from collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        g = defaultdict(list)
        for u, nodes in enumerate(graph):
            for v in nodes:
                g[u].append(v)
        
        cache = [0] * n # ternary cache
        def dfs(u: int) -> bool:
            if not graph[u] or cache[u] == 1:
                return True
            if cache[u] == -1:
                return False
            cache[u] = -1
            for v in graph[u]:
                if not dfs(v):
                    return False
            cache[u] = 1
            return True

        res = []
        for u in range(n):
            if dfs(u):
                res.append(u)
        return res