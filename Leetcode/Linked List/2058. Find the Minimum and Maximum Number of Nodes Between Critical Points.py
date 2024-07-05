from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx, cps = 0, []
        node, prev = head.next, head.val
        while node.next:
            if prev > node.val and node.next and node.next.val > node.val:
                cps.append(idx)
            elif prev < node.val and node.next and node.next.val < node.val:
                cps.append(idx)
            prev = node.val
            node = node.next
            idx += 1
        
        mindis = float('inf')
        for i in range(len(cps)-1):
            mindis = min(mindis, cps[i+1] - cps[i])

        if len(cps) > 1:
            return [mindis, cps[-1]-cps[0]]
        else:
            return [-1, -1]