from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        first = head
        while first:
            tmp = first.next
            first.next = prev
            prev = first
            first = tmp

        tail = prev
        biggest = prev.val
        while prev.next:
            if prev.next.val < biggest:
                tmp = prev.next
                while tmp and tmp.val < biggest:
                    tmp = tmp.next
                
                prev.next = tmp
                prev = tmp
                if prev:
                    biggest = prev.val
            else:
                biggest = prev.next.val
                prev = prev.next
            
            if not prev:
                break
        
        while tail:
            tmp = tail.next
            tail.next = first
            first = tail 
            tail = tmp
        
        return first