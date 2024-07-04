from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        arr.sort()
        
        if len(arr) == 0:
            return None
        
        ans = ListNode(arr[0])
        node = ans
        for i in range(1, len(arr)):
            new = ListNode(arr[i])
            node.next = new
            node = node.next
        return ans