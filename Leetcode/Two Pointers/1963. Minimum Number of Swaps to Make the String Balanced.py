class Solution:
    def minSwaps(self, s: str) -> int:
        opening, closing = 0, 0
        r = len(s)-1

        ans = 0
        for ch in s:
            if ch == '[':
                opening += 1
            else:
                closing += 1
            
            if closing > opening:
                while s[r] != ']':
                    r -= 1
                ans += 1
                closing -= 1
                opening += 1
        return ans