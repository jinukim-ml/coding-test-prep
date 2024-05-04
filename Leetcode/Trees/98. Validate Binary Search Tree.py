from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.arr = []
        
        self.inordertraverse(root)
        
        for i in range(len(self.arr)-1):
            if self.arr[i] >= self.arr[i+1]:
                return False
        return True
    
    def inordertraverse(self, root: Optional[TreeNode]) -> None:
        if root.left:
            self.inordertraverse(root.left)
        self.arr.append(root.val)
        if root.right:
            self.inordertraverse(root.right)