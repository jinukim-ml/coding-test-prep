from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delve(self, node: Optional[TreeNode], curr_level: int) -> int:
        if node is None:
            return curr_level - 1
        leftdepth = self.delve(node.left, curr_level + 1)
        rightdepth = self.delve(node.right, curr_level + 1)
        
        return max(leftdepth, rightdepth)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.delve(root, 1)
        return depth