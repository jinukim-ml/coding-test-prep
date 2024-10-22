from collections import deque
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        q = deque([root])
        levsum = []
        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(levsum, -total)

        if len(levsum) < k:
            return -1

        ans = 0
        for _ in range(k):
            ans = heapq.heappop(levsum)
        return -ans