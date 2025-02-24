from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        g = defaultdict(set)
        upstream = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            upstream[v].add(u)
        
        b_path = {}
        def find_root(node: int, parent: int) -> bool:
            if node == 0:
                return True
            for v in g[node]:
                b_path[node] = len(b_path)
                if v != parent and find_root(v, node):
                    return True
                b_path.pop(node)
            return False
        find_root(bob, -1)
        b_path[0] = len(b_path)

        seen = set()
        def dfs(i: int, step: int, cost: int, parent: int) -> int:
            seen.add(i)
            if i in b_path:
                if b_path[i] == step: # Alice arrived at node i simultaneously as Bob
                    cost += amount[i]//2
                elif b_path[i] > step:
                    cost += amount[i]
            else:
                cost += amount[i]
            if len(g[i]) == 1 and parent in g[i]:
                return cost
            
            res = float('-inf')
            for v in g[i]:
                if v not in seen:
                    res = max(res, dfs(v, step+1, cost, i))
            return res
        return dfs(0, 0, 0, -1)