from collections import Counter

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        alphabets = {}
        for w in words2:
            for k, v in Counter(w).items():
                if k not in alphabets or alphabets[k] < v:
                    alphabets[k] = v
        items = alphabets.items()
        
        res = []
        for w in words1:
            cnt = dict(Counter(w))
            for k, v in items:
                if k not in cnt or cnt[k] < v:
                    break
            else:
                res.append(w)
        return res