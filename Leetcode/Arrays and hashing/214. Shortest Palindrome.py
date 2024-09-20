class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return s
        
        l = 0
        for r in range(length-1, -1, -1):
            if s[l] == s[r]:
                l += 1
        
        if l == length:
            return s
        
        suffix = s[l:]
        return suffix[::-1] + self.shortestPalindrome(s[:l]) + suffix