class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # TC O(n) SC O(n)
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        for l in range(len(arr)//2):
            r = len(arr)-l-1
            if arr[l] != arr[r]:
                return False
        return True

class Solution: # TC O(n) SC O(1)
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True