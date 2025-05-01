class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        num_vowels = 0
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in vowels:
                num_vowels += 1
            if r - l + 1 > k:
                if s[l] in vowels:
                    num_vowels -= 1
                l += 1
            if r - l + 1 == k:
                res = max(res, num_vowels)
        return res