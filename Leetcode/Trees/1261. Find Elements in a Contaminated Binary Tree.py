class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.seen = set([0])
        def dfs(node: TreeNode):
            if not node:
                return
            if node.left:
                node.left.val = 2 * node.val + 1
                self.seen.add(node.left.val)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.seen.add(node.right.val)
            dfs(node.left)
            dfs(node.right)
        dfs(self.root)
    def find(self, target: int) -> bool:
        return target in self.seen