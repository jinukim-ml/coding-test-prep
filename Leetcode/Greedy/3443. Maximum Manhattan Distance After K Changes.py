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

class Solution: # a little bit slower but more readable
    def maxDistance(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        for ch in s:
            freq[ch] += 1
            base_x = abs(freq['E'] - freq['W'])
            base_y = abs(freq['N'] - freq['S'])

            x_opp = min(freq['E'], freq['W'])
            y_opp = min(freq['N'], freq['S'])

            flips = min(k, x_opp + y_opp)
            res = max(res, base_x + base_y + 2*flips)
        return res