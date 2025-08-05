class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        newtree = TreeNode()
        def dfs(node1, node2):
            if node1 and node2:
                newnode = TreeNode(node1.val+node2.val)
                newnode.left = dfs(node1.left, node2.left)
                newnode.right = dfs(node1.right, node2.right)
            elif node1:
                newnode = TreeNode(node1.val)
                newnode.left = dfs(node1.left, None)
                newnode.right = dfs(node1.right, None)
            elif node2:
                newnode = TreeNode(node2.val)
                newnode.left = dfs(None, node2.left)
                newnode.right = dfs(None, node2.right)
            else:
                newnode = None
            return newnode
        newtree = dfs(root1, root2)
        return newtree