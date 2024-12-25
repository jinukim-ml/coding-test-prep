from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:
        res = []
        dq = deque()
        if root:
            dq.append(root)
        while dq:
            largest = -float('inf')
            for _ in range(len(dq)):
                node = dq.popleft()
                largest = max(largest, node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(largest)
        return res