class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if j == i:
                    continue
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res