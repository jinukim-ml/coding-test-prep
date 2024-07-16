# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node: TreeNode, target: int, path: list[TreeNode]) -> bool:
            path.append(node)
            if node.val == target:
                return True
            
            if node.left and search(node.left, target, path):
                return True
            elif node.right and search(node.right, target, path):
                return True
            path.pop()
            return False
        
        ppath, qpath = [], []
        search(root, p.val, ppath)
        search(root, q.val, qpath)
        
        for i in range(min(len(ppath), len(qpath))):
            if ppath[i].val != qpath[i].val:
                break
        
        if i == min(len(ppath), len(qpath))-1 and ppath[i].val == qpath[i].val: # one of them is LCA
            return ppath[i]
        else: # another node is LCA
            return ppath[i-1]