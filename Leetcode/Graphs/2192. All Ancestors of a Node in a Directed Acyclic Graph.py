from typing import List
from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for fr, to in edges:
            graph[to].append(fr)
        
        def dfs(arr: list, vis: set, node: int) -> None:
            for v in graph[node]:
                if v not in vis:
                    arr.append(v)
                    vis.add(v)
                    dfs(arr, vis, v)

        ans = []
        for i in range(n):
            ancestors = []
            vis = set()
            dfs(ancestors, vis, i)
            ans.append(sorted(ancestors))
        return ans