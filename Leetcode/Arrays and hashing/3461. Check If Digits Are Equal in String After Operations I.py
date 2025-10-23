class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, s))
        while len(s) > 2:
            temp = []
            for i in range(1, len(s)):
                temp.append((s[i]+s[i-1])%10)
            s = temp
        return s[0] == s[1]