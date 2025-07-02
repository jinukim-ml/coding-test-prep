class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                break
            i = l+1
            while i < r and s[l] == s[i]:
                i += 1
            j = r-1
            while j > i and s[r] == s[j]:
                j -= 1
            l = i
            r = j
        return r-l+1