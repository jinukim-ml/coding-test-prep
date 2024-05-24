from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = 0

        cnt = Counter(letters)
        wordscores = {}
        for w in words:
            points = 0
            for ch in w:
                points += score[ord(ch) - 97]
            wordscores[w] = points

        def backtrack(i, counter, curr_score):
            nonlocal ans

            ans = max(ans, curr_score)
            if i == len(words):
                return

            for j in range(i, len(words)):
                localcnt = counter.copy()

                pos, points = 0, 0
                while pos < len(words[j]) and words[j][pos] in localcnt and localcnt[words[j][pos]] > 0:
                    localcnt[words[j][pos]] -= 1
                    pos += 1
                if pos == len(words[j]):
                    backtrack(j+1, localcnt, curr_score + wordscores[words[j]])

        backtrack(0, cnt, 0)
        return ans