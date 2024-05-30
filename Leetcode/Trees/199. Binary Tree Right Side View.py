from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        q = deque()
        if root:
            q.append(root)
        while q:
            final_node_idx = len(q)-1
            for i in range(len(q)):
                node:TreeNode = q.popleft()
                if i == final_node_idx:
                    ans.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans