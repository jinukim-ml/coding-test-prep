class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [''] * numRows
        indices = [i for i in range(numRows)] + [i for i in range(numRows-2, 0, -1)]
        for i, ch in enumerate(s):
            strings[indices[i%len(indices)]] += ch
        
        ans = ''
        for string in strings:
            ans += string
        return ans