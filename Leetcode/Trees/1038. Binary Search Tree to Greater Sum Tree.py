# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, val: int) -> int:
            if not node:
                return val
            node.val += dfs(node.right, val)
            return dfs(node.left, node.val)
        
        dfs(root, 0)
        return root