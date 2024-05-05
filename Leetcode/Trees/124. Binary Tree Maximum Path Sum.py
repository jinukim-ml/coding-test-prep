from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return 0

        leftmax = self.dfs(root.left)
        rightmax = self.dfs(root.right)

        leftmax = max(leftmax, 0)
        rightmax = max(rightmax, 0)
        self.res = max(self.res, root.val + leftmax + rightmax)

        return root.val + max(leftmax, rightmax)