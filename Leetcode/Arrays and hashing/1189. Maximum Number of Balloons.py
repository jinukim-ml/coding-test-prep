from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        res = 0 
        while True:
            for ch in ['b', 'a', 'l', 'l', 'o', 'o', 'n']:
                if ch not in counter:
                    break
                counter[ch] -= 1
                if counter[ch] == 0:
                    counter.pop(ch)
            else:
                res += 1
                continue
            break
        return res