from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = '', ''
        ptr = l1
        while ptr:
            n1 += str(ptr.val)
            ptr = ptr.next
        ptr = l2
        while ptr:
            n2 += str(ptr.val)
            ptr = ptr.next
        
        n = str(int(n1[::-1]) + int(n2[::-1]))
        ans = ListNode()
        ptr = ans

        for i in range(len(n)):
            if i != 0:
                newnode = ListNode(int(n[len(n)-i-1]))
                ptr.next = newnode
                ptr = newnode
            else:
                ptr.val = int(n[len(n)-i-1])
        return ans