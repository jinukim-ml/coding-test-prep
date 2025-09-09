from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = deque([0 for _ in range(forget)])
        people[0] = 1
        window = 0
        for day in range(n-1):
            window += people[delay-1] - people.pop()
            people.appendleft(window)
        return sum(people)%(10**9+7)