# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        each_size = length // k
        additional = length % k

        ans = []
        node = head
        for i in range(k):
            curr_size = each_size
            if additional > 0:
                curr_size += 1
                additional -= 1
            
            ans.append(node)
            for _ in range(curr_size-1):
                node = node.next
            
            if node:
                tmp = node.next
                node.next = None
                node = tmp
        return ans