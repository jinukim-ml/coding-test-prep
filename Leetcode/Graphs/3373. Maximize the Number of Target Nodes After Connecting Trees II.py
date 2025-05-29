from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        n, m = len(edges1)+1, len(edges2)+1
        
        g1 = defaultdict(list)
        for a, b in edges1:
            g1[a].append(b)
            g1[b].append(a)

        g2 = defaultdict(list)
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)
        
        def dfs(parent: int, node: int, depth: int, g: dict[list[int]], colors: list[int]) -> int:
            res = 1 - depth%2
            colors[node] = depth%2
            for v in g[node]:
                if v != parent:
                    res += dfs(node, v, depth+1, g, colors)
            return res
        
        # g1
        colors1 = [0] * n
        c = dfs(-1, 0, 1, g1, colors1)
        partition = [c, n-c]

        # g2
        colors2 = [0] * m
        c = dfs(-1, 0, 1, g2, colors2)
        max_color = max(c, m-c)
        
        res = []
        for i in range(n):
            res.append(partition[colors1[i]] + max_color)
        return res