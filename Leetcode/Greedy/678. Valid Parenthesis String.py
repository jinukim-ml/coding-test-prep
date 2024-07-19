class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin, leftmax = 0, 0

        for ch in s:
            if ch == '(':
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif ch == ')':
                leftmin, leftmax = leftmin - 1, leftmax - 1
            else: # wildcard
                leftmin, leftmax = leftmin - 1, leftmax + 1
        
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0
        
        return leftmin == 0