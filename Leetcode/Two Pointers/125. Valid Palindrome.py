import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(re.findall('[a-z0-9]', s))
        
        for i in range(len(s)):
            if s[i] != s[len(s)-(i+1)]:
                return False
        return True