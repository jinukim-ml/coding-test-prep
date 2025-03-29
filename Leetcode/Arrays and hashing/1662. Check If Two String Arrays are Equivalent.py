class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s1 = ''
        s2 = ''
        i = 0
        while i < min(len(word1), len(word2)):
            s1 += word1[i]
            s2 += word2[i]
            i += 1
        while i < len(word1):
            s1 += word1[i]
            i += 1
        while i < len(word2):
            s2 += word2[i]
            i += 1
        return s1 == s2

class Solution: # more pythonian solution
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)