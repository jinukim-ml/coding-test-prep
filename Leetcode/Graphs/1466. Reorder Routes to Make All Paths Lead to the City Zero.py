from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        undirected = defaultdict(list)
        directed = set()
        for u, v in connections:
            undirected[u].append(v)
            undirected[v].append(u)
            directed.add((u,v))
        
        directed.add((0,-1))
        visited = set()
        res = 0
        def dfs(u: int, prev: int) -> None:
            if u in visited:
                return
            if (u, prev) not in directed:
                nonlocal res
                res += 1
            visited.add(u)
            for v in undirected[u]:
                dfs(v, u)
        dfs(0, -1)
        return res