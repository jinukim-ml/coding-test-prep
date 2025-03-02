import re
class Solution: # Solution using regex
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(re.findall('[a-z0-9]', s))
        
        for i in range(len(s)):
            if s[i] != s[len(s)-(i+1)]:
                return False
        return True

class Solution: # Two pointers solution
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True