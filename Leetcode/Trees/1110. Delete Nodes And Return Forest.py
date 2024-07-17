from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        def disintegrate(node: TreeNode):
            if not node:
                return
            node.left = disintegrate(node.left)
            node.right = disintegrate(node.right)

            if node.val not in to_delete:
                return node
            else: # we already dealt with the case where both a parent node and its child node are in to_delete
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return None

        if disintegrate(root):
            ans.append(root)
        return ans