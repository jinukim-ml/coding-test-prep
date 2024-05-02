from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # idea: save memory address of each node in a hash table and check for dupliactes
        start = head
        table = {}
        while start:
            address = hex(id(start))
            table[address] = table.get(address, 0) + 1
            start = start.next

            if table[address] > 1:
                return True
        return False
    
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # idea: compare slow pointer and fast pointer. if they point the same node, there's a cycle
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False