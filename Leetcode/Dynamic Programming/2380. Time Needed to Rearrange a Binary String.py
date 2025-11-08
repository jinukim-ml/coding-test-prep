class Solution: # time O(n), space O(1)
    def secondsToRemoveOccurrences(self, s: str) -> int:
        consec, pos, res = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                if i != pos:
                    res = max(res, i-pos+consec)
                    consec += 1
                pos += 1
            else:
                consec = max(consec-1, 0)
        return res

class Solution: # brute force
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        res = 0
        while True:
            cnt, i = 0, 1
            while i < len(s):
                if s[i-1] == '0' and s[i] == '1':
                    s[i-1] = '1'
                    s[i] = '0'
                    cnt += 1
                    i += 2
                else:
                    i += 1
            if cnt == 0:
                break
            res += 1
        return res