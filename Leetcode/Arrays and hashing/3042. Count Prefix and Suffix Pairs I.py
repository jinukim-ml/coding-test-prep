class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        def is_prefixsuffix(w1: str, w2: str) -> bool:
            if len(w2) < len(w1):
                return False
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    return False
            i = len(w1)-1
            j = len(w2)-1
            while i >= 0 and j >= 0 and w1[i] == w2[j]:
                i -= 1
                j -= 1
            return True if i == -1 else False

        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if is_prefixsuffix(words[i], words[j]):
                    res += 1
        return res