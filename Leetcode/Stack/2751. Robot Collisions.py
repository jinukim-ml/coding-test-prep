from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        indices = [i for i in range(len(positions))]
        for p, h, d, i in zip(positions, healths, directions, indices):
            robots.append([p, h, d, i])
        robots.sort()
        stack = []

        for p, h, d, i in robots:
            if not stack or stack[-1][2] == 'L' or d == 'R':
                stack.append([p,h,d,i])
            else: # there's at least one element in stack and the top element of stack's direction is R and current robot's direction is L (collision)
                health = h
                while stack and stack[-1][2] == 'R' and health > 0:
                    if stack[-1][1] > health:
                        if stack[-1][1] > 1:
                            stack[-1][1] -= 1
                        else:
                            stack.pop()
                        health = 0
                    elif stack[-1][1] < health:
                        stack.pop()
                        if health > 1:
                            health -= 1
                        else:
                            health = 0
                    else:
                        stack.pop()
                        health = 0
                
                if health:
                    stack.append([p,health,d,i])

        stack.sort(key=lambda item: item[-1])
        ans = []
        for p, h, d, i in stack:
            ans.append(h)
        return ans