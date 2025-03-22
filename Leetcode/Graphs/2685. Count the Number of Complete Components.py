from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        visited = set()
        res = 0
        for node in range(n):
            if node not in visited:
                component = []
                q = deque([node])
                visited.add(node)
                while q:
                    curr = q.popleft()
                    component.append(curr)
                    for v in g[curr]:
                        if v not in visited:
                            q.append(v)
                            visited.add(v)
                
                for v in component:
                    if len(g[v]) != len(component)-1:
                        break
                else:
                    res += 1
        return res