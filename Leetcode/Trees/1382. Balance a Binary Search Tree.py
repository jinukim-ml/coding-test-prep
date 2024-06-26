from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(node: TreeNode) -> List[int]:
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        
        def makebst(l: int, r: int) -> TreeNode:
            if l == r:
                return TreeNode(arr[l])
            if l > r or r < l:
                return None
            mid = (l + r) // 2
            node = TreeNode(arr[mid])
            node.left = makebst(l, mid-1)
            node.right = makebst(mid+1, r)
            return node
        return makebst(0, len(arr)-1)