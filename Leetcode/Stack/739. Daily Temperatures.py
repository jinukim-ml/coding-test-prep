from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, idx = stack.pop()
                answer[idx] = i - idx

            stack.append((temperatures[i], i))
        return answer