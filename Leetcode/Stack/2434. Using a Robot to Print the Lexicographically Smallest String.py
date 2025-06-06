from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        ch_idx = 0
        res = ''
        for i in range(len(s)):
            stack.append(s[i])
            counter[s[i]] -= 1
            while ch_idx < 26 and counter[chr(ch_idx+97)] == 0:
                ch_idx += 1
            while stack and ord(stack[-1])-97 <= ch_idx:
                res += stack.pop()
        return res