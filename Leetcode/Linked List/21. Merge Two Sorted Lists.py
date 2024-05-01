from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        nextnode = head
        while list1 and list2:
            if list1.val <= list2.val:
                new = ListNode(list1.val)
                nextnode.next = new
                list1 = list1.next
                nextnode = nextnode.next
            else:
                new = ListNode(list2.val)
                nextnode.next = new
                list2 = list2.next
                nextnode = nextnode.next
        
        if list1 and not list2:
            while list1:
                new = ListNode(list1.val)
                nextnode.next = new
                list1 = list1.next
                nextnode = nextnode.next
        elif not list1 and list2:
            while list2:
                new = ListNode(list2.val)
                nextnode.next = new
                list2 = list2.next
                nextnode = nextnode.next
        
        if head.next:
            head = head.next
            return head
        else:
            return None