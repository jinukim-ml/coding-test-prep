class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0, 0
            num_left, left_total = dfs(node.left)
            num_right, right_total = dfs(node.right)
            total = node.val + left_total + right_total
            num_nodes = 1 + num_left + num_right
            if node.val == total//num_nodes:
                nonlocal res
                res += 1
            return num_nodes, total
        dfs(root)
        return res