class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        book = {'a': 0, 'b': 0, 'c': 0}
        for i, ch in enumerate(s):
            book[ch] += 1
        if book['a'] < k or book['b'] < k or book['c'] < k:
            return -1

        max_window = 0
        l = 0
        window = [0, 0, 0]
        for r in range(len(s)):
            window[ord(s[r]) - 97] += 1
            while l <= r and (book['a'] - window[0] < k or book['b'] - window[1] < k or book['c'] - window[2] < k):
                window[ord(s[l]) - 97] -= 1
                l += 1
            max_window = max(max_window, r - l + 1)
        return len(s) - max_window