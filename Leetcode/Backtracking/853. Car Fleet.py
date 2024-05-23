from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        for p, s in pairs:
            t = (target  - p) / s
            if len(stack) == 0 or stack[-1] < t:
                stack.append(t)
        
        return len(stack)