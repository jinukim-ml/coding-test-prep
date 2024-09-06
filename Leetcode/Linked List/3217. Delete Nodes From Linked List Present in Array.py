# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        nums = set(nums)
        while head.val in nums:
            head = head.next
        prev = head
        node = prev.next
        while node:
            if node.val in nums:
                prev.next = node.next
                node.next = None
                node = prev.next
            else:
                prev = node
                node = node.next
        return head