class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        def build() -> TreeNode:
            node = TreeNode(postorder.pop())
            if node.val != preorder[-1]:
                node.right = build()
            if node.val != preorder[-1]:
                node.left = build()
            preorder.pop()
            return node
        root = build()
        return root