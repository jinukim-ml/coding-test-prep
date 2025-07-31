class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        def traverse(node: TreeNode, val: int) -> bool:
            if not node:
                if val == 0:
                    return True
                else:
                    return False
            val -= node.val
            if node.left and node.right:
                return traverse(node.left, val) or traverse(node.right, val)
            elif node.left:
                return traverse(node.left, val)
            else:
                return traverse(node.right, val)
        return traverse(root, targetSum)