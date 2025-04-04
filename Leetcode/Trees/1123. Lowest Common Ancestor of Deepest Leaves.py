class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode, depth: int) -> TreeNode:
            if not node:
                return (None, depth)
            node_left, depth_left = dfs(node.left, depth+1)
            node_right, depth_right = dfs(node.right, depth+1)
            
            if depth_left > depth_right:
                return (node_left, depth_left)
            elif depth_left < depth_right:
                return (node_right, depth_right)
            else:
                return (node, depth_left)
        
        node, _ = dfs(root, 0)
        return node