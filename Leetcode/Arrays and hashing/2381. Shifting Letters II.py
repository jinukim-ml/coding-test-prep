class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        diff = [0] * (len(s) + 2)
        for start, end, direction in shifts:
            add = 1 if direction == 1 else -1
            diff[start] += add
            diff[end+1] += -1 * add

        res = ''
        for i in range(len(s)):
            diff[i] += diff[i-1]

            ch_idx = ord(s[i]) - 97
            res += chr(97 + (ch_idx + diff[i])%26)
        return res