import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        h = []
        for l in lists:
            head = l
            while head:
                heapq.heappush(h, head.val)
                head = head.next
        
        if not h:
            return None
        
        val = heapq.heappop(h)
        ans = ListNode(val=val)
        node = ans
        
        while h:
            newnode = ListNode(heapq.heappop(h))
            node.next = newnode
            node = newnode
        return ans