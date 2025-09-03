from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque([(root, 1)])
        res = 0
        while q:
            res = max(res, q[-1][1]-q[0][1]+1)
            for _ in range(len(q)):
                node, val = q.popleft()
                if node.left:
                    q.append((node.left, 2*val))
                if node.right:
                    q.append((node.right, 2*val+1))
        return res