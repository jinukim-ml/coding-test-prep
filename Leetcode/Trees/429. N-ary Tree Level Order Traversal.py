from collections import deque
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)

        nswer = []
        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                for j in range(len(node.children)):
                    q.append(node.children[j])
                
                lvl.append(node.val)
            nswer.append(lvl)
        return nswer