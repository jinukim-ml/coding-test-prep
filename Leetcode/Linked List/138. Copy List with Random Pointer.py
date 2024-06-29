from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        lead = head
        while lead:
            tmp = lead.next
            lead.next = Node(lead.val, lead.next, lead.random)
            lead = tmp
        
        fast = head.next
        while fast:
            fast.random = fast.random.next if fast.random else None
            fast.next = fast.next.next if fast.next else None
            fast = fast.next
        return head.next