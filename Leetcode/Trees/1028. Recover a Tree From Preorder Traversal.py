class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        i = 0
        level = 0
        dummy = TreeNode()
        def dfs(parent: TreeNode, curr_lvl: int):
            nonlocal i, level
            while i < len(traversal) and curr_lvl == level:
                val = 0
                while i < len(traversal) and traversal[i].isdigit():
                    val = val * 10 + int(traversal[i])
                    i += 1
                node = TreeNode(val)
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                
                level = 0
                while i < len(traversal) and traversal[i] == '-':
                    level += 1
                    i += 1
                dfs(node, curr_lvl+1)
        dfs(dummy, 0)
        return dummy.left