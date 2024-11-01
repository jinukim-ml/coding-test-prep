class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for i in range(1, len(s)):
            ch = s[i]
            if ans[-1] == ch:
                cnt += 1
                if cnt < 3:
                    ans += ch
            else:
                cnt = 1
                ans += ch
        return ans