from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Case 1. the deleted node is the head node
        # return head.next

        # Case 2. the deleted node is between two nodes
        # Case 3. the deleted node is the tail node
        # we traverse through the linked list and stop right before the node we are deleting

        length = 0 # length of the list
        tmphead = head
        while tmphead:
            tmphead = tmphead.next
            length += 1
        
        if n == length: # we are deleting the first node
            return head.next
        else: # we are deleting the last node
            cnt = 0
            tmphead = head
            while cnt < length - n - 1:
                tmphead = tmphead.next
                cnt += 1
            
            if tmphead.next.next: # is it between two nodes?
                nextnode = tmphead.next.next
                tmphead.next = nextnode
            else: # we are deleting the last node
                tmphead.next = None
            
            return head