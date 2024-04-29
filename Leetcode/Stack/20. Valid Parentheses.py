from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        table = {')': '(', '}': '{', ']': '['}
        stack = deque()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if stack and stack[-1] == table[s[i]]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True