from collections import Counter

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res = [words[0]]
        for i in range(1, len(words)):
            if Counter(words[i]) != Counter(words[i-1]):
                res.append(words[i])
        return res
    
class Solution: # same idea but faster
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i-1]):
                res.append(words[i])
        return res