from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        q = deque([root])
        levels = deque()
        while q:
            total = 0
            for _ in range(len(q)):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(total)

        q = deque([(root, 0)])
        while q:
            v = levels.popleft()
            for _ in range(len(q)):
                node, sib_val = q.popleft()
                node.val = v - sib_val - node.val

                if node.left and node.right:
                    q.append((node.left, node.right.val))
                    q.append((node.right, node.left.val))
                elif node.left:
                    q.append((node.left, 0))
                elif node.right:
                    q.append((node.right, 0))
        return root