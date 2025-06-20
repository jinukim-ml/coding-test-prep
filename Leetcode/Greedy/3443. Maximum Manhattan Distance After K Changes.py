from collections import defaultdict

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        for ch in s:
            freq[ch] += 1
            if freq['N'] >= freq['S']:
                change = min(freq['S'], k)
                y = freq['N'] - freq['S'] + 2*change
                remaining = k - change
            else:
                change = min(freq['N'], k)
                y = freq['S'] - freq['N'] + 2*change
                remaining = k - change
            if freq['E'] >= freq['W']:
                change = min(freq['W'], remaining)
                x = freq['E'] - freq['W'] + 2*change
            else:
                change = min(freq['E'], remaining)
                x = freq['W'] - freq['E'] + 2*change
            res = max(res, x+y)
        return res