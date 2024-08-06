from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        mapped = [0] * 10
        curr = 1
        ans = 0
        for v in sorted(cnt.values(), reverse=True):
            mapped[curr] += 1
            if mapped[curr] == 9:
                curr += 1
                mapped[curr] += 1
            ans += v * curr
        return ans