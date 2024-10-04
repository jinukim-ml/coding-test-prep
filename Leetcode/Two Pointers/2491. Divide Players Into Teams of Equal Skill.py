class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        target = skill[l] + skill[r]
        
        ans = 0
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            
            ans += skill[l] * skill[r]
            l += 1
            r -= 1
        return ans