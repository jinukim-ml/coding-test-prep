from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.hashmap = {}
        for pair in edges: # undriected graph
            if pair[0] < pair[1]:
                parent, child = pair[0], pair[1]
            else:
                parent, child = pair[1], pair[0]
            self.hashmap[parent] = self.hashmap.get(parent, []) + [child]
        
        # 1. no cycle.
        # 2. graph is connected.
        self.vis = set()
        if not self.dfs(0): # cycle check
            return False
        
        compare = set([i for i in range(n)]) # have we visited all nodes?

        return self.vis == compare and len(edges) == n-1 # if graph is connected -> (V-1) edges

    def dfs(self, node: int) -> bool:
        if node in self.vis:
            return False

        self.vis.add(node)
        if node in self.hashmap:
            for nextnode in self.hashmap[node]:
                if not self.dfs(nextnode):
                    return False
        return True