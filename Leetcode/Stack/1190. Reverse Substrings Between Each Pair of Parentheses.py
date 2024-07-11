class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ')':
                reverse = ''
                while stack and stack[-1] != '(':
                    reverse += stack.pop()
                if stack:
                    stack.pop()
                    
                for i in range(len(reverse)):
                    stack.append(reverse[i])
            else:
                stack.append(ch)
        return ''.join(stack)