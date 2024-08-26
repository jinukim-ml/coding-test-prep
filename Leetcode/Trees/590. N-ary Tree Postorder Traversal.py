# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        ans = []
        def traverse(node: Node) -> None:
            if node:
                for c in node.children:
                    traverse(c)
                ans.append(node.val)
        traverse(root)
        return ans