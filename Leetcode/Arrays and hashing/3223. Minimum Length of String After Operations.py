class Solution:
    def minimumLength(self, s: str) -> int:
        length = len(s)
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1
            if cnt[ch] == 3:
                cnt[ch] -= 2
                length -= 2
        return length