class Solution:
    def minMaxDifference(self, num: int) -> int:
        string = str(num)
        mapping = {0: 0, 9: 9}
        for ch in string:
            if ch != '9':
                mapping[9] = ch
                break
        mapping[0] = string[0]
        maximum = ''
        minimum = ''
        for ch in string:
            if mapping[9] == ch:
                maximum += '9'
            else:
                maximum += ch
            if mapping[0] == ch:
                minimum += '0'
            else:
                minimum += ch
        return int(maximum) - int(minimum)