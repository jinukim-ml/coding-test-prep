from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        val, cnt = 0, deque()
        ans = ListNode()
        ans_head = ans
        while node:
            if node.val == 0:
                cnt.append(node)
                if len(cnt) == 2:
                    ans.next = ListNode(val=val)
                    ans = ans.next
                    cnt.popleft()
                    val = 0
            val += node.val
            node = node.next
        return ans_head.next