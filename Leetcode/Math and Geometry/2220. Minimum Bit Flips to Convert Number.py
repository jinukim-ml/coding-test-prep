class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]

        if len(start) > len(goal):
            goal = '0' * (len(start)-len(goal)) + goal
        else:
            start = '0' * (len(goal)-len(start)) + start
        
        ans = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                ans += 1
        return ans