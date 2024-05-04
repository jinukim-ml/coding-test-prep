from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []

        self.inordertraverse(root)
        return self.arr[k-1]
    
    def inordertraverse(self, root: Optional[TreeNode]):
        if root.left:
            self.inordertraverse(root.left)
        self.arr.append(root.val)
        if root.right:
            self.inordertraverse(root.right)