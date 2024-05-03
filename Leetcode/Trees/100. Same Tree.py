from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
            
        if p and not q:
            return False
        elif not p and q:
            return False
        elif p and q and p.val != q.val:
            return False
        elif self.isSameTree(p.left, q.left) == False:
            return False
        elif self.isSameTree(p.right, q.right) == False:
            return False
        else:
            return True