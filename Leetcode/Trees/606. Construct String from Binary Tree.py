class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root:TreeNode) -> str:
        s = f'{root.val}'
        if not root.left and root.right:
            s +=  f'()({self.tree2str(root.right)})'
        elif root.left and not root.right:
            s += f'({self.tree2str(root.left)})'
        elif root.left and root.right:
            s += f'({self.tree2str(root.left)})({self.tree2str(root.right)})'
        return s