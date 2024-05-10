from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        self.hashtable = {}
        for pair in edges:
            if pair[0] < pair[1]:
                parent, child = pair[0], pair[1]
            else:
                parent, child = pair[1], pair[0]
            self.hashtable[parent] = self.hashtable.get(parent, []) + [child]
        
        components = 0
        self.vis = set()
        for v1, v2 in edges:
            if v1 not in self.vis and v2 not in self.vis:
                self.dfs(v1)
                components += 1
            elif v1 not in self.vis:
                self.dfs(v1)
            else:
                self.dfs(v2)
        
        for i in range(n):
            if i not in self.vis:
                components += 1
        
        return components
    
    def dfs(self, node) -> None:
        if node in self.vis:
            return
        
        self.vis.add(node)
        if node in self.hashtable:
            for nextnode in self.hashtable[node]:
                self.dfs(nextnode)
        return