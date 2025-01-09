class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        res = 0
        for w in words:
            i = 0
            while i < min(len(pref), len(w)) and pref[i] == w[i]:
                i += 1
            if i == len(pref):
                res += 1
        return res