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

'''
After search() function, we have the path to each node (reversed).
By deleting common prefix, we have the path to each node from LCA (still reversed).
The final result utilizes the fact that length of the list s is the length from LCA to s.
To go from s to LCA, we need to go up len(s) times. And then we go to d.
Solution credit: votrubac from Leetcode (https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/solutions/1612105/3-steps/)
'''