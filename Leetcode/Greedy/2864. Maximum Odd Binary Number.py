from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        freq = Counter(s)
        res = ''
        if freq['1'] > 1:
            res = '1'*(freq['1']-1) + '0'*freq['0'] + '1'
        else:
            res = '0'*freq['0'] + '1'
        return res