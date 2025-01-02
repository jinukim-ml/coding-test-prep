class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        prefix = [0]
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for w in words:
            s = prefix[-1]
            if w[0] in vowels and w[-1] in vowels:
                s += 1
            prefix.append(s)

        res = []
        for l, r in queries:
            res.append(prefix[r+1] - prefix[l])
        return res