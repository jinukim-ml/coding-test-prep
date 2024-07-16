from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def search(node: TreeNode, target:int, path:list[str]):
            if node.val == target:
                return True
            
            if node.left and search(node.left, target, path):
                path += 'L'
            elif node.right and search(node.right, target, path):
                path += 'R'
            return path
        
        s, d = [], []
        search(root, startValue, s)
        search(root, destValue, d)

        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))