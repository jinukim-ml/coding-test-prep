# Josephus problem
from collections import deque

class Solution: # O(n)
    def findTheWinner(self, n: int, k: int) -> int:
        def winner(remaining: int, k: int) -> int:
            if remaining == 1:
                return 0
            return (winner(remaining-1, k) + k) % remaining
        
        return winner(n, k) + 1

class Solution: # O(kn)
    def findTheWinner(self, n: int, k: int) -> int:
        group = deque([i for i in range(1, n+1)])
        
        while len(group) > 1:
            for i in range(k-1):
                friend = group.popleft()
                group.append(friend)
            group.popleft()
        return group.popleft()