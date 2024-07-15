from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        pset, cset = set(), set()
        treemap = dict()

        for p, c, isleft in descriptions:
            pset.add(p)
            cset.add(c)

            if p in treemap:
                parent = treemap[p]
            else:
                parent = TreeNode(p)
                treemap[p] = parent

            if c in treemap:
                child = treemap[c]
            else:
                child = TreeNode(c)
                treemap[c] = child

            if isleft:
                parent.left = child
            else:
                parent.right = child
        
        for v in pset:
            if v not in cset:
                return treemap[v]