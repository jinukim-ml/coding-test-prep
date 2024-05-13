class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l: int, r: int) -> int:
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt
        
        if len(s) == 1:
            return 1
        
        ans = 0
        for i in range(len(s)-1):
            ans += expand(i, i+1) + expand(i, i)
        ans += expand(len(s)-1, len(s)-1)
        return ans