class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node = head
        n = 0
        while node:
            n += 1
            node = node.next
        
        node = head
        for _ in range(k-1):
            node = node.next
        a = node
        
        node = head
        for _ in range(n-k):
            node = node.next
        b = node

        a.val, b.val = b.val, a.val
        return head