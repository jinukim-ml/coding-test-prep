# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> list[list[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        top, bottom, left, right = 0, m-1, 0, n-1
        
        while head:
            col = left
            while head and col <= right:
                ans[top][col] = head.val
                head = head.next
                col += 1
            top += 1
            
            row = top
            while head and row <= bottom:
                ans[row][right] = head.val
                head = head.next
                row += 1
            right -= 1
            
            col = right
            while head and col >= left:
                ans[bottom][col] = head.val
                head = head.next
                col -= 1
            bottom -= 1

            row = bottom
            while head and row >= top:
                ans[row][left] = head.val
                head = head.next
                row -= 1
            left += 1

        return ans