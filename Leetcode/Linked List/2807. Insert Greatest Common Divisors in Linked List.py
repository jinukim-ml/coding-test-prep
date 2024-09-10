from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        def get_gcd(a: int, b: int) -> int:
            gcd = 1
            for x in range(2, min(a,b)+1):
                if a//x == a/x and b//x == b/x:
                    gcd = x
            return gcd
        
        node = head
        prev = node
        node = node.next
        while node:
            newnode = ListNode(val=gcd(prev.val, node.val), next=node)
            prev.next = newnode
            prev = node
            node = node.next
        
        return head