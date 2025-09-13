from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        consonants = defaultdict(int)
        max_vcount, max_ccount = 0, 0
        for ch in s:
            if ch in vowels:
                vowels[ch] += 1
                max_vcount = max(max_vcount, vowels[ch])
            else:
                consonants[ch] += 1
                max_ccount = max(max_ccount, consonants[ch])
        return max_vcount + max_ccount