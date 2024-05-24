from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                pos, y = stack.pop()
                ans = max(ans, y * (i - pos))
                start = pos
            stack.append((start, h))

        for i, h in stack:
            ans = max(ans, h * (len(heights) - i))

        return ans