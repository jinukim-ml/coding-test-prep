from collections import Counter

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        book = Counter(words)
        single_symmetry = False
        seen = set()
        res = 0
        for w, v in book.items():
            if w[0] == w[1]:
                if v%2:
                    single_symmetry = True
                res += v//2 * 4
            else:
                rev = w[::-1]
                if rev in book and rev not in seen:
                    res += min(book[w], book[rev]) * 4
                seen.add(w)
        if single_symmetry:
            res += 2
        return res