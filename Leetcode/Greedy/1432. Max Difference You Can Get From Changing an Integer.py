class Solution:
    def maxDiff(self, num: int) -> int:
        string = str(num)
        mapping = {1: 1, 9: 9}
        for ch in string:
            if ch != '9':
                mapping[9] = ch
                break
        for ch in string:
            if ch != '0':
                if string[0] != ch:
                    mapping[0] = ch
                elif ch != '1':
                    mapping[1] = ch
                else:
                    continue
                break
        minimum = 1
        if 0 in mapping:
            minimum = 0

        a, b = '', ''
        for ch in string:
            if mapping[9] == ch:
                a += '9'
            else:
                a += ch
            if mapping[minimum] == ch:
                b += str(minimum)
            else:
                b += ch
        return int(a) - int(b)