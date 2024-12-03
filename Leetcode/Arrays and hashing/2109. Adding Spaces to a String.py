class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        res = ''
        i, curr = 0, 0
        while i < len(s) and curr < len(spaces):
            if i == spaces[curr]:
                res += ' '
                curr += 1
            res += s[i]
            i += 1
        res += s[i:]
        return res