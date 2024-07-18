# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        def dfs(node: TreeNode) -> list[int]:
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal ans
            for l in left:
                for r in right:
                    if l + r <= distance:
                        ans += 1
            leaves = []
            for x in left + right:
                x += 1
                if x < distance:
                    leaves.append(x)
            return leaves
        dfs(root)
        return ans
    
class Solution: # slower, more naive approach
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaves = []

        def pathfind(node: TreeNode, path):
            if not node:
                return
            
            pathfind(node.left, path + 'L')
            pathfind(node.right, path + 'R')
            if not node.left and not node.right:
                leaves.append(path)
        pathfind(root, '')
        
        ans = 0
        for i in range(len(leaves)-1):
            for j in range(i+1, len(leaves)):
                k = 0
                while leaves[i][k] == leaves[j][k]:
                    k += 1
                if len(leaves[i])-k + len(leaves[j])-k <= distance:
                    ans += 1
        return ans