# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root:
            return False
        
        res = self.dfs(root, head)
        res = res or self.isSubPath(head, root.left)
        res = res or self.isSubPath(head, root.right)
        return res
    
    def dfs(self, tnode: TreeNode, ll: ListNode):
        if not ll:
            return True
        if not tnode:
            return False

        res = False
        if tnode.val == ll.val:
            res = self.dfs(tnode.left, ll.next) or self.dfs(tnode.right, ll.next)
        return res