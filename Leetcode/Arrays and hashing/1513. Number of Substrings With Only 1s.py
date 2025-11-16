class Solution:
    def numSub(self, s: str) -> int:
        l, r, res = 0, 0, 0
        while r < len(s):
            if s[r] == '1':
                l = r
                while r < len(s)-1 and s[r+1] == '1':
                    r += 1
                window_size = r - l + 1
                res += (window_size * (window_size+1))//2
            r += 1
        return res%(10**9+7)

class Solution:
    def numSub(self, s: str) -> int:
        cnt, res = 0, 0
        for ch in s:
            if ch == '1':
                cnt += 1
            else:
                res += (cnt*(cnt+1))//2
                cnt = 0
        res += (cnt*(cnt+1))//2
        return res%(10**9+7)