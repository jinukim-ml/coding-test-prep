class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        n, m = len(skill), len(mana)
        free = [0 for _ in range(n)]

        for i in range(m):
            now = free[0]
            for j in range(1,n):
                now = max(now + mana[i]*skill[j-1], free[j])
            
            free[-1] = now + mana[i]*skill[-1]
            for j in reversed(range(n-1)):
                free[j] = free[j+1] - mana[i]*skill[j+1]
        return free[-1]