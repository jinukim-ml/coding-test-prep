# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:
        res_map = {}
        height_cache = {}
        
        def get_height(node: TreeNode) -> int:
            if not node:
                return -1
            if node in height_cache:
                return height_cache[node]
            
            h = 1 + max(get_height(node.left), get_height(node.right))
            height_cache[node] = h
            return h

        def dfs(node: TreeNode, depth: int, max_val: int) -> None:
            if not node:
                return
            res_map[node.val] = max_val
            dfs(node.left, depth + 1, max(max_val, depth + 1 + get_height(node.right)))
            dfs(node.right, depth + 1, max(max_val, depth + 1 + get_height(node.left)))
        
        dfs(root, 0, 0)
        
        ans = []
        for q in queries:
            ans.append(res_map[q])
        return ans