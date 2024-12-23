from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_swaps(self, arr: list[int]) -> int:
        pos = {num: i for i, num in enumerate(sorted(arr))}
        n = len(arr)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[arr[i]] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[arr[j]]
                cycle_size += 1
            swaps += cycle_size - 1
        return swaps
    
    def minimumOperations(self, root: TreeNode) -> int:
        dq = deque([root])
        res = 0
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    dq.append(node.right)
                    level.append(node.right.val)
            res += self.get_swaps(level)
        return res