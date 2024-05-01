from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Idea
        # split the linked list into two parts: one pointer for the head and one pointer for the tail
        # reverse the second half of the list

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None # cut the list in two separate halves

        # reverse the second half of the list
        backward = None
        while right:
            temp = right.next
            right.next = backward
            backward = right
            right = temp

        left = head
        # actual linking
        while backward:
            temp, temp2 = left.next, backward.next
            left.next = backward
            backward.next = temp

            left = temp
            backward = temp2