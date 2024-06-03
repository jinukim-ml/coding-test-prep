class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l1, l2 = 0, 0
        while l1 < len(s) and l2 < len(t):
            if s[l1] == t[l2]:
                l2 +=1
            l1 += 1
        
        return len(t)-l2