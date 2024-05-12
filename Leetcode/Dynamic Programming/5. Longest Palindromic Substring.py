class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(idx1, idx2):
            while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
                idx1 -= 1
                idx2 += 1
            idx1 += 1
            idx2 -= 1
            return idx1, idx2, idx2-idx1+1
        
        if len(s) == 1:
            return s

        maxlen = 0
        for i in range(len(s)-1):
            odd = expand(i, i)
            even = expand(i, i+1)

            if odd[2] > maxlen:
                l, r = odd[0], odd[1]
                maxlen = odd[2]
            if even[2] > maxlen:
                l, r = even[0], even[1]
                maxlen = even[2]
        return s[l:r+1]