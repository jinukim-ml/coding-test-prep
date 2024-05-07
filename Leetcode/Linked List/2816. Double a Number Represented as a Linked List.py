import sys
from typing import Optional
sys.set_int_max_str_digits(0)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = ""
        root = head
        while root:
            num += str(root.val)
            root = root.next
        
        doubled = str(int(num) * 2)

        if len(doubled) > len(num): # carry
            newnode = ListNode(val=1, next=head)
            idx = 1
            while head:
                head.val = doubled[idx]
                head = head.next
                idx += 1

            return newnode
        else:
            idx = 0
            root = head
            while root:
                root.val = doubled[idx]
                root = root.next
                idx += 1
            return head