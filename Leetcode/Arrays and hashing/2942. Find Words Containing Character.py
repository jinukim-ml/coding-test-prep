class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        res = []
        for i, w in enumerate(words):
            for ch in w:
                if ch == x:
                    break
            else:
                continue
            res.append(i)
        return res