from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        self.hashmap = {}
        
        return self.dfs(node)

    def dfs(self, node):
        if node in self.hashmap:
            return self.hashmap[node]

        copy = Node(node.val)
        self.hashmap[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(self.dfs(nei))
        return copy