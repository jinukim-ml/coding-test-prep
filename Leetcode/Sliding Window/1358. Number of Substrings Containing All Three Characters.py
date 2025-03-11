class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        indices = [-1, -1, -1]
        lookup = {}
        for i in range(len(s)-1, -1, -1):
            indices[ord(s[i]) - 97] = i
            lookup[i] = (indices[0], indices[1], indices[2])
        
        res = 0
        for i in range(len(s)):
            a, b, c = lookup[i]
            if a == -1 or b == -1 or c == -1:
                break
            else:
                largest = max(a, b, c)
                res += n - largest
        return res